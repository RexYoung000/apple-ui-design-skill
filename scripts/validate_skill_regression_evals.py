#!/usr/bin/env python3
"""Validate the unified Apple UI skill trigger and output regression matrix."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path


SKILLS = {
    "apple-ui-direction",
    "apple-platform-adaptation",
    "apple-ui-review",
}
SCENARIO_TYPES = {"direct", "indirect", "incomplete", "negative", "risk"}
REQUIRED_CASE_FIELDS = {
    "id",
    "owner_skill",
    "scenario_type",
    "request",
    "fixture_paths",
    "expected_route",
    "output_assertions",
    "behavior",
}


def non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def non_empty_string_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(non_empty_string(item) for item in value)
    )


def load_json(path: Path, label: str, errors: list[str]) -> dict | None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        errors.append(f"missing {label}: {path}")
        return None
    except json.JSONDecodeError as exc:
        errors.append(f"{label} must be valid JSON: {exc}")
        return None
    if not isinstance(payload, dict):
        errors.append(f"{label} root must be an object")
        return None
    return payload


def validate_repo_path(
    value: object,
    *,
    label: str,
    root: Path,
    required_prefix: Path | None,
    errors: list[str],
) -> Path | None:
    if not non_empty_string(value):
        errors.append(f"{label} must be a non-empty path string")
        return None
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        errors.append(f"{label} must stay inside the repository")
        return None
    if required_prefix is not None and not path.is_relative_to(required_prefix):
        errors.append(f"{label} must stay in {required_prefix}")
        return None
    resolved = (root / path).resolve()
    try:
        resolved.relative_to(root)
    except ValueError:
        errors.append(f"{label} escapes the repository")
        return None
    if not resolved.is_file():
        errors.append(f"{label} does not exist: {value}")
        return None
    return resolved


def validate(
    cases_path: Path,
    goldens_path: Path,
    repo_root: Path | None = None,
) -> tuple[list[str], Counter[str]]:
    errors: list[str] = []
    coverage: Counter[str] = Counter()
    root = (repo_root or cases_path.resolve().parents[2]).resolve()

    suite = load_json(cases_path, "skill regression suite", errors)
    goldens = load_json(goldens_path, "golden registry", errors)
    if suite is None or goldens is None:
        return errors, coverage

    if suite.get("schema_version") != 1:
        errors.append("skill regression schema_version must equal 1")
    if suite.get("suite") != "skill-regression":
        errors.append("suite must equal 'skill-regression'")
    if not non_empty_string(suite.get("purpose")):
        errors.append("purpose must be a non-empty string")
    linked_issues = suite.get("linked_issues")
    if not isinstance(linked_issues, list) or not {2, 3, 4, 5, 6}.issubset(
        {issue for issue in linked_issues if isinstance(issue, int)}
    ):
        errors.append("linked_issues must include Issues #2, #3, #4, #5, and #6")

    policy_sources = suite.get("skill_policy_sources")
    if not isinstance(policy_sources, dict) or set(policy_sources) != SKILLS:
        errors.append("skill_policy_sources must define exactly the three bundled skills")
    else:
        for skill, policy in policy_sources.items():
            label = f"skill_policy_sources.{skill}"
            if not isinstance(policy, dict):
                errors.append(f"{label} must be an object")
                continue
            resolved = validate_repo_path(
                policy.get("path"),
                label=f"{label}.path",
                root=root,
                required_prefix=Path("plugins/apple-ui-design/skills") / skill,
                errors=errors,
            )
            markers = policy.get("required_markers")
            if not non_empty_string_list(markers):
                errors.append(f"{label}.required_markers must be non-empty")
            elif resolved is not None:
                contents = resolved.read_text(encoding="utf-8")
                for marker in markers:
                    if marker not in contents:
                        errors.append(
                            f"{label} missing required skill behavior marker: {marker!r}"
                        )

    cases = suite.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a non-empty list"], coverage

    ids: set[str] = set()
    cases_by_id: dict[str, dict] = {}
    fixture_prefix = Path("evals/skill-regression/fixtures")

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
            cases_by_id[case_id] = case

        skill = case["owner_skill"]
        scenario = case["scenario_type"]
        if skill not in SKILLS:
            errors.append(f"{label}.owner_skill is invalid: {skill!r}")
        if scenario not in SCENARIO_TYPES:
            errors.append(f"{label}.scenario_type is invalid: {scenario!r}")
        if skill in SKILLS and scenario in SCENARIO_TYPES:
            coverage[f"{skill}/{scenario}"] += 1
            coverage[f"skill/{skill}"] += 1
            coverage[f"scenario/{scenario}"] += 1

        if not non_empty_string(case["request"]):
            errors.append(f"{label}.request must be a non-empty string")
        elif scenario == "direct" and f"${skill}" not in case["request"]:
            errors.append(f"{label} direct request must name ${skill}")
        elif scenario == "indirect" and "$apple-" in case["request"]:
            errors.append(f"{label} indirect request must not name a skill")

        fixtures = case["fixture_paths"]
        if not non_empty_string_list(fixtures):
            errors.append(f"{label}.fixture_paths must be a non-empty string list")
        else:
            for fixture_index, fixture in enumerate(fixtures):
                validate_repo_path(
                    fixture,
                    label=f"{label}.fixture_paths[{fixture_index}]",
                    root=root,
                    required_prefix=fixture_prefix,
                    errors=errors,
                )

        route = case["expected_route"]
        if not isinstance(route, dict):
            errors.append(f"{label}.expected_route must be an object")
        else:
            must_load = route.get("must_load")
            must_not_load = route.get("must_not_load")
            if not isinstance(must_load, list) or not all(
                item in SKILLS for item in must_load
            ):
                errors.append(f"{label}.expected_route.must_load is invalid")
            if not isinstance(must_not_load, list) or not all(
                item in SKILLS for item in must_not_load
            ):
                errors.append(f"{label}.expected_route.must_not_load is invalid")
            if isinstance(must_load, list) and isinstance(must_not_load, list):
                if set(must_load) & set(must_not_load):
                    errors.append(f"{label} cannot both load and forbid a skill")
                if scenario == "negative":
                    if must_load or set(must_not_load) != SKILLS:
                        errors.append(
                            f"{label} negative case must forbid all bundled skills"
                        )
                elif must_load != [skill] or set(must_not_load) != SKILLS - {skill}:
                    errors.append(
                        f"{label} must load only its owner skill and forbid the others"
                    )

        assertions = case["output_assertions"]
        if not isinstance(assertions, dict):
            errors.append(f"{label}.output_assertions must be an object")
        else:
            required_all = assertions.get("required_all")
            required_any = assertions.get("required_any")
            forbidden = assertions.get("forbidden")
            if not non_empty_string_list(required_all):
                errors.append(
                    f"{label}.output_assertions.required_all must be non-empty"
                )
            if (
                not isinstance(required_any, list)
                or not required_any
                or not all(non_empty_string_list(group) for group in required_any)
            ):
                errors.append(
                    f"{label}.output_assertions.required_any must contain "
                    "non-empty pattern groups"
                )
            if not non_empty_string_list(forbidden):
                errors.append(
                    f"{label}.output_assertions.forbidden must be non-empty"
                )
            pattern_lists: list[list[str]] = []
            if isinstance(required_all, list):
                pattern_lists.append(required_all)
            if isinstance(required_any, list):
                pattern_lists.extend(
                    group for group in required_any if isinstance(group, list)
                )
            if isinstance(forbidden, list):
                pattern_lists.append(forbidden)
            for patterns in pattern_lists:
                for pattern in patterns:
                    if not isinstance(pattern, str):
                        continue
                    try:
                        re.compile(pattern)
                    except re.error as exc:
                        errors.append(
                            f"{label} contains invalid regex {pattern!r}: {exc}"
                        )

        behavior = case["behavior"]
        if not isinstance(behavior, dict):
            errors.append(f"{label}.behavior must be an object")
        else:
            for field in ("must_do", "must_not_do"):
                if not non_empty_string_list(behavior.get(field)):
                    errors.append(f"{label}.behavior.{field} must be non-empty")

    for skill in sorted(SKILLS):
        if coverage[f"skill/{skill}"] != len(SCENARIO_TYPES):
            errors.append(f"{skill} must have exactly five regression cases")
        for scenario in sorted(SCENARIO_TYPES):
            count = coverage[f"{skill}/{scenario}"]
            if count != 1:
                errors.append(
                    f"{skill} must have exactly one {scenario} case; found {count}"
                )

    if goldens.get("schema_version") != 1:
        errors.append("golden registry schema_version must equal 1")
    entries = goldens.get("goldens")
    if not isinstance(entries, list) or not entries:
        errors.append("at least one golden output is required")
    else:
        golden_case_ids: set[str] = set()
        for index, entry in enumerate(entries):
            label = f"goldens[{index}]"
            if not isinstance(entry, dict):
                errors.append(f"{label} must be an object")
                continue
            case_id = entry.get("case_id")
            if case_id not in cases_by_id:
                errors.append(f"{label}.case_id does not match a regression case")
            elif case_id in golden_case_ids:
                errors.append(f"duplicate golden case id: {case_id}")
            else:
                golden_case_ids.add(case_id)
            if entry.get("review_status") != "reviewed":
                errors.append(f"{label}.review_status must equal 'reviewed'")
            if not non_empty_string(entry.get("rationale")):
                errors.append(f"{label}.rationale must be a non-empty string")
            resolved = validate_repo_path(
                entry.get("output_path"),
                label=f"{label}.output_path",
                root=root,
                required_prefix=Path("evals"),
                errors=errors,
            )
            checksum = entry.get("sha256")
            if not isinstance(checksum, str) or not re.fullmatch(
                r"[0-9a-f]{64}", checksum
            ):
                errors.append(f"{label}.sha256 must be a lowercase SHA-256")
            elif resolved is not None:
                actual = hashlib.sha256(resolved.read_bytes()).hexdigest()
                if actual != checksum:
                    errors.append(
                        f"{label} checksum mismatch: expected {checksum}, got {actual}"
                    )

    return errors, coverage


def main() -> int:
    parser = argparse.ArgumentParser()
    repo_root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "cases",
        nargs="?",
        type=Path,
        default=repo_root / "evals" / "skill-regression" / "cases.json",
    )
    parser.add_argument(
        "--goldens",
        type=Path,
        default=repo_root / "evals" / "skill-regression" / "goldens.json",
    )
    parser.add_argument("--repo-root", type=Path, default=repo_root)
    args = parser.parse_args()

    errors, coverage = validate(args.cases, args.goldens, args.repo_root)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1
    print(
        "skill regression suite valid: "
        f"{sum(coverage[f'scenario/{name}'] for name in SCENARIO_TYPES)} cases, "
        f"{len(SKILLS)} skills x {len(SCENARIO_TYPES)} scenarios"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
