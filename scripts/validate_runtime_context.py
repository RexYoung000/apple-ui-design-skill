#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_GROUPS = {"skills", "references", "total"}
REQUIRED_METRICS = {"lines", "words", "bytes"}
REQUIRED_SKILLS = {
    "apple-ui-direction",
    "apple-platform-adaptation",
    "apple-ui-review",
}
REQUIRED_REFERENCES = {
    "accessibility-and-localization.md",
    "apple-platform-adaptation.md",
    "authority-and-principles.md",
    "content-and-sensitive-flows.md",
    "context-and-alignment.md",
    "current-sources.md",
    "delivery-contracts.md",
    "design-system-and-dna.md",
    "engineering-routing.md",
    "interaction-and-motion.md",
    "prototyping-and-implementation.md",
    "research-and-source-evidence.md",
    "validation-and-review.md",
}
REQUIRED_FORWARD_SCENARIOS = {
    "small-static-direction",
    "behavioral-platform-adaptation",
}


def measure(paths: list[Path]) -> dict[str, int]:
    lines = 0
    words = 0
    byte_count = 0
    for path in paths:
        raw = path.read_bytes()
        lines += raw.count(b"\n")
        words += len(re.findall(r"\S+", raw.decode("utf-8")))
        byte_count += len(raw)
    return {"lines": lines, "words": words, "bytes": byte_count}


def valid_metric_group(value: object) -> bool:
    return (
        isinstance(value, dict)
        and set(value) == REQUIRED_METRICS
        and all(isinstance(value[key], int) and value[key] > 0 for key in REQUIRED_METRICS)
    )


def repository_file(root: Path, value: object, label: str, errors: list[str]) -> Path | None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} must be a non-empty repository path")
        return None
    path = (root / value).resolve()
    try:
        path.relative_to(root)
    except ValueError:
        errors.append(f"{label} escapes repository: {value}")
        return None
    if not path.is_file():
        errors.append(f"{label} does not exist: {value}")
        return None
    return path


