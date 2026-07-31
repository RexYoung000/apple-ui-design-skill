from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from build_portable_skill import build  # noqa: E402
from validate_portable_skill import validate_package  # noqa: E402


class PortableSkillTests(unittest.TestCase):
    def build_fixture(self, temp_dir: str) -> tuple[Path, Path]:
        return build(REPO_ROOT, Path(temp_dir) / "dist")

    def test_generated_folder_and_zip_are_valid(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            package_dir, zip_path = self.build_fixture(temp_dir)
            self.assertEqual(validate_package(package_dir, REPO_ROOT), [])
            self.assertEqual(validate_package(zip_path, REPO_ROOT), [])

    def test_generated_skill_is_at_artifact_root(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            package_dir, _ = self.build_fixture(temp_dir)
            self.assertTrue((package_dir / "SKILL.md").is_file())
            self.assertFalse((package_dir / "apple-ui-design").exists())

    def test_parent_directory_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            package_dir, _ = self.build_fixture(temp_dir)
            skill = package_dir / "SKILL.md"
            skill.write_text(
                skill.read_text(encoding="utf-8")
                + "\nRead `../private/instructions.md`.\n",
                encoding="utf-8",
            )
            errors = validate_package(package_dir, REPO_ROOT)
            self.assertTrue(any("parent-directory reference" in error for error in errors))

    def test_codex_metadata_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            package_dir, _ = self.build_fixture(temp_dir)
            metadata = package_dir / "agents" / "openai.yaml"
            metadata.parent.mkdir()
            metadata.write_text("interface: {}\n", encoding="utf-8")
            errors = validate_package(package_dir, REPO_ROOT)
            self.assertTrue(any("unexpected package files" in error for error in errors))
            self.assertTrue(any("forbidden package entry" in error for error in errors))

    def test_missing_shared_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            package_dir, _ = self.build_fixture(temp_dir)
            (package_dir / "references" / "delivery-contracts.md").unlink()
            errors = validate_package(package_dir, REPO_ROOT)
            self.assertTrue(any("missing package files" in error for error in errors))

    def test_unexpected_repository_document_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            package_dir, _ = self.build_fixture(temp_dir)
            shutil.copy2(REPO_ROOT / "README.md", package_dir / "README.md")
            errors = validate_package(package_dir, REPO_ROOT)
            self.assertTrue(any("unexpected package files" in error for error in errors))
            self.assertTrue(any("forbidden package entry" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
