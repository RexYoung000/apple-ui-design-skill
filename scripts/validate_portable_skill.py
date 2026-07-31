#!/usr/bin/env python3
"""Validate a generated cross-agent Apple UI Design Skill package."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath


SKILL_NAME = "apple-ui-design"
MAX_PACKAGE_BYTES = 20 * 1024 * 1024
STANDARD_FRONTMATTER_FIELDS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
}
WORKFLOW_FILES = {
    "workflow-ui-direction.md",
    "workflow-platform-adaptation.md",
    "workflow-ui-review.md",
}
FORBIDDEN_NAMES = {
    ".agents",
    ".codex-plugin",
    ".git",
    ".github",
    "README.md",
    "README.zh-CN.md",
    "agents",
    "docs",
    "evals",
    "tests",
}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REFERENCE_PATTERN = re.compile(r"`(references/[^`]+)`")


def canonical_reference_names(repo_root: Path) -> set[str]:
    source = repo_root / "plugins" / SKILL_NAME / "references"
    return {path.name for path in source.iterdir() if path.is_file()}


def expected_relative_files(repo_root: Path) -> set[str]:
    references = canonical_reference_names(repo_root) | WORKFLOW_FILES
    return {"SKILL.md", "LICENSE"} | {
        f"references/{name}" for name in references
    }


def parse_frontmatter(contents: str, errors: list[str]) -> dict[str, object]:
    if not contents.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
        return {}
    end = contents.find("\n---\n", 4)
    if end == -1:
        errors.append("SKILL.md frontmatter is not closed")
        return {}

    fields: dict[str, object] = {}
    current_mapping: dict[str, str] | None = None
    for line in contents[4:end].splitlines():
        if line.startswith("  "):
            if current_mapping is None or ":" not in line:
                errors.append(f"invalid nested frontmatter line: {line!r}")
                continue
            key, value = line.strip().split(":", 1)
            current_mapping[key.strip()] = value.strip().strip("\"'")
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line!r}")
            current_mapping = None
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        scalar = value.strip().strip("\"'")
        if scalar:
            fields[key] = scalar
            current_mapping = None
        else:
            nested: dict[str, str] = {}
            fields[key] = nested
            current_mapping = nested
    return fields


def validate_contents(
    files: dict[str, bytes], repo_root: Path, package_label: str
) -> list[str]:
    errors: list[str] = []
    expected = expected_relative_files(repo_root)
    actual = set(files)
    missing = expected - actual
    unexpected = actual - expected
    if missing:
        errors.append("missing package files: " + ", ".join(sorted(missing)))
    if unexpected:
        errors.append("unexpected package files: " + ", ".join(sorted(unexpected)))

    for relative in actual:
        path = PurePosixPath(relative)
        if path.is_absolute() or ".." in path.parts:
            errors.append(f"package path escapes its root: {relative}")
        if any(part in FORBIDDEN_NAMES for part in path.parts):
            errors.append(f"forbidden package entry: {relative}")

    skill_bytes = files.get("SKILL.md")
    if skill_bytes is None:
        return errors
    try:
        skill = skill_bytes.decode("utf-8")
    except UnicodeDecodeError:
        errors.append("SKILL.md must be UTF-8")
        return errors

    fields = parse_frontmatter(skill, errors)
    unknown = set(fields) - STANDARD_FRONTMATTER_FIELDS
    if unknown:
        errors.append("non-standard frontmatter fields: " + ", ".join(sorted(unknown)))
    name = fields.get("name")
    if name != SKILL_NAME:
        errors.append(f"frontmatter name must equal {SKILL_NAME!r}")
    if isinstance(name, str) and not NAME_PATTERN.fullmatch(name):
        errors.append("frontmatter name does not follow Agent Skills naming rules")
    description = fields.get("description")
    if not isinstance(description, str) or not 1 <= len(description) <= 1024:
        errors.append("frontmatter description must contain 1-1024 characters")
    compatibility = fields.get("compatibility")
    if compatibility is not None and (
        not isinstance(compatibility, str) or not 1 <= len(compatibility) <= 500
    ):
        errors.append("frontmatter compatibility must contain 1-500 characters")
    metadata = fields.get("metadata")
    if not isinstance(metadata, dict) or not all(
        isinstance(key, str) and isinstance(value, str)
        for key, value in metadata.items()
    ):
        errors.append("frontmatter metadata must be a string-to-string mapping")
    if len(skill.splitlines()) > 500:
        errors.append("SKILL.md exceeds the 500-line progressive-disclosure budget")

    for relative, payload in files.items():
        if not relative.endswith((".md", ".json")):
            continue
        try:
            text = payload.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"runtime text file must be UTF-8: {relative}")
            continue
        if "../" in text or "..\\" in text:
            errors.append(f"runtime file contains a parent-directory reference: {relative}")
        if relative.startswith("references/workflow-") and "$apple-" in text:
            errors.append(f"portable workflow contains a Codex-specific invocation: {relative}")
        for reference in REFERENCE_PATTERN.findall(text):
            if reference not in files:
                errors.append(f"{relative} points to missing package reference: {reference}")

    total_size = sum(len(payload) for payload in files.values())
    if total_size > MAX_PACKAGE_BYTES:
        errors.append(
            f"{package_label} expands to {total_size} bytes, above the 20 MB limit"
        )
    return errors


def read_directory(package: Path) -> tuple[dict[str, bytes], list[str]]:
    errors: list[str] = []
    if package.name != SKILL_NAME:
        errors.append(f"package directory must be named {SKILL_NAME!r}")
    files: dict[str, bytes] = {}
    for path in package.rglob("*"):
        if path.is_symlink():
            errors.append(f"package must not contain symlinks: {path.relative_to(package)}")
        elif path.is_file():
            files[path.relative_to(package).as_posix()] = path.read_bytes()
    return files, errors


def read_zip(package: Path) -> tuple[dict[str, bytes], list[str]]:
    errors: list[str] = []
    if package.stat().st_size > MAX_PACKAGE_BYTES:
        errors.append(
            f"ZIP is {package.stat().st_size} bytes, above SkillPay's 20 MB limit"
        )
    files: dict[str, bytes] = {}
    try:
        with zipfile.ZipFile(package) as archive:
            for info in archive.infolist():
                if info.is_dir():
                    continue
                path = PurePosixPath(info.filename)
                if path.is_absolute() or ".." in path.parts:
                    errors.append(f"ZIP path escapes its root: {info.filename}")
                    continue
                files[path.as_posix()] = archive.read(info)
    except zipfile.BadZipFile:
        errors.append("package is not a valid ZIP file")
    return files, errors


def validate_package(package: Path, repo_root: Path) -> list[str]:
    if not package.exists():
        return [f"portable package does not exist: {package}"]
    if package.is_dir():
        files, errors = read_directory(package)
    elif package.suffix.lower() == ".zip":
        files, errors = read_zip(package)
    else:
        return ["portable package must be a directory or .zip file"]
    errors.extend(validate_contents(files, repo_root, package.name))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", type=Path)
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    errors = validate_package(args.package.resolve(), repo_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"portable Skill package is valid: {args.package}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
