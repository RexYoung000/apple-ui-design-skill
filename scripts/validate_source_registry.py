#!/usr/bin/env python3
"""Validate the curated source registry with no third-party dependencies."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


REQUIRED_FIELDS = {
    "id",
    "name",
    "url",
    "category",
    "access",
    "platforms",
    "allowed_uses",
    "reuse_status",
    "last_checked",
    "status",
    "notes",
}
VALID_STATUSES = {"active", "conditional", "excluded"}
VALID_CATEGORIES = {
    "official-authority",
    "official-assets",
    "shipped-examples",
    "observable-gallery",
    "inspiration-only",
    "implementation-inspiration",
    "third-party-assets",
    "limited-preview",
    "excluded",
}


def normalize_url(value: str) -> str:
    parts = urlsplit(value)
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, parts.query, ""))


def parse_date(value: str, field: str, errors: list[str]) -> date | None:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        errors.append(f"{field} must use YYYY-MM-DD: {value!r}")
        return None


def validate(path: Path, max_age_days: int) -> tuple[list[str], list[str], Counter[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot load {path}: {exc}"], warnings, Counter()

    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")

    reviewed = parse_date(data.get("last_reviewed"), "last_reviewed", errors)
    if reviewed and reviewed > date.today():
        errors.append("last_reviewed cannot be in the future")

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        return errors + ["sources must be a non-empty list"], warnings, Counter()

    ids: set[str] = set()
    urls: set[str] = set()
    categories: Counter[str] = Counter()

    for index, source in enumerate(sources):
        label = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{label} must be an object")
            continue

        missing = sorted(REQUIRED_FIELDS - source.keys())
        if missing:
            errors.append(f"{label} missing fields: {', '.join(missing)}")
            continue

        source_id = source["id"]
        if not isinstance(source_id, str) or not source_id:
            errors.append(f"{label}.id must be a non-empty string")
        elif source_id in ids:
            errors.append(f"duplicate id: {source_id}")
        else:
            ids.add(source_id)

        url = source["url"]
        parts = urlsplit(url) if isinstance(url, str) else None
        if not parts or parts.scheme != "https" or not parts.netloc:
            errors.append(f"{label}.url must be an absolute HTTPS URL: {url!r}")
        else:
            normalized = normalize_url(url)
            if normalized in urls:
                errors.append(f"duplicate URL: {url}")
            urls.add(normalized)

        category = source["category"]
        categories[category] += 1
        if category not in VALID_CATEGORIES:
            errors.append(f"{label}.category is invalid: {category!r}")

        status = source["status"]
        if status not in VALID_STATUSES:
            errors.append(f"{label}.status is invalid: {status!r}")
        if category == "excluded" and status != "excluded":
            errors.append(f"{label} excluded category must use excluded status")
        if status == "excluded" and source["allowed_uses"] != ["none"]:
            errors.append(f"{label} excluded source must allow only 'none'")

        for list_field in ("platforms", "allowed_uses"):
            value = source[list_field]
            if not isinstance(value, list) or not value or not all(isinstance(item, str) and item for item in value):
                errors.append(f"{label}.{list_field} must be a non-empty string list")

        checked = parse_date(source["last_checked"], f"{label}.last_checked", errors)
        if checked:
            age = (date.today() - checked).days
            if age < 0:
                errors.append(f"{label}.last_checked cannot be in the future")
            elif age > max_age_days and status != "excluded":
                warnings.append(f"{source_id} was last checked {age} days ago")

        for text_field in ("name", "access", "reuse_status", "notes"):
            if not isinstance(source[text_field], str) or not source[text_field].strip():
                errors.append(f"{label}.{text_field} must be a non-empty string")

    return errors, warnings, categories


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "references" / "source-registry.json",
    )
    parser.add_argument("--max-age-days", type=int, default=180)
    args = parser.parse_args()

    errors, warnings, categories = validate(args.path, args.max_age_days)
    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)

    if errors:
        return 1

    category_summary = ", ".join(f"{name}={count}" for name, count in sorted(categories.items()))
    print(f"source registry valid: {sum(categories.values())} sources ({category_summary})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