def validate(contract_path: Path, repo_root: Path | None = None) -> tuple[list[str], dict[str, dict[str, int]]]:
    errors: list[str] = []
    metrics: dict[str, dict[str, int]] = {}
    root = (repo_root or contract_path.resolve().parents[2]).resolve()

    try:
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
    except OSError:
        return [f"missing runtime-context contract: {contract_path}"], metrics
    except json.JSONDecodeError as exc:
        return [f"runtime-context contract must be valid JSON: {exc}"], metrics

    if not isinstance(contract, dict):
        return ["runtime-context contract root must be an object"], metrics
    if contract.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if contract.get("suite") != "runtime-context":
        errors.append("suite must equal 'runtime-context'")
    if contract.get("linked_issue") != 10:
        errors.append("linked_issue must equal 10")
    if contract.get("measured_at") != "2026-07-31":
        errors.append("measured_at must equal 2026-07-31")

    skills_root = root / "plugins" / "apple-ui-design" / "skills"
    references_root = root / "plugins" / "apple-ui-design" / "references"
    skill_paths = sorted(skills_root.glob("*/SKILL.md"))
    markdown_references = sorted(references_root.glob("*.md"))
    source_registry = references_root / "source-registry.json"
    reference_paths = markdown_references + ([source_registry] if source_registry.is_file() else [])

    if {path.parent.name for path in skill_paths} != REQUIRED_SKILLS:
        errors.append("runtime skill set must match the three bundled skills")
    if {path.name for path in markdown_references} != REQUIRED_REFERENCES:
        errors.append("runtime Markdown reference set must match the declared shared references")
    if not source_registry.is_file():
        errors.append("runtime source-registry.json is missing")

    if skill_paths and reference_paths:
        metrics["skills"] = measure(skill_paths)
        metrics["references"] = measure(reference_paths)
        metrics["total"] = {
            key: metrics["skills"][key] + metrics["references"][key]
            for key in REQUIRED_METRICS
        }

    for field in ("baseline", "current"):
        value = contract.get(field)
        if not isinstance(value, dict) or set(value) != REQUIRED_GROUPS:
            errors.append(f"{field} must contain skills, references, and total")
            continue
        for group in REQUIRED_GROUPS:
            if not valid_metric_group(value.get(group)):
                errors.append(f"{field}.{group} must contain positive lines, words, and bytes")
        if field == "current" and metrics:
            for group in REQUIRED_GROUPS:
                if value.get(group) != metrics[group]:
                    errors.append(f"current.{group} does not match measured runtime files")

    baseline = contract.get("baseline")
    current = contract.get("current")
    if isinstance(baseline, dict) and isinstance(current, dict):
        for group in REQUIRED_GROUPS:
            if valid_metric_group(baseline.get(group)) and valid_metric_group(current.get(group)):
                if current[group]["words"] >= baseline[group]["words"]:
                    errors.append(f"current.{group}.words must be lower than baseline")

    limits = contract.get("limits")
    required_limits = {
        "skill_words",
        "total_words",
        "single_skill_lines",
        "long_reference_lines",
    }
    if not isinstance(limits, dict) or set(limits) != required_limits:
        errors.append("limits must define all runtime context ceilings")
        limits = {}
    elif not all(isinstance(value, int) and value > 0 for value in limits.values()):
        errors.append("all runtime context limits must be positive integers")

    if metrics and limits:
        if metrics["skills"]["words"] > limits["skill_words"]:
            errors.append("Skill entry instructions exceed the word budget")
        if metrics["total"]["words"] > limits["total_words"]:
            errors.append("total runtime instructions exceed the word budget")
        for path in skill_paths:
            line_count = measure([path])["lines"]
            if line_count > limits["single_skill_lines"]:
                errors.append(f"Skill entry exceeds line budget: {path.relative_to(root)}")
        for path in markdown_references:
            source = path.read_text(encoding="utf-8")
            line_count = measure([path])["lines"]
            if "## Load When" not in source:
                errors.append(f"reference missing Load When: {path.relative_to(root)}")
            if line_count > limits["long_reference_lines"] and "## Contents" not in source:
                errors.append(f"long reference missing Contents: {path.relative_to(root)}")

    reference_contracts = contract.get("reference_contracts")
    configured_paths: set[str] = set()
    load_markers: set[str] = set()
    ownership_markers: set[str] = set()
    runtime_text = "\n".join(
        path.read_text(encoding="utf-8") for path in skill_paths + markdown_references
    )
    if not isinstance(reference_contracts, list):
        errors.append("reference_contracts must be a list")
    else:
        for index, item in enumerate(reference_contracts):
            label = f"reference_contracts[{index}]"
            if not isinstance(item, dict) or set(item) != {"path", "load_marker", "ownership_marker"}:
                errors.append(f"{label} must define path, load_marker, and ownership_marker")
                continue
            path_value = item["path"]
            load_marker = item["load_marker"]
            ownership_marker = item["ownership_marker"]
            if not all(isinstance(value, str) and value.strip() for value in item.values()):
                errors.append(f"{label} values must be non-empty strings")
                continue
            if path_value in configured_paths:
                errors.append(f"duplicate reference contract path: {path_value}")
            configured_paths.add(path_value)
            if load_marker in load_markers:
                errors.append(f"duplicate reference load marker: {load_marker}")
            load_markers.add(load_marker)
            if ownership_marker in ownership_markers:
                errors.append(f"duplicate reference ownership marker: {ownership_marker}")
            ownership_markers.add(ownership_marker)
            path = repository_file(root, path_value, label, errors)
            if path is None:
                continue
            source = path.read_text(encoding="utf-8")
            if load_marker not in source:
                errors.append(f"{label} load marker missing from {path_value}")
            if ownership_marker not in source:
                errors.append(f"{label} ownership marker missing from {path_value}")
            if runtime_text.count(ownership_marker) != 1:
                errors.append(f"ownership marker must appear once in runtime: {ownership_marker}")

    expected_reference_paths = {
        str(path.relative_to(root)) for path in markdown_references
    }
    if configured_paths != expected_reference_paths:
        errors.append("reference_contracts must cover every Markdown reference exactly once")

    registry_contract = contract.get("source_registry")
    if not isinstance(registry_contract, dict) or set(registry_contract) != {"path", "route_owner", "route_marker"}:
        errors.append("source_registry must define path, route_owner, and route_marker")
    else:
        registry_path = repository_file(root, registry_contract["path"], "source_registry.path", errors)
        owner_path = repository_file(root, registry_contract["route_owner"], "source_registry.route_owner", errors)
        if registry_path and owner_path:
            owner_source = owner_path.read_text(encoding="utf-8")
            if registry_contract["route_marker"] not in owner_source:
                errors.append("source_registry route marker missing from its runtime owner")

    forbidden_markers = contract.get("forbidden_runtime_markers")
    if not isinstance(forbidden_markers, list) or not forbidden_markers or not all(
        isinstance(marker, str) and marker.strip() for marker in forbidden_markers
    ):
        errors.append("forbidden_runtime_markers must be a non-empty string list")
    else:
        for marker in forbidden_markers:
            if marker in runtime_text:
                errors.append(f"repository-only marker found in runtime: {marker}")

    forward_test = contract.get("forward_test_record")
    if not isinstance(forward_test, dict) or set(forward_test) != {"path", "scenarios"}:
        errors.append("forward_test_record must define path and scenarios")
    else:
        record_path = repository_file(
            root, forward_test["path"], "forward_test_record.path", errors
        )
        scenarios = forward_test["scenarios"]
        if not isinstance(scenarios, list) or set(scenarios) != REQUIRED_FORWARD_SCENARIOS:
            errors.append("forward-test scenarios must match the two runtime-context runs")
        elif record_path is not None:
            record = record_path.read_text(encoding="utf-8")
            for scenario in REQUIRED_FORWARD_SCENARIOS:
                if scenario not in record:
                    errors.append(f"forward-test record missing scenario: {scenario}")

    return errors, metrics


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    contract_path = root / "evals" / "runtime-context" / "contract.json"
    errors, metrics = validate(contract_path, repo_root=root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "runtime context valid: "
        f"{metrics['skills']['words']} Skill words, "
        f"{metrics['total']['words']} total words"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
