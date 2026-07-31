#!/usr/bin/env python3
"""Validate public Plugin and Skill metadata, assets, and README examples."""

from __future__ import annotations

import json
import re
import struct
import sys
from pathlib import Path, PurePosixPath


PLUGIN_NAME = "apple-ui-design"
BRAND_COLOR = "#007A6E"
SKILLS = {
    "apple-ui-direction": "Apple UI Direction",
    "apple-platform-adaptation": "Apple Platform Adaptation",
    "apple-ui-review": "Apple UI Review",
}
PLUGIN_ASSETS = {
    "composerIcon": "./assets/composer-icon.png",
    "logo": "./assets/logo-light.png",
    "logoDark": "./assets/logo-dark.png",
}
SCREENSHOTS = [
    "./assets/screenshot-direction.png",
    "./assets/screenshot-adaptation.png",
    "./assets/screenshot-review.png",
]
README_IMAGES = [path.removeprefix("./") for path in SCREENSHOTS]
EVIDENCE_PATHS = [
    "evals/delivery-contracts/runs/2026-07-29/visual-direction/README.md",
    "evals/delivery-contracts/runs/2026-07-29/visual-direction/validation-report.md",
    "evals/delivery-contracts/runs/2026-07-29/platform-adaptation/decision-matrix.md",
    "evals/delivery-contracts/runs/2026-07-29/platform-adaptation/validation.md",
    "evals/delivery-contracts/runs/2026-07-29/ui-review/review.md",
    "evals/delivery-contracts/fixtures/ui-review.md",
]
FORWARD_RECORD = "evals/public-interface/runs/2026-07-31.md"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
HEX_COLOR = re.compile(r"^#[0-9A-Fa-f]{6}$")
YAML_STRING = re.compile(r'^  ([a-z_]+): "(.*)"$')


def read_json(path: Path, label: str, errors: list[str]) -> dict | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        errors.append(f"missing {label}: {path}")
        return None
    except json.JSONDecodeError as exc:
        errors.append(f"{label} must be valid JSON: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{label} must contain a JSON object")
        return None
    return value


