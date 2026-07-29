#!/usr/bin/env python3
"""Validate all six mode-level delivery contract evaluation cases."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


CONTRACT_OWNERS = {
    "visual-direction": "apple-ui-direction",
    "screen-flow": "apple-ui-direction",
    "design-system": "apple-ui-direction",
    "platform-adaptation": "apple-platform-adaptation",
    "native-prototype": "apple-ui-direction",
    "ui-review": "apple-ui-review",
}
VALID_STARTING_POINTS = {"existing-product", "zero-to-one"}
REQUIRED_CASE_FIELDS = {
    "id",
    "contract",
    "owner_skill",
    "starting_point",
    "request",
    "fixture_paths",
    "run_evidence_paths",
    "expected_artifacts",
    "evidence_requirements",
    "forbidden_claims",
    "assertions",
}


def non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def non_empty_string_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(non_empty_string(item) for item in value)
    )


def validate(path: Path, repo_root: Path | None = None) -> tuple[list[str], Counter[str]]:
    errors: list[str] = []
    coverage: Counter[str] = Counter()
    root = (repo_root or path.resolve().parents[2]).resolve()

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot load {path}: {exc}"], coverage

    if not isinstance(data, dict):
        return ["suite root must be an object"], coverage

    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if data.get("suite") != "delivery-contracts":
        errors.append("suite must equal 'delivery-contracts'")
    if not non_empty_string(data.get("purpose")):
        errors.append("purpose must be a non-empty string")

    linked_issues = data.get("linked_issues")
    if not isinstance(linked_issues, list) or not all(
        isinstance(issue, int) and issue > 0 for issue in linked_issues
    ):
        errors.append("linked_issues must be a list of positive integers")
    elif not {3, 4, 14}.issubset(linked_issues):
        errors.append("linked_issues must include Issues #3, #4, and #14")

    cases = data.get("cases")
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

        contract = case["contract"]
        if contract not in CONTRACT_OWNERS:
            errors.append(f"{label}.contract is invalid: {contract!r}")
        else:
            coverage[contract] += 1
            expected_owner = CONTRACT_OWNERS[contract]
            if case["owner_skill"] != expected_owner:
                errors.append(
                    f"{label}.owner_skill must be {expected_owner!r} "
                    f"for contract {contract!r}"
                )

        if case["starting_point"] not in VALID_STARTING_POINTS:
            errors.append(
                f"{label}.starting_point is invalid: {case['starting_point']!r}"
            )
        if not non_empty_string(case["request"]):
            errors.append(f"{label}.request must be a non-empty string")

        fixture_paths = case["fixture_paths"]
        if not non_empty_string_list(fixture_paths):
            errors.append(f"{label}.fixture_paths must be a non-empty string list")
        else:
            for fixture_index, fixture_value in enumerate(fixture_paths):
                fixture = Path(fixture_value)
                expected_prefix = Path("evals/delivery-contracts/fixtures")
                if (
                    fixture.is_absolute()
                    or ".." in fixture.parts
                    or not fixture.is_relative_to(expected_prefix)
                ):
                    errors.append(
                        f"{label}.fixture_paths[{fixture_index}] must stay in "
                        "evals/delivery-contracts/fixtures"
                    )
                    continue
                resolved = (root / fixture).resolve()
                try:
                    resolved.relative_to(root)
                except ValueError:
                    errors.append(
                        f"{label}.fixture_paths[{fixture_index}] escapes the repository"
                    )
                    continue
                if not resolved.is_file():
                    errors.append(f"{label} fixture does not exist: {fixture_value}")

        run_evidence_paths = case["run_evidence_paths"]
        if not non_empty_string_list(run_evidence_paths):
            errors.append(
                f"{label}.run_evidence_paths must be a non-empty string list"
            )
        else:
            for evidence_index, evidence_value in enumerate(run_evidence_paths):
                evidence = Path(evidence_value)
                expected_prefix = Path("evals/delivery-contracts/runs")
                if (
                    evidence.is_absolute()
                    or ".." in evidence.parts
                    or not evidence.is_relative_to(expected_prefix)
                ):
                    errors.append(
                        f"{label}.run_evidence_paths[{evidence_index}] must stay in "
                        "evals/delivery-contracts/runs"
                    )
                    continue
                resolved = (root / evidence).resolve()
                try:
                    resolved.relative_to(root)
                except ValueError:
                    errors.append(
                        f"{label}.run_evidence_paths[{evidence_index}] "
                        "escapes the repository"
                    )
                    continue
                if not resolved.is_file():
                    errors.append(
                        f"{label} run evidence does not exist: {evidence_value}"
                    )

        for field in (
            "expected_artifacts",
            "evidence_requirements",
            "forbidden_claims",
        ):
            if not non_empty_string_list(case[field]):
                errors.append(f"{label}.{field} must be a non-empty string list")

        assertions = case["assertions"]
        if not isinstance(assertions, dict):
            errors.append(f"{label}.assertions must be an object")
        else:
            for assertion_name in ("must_do", "must_not_do"):
                if not non_empty_string_list(assertions.get(assertion_name)):
                    errors.append(
                        f"{label}.assertions.{assertion_name} "
                        "must be a non-empty string list"
                    )

    for contract in sorted(CONTRACT_OWNERS):
        count = coverage[contract]
        if count == 0:
            errors.append(f"missing required contract: {contract}")
        elif count > 1:
            errors.append(
                f"contract must have exactly one evaluation case: {contract}={count}"
            )

    return errors, coverage


def main() -> int:
    parser = argparse.ArgumentParser()
    default_path = (
        Path(__file__).resolve().parents[1]
        / "evals"
        / "delivery-contracts"
        / "cases.json"
    )
    parser.add_argument("path", nargs="?", type=Path, default=default_path)
    parser.add_argument("--repo-root", type=Path)
    args = parser.parse_args()

    errors, coverage = validate(args.path, args.repo_root)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1

    summary = ", ".join(
        f"{contract}={coverage[contract]}" for contract in sorted(coverage)
    )
    print(f"delivery contract evals valid: {sum(coverage.values())} cases ({summary})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
