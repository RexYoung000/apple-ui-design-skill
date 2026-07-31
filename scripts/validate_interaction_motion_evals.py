#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


REQUIRED_CASE_FIELDS = {
    "id",
    "scenario",
    "skill",
    "tags",
    "prompt",
    "expected_behavior",
    "forbidden_behavior",
    "source_markers",
}
REQUIRED_CASE_IDS = {
    "tool-spatial-navigation-platform-inputs",
    "content-reading-continuity",
    "experimental-radial-scrub-review",
    "rapid-repeat-final-intent",
    "reduced-motion-parallel-expression",
    "html-build-is-not-native-evidence",
    "meaningful-interaction-exploration",
}
REQUIRED_SKILLS = {
    "apple-ui-direction",
    "apple-platform-adaptation",
    "apple-ui-review",
}
REQUIRED_SCENARIOS = {"tool", "content", "experimental"}
REQUIRED_TAGS = {
    "product-authority",
    "experience-contract",
    "motion-language",
    "platform-inputs",
    "interruption-reversal",
    "reduced-motion",
    "native-evidence",
    "meaningful-exploration",
}
REQUIRED_EVIDENCE_PATHS = {
    "evals/delivery-contracts/runs/2026-07-29/native-prototype/DESIGN.md",
    "evals/delivery-contracts/runs/2026-07-29/native-prototype/VALIDATION.md",
    "evals/delivery-contracts/runs/2026-07-29/native-prototype/evidence/recordings/standard-interruption-reversal.mp4",
    "evals/delivery-contracts/runs/2026-07-29/native-prototype/evidence/recordings/reduce-motion-interruption-reversal.mp4",
}


def non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def non_empty_string_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(non_empty_string(item) for item in value)
    )


def validate_repository_path(
    relative_path: str,
    root: Path,
    label: str,
    errors: list[str],
) -> Path | None:
    path = (root / relative_path).resolve()
    try:
        path.relative_to(root)
    except ValueError:
        errors.append(f"{label} escapes repository: {relative_path}")
        return None
    if not path.is_file():
        errors.append(f"{label} does not exist: {relative_path}")
        return None
    return path


