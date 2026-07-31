from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_public_interface import EVIDENCE_PATHS, FORWARD_RECORD, validate  # noqa: E402


class PublicInterfaceTests(unittest.TestCase):
    def make_fixture(self, temp_dir: str) -> Path:
        fixture = Path(temp_dir) / "repo"
        shutil.copytree(
            REPO_ROOT / "plugins" / "apple-ui-design",
            fixture / "plugins" / "apple-ui-design",
        )
        for filename in ("README.md", "README.zh-CN.md"):
            target = fixture / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO_ROOT / filename, target)
        for evidence_path in EVIDENCE_PATHS:
            source = REPO_ROOT / evidence_path
            target = fixture / evidence_path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        forward_target = fixture / FORWARD_RECORD
        forward_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO_ROOT / FORWARD_RECORD, forward_target)
        return fixture

    def test_current_public_interface_is_valid(self) -> None:
        self.assertEqual(validate(REPO_ROOT), [])

    def test_missing_skill_icon_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            (
                fixture
                / "plugins"
                / "apple-ui-design"
                / "skills"
                / "apple-ui-review"
                / "assets"
                / "icon.png"
            ).unlink()
            errors = validate(fixture)
        self.assertTrue(any("missing asset" in error for error in errors))

    def test_low_contrast_brand_color_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            manifest_path = (
                fixture
                / "plugins"
                / "apple-ui-design"
                / ".codex-plugin"
                / "plugin.json"
            )
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["interface"]["brandColor"] = "#777777"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            errors = validate(fixture)
        self.assertTrue(any("brandColor" in error for error in errors))

    def test_chinese_evidence_label_drift_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            readme = fixture / "README.zh-CN.md"
            contents = readme.read_text(encoding="utf-8")
            readme.write_text(
                contents.replace("**证据标签：**", "**结果：**", 1),
                encoding="utf-8",
            )
            errors = validate(fixture)
        self.assertIn("README.zh-CN.md must contain three evidence labels", errors)

    def test_skill_default_prompt_must_route_to_itself(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            metadata = (
                fixture
                / "plugins"
                / "apple-ui-design"
                / "skills"
                / "apple-ui-review"
                / "agents"
                / "openai.yaml"
            )
            contents = metadata.read_text(encoding="utf-8")
            metadata.write_text(
                contents.replace("$apple-ui-review", "$apple-ui-direction"),
                encoding="utf-8",
            )
            errors = validate(fixture)
        self.assertIn(
            "apple-ui-review default_prompt must mention $apple-ui-review", errors
        )

    def test_missing_first_use_scenario_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            record = fixture / FORWARD_RECORD
            contents = record.read_text(encoding="utf-8")
            record.write_text(
                contents.replace("public-review-first-use", "review-run"),
                encoding="utf-8",
            )
            errors = validate(fixture)
        self.assertIn(
            "public first-use record missing scenario: public-review-first-use",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
