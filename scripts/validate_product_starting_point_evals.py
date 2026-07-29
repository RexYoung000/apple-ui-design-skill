#!/usr/bin/env python3
"""Validate the fixed existing-product and zero-to-one evaluation suite."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


REQUIRED_CASE_FIELDS = {
    "id",
    "starting_point",
    "decision_scale",
    "request",
    "fixture_paths",
    "mode_contract_inputs",
    "assertions",
}
REQUIRED_SCENARIOS = {
    ("existing-product", "small-reversible"),
    ("existing-product", "major-redesign"),
    ("zero-to-one", "new-direction"),
}
VALID_STARTING_POINTS = {"existing-product", "zero-to-one"}
VALID_DECISION_SCALES = {"small-reversible", "major-redesign", "new-direction"}


def non_empty_string_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, str) and bool(item.strip()) for item in value)
    )


def validate(path: Path, repo_root: Path | None = None) -> tuple[list[str], Counter[str]]:
    errors: list[str] = []
    scenarios: Counter[str] = Counter()
    root = (repo_root or path.resolve().parents[2]).resolve()

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot load {path}: {exc}"], scenarios

    if not isinstance(data, dict):
        return ["suite root must be an object"], scenarios

    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if data.get("suite") != "product-starting-point":
        errors.append("suite must equal 'product-starting-point'")
    if not non_empty_string_list(data.get("purpose", "").splitlines()):
        errors.append("purpose must be a non-empty string")

    linked_issues = data.get("linked_issues")
    if not isinstance(linked_issues, list) or not all(
        isinstance(issue, int) and issue > 0 for issue in linked_issues
    ):
        errors.append("linked_issues must be a list of positive integers")
    elif not {13, 3, 4}.issubset(linked_issues):
        errors.append("linked_issues must connect Issue #13 to Issues #3 and #4")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a non-empty list"], scenarios

    ids: set[str] = set()
    observed_scenarios: set[tuple[str, str]] = set()

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
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{label}.id must be a non-empty string")
        elif case_id in ids:
            errors.append(f"duplicate case id: {case_id}")
        else:
            ids.add(case_id)

        starting_point = case["starting_point"]
        decision_scale = case["decision_scale"]
        if starting_point not in VALID_STARTING_POINTS:
            errors.append(f"{label}.starting_point is invalid: {starting_point!r}")
        if decision_scale not in VALID_DECISION_SCALES:
            errors.append(f"{label}.decision_scale is invalid: {decision_scale!r}")
        if starting_point in VALID_STARTING_POINTS and decision_scale in VALID_DECISION_SCALES:
            observed_scenarios.add((starting_point, decision_scale))
            scenarios[f"{starting_point}/{decision_scale}"] += 1

        if not isinstance(case["request"], str) or not case["request"].strip():
            errors.append(f"{label}.request must be a non-empty string")

        fixture_paths = case["fixture_paths"]
        if not non_empty_string_list(fixture_paths):
            errors.append(f"{label}.fixture_paths must be a non-empty string list")
        else:
            for fixture_index, fixture_value in enumerate(fixture_paths):
                fixture = Path(fixture_value)
                if fixture.is_absolute() or ".." in fixture.parts:
                    errors.append(
                        f"{label}.fixture_paths[{fixture_index}] must stay inside the repository"
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

        if not non_empty_string_list(case["mode_contract_inputs"]):
            errors.append(f"{label}.mode_contract_inputs must be a non-empty string list")

        assertions = case["assertions"]
        if not isinstance(assertions, dict):
            errors.append(f"{label}.assertions must be an object")
        else:
            for assertion_name in ("must_do", "must_not_do"):
                if not non_empty_string_list(assertions.get(assertion_name)):
                    errors.append(
                        f"{label}.assertions.{assertion_name} must be a non-empty string list"
                    )

    missing_scenarios = REQUIRED_SCENARIOS - observed_scenarios
    for starting_point, decision_scale in sorted(missing_scenarios):
        errors.append(f"missing required scenario: {starting_point}/{decision_scale}")

    return errors, scenarios


def main() -> int:
    parser = argparse.ArgumentParser()
    default_path = (
        Path(__file__).resolve().parents[1]
        / "evals"
        / "product-starting-point"
        / "cases.json"
    )
    parser.add_argument("path", nargs="?", type=Path, default=default_path)
    parser.add_argument("--repo-root", type=Path)
    args = parser.parse_args()

    errors, scenarios = validate(args.path, args.repo_root)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1

    scenario_summary = ", ".join(
        f"{name}={count}" for name, count in sorted(scenarios.items())
    )
    print(
        f"product starting-point evals valid: "
        f"{sum(scenarios.values())} cases ({scenario_summary})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