def validate(cases_path: Path, repo_root: Path | None = None) -> tuple[list[str], Counter[str]]:
    errors: list[str] = []
    coverage: Counter[str] = Counter()
    root = (repo_root or cases_path.resolve().parents[2]).resolve()

    try:
        suite = json.loads(cases_path.read_text(encoding="utf-8"))
    except OSError:
        return [f"missing interaction-motion suite: {cases_path}"], coverage
    except json.JSONDecodeError as exc:
        return [f"interaction-motion suite must be valid JSON: {exc}"], coverage

    if not isinstance(suite, dict):
        return ["interaction-motion suite root must be an object"], coverage
    if suite.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if suite.get("suite") != "interaction-motion":
        errors.append("suite must equal 'interaction-motion'")
    if suite.get("linked_issue") != 14:
        errors.append("linked_issue must equal 14")
    if not non_empty_string(suite.get("purpose")):
        errors.append("purpose must be a non-empty string")

    declared_tags = suite.get("required_tags")
    if not non_empty_string_list(declared_tags):
        errors.append("required_tags must be a non-empty string list")
        declared_tag_set: set[str] = set()
    else:
        declared_tag_set = set(declared_tags)
        if declared_tag_set != REQUIRED_TAGS:
            errors.append("required_tags must match the Issue #14 coverage contract")

    evidence = suite.get("preserved_evidence")
    if not isinstance(evidence, dict):
        errors.append("preserved_evidence must be an object")
    else:
        if evidence.get("scenario") != "tool":
            errors.append("preserved_evidence.scenario must equal 'tool'")
        artifacts = evidence.get("artifacts")
        if not non_empty_string_list(artifacts):
            errors.append("preserved_evidence.artifacts must be a non-empty string list")
        else:
            artifact_set = set(artifacts)
            if artifact_set != REQUIRED_EVIDENCE_PATHS:
                errors.append("preserved evidence paths must match the Stillpoint record")
            for relative_path in artifacts:
                validate_repository_path(relative_path, root, "evidence artifact", errors)
        for field in ("supports", "does_not_support"):
            if not non_empty_string_list(evidence.get(field)):
                errors.append(f"preserved_evidence.{field} must be a non-empty string list")

    cases = suite.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a non-empty list"], coverage

    ids: set[str] = set()
    for index, case in enumerate(cases):
        label = f"cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{label} must be an object")
            continue

        missing = sorted(REQUIRED_CASE_FIELDS - case.keys())
        if missing:
            errors.append(f"{label} missing fields: {', '.join(missing)}")
            continue

        case_id = case["id"]
        if not non_empty_string(case_id):
            errors.append(f"{label}.id must be a non-empty string")
        elif case_id in ids:
            errors.append(f"duplicate case id: {case_id}")
        else:
            ids.add(case_id)

        scenario = case["scenario"]
        if scenario not in REQUIRED_SCENARIOS:
            errors.append(f"{label}.scenario is not a supported product scenario")
        else:
            coverage[f"scenario/{scenario}"] += 1

        skill = case["skill"]
        if skill not in REQUIRED_SKILLS:
            errors.append(f"{label}.skill is not a bundled Apple UI skill")
        else:
            coverage[f"skill/{skill}"] += 1

        tags = case["tags"]
        if not non_empty_string_list(tags):
            errors.append(f"{label}.tags must be a non-empty string list")
        else:
            for tag in tags:
                if tag not in REQUIRED_TAGS:
                    errors.append(f"{label}.tags contains unknown tag: {tag}")
                coverage[f"tag/{tag}"] += 1

        if not non_empty_string(case["prompt"]):
            errors.append(f"{label}.prompt must be a non-empty string")
        for field in ("expected_behavior", "forbidden_behavior"):
            if not non_empty_string_list(case[field]):
                errors.append(f"{label}.{field} must be a non-empty string list")

        markers = case["source_markers"]
        if not isinstance(markers, dict) or not markers:
            errors.append(f"{label}.source_markers must be a non-empty object")
            continue
        for relative_path, required_markers in markers.items():
            if not non_empty_string(relative_path):
                errors.append(f"{label}.source_markers contains an invalid path")
                continue
            if not non_empty_string_list(required_markers):
                errors.append(
                    f"{label}.source_markers[{relative_path!r}] must be a non-empty string list"
                )
                continue
            path = validate_repository_path(relative_path, root, "source file", errors)
            if path is None:
                continue
            source = path.read_text(encoding="utf-8")
            for marker in required_markers:
                if marker not in source:
                    errors.append(
                        f"{label} source marker missing from {relative_path}: {marker}"
                    )

    if ids != REQUIRED_CASE_IDS:
        errors.append("case ids must match the seven Issue #14 regression scenarios")
    for skill in sorted(REQUIRED_SKILLS):
        if coverage[f"skill/{skill}"] == 0:
            errors.append(f"suite must cover skill: {skill}")
    for scenario in sorted(REQUIRED_SCENARIOS):
        if coverage[f"scenario/{scenario}"] == 0:
            errors.append(f"suite must cover scenario: {scenario}")
    for tag in sorted(REQUIRED_TAGS):
        if coverage[f"tag/{tag}"] == 0:
            errors.append(f"suite must cover tag: {tag}")
    if declared_tag_set and {
        key.removeprefix("tag/") for key in coverage if key.startswith("tag/")
    } != declared_tag_set:
        errors.append("case tag coverage must match required_tags")

    return errors, coverage


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    cases_path = repo_root / "evals" / "interaction-motion" / "cases.json"
    errors, coverage = validate(cases_path, repo_root=repo_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    case_count = sum(
        value for key, value in coverage.items() if key.startswith("scenario/")
    )
    print(f"Interaction-motion suite is valid ({case_count} cases).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
