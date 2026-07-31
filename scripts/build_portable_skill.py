#!/usr/bin/env python3
"""Build the self-contained Agent Skills and SkillPay distribution."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
import zipfile
from pathlib import Path

from validate_portable_skill import validate_package


SKILL_NAME = "apple-ui-design"
WORKFLOWS = {
    "apple-ui-direction": "workflow-ui-direction.md",
    "apple-platform-adaptation": "workflow-platform-adaptation.md",
    "apple-ui-review": "workflow-ui-review.md",
}
PORTABLE_ROUTES = {
    "apple-ui-direction": "the UI Direction workflow in `references/workflow-ui-direction.md`",
    "apple-platform-adaptation": "the Platform Adaptation workflow in `references/workflow-platform-adaptation.md`",
    "apple-ui-review": "the UI Review workflow in `references/workflow-ui-review.md`",
}
ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def strip_frontmatter(contents: str, source: Path) -> str:
    if not contents.startswith("---\n"):
        raise ValueError(f"workflow source lacks frontmatter: {source}")
    end = contents.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"workflow source has unclosed frontmatter: {source}")
    return contents[end + 5 :].lstrip()


def portable_workflow(contents: str, source: Path) -> str:
    result = strip_frontmatter(contents, source)
    result = result.replace("../../references/", "references/")
    for skill_name, replacement in PORTABLE_ROUTES.items():
        result = result.replace(f"`${skill_name}`", replacement)
    return result.rstrip() + "\n"


def write_deterministic_zip(package_dir: Path, zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(package_dir.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(package_dir).as_posix()
            info = zipfile.ZipInfo(relative, ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())


def build(repo_root: Path, output_root: Path) -> tuple[Path, Path]:
    plugin_root = repo_root / "plugins" / SKILL_NAME
    package_dir = output_root / SKILL_NAME
    zip_path = output_root / f"{SKILL_NAME}.zip"

    if package_dir.exists():
        shutil.rmtree(package_dir)
    if zip_path.exists():
        zip_path.unlink()
    references_dir = package_dir / "references"
    references_dir.mkdir(parents=True)

    template = repo_root / "packaging" / "portable-skill" / "SKILL.md.in"
    shutil.copy2(template, package_dir / "SKILL.md")
    shutil.copy2(repo_root / "LICENSE", package_dir / "LICENSE")

    for source in sorted((plugin_root / "references").iterdir()):
        if source.is_file():
            shutil.copy2(source, references_dir / source.name)

    for skill_name, output_name in WORKFLOWS.items():
        source = plugin_root / "skills" / skill_name / "SKILL.md"
        generated = portable_workflow(source.read_text(encoding="utf-8"), source)
        (references_dir / output_name).write_text(generated, encoding="utf-8")

    directory_errors = validate_package(package_dir, repo_root)
    if directory_errors:
        raise ValueError("\n".join(directory_errors))
    write_deterministic_zip(package_dir, zip_path)
    zip_errors = validate_package(zip_path, repo_root)
    if zip_errors:
        raise ValueError("\n".join(zip_errors))
    return package_dir, zip_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory; defaults to <repository>/dist",
    )
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    output_root = (
        args.output_dir.resolve() if args.output_dir else repo_root / "dist"
    )
    output_root.mkdir(parents=True, exist_ok=True)
    try:
        package_dir, zip_path = build(repo_root, output_root)
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    print(f"portable folder: {package_dir}")
    print(f"SkillPay ZIP: {zip_path} ({zip_path.stat().st_size} bytes)")
    print(f"SHA-256: {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
