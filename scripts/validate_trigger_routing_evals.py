#!/usr/bin/env python3
"""Validate trigger ownership and design-engineering routing evaluation cases."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


REQUIRED_CASE_FIELDS = {
    "id",
    "case_kind",
    "request",
    "expected_primary_route",
    "allowed_support_routes",
    "framework",
    "engineering_domain",
    "implementation_scope",
    "must_do",
    "must_not_do",
}
VALID_CASE_KINDS = {"positive", "negative", "boundary"}
VALID_ROUTES = {
    "apple-ui-direction",
    "apple-platform-adaptation",
    "apple-ui-review",
    "engineering-workflow",
    "clarify-route",
}
DESIGN_ROUTES = {
    "apple-ui-direction",
    "apple-platform-adaptation",
    "apple-ui-review",
}
VALID_FRAMEWORKS = {"framework-neutral", "swiftui", "uikit", "appkit"}
VALID_IMPLEMENTATION_SCOPES = {
    "design-artifact-only",
    "adaptation-decision",
    "review-only",
    "bounded-design-led",
    "engineering-required",
    "mixed-handoff",
}
REQUIRED_NEGATIVE_DOMAINS = {
    "compilation",
    "concurrency",
    "architecture-performance",
    "api",
    "ci-release",
    "uikit-engineering",
    "appkit-engineering",
}


def non_empty_string_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, str) and bool(item.strip()) for item in value)
    )


def validate(path: Path) -> tuple[list[str], Counter[str]]:
    errors: list[str] = []
    coverage: Counter[str] = Counter()

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot load {path}: {exc}"], coverage

    if not isinstance(data, dict):
        return ["suite root must be an object"], coverage
    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if data.get("suite") != "trigger-routing":
        errors.append("suite must equal 'trigger-routing'")
    if not isinstance(data.get("purpose"), str) or not data["purpose"].strip():
        errors.append("purpose must be a non-empty string")

    linked_issues = data.get("linked_issues")
    if not isinstance(linked_issues, list) or not all(
        isinstance(issue, int) and issue > 0 for issue in linked_issues
    ):
        errors.append("linked_issues must be a list of positive integers")
    elif not {4, 5}.issubset(linked_issues):
        errors.append("linked_issues must connect Issue #5 to Issue #4")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a non-empty list"], coverage

    ids: set[str] = set()
    requests: set[str] = set()
    observed_design_routes: set[str] = set()
    observed_negative_domains: set[str] = set()

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

        request = case["request"]
        if not isinstance(request, str) or not request.strip():
            errors.append(f"{label}.request must be a non-empty string")
        elif request in requests:
            errors.append(f"duplicate case request: {request}")
        else:
            requests.add(request)

        case_kind = case["case_kind"]
        if case_kind not in VALID_CASE_KINDS:
            errors.append(f"{label}.case_kind is invalid: {case_kind!r}")
        else:
            coverage[f"kind/{case_kind}"] += 1

        route = case["expected_primary_route"]
        if route not in VALID_ROUTES:
            errors.append(f"{label}.expected_primary_route is invalid: {route!r}")
        else:
            coverage[f"route/{route}"] += 1
            if route in DESIGN_ROUTES:
                observed_design_routes.add(route)

        support_routes = case["allowed_support_routes"]
        if not isinstance(support_routes, list) or not all(
            isinstance(item, str) and item in VALID_ROUTES for item in support_routes
        ):
            errors.append(
                f"{label}.allowed_support_routes must contain only known routes"
            )
        elif route in support_routes:
            errors.append(f"{label} repeats its primary route as a support route")

        framework = case["framework"]
        if framework not in VALID_FRAMEWORKS:
            errors.append(f"{label}.framework is invalid: {framework!r}")
        else:
            coverage[f"framework/{framework}"] += 1

        scope = case["implementation_scope"]
        if scope not in VALID_IMPLEMENTATION_SCOPES:
            errors.append(f"{label}.implementation_scope is invalid: {scope!r}")
        else:
            coverage[f"scope/{scope}"] += 1

        domain = case["engineering_domain"]
        if not isinstance(domain, str) or not domain.strip():
            errors.append(f"{label}.engineering_domain must be a non-empty string")

        if case_kind == "positive" and route not in DESIGN_ROUTES:
            errors.append(f"{label} positive case must select a bundled design skill")
        if case_kind == "negative":
            if route != "engineering-workflow":
                errors.append(
                    f"{label} negative case must select engineering-workflow"
                )
            if scope != "engineering-required":
                errors.append(
                    f"{label} negative case must require engineering implementation"
                )
            if isinstance(domain, str):
                observed_negative_domains.add(domain)

        for field in ("must_do", "must_not_do"):
            if not non_empty_string_list(case[field]):
                errors.append(f"{label}.{field} must be a non-empty string list")

    for case_kind in sorted(VALID_CASE_KINDS):
        if coverage[f"kind/{case_kind}"] < 2:
            errors.append(f"at least two {case_kind} cases are required")

    missing_design_routes = DESIGN_ROUTES - observed_design_routes
    if missing_design_routes:
        errors.append(
            "missing positive or boundary route coverage: "
            + ", ".join(sorted(missing_design_routes))
        )

    missing_negative_domains = REQUIRED_NEGATIVE_DOMAINS - observed_negative_domains
    if missing_negative_domains:
        errors.append(
            "missing engineering-negative domains: "
            + ", ".join(sorted(missing_negative_domains))
        )

    for framework in ("swiftui", "uikit", "appkit"):
        if coverage[f"framework/{framework}"] < 2:
            errors.append(f"at least two {framework} cases are required")

    return errors, coverage


def main() -> int:
    parser = argparse.ArgumentParser()
    default_path = (
        Path(__file__).resolve().parents[1]
        / "evals"
        / "trigger-routing"
        / "cases.json"
    )
    parser.add_argument("path", nargs="?", type=Path, default=default_path)
    args = parser.parse_args()

    errors, coverage = validate(args.path)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1

    summary = ", ".join(
        f"{name}={count}"
        for name, count in sorted(coverage.items())
        if name.startswith("kind/")
    )
    print(f"trigger-routing evals valid: {sum(coverage[name] for name in coverage if name.startswith('kind/'))} cases ({summary})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
