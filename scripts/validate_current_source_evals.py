#!/usr/bin/env python3
"""Validate current Apple source scenarios and preserved verification records."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlsplit


SKILLS = {
    "apple-ui-direction",
    "apple-platform-adaptation",
    "apple-ui-review",
}
REQUIRED_TAGS = {
    "exact-source",
    "access-failure",
    "version-split",
    "runtime-conflict",
    "evidence-labeling",
    "new-capability-record",
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
REQUIRED_RECORD_FIELDS = {
    "schema_version",
    "id",
    "status",
    "verified_on",
    "claim",
    "claim_type",
    "product_context",
    "official_sources",
    "version_scope",
    "runtime_evidence",
    "evidence_labels",
    "conflicts",
    "remaining_unverified",
}
VALID_RECORD_STATUSES = {"verified", "partially-verified", "unverified"}
VALID_RUNTIME_STATUSES = {"not-run", "compile-verified", "runtime-verified"}
BROAD_APPLE_PATHS = {
    "/",
    "/documentation",
    "/documentation/",
    "/design/human-interface-guidelines",
    "/design/human-interface-guidelines/",
    "/design/resources",
    "/design/resources/",
    "/videos",
    "/videos/",
}


def non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def non_empty_string_list(value: object) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(non_empty_string(item) for item in value)
    )


def parse_date(value: object, field: str, errors: list[str]) -> date | None:
    try:
        parsed = datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        errors.append(f"{field} must use YYYY-MM-DD: {value!r}")
        return None
    if parsed > date.today():
        errors.append(f"{field} cannot be in the future")
    return parsed


def resolve_repo_file(
    value: object,
    field: str,
    repo_root: Path,
    allowed_root: Path,
    errors: list[str],
) -> Path | None:
    if not non_empty_string(value):
        errors.append(f"{field} must be a non-empty repository-relative path")
        return None
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        errors.append(f"{field} must stay inside {allowed_root.as_posix()}")
        return None
    try:
        path.relative_to(allowed_root)
    except ValueError:
        errors.append(f"{field} must stay inside {allowed_root.as_posix()}")
        return None
    resolved = (repo_root / path).resolve()
    try:
        resolved.relative_to((repo_root / allowed_root).resolve())
    except ValueError:
        errors.append(f"{field} escapes {allowed_root.as_posix()}")
        return None
    if not resolved.is_file():
        errors.append(f"{field} does not exist: {value}")
        return None
    return resolved


def validate_record(
    record: object,
    record_path: Path,
    repo_root: Path,
) -> list[str]:
    errors: list[str] = []
    label = f"record {record_path.as_posix()}"
    if not isinstance(record, dict):
        return [f"{label} must be an object"]

    missing = sorted(REQUIRED_RECORD_FIELDS - record.keys())
    if missing:
        return [f"{label} missing fields: {', '.join(missing)}"]
    if record["schema_version"] != 1:
        errors.append(f"{label}.schema_version must equal 1")
    for field in ("id", "claim", "claim_type"):
        if not non_empty_string(record[field]):
            errors.append(f"{label}.{field} must be a non-empty string")

    status = record["status"]
    if status not in VALID_RECORD_STATUSES:
        errors.append(f"{label}.status is invalid: {status!r}")
    if status == "unverified" and not non_empty_string(record.get("unverified_reason")):
        errors.append(f"{label}.unverified_reason is required when status is unverified")
    parse_date(record["verified_on"], f"{label}.verified_on", errors)

    product_context = record["product_context"]
    if not isinstance(product_context, dict):
        errors.append(f"{label}.product_context must be an object")
    else:
        if not non_empty_string_list(product_context.get("target_platforms")):
            errors.append(f"{label}.product_context.target_platforms must be a non-empty string list")
        if not non_empty_string(product_context.get("decision")):
            errors.append(f"{label}.product_context.decision must be a non-empty string")

    official_sources = record["official_sources"]
    if status != "unverified" and (not isinstance(official_sources, list) or not official_sources):
        errors.append(f"{label}.official_sources must be non-empty for verified records")
    if not isinstance(official_sources, list):
        errors.append(f"{label}.official_sources must be a list")
        official_sources = []
    for index, source in enumerate(official_sources):
        source_label = f"{label}.official_sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{source_label} must be an object")
            continue
        for field in ("title", "url", "accessed_on", "supports"):
            if field not in source:
                errors.append(f"{source_label} missing field: {field}")
        if not non_empty_string(source.get("title")):
            errors.append(f"{source_label}.title must be a non-empty string")
        url = source.get("url")
        parts = urlsplit(url) if isinstance(url, str) else None
        if (
            not parts
            or parts.scheme != "https"
            or parts.netloc.lower() != "developer.apple.com"
            or parts.path in BROAD_APPLE_PATHS
        ):
            errors.append(f"{source_label}.url must be an exact HTTPS Apple Developer page: {url!r}")
        parse_date(source.get("accessed_on"), f"{source_label}.accessed_on", errors)
        if not non_empty_string_list(source.get("supports")):
            errors.append(f"{source_label}.supports must be a non-empty string list")

    version_scope = record["version_scope"]
    if not isinstance(version_scope, dict):
        errors.append(f"{label}.version_scope must be an object")
    else:
        minimum = version_scope.get("project_minimum_versions")
        enhancement = version_scope.get("enhancement_versions")
        for field, value in (
            ("project_minimum_versions", minimum),
            ("enhancement_versions", enhancement),
        ):
            if (
                not isinstance(value, dict)
                or not value
                or not all(non_empty_string(key) and non_empty_string(item) for key, item in value.items())
            ):
                errors.append(f"{label}.version_scope.{field} must be a non-empty string map")
        if isinstance(minimum, dict) and isinstance(enhancement, dict):
            shared = set(minimum) & set(enhancement)
            if not shared:
                errors.append(f"{label}.version_scope must compare at least one shared platform")
            elif all(minimum[key] == enhancement[key] for key in shared):
                errors.append(f"{label}.version_scope must separate minimum and enhancement versions")
        if not non_empty_string(version_scope.get("fallback")):
            errors.append(f"{label}.version_scope.fallback must be a non-empty string")

    runtime = record["runtime_evidence"]
    if not isinstance(runtime, dict):
        errors.append(f"{label}.runtime_evidence must be an object")
    else:
        runtime_status = runtime.get("status")
        if runtime_status not in VALID_RUNTIME_STATUSES:
            errors.append(f"{label}.runtime_evidence.status is invalid: {runtime_status!r}")
        environment = runtime.get("environment")
        if not isinstance(environment, dict) or not environment:
            errors.append(f"{label}.runtime_evidence.environment must be a non-empty object")
        elif not all(non_empty_string(key) and non_empty_string(value) for key, value in environment.items()):
            errors.append(f"{label}.runtime_evidence.environment must contain non-empty strings")
        checks = runtime.get("checks")
        if runtime_status != "not-run" and (not isinstance(checks, list) or not checks):
            errors.append(f"{label}.runtime_evidence.checks must be non-empty when evidence was run")
        if not isinstance(checks, list):
            errors.append(f"{label}.runtime_evidence.checks must be a list")
            checks = []
        for index, check in enumerate(checks):
            check_label = f"{label}.runtime_evidence.checks[{index}]"
            if not isinstance(check, dict):
                errors.append(f"{check_label} must be an object")
                continue
            for field in ("id", "expected", "result"):
                if not non_empty_string(check.get(field)):
                    errors.append(f"{check_label}.{field} must be a non-empty string")
            resolve_repo_file(
                check.get("evidence"),
                f"{check_label}.evidence",
                repo_root,
                Path("evals/current-source-verification"),
                errors,
            )

    labels = record["evidence_labels"]
    required_labels = {"official_source", "project_runtime", "design_inference"}
    if not isinstance(labels, dict):
        errors.append(f"{label}.evidence_labels must be an object")
    else:
        missing_labels = sorted(required_labels - labels.keys())
        if missing_labels:
            errors.append(f"{label}.evidence_labels missing fields: {', '.join(missing_labels)}")
        for field in required_labels:
            if field in labels and not non_empty_string(labels[field]):
                errors.append(f"{label}.evidence_labels.{field} must be a non-empty string")

    if not isinstance(record["conflicts"], list):
        errors.append(f"{label}.conflicts must be a list")
    if not non_empty_string_list(record["remaining_unverified"]):
        errors.append(f"{label}.remaining_unverified must be a non-empty string list")

    return errors


def validate(
    cases_path: Path,
    repo_root: Path | None = None,
) -> tuple[list[str], Counter[str], int]:
    errors: list[str] = []
    coverage: Counter[str] = Counter()
    record_count = 0
    root = (repo_root or cases_path.resolve().parents[2]).resolve()

    try:
        suite = json.loads(cases_path.read_text(encoding="utf-8"))
    except OSError:
        return [f"missing current-source suite: {cases_path}"], coverage, record_count
    except json.JSONDecodeError as exc:
        return [f"current-source suite must be valid JSON: {exc}"], coverage, record_count

    if not isinstance(suite, dict):
        return ["current-source suite root must be an object"], coverage, record_count
    if suite.get("schema_version") != 1:
        errors.append("current-source schema_version must equal 1")
    if suite.get("suite") != "current-source-verification":
        errors.append("suite must equal 'current-source-verification'")
    if suite.get("linked_issue") != 9:
        errors.append("linked_issue must equal 9")
    if not non_empty_string(suite.get("purpose")):
        errors.append("purpose must be a non-empty string")

    cases = suite.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a non-empty list"], coverage, record_count

    ids: set[str] = set()
    records: set[Path] = set()
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
            tags = []
        else:
            unknown = set(tags) - REQUIRED_TAGS
            if unknown:
                errors.append(f"{label}.tags contains unknown values: {sorted(unknown)}")
            for tag in tags:
                coverage[f"tag/{tag}"] += 1

        if not non_empty_string(case["prompt"]):
            errors.append(f"{label}.prompt must be a non-empty string")
        for field in ("expected_behavior", "forbidden_behavior"):
            if not non_empty_string_list(case[field]):
                errors.append(f"{label}.{field} must be a non-empty string list")

        markers = case["source_markers"]
        if not isinstance(markers, dict) or not markers:
            errors.append(f"{label}.source_markers must be a non-empty object")
        else:
            for source, required_markers in markers.items():
                source_path = resolve_repo_file(
                    source,
                    f"{label}.source_markers.{source}",
                    root,
                    Path("plugins/apple-ui-design"),
                    errors,
                )
                if not non_empty_string_list(required_markers):
                    errors.append(f"{label}.source_markers.{source} must be a non-empty string list")
                    continue
                if source_path:
                    contents = source_path.read_text(encoding="utf-8")
                    for marker in required_markers:
                        if marker not in contents:
                            errors.append(
                                f"{label}.source_markers.{source} missing policy marker: {marker!r}"
                            )

        record_value = case.get("verification_record")
        if "new-capability-record" in tags and not record_value:
            errors.append(f"{label} new-capability-record case requires verification_record")
        if record_value:
            record_path = resolve_repo_file(
                record_value,
                f"{label}.verification_record",
                root,
                Path("evals/current-source-verification"),
                errors,
            )
            if record_path and record_path not in records:
                records.add(record_path)
                record_count += 1
                try:
                    record = json.loads(record_path.read_text(encoding="utf-8"))
                except json.JSONDecodeError as exc:
                    errors.append(f"{record_path} must be valid JSON: {exc}")
                else:
                    errors.extend(validate_record(record, record_path.relative_to(root), root))

    for skill in sorted(SKILLS):
        if coverage[f"skill/{skill}"] == 0:
            errors.append(f"{skill} must own at least one current-source case")
    for tag in sorted(REQUIRED_TAGS):
        if coverage[f"tag/{tag}"] == 0:
            errors.append(f"current-source suite must cover tag: {tag}")
    if record_count == 0:
        errors.append("current-source suite must preserve at least one verification record")

    return errors, coverage, record_count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cases",
        type=Path,
        default=Path("evals/current-source-verification/cases.json"),
    )
    args = parser.parse_args()
    errors, coverage, records = validate(args.cases)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "current source verification valid: "
        f"{sum(value for key, value in coverage.items() if key.startswith('skill/'))} cases, "
        f"{sum(1 for tag in REQUIRED_TAGS if coverage[f'tag/{tag}'])} policy tags, "
        f"{records} records"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
