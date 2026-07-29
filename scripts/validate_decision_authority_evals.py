#!/usr/bin/env python3
"""Validate decision-authority scenarios and their installable policy markers."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


SKILLS = {
    "apple-ui-direction",
    "apple-platform-adaptation",
    "apple-ui-review",
}
REQUIRED_TAGS = {
    "hard-boundary",
    "product-authority",
    "experience-baseline",
    "platform-advice",
    "shipped-evidence",
    "implementation-advice",
    "communication-pace",
    "internal-terminology",
}
REQUIRED_CASE_FIELDS = {
    "id",
    "owner_skill",
    "tags",
    "prompt",
    "expected_behavior",
    "forbidden_behavior",
    "source_markers",
}


def non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def non_empty_string_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(non_empty_string(item) for item in value)
    )


def validate(cases_path: Path, repo_root: Path | None = None) -> tuple[list[str], Counter[str]]:
    errors: list[str] = []
    coverage: Counter[str] = Counter()
    root = (repo_root or cases_path.resolve().parents[2]).resolve()

    try:
        suite = json.loads(cases_path.read_text(encoding="utf-8"))
    except OSError:
        return [f"missing decision-authority suite: {cases_path}"], coverage
    except json.JSONDecodeError as exc:
        return [f"decision-authority suite must be valid JSON: {exc}"], coverage

    if not isinstance(suite, dict):
        return ["decision-authority suite root must be an object"], coverage
    if suite.get("schema_version") != 1:
        errors.append("decision-authority schema_version must equal 1")
    if suite.get("suite") != "decision-authority":
        errors.append("suite must equal 'decision-authority'")
    if suite.get("linked_issue") != 6:
        errors.append("linked_issue must equal 6")
    if not non_empty_string(suite.get("purpose")):
        errors.append("purpose must be a non-empty string")

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

        skill = case["owner_skill"]
        if skill not in SKILLS:
            errors.append(f"{label}.owner_skill is invalid: {skill!r}")
        else:
            coverage[f"skill/{skill}"] += 1

        tags = case["tags"]
        if not non_empty_string_list(tags):
            errors.append(f"{label}.tags must be a non-empty string list")
        else:
            unknown_tags = set(tags) - REQUIRED_TAGS
            if unknown_tags:
                errors.append(f"{label}.tags contains unknown values: {sorted(unknown_tags)}")
            for tag in tags:
                coverage[f"tag/{tag}"] += 1

        for field in ("prompt",):
            if not non_empty_string(case[field]):
                errors.append(f"{label}.{field} must be a non-empty string")
        for field in ("expected_behavior", "forbidden_behavior"):
            if not non_empty_string_list(case[field]):
                errors.append(f"{label}.{field} must be a non-empty string list")

        source_markers = case["source_markers"]
        if not isinstance(source_markers, dict) or not source_markers:
            errors.append(f"{label}.source_markers must be a non-empty object")
            continue
        for source, markers in source_markers.items():
            source_label = f"{label}.source_markers.{source}"
            if not non_empty_string(source):
                errors.append(f"{source_label} path must be a non-empty string")
                continue
            path = Path(source)
            if (
                path.is_absolute()
                or ".." in path.parts
                or not path.is_relative_to(Path("plugins/apple-ui-design"))
            ):
                errors.append(f"{source_label} must stay inside plugins/apple-ui-design")
                continue
            resolved = (root / path).resolve()
            try:
                resolved.relative_to((root / "plugins" / "apple-ui-design").resolve())
            except ValueError:
                errors.append(f"{source_label} escapes the installable plugin")
                continue
            if not resolved.is_file():
                errors.append(f"{source_label} does not exist")
                continue
            if not non_empty_string_list(markers):
                errors.append(f"{source_label} markers must be a non-empty string list")
                continue
            contents = resolved.read_text(encoding="utf-8")
            for marker in markers:
                if marker not in contents:
                    errors.append(f"{source_label} missing policy marker: {marker!r}")

    for skill in sorted(SKILLS):
        if coverage[f"skill/{skill}"] == 0:
            errors.append(f"{skill} must own at least one decision-authority case")
    for tag in sorted(REQUIRED_TAGS):
        if coverage[f"tag/{tag}"] == 0:
            errors.append(f"decision-authority suite must cover tag: {tag}")

    return errors, coverage


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cases",
        type=Path,
        default=Path("evals/decision-authority/cases.json"),
    )
    args = parser.parse_args()
    errors, coverage = validate(args.cases)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "decision-authority evals valid: "
        f"{sum(value for key, value in coverage.items() if key.startswith('skill/'))} cases, "
        f"{sum(1 for tag in REQUIRED_TAGS if coverage[f'tag/{tag}'])} policy tags"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
