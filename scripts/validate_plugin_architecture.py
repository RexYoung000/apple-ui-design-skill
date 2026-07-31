#!/usr/bin/env python3
"""Validate the Apple UI Design plugin split with no third-party dependencies."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


PLUGIN_NAME = "apple-ui-design"
EXPECTED_SKILLS = {
    "apple-ui-direction": {
        "required_headings": {"## Required Starting Point", "## Successful Result"},
        "description_markers": {
            "requested outcome",
            "implementation-only Swift",
            "critique-only review",
        },
    },
    "apple-platform-adaptation": {
        "required_headings": {"## Required Inputs", "## Successful Result"},
        "description_markers": {
            "Adapt an established",
            "requested outcome",
            "implementation-only Swift",
            "critique-only review",
        },
    },
    "apple-ui-review": {
        "required_headings": {"## Required Evidence", "## Successful Result"},
        "description_markers": {
            "Review an existing",
            "requested outcome",
            "implementation-only Swift",
            "cross-platform adaptation",
        },
    },
}
REQUIRED_SHARED_REFERENCES = {
    "accessibility-and-localization.md",
    "apple-platform-adaptation.md",
    "authority-and-principles.md",
    "context-and-alignment.md",
    "current-sources.md",
    "content-and-sensitive-flows.md",
    "design-system-and-dna.md",
    "delivery-contracts.md",
    "engineering-routing.md",
    "interaction-and-motion.md",
    "prototyping-and-implementation.md",
    "research-and-source-evidence.md",
    "source-registry.json",
    "validation-and-review.md",
}
FORBIDDEN_PACKAGE_ENTRIES = {
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "docs",
    "evals",
    "tests",
}
REFERENCE_PATTERN = re.compile(r"`(\.\./\.\./references/[^`]+)`")
DELIVERY_CONTRACT_REFERENCE = "../../references/delivery-contracts.md"
ENGINEERING_ROUTING_REFERENCE = "../../references/engineering-routing.md"
ENGINEERING_NEGATIVE_MARKERS = {
    "compilation",
    "concurrency",
    "architecture",
    "performance",
    "API usage",
    "CI",
    "packaging",
    "release",
}
REQUIRED_DELIVERY_CONTRACT_HEADINGS = {
    "## Contract 1: Visual Direction",
    "## Contract 2: Screen or Flow",
    "## Contract 3: Design System",
    "## Contract 4: Platform Adaptation",
    "## Contract 5: Native Prototype",
    "## Contract 6: UI Review",
}


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
        errors.append(f"{label} must contain a JSON object")
        return None
    return payload


def read_frontmatter(path: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    try:
        contents = path.read_text(encoding="utf-8")
    except OSError:
        errors.append(f"missing skill manifest: {path}")
        return {}, ""

    if not contents.startswith("---\n"):
        errors.append(f"{path} must start with YAML frontmatter")
        return {}, contents
    end = contents.find("\n---\n", 4)
    if end == -1:
        errors.append(f"{path} frontmatter is not closed")
        return {}, contents

    fields: dict[str, str] = {}
    for line in contents[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")
    return fields, contents


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    root = repo_root.resolve()
    plugin_root = root / "plugins" / PLUGIN_NAME
    skills_root = plugin_root / "skills"
    references_root = plugin_root / "references"

    manifest = load_json(
        plugin_root / ".codex-plugin" / "plugin.json", "plugin manifest", errors
    )
    if manifest is not None:
        if manifest.get("name") != PLUGIN_NAME:
            errors.append(f"plugin name must equal {PLUGIN_NAME!r}")
        if manifest.get("skills") != "./skills/":
            errors.append("plugin manifest skills path must equal './skills/'")
        for forbidden_field in ("apps", "mcpServers", "hooks"):
            if forbidden_field in manifest:
                errors.append(
                    f"skills-only plugin must not declare {forbidden_field!r}"
                )

    if not skills_root.is_dir():
        errors.append("plugin skills directory is missing")
        actual_skills: set[str] = set()
    else:
        actual_skills = {
            path.name
            for path in skills_root.iterdir()
            if path.is_dir() and not path.name.startswith(".")
        }
    if actual_skills != set(EXPECTED_SKILLS):
        errors.append(
            "plugin skills must be exactly: "
            + ", ".join(sorted(EXPECTED_SKILLS))
            + f"; found: {', '.join(sorted(actual_skills)) or 'none'}"
        )

    for skill_name, contract in EXPECTED_SKILLS.items():
        skill_root = skills_root / skill_name
        fields, contents = read_frontmatter(skill_root / "SKILL.md", errors)
        if fields.get("name") != skill_name:
            errors.append(f"{skill_name} frontmatter name must match its folder")
        description = fields.get("description", "")
        for marker in contract["description_markers"]:
            if marker not in description:
                errors.append(
                    f"{skill_name} description missing boundary marker: {marker!r}"
                )
        for marker in ENGINEERING_NEGATIVE_MARKERS:
            if marker not in description:
                errors.append(
                    f"{skill_name} description missing engineering negative: {marker!r}"
                )
        for heading in contract["required_headings"]:
            if heading not in contents:
                errors.append(f"{skill_name} missing contract heading: {heading}")
        if "[TODO:" in contents:
            errors.append(f"{skill_name} contains a TODO placeholder")

        local_references = skill_root / "references"
        if local_references.exists():
            errors.append(
                f"{skill_name} must use plugin shared references, not a local references directory"
            )

        referenced_paths = REFERENCE_PATTERN.findall(contents)
        if not referenced_paths:
            errors.append(f"{skill_name} must link directly to shared references")
        if DELIVERY_CONTRACT_REFERENCE not in referenced_paths:
            errors.append(
                f"{skill_name} must directly apply the shared delivery contracts"
            )
        if ENGINEERING_ROUTING_REFERENCE not in referenced_paths:
            errors.append(
                f"{skill_name} must directly apply the engineering routing rules"
            )
        for relative_path in referenced_paths:
            resolved = (skill_root / relative_path).resolve()
            try:
                resolved.relative_to(plugin_root.resolve())
            except ValueError:
                errors.append(
                    f"{skill_name} reference escapes the plugin: {relative_path}"
                )
                continue
            if not resolved.is_file():
                errors.append(
                    f"{skill_name} points to a missing shared reference: {relative_path}"
                )

        agent_yaml = skill_root / "agents" / "openai.yaml"
        try:
            agent_contents = agent_yaml.read_text(encoding="utf-8")
        except OSError:
            errors.append(f"{skill_name} is missing agents/openai.yaml")
        else:
            if f"${skill_name}" not in agent_contents:
                errors.append(
                    f"{skill_name} agents/openai.yaml default prompt must mention ${skill_name}"
                )
            if "allow_implicit_invocation: true" not in agent_contents:
                errors.append(
                    f"{skill_name} agents/openai.yaml must explicitly enable "
                    "implicit invocation"
                )

    if not references_root.is_dir():
        errors.append("plugin shared references directory is missing")
    else:
        actual_references = {
            path.name for path in references_root.iterdir() if path.is_file()
        }
        missing_references = REQUIRED_SHARED_REFERENCES - actual_references
        if missing_references:
            errors.append(
                "missing shared references: "
                + ", ".join(sorted(missing_references))
            )
        try:
            delivery_contracts = (
                references_root / "delivery-contracts.md"
            ).read_text(encoding="utf-8")
        except OSError:
            pass
        else:
            for heading in REQUIRED_DELIVERY_CONTRACT_HEADINGS:
                if heading not in delivery_contracts:
                    errors.append(
                        f"delivery contracts missing required heading: {heading}"
                    )

    if (root / "references").exists():
        errors.append("root references directory duplicates plugin shared ownership")
    source_registries = [
        path
        for path in root.rglob("source-registry.json")
        if ".git" not in path.parts
    ]
    if source_registries != [references_root / "source-registry.json"]:
        errors.append("source-registry.json must have exactly one plugin-owned copy")

    for entry in FORBIDDEN_PACKAGE_ENTRIES:
        if (plugin_root / entry).exists():
            errors.append(f"installable package contains forbidden repository entry: {entry}")

    legacy_fields, legacy_contents = read_frontmatter(root / "SKILL.md", errors)
    if legacy_fields.get("name") != "apple-ui-design":
        errors.append("legacy root skill must retain the apple-ui-design name")
    if "Legacy explicit-invocation compatibility router" not in legacy_fields.get(
        "description", ""
    ):
        errors.append("root skill must identify itself as the legacy router")
    if "plugins/apple-ui-design/skills/" not in legacy_contents:
        errors.append("legacy root skill must route to bundled skills")
    try:
        legacy_agent = (root / "agents" / "openai.yaml").read_text(encoding="utf-8")
    except OSError:
        errors.append("legacy root agents/openai.yaml is missing")
    else:
        if "allow_implicit_invocation: false" not in legacy_agent:
            errors.append("legacy root skill must disable implicit invocation")

    marketplace = load_json(
        root / ".agents" / "plugins" / "marketplace.json",
        "repository marketplace",
        errors,
    )
    if marketplace is not None:
        if marketplace.get("name") != PLUGIN_NAME:
            errors.append(f"marketplace name must equal {PLUGIN_NAME!r}")
        entries = marketplace.get("plugins")
        if not isinstance(entries, list) or len(entries) != 1:
            errors.append("marketplace must contain exactly one plugin entry")
        else:
            entry = entries[0]
            if not isinstance(entry, dict) or entry.get("name") != PLUGIN_NAME:
                errors.append("marketplace plugin entry name is invalid")
            source = entry.get("source") if isinstance(entry, dict) else None
            expected_source = {
                "source": "local",
                "path": "./plugins/apple-ui-design",
            }
            if source != expected_source:
                errors.append(
                    "marketplace source must point to ./plugins/apple-ui-design"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "repo_root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    args = parser.parse_args()

    errors = validate(args.repo_root)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1
    print("plugin architecture valid: 3 focused skills, 1 shared reference source")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
