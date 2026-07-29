#!/usr/bin/env python3
"""Evaluate a saved Codex trace and final response against one regression case."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SKILLS = (
    "apple-ui-direction",
    "apple-platform-adaptation",
    "apple-ui-review",
)


def load_cases(path: Path) -> dict[str, dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {case["id"]: case for case in payload["cases"]}


def installed_skill_was_loaded(trace: str, skill: str) -> bool:
    path_pattern = (
        r"plugins[/\\]cache[/\\]apple-ui-design[/\\]apple-ui-design"
        r"[/\\][^/\\]+[/\\]skills[/\\]"
        + re.escape(skill)
        + r"[/\\]SKILL\.md"
    )
    return re.search(path_pattern, trace, flags=re.IGNORECASE) is not None


def evaluate_case(
    case: dict,
    output: str,
    trace: str | None = None,
) -> list[str]:
    failures: list[str] = []
    assertions = case["output_assertions"]

    for pattern in assertions["required_all"]:
        if re.search(pattern, output, flags=re.MULTILINE) is None:
            failures.append(f"missing required output pattern: {pattern}")

    for group in assertions["required_any"]:
        if not any(re.search(pattern, output, flags=re.MULTILINE) for pattern in group):
            failures.append(
                "missing every pattern in required-any group: " + " | ".join(group)
            )

    for pattern in assertions["forbidden"]:
        if re.search(pattern, output, flags=re.MULTILINE) is not None:
            failures.append(f"matched forbidden output pattern: {pattern}")

    if trace is not None:
        route = case["expected_route"]
        for skill in route["must_load"]:
            if not installed_skill_was_loaded(trace, skill):
                failures.append(f"expected installed skill was not loaded: {skill}")
        for skill in route["must_not_load"]:
            if installed_skill_was_loaded(trace, skill):
                failures.append(f"forbidden installed skill was loaded: {skill}")

    return failures


def evaluate_goldens(
    cases_path: Path,
    goldens_path: Path,
    repo_root: Path,
) -> list[str]:
    failures: list[str] = []
    cases = load_cases(cases_path)
    payload = json.loads(goldens_path.read_text(encoding="utf-8"))
    for golden in payload["goldens"]:
        case_id = golden["case_id"]
        output = (repo_root / golden["output_path"]).read_text(encoding="utf-8")
        case_failures = evaluate_case(cases[case_id], output)
        failures.extend(f"{case_id}: {failure}" for failure in case_failures)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    repo_root = Path(__file__).resolve().parents[1]
    default_cases = repo_root / "evals" / "skill-regression" / "cases.json"
    default_goldens = repo_root / "evals" / "skill-regression" / "goldens.json"
    parser.add_argument("case_id", nargs="?")
    parser.add_argument("--cases", type=Path, default=default_cases)
    parser.add_argument("--trace", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--goldens", action="store_true")
    parser.add_argument("--goldens-path", type=Path, default=default_goldens)
    parser.add_argument("--repo-root", type=Path, default=repo_root)
    args = parser.parse_args()

    if args.goldens:
        failures = evaluate_goldens(
            args.cases, args.goldens_path, args.repo_root.resolve()
        )
        label = "golden outputs"
    else:
        if not args.case_id or args.output is None:
            parser.error("case_id and --output are required unless --goldens is used")
        cases = load_cases(args.cases)
        if args.case_id not in cases:
            parser.error(f"unknown case id: {args.case_id}")
        output = args.output.read_text(encoding="utf-8")
        trace = (
            args.trace.read_text(encoding="utf-8", errors="replace")
            if args.trace
            else None
        )
        failures = evaluate_case(cases[args.case_id], output, trace)
        label = args.case_id

    for failure in failures:
        print(f"error: {failure}", file=sys.stderr)
    if failures:
        return 1
    print(f"skill regression output valid: {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