def parse_agent_yaml(path: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    try:
        contents = path.read_text(encoding="utf-8")
    except OSError:
        errors.append(f"missing Skill interface metadata: {path}")
        return {}, ""
    fields = {
        match.group(1): match.group(2)
        for line in contents.splitlines()
        if (match := YAML_STRING.fullmatch(line)) is not None
    }
    return fields, contents


def resolve_asset(
    owner: Path, raw_path: object, label: str, errors: list[str]
) -> Path | None:
    if not isinstance(raw_path, str) or not raw_path.startswith("./"):
        errors.append(f"{label} must be a quoted ./ relative path")
        return None
    relative = PurePosixPath(raw_path)
    if ".." in relative.parts:
        errors.append(f"{label} must not escape its owner")
        return None
    resolved = (owner / raw_path.removeprefix("./")).resolve()
    try:
        resolved.relative_to(owner.resolve())
    except ValueError:
        errors.append(f"{label} must remain inside {owner}")
        return None
    if not resolved.is_file():
        errors.append(f"{label} points to a missing asset: {raw_path}")
        return None
    return resolved


def png_dimensions(path: Path, label: str, errors: list[str]) -> tuple[int, int] | None:
    try:
        header = path.read_bytes()[:24]
    except OSError:
        errors.append(f"unable to read {label}: {path}")
        return None
    if len(header) < 24 or header[:8] != PNG_SIGNATURE or header[12:16] != b"IHDR":
        errors.append(f"{label} must be a valid PNG: {path}")
        return None
    return struct.unpack(">II", header[16:24])


def relative_luminance(color: str) -> float:
    channels = [int(color[index : index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [
        value / 12.92
        if value <= 0.04045
        else ((value + 0.055) / 1.055) ** 2.4
        for value in channels
    ]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(first: str, second: str) -> float:
    first_luminance = relative_luminance(first)
    second_luminance = relative_luminance(second)
    lighter = max(first_luminance, second_luminance)
    darker = min(first_luminance, second_luminance)
    return (lighter + 0.05) / (darker + 0.05)


def validate_skill_metadata(plugin_root: Path, errors: list[str]) -> None:
    for skill_name, display_name in SKILLS.items():
        skill_root = plugin_root / "skills" / skill_name
        fields, contents = parse_agent_yaml(
            skill_root / "agents" / "openai.yaml", errors
        )
        if fields.get("display_name") != display_name:
            errors.append(f"{skill_name} display_name must be {display_name!r}")

        description = fields.get("short_description", "")
        if not 25 <= len(description) <= 64:
            errors.append(
                f"{skill_name} short_description must contain 25-64 characters; "
                f"found {len(description)}"
            )

        if fields.get("brand_color") != BRAND_COLOR:
            errors.append(f"{skill_name} brand_color must equal {BRAND_COLOR}")

        prompt = fields.get("default_prompt", "")
        if f"${skill_name}" not in prompt:
            errors.append(f"{skill_name} default_prompt must mention ${skill_name}")
        if not prompt.endswith(".") or "\n" in prompt:
            errors.append(f"{skill_name} default_prompt must be one complete sentence")
        if "allow_implicit_invocation: true" not in contents:
            errors.append(f"{skill_name} must keep implicit invocation enabled")

        small_icon = resolve_asset(
            skill_root, fields.get("icon_small"), f"{skill_name} icon_small", errors
        )
        large_icon = resolve_asset(
            skill_root, fields.get("icon_large"), f"{skill_name} icon_large", errors
        )
        if small_icon is not None:
            if small_icon.suffix.lower() != ".svg":
                errors.append(f"{skill_name} icon_small must be an SVG")
            else:
                svg = small_icon.read_text(encoding="utf-8")
                if "<svg" not in svg or BRAND_COLOR not in svg or "<image" in svg:
                    errors.append(
                        f"{skill_name} icon_small must be an original local brand SVG"
                    )
        if large_icon is not None:
            dimensions = png_dimensions(
                large_icon, f"{skill_name} icon_large", errors
            )
            if dimensions is not None and (
                dimensions[0] != dimensions[1] or dimensions[0] < 100
            ):
                errors.append(f"{skill_name} icon_large must be a square PNG >= 100px")


def validate_plugin_manifest(plugin_root: Path, errors: list[str]) -> None:
    manifest = read_json(
        plugin_root / ".codex-plugin" / "plugin.json", "plugin manifest", errors
    )
    if manifest is None:
        return
    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        errors.append("plugin manifest interface must be an object")
        return

    brand_color = interface.get("brandColor")
    if brand_color != BRAND_COLOR:
        errors.append(f"plugin brandColor must equal {BRAND_COLOR}")
    if isinstance(brand_color, str) and HEX_COLOR.fullmatch(brand_color):
        for surface in ("#FFFFFF", "#000000"):
            ratio = contrast_ratio(brand_color, surface)
            if ratio < 3:
                errors.append(
                    f"plugin brandColor contrast against {surface} must be >= 3:1; "
                    f"found {ratio:.2f}:1"
                )

    for field, expected in PLUGIN_ASSETS.items():
        if interface.get(field) != expected:
            errors.append(f"plugin {field} must equal {expected}")
        path = resolve_asset(plugin_root, interface.get(field), f"plugin {field}", errors)
        if path is not None:
            dimensions = png_dimensions(path, f"plugin {field}", errors)
            if dimensions is not None and (
                dimensions[0] != dimensions[1] or dimensions[0] < 100
            ):
                errors.append(f"plugin {field} must be a square PNG >= 100px")

    screenshots = interface.get("screenshots")
    if screenshots != SCREENSHOTS:
        errors.append("plugin screenshots must map to direction, adaptation, and review")
    if isinstance(screenshots, list):
        for index, raw_path in enumerate(screenshots):
            path = resolve_asset(
                plugin_root, raw_path, f"plugin screenshots[{index}]", errors
            )
            if path is None:
                continue
            if path.suffix.lower() != ".png":
                errors.append(f"plugin screenshots[{index}] must be a PNG")
                continue
            dimensions = png_dimensions(path, f"plugin screenshots[{index}]", errors)
            if dimensions is not None and (
                dimensions[0] < 1200 or dimensions[1] < 800
            ):
                errors.append(
                    f"plugin screenshots[{index}] must be at least 1200x800"
                )

    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or len(prompts) != 3:
        errors.append("plugin defaultPrompt must contain exactly three starter prompts")
    else:
        for index, skill_name in enumerate(SKILLS):
            prompt = prompts[index]
            if not isinstance(prompt, str) or f"${skill_name}" not in prompt:
                errors.append(
                    f"plugin defaultPrompt[{index}] must route to ${skill_name}"
                )
            elif len(prompt) > 128:
                errors.append(f"plugin defaultPrompt[{index}] exceeds 128 characters")

    if interface.get("capabilities") != [
        "UI Direction",
        "Platform Adaptation",
        "UI Review",
    ]:
        errors.append("plugin capabilities must match the three bundled workflows")


def public_section(contents: str, heading: str, errors: list[str]) -> str:
    marker = f"## {heading}\n"
    if marker not in contents:
        errors.append(f"README is missing section: {heading}")
        return ""
    section = contents.split(marker, 1)[1]
    return section.split("\n## ", 1)[0]


def validate_readmes(root: Path, errors: list[str]) -> None:
    contracts = {
        "README.md": {
            "heading": "Verified Workflow Examples",
            "examples": [
                "### UI direction: Today",
                "### Platform adaptation: OrbitCut",
                "### UI review: LedgerDesk",
            ],
            "label": "**Evidence label:**",
            "markers": ["Prototype", "Product code", "Experience validation"],
        },
        "README.zh-CN.md": {
            "heading": "已验证工作流示例",
            "examples": [
                "### 界面方向：Today",
                "### 平台适配：OrbitCut",
                "### 界面评审：LedgerDesk",
            ],
            "label": "**证据标签：**",
            "markers": ["原型", "产品代码", "体验验证"],
        },
    }
    sections: dict[str, str] = {}
    for filename, contract in contracts.items():
        path = root / filename
        try:
            contents = path.read_text(encoding="utf-8")
        except OSError:
            errors.append(f"missing public README: {filename}")
            continue
        section = public_section(contents, contract["heading"], errors)
        sections[filename] = section
        for example in contract["examples"]:
            if example not in section:
                errors.append(f"{filename} is missing public example: {example}")
        if section.count(contract["label"]) != 3:
            errors.append(f"{filename} must contain three evidence labels")
        for marker in contract["markers"]:
            if section.count(marker) < 3:
                errors.append(
                    f"{filename} must classify {marker!r} for all three examples"
                )
        for skill_name in SKILLS:
            if f"${skill_name}" not in section:
                errors.append(f"{filename} examples must name ${skill_name}")
        for image in README_IMAGES:
            public_path = f"plugins/{PLUGIN_NAME}/{image}"
            if section.count(public_path) != 1:
                errors.append(f"{filename} must show {public_path} exactly once")
        for evidence_path in EVIDENCE_PATHS:
            if evidence_path not in section:
                errors.append(f"{filename} must link to preserved evidence: {evidence_path}")
            if not (root / evidence_path).is_file():
                errors.append(f"public example evidence is missing: {evidence_path}")

    if len(sections) == 2:
        for skill_name in SKILLS:
            counts = [section.count(f"${skill_name}") for section in sections.values()]
            if counts[0] != counts[1]:
                errors.append(
                    f"English and Chinese examples must mention ${skill_name} equally"
                )


def validate_forward_record(root: Path, errors: list[str]) -> None:
    path = root / FORWARD_RECORD
    try:
        contents = path.read_text(encoding="utf-8")
    except OSError:
        errors.append(f"missing public first-use record: {FORWARD_RECORD}")
        return
    if "no-history" not in contents:
        errors.append("public first-use record must document no-history execution")
    scenarios = {
        "public-direction-first-use": "$apple-ui-direction",
        "public-adaptation-first-use": "$apple-platform-adaptation",
        "public-review-first-use": "$apple-ui-review",
    }
    for scenario, skill_name in scenarios.items():
        if contents.count(scenario) < 2:
            errors.append(f"public first-use record missing scenario: {scenario}")
        if skill_name not in contents:
            errors.append(f"public first-use record missing Skill: {skill_name}")
    if contents.count("PASS") != 3:
        errors.append("public first-use record must preserve three PASS results")


def validate(repo_root: Path) -> list[str]:
    root = repo_root.resolve()
    plugin_root = root / "plugins" / PLUGIN_NAME
    errors: list[str] = []
    validate_skill_metadata(plugin_root, errors)
    validate_plugin_manifest(plugin_root, errors)
    validate_readmes(root, errors)
    validate_forward_record(root, errors)
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = validate(root)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1
    print(
        "public interface valid: 3 routed skills, accessible brand color, "
        "3 packaged examples, bilingual evidence parity"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
