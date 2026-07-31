#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


REQUIRED_CASE_FIELDS = {
    "id",
    "flow",
    "skill",
    "tags",
    "prompt",
    "expected_behavior",
    "forbidden_behavior",
    "source_markers",
}
REQUIRED_CASE_IDS = {
    "photo-permission-denial-limited",
    "account-export-deletion",
    "subscription-trial-paywall-review",
    "cross-platform-account-commerce-adaptation",
    "financial-transfer-error-content",
    "health-insight-professional-boundary",
    "mocked-system-and-service-evidence",
}
REQUIRED_SKILLS = {
    "apple-ui-direction",
    "apple-platform-adaptation",
    "apple-ui-review",
}
REQUIRED_FLOWS = {
    "content-recovery",
    "permission-privacy",
    "identity-account-data",
    "commerce",
    "regulated-professional",
}
REQUIRED_TAGS = {
    "content-clarity",
    "permission-control",
    "privacy-minimization",
    "identity-data-control",
    "commerce-transparency",
    "failure-recovery",
    "professional-boundary",
    "evidence-boundary",
}
REQUIRED_SOURCE_URLS = {
    "https://developer.apple.com/design/human-interface-guidelines/writing",
    "https://developer.apple.com/design/human-interface-guidelines/privacy",
    "https://developer.apple.com/design/human-interface-guidelines/in-app-purchase",
    "https://developer.apple.com/app-store/subscriptions/",
    "https://developer.apple.com/app-store/review/guidelines/",
    "https://developer.apple.com/support/offering-account-deletion-in-your-app/",
    "https://developer.apple.com/app-store/app-privacy-details/",
}
REQUIRED_EVIDENCE_PATHS = {
    "evals/delivery-contracts/runs/2026-07-29/screen-flow/design-brief.md",
    "evals/delivery-contracts/runs/2026-07-29/screen-flow/flow-map.md",
    "evals/delivery-contracts/runs/2026-07-29/screen-flow/evidence/operations-tested.json",
}
REQUIRED_FORWARD_TEST_SCENARIOS = {
    "subscription-trial-paywall-review",
    "health-insight-professional-boundary",
}
REQUIRED_FORWARD_TEST_PATH = "evals/content-sensitive-flows/runs/2026-07-31.md"


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
        return [f"missing content-sensitive-flows suite: {cases_path}"], coverage
    except json.JSONDecodeError as exc:
        return [f"content-sensitive-flows suite must be valid JSON: {exc}"], coverage

    if not isinstance(suite, dict):
        return ["content-sensitive-flows suite root must be an object"], coverage
    if suite.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if suite.get("suite") != "content-sensitive-flows":
        errors.append("suite must equal 'content-sensitive-flows'")
    if suite.get("linked_issue") != 8:
        errors.append("linked_issue must equal 8")
    if not non_empty_string(suite.get("purpose")):
        errors.append("purpose must be a non-empty string")

    declared_tags = suite.get("required_tags")
    if not non_empty_string_list(declared_tags):
        errors.append("required_tags must be a non-empty string list")
        declared_tag_set: set[str] = set()
    else:
        declared_tag_set = set(declared_tags)
        if declared_tag_set != REQUIRED_TAGS:
            errors.append("required_tags must match the Issue #8 coverage contract")

    source_review = suite.get("source_review")
    if not isinstance(source_review, dict):
        errors.append("source_review must be an object")
    else:
        if source_review.get("accessed") != "2026-07-31":
            errors.append("source_review.accessed must equal 2026-07-31")
        urls = source_review.get("urls")
        if not non_empty_string_list(urls):
            errors.append("source_review.urls must be a non-empty string list")
        elif set(urls) != REQUIRED_SOURCE_URLS:
            errors.append("source_review.urls must match the Issue #8 official-source set")
        try:
            maintenance = (root / "docs" / "maintenance-and-sources.md").read_text(
                encoding="utf-8"
            )
        except OSError:
            errors.append("maintenance source record is missing")
        else:
            for url in REQUIRED_SOURCE_URLS:
                if url not in maintenance:
                    errors.append(f"maintenance source record missing URL: {url}")

    evidence = suite.get("preserved_evidence")
    if not isinstance(evidence, dict):
        errors.append("preserved_evidence must be an object")
    else:
        if evidence.get("flow") != "permission-privacy":
            errors.append("preserved_evidence.flow must equal 'permission-privacy'")
        artifacts = evidence.get("artifacts")
        if not non_empty_string_list(artifacts):
            errors.append("preserved_evidence.artifacts must be a non-empty string list")
        else:
            if set(artifacts) != REQUIRED_EVIDENCE_PATHS:
                errors.append("preserved evidence paths must match the FrameKeep record")
            for relative_path in artifacts:
                validate_repository_path(relative_path, root, "evidence artifact", errors)
        for field in ("supports", "does_not_support"):
            if not non_empty_string_list(evidence.get(field)):
                errors.append(f"preserved_evidence.{field} must be a non-empty string list")

    forward_test = suite.get("forward_test_record")
    if not isinstance(forward_test, dict):
        errors.append("forward_test_record must be an object")
    else:
        path = forward_test.get("path")
        if path != REQUIRED_FORWARD_TEST_PATH:
            errors.append("forward_test_record.path must match the Issue #8 run record")
        else:
            validate_repository_path(path, root, "forward-test record", errors)
        scenarios = forward_test.get("scenarios")
        if not non_empty_string_list(scenarios):
            errors.append("forward_test_record.scenarios must be a non-empty string list")
        elif set(scenarios) != REQUIRED_FORWARD_TEST_SCENARIOS:
            errors.append("forward-test scenarios must match the two Issue #8 product runs")

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

        flow = case["flow"]
        if flow not in REQUIRED_FLOWS:
            errors.append(f"{label}.flow is not a supported sensitive-flow family")
        else:
            coverage[f"flow/{flow}"] += 1

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
        errors.append("case ids must match the seven Issue #8 regression scenarios")
    for skill in sorted(REQUIRED_SKILLS):
        if coverage[f"skill/{skill}"] == 0:
            errors.append(f"suite must cover skill: {skill}")
    for flow in sorted(REQUIRED_FLOWS):
        if coverage[f"flow/{flow}"] == 0:
            errors.append(f"suite must cover flow: {flow}")
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
    cases_path = repo_root / "evals" / "content-sensitive-flows" / "cases.json"
    errors, coverage = validate(cases_path, repo_root=repo_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    case_count = sum(value for key, value in coverage.items() if key.startswith("flow/"))
    print(f"Content-sensitive-flow suite is valid ({case_count} cases).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
