from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_plugin_architecture import validate  # noqa: E402


class PluginArchitectureTests(unittest.TestCase):
    def make_fixture(self, temp_dir: str) -> Path:
        fixture = Path(temp_dir) / "repo"
        (fixture / "plugins").mkdir(parents=True)
        shutil.copytree(
            REPO_ROOT / "plugins" / "apple-ui-design",
            fixture / "plugins" / "apple-ui-design",
        )
        shutil.copytree(REPO_ROOT / "agents", fixture / "agents")
        shutil.copytree(REPO_ROOT / ".agents", fixture / ".agents")
        shutil.copy2(REPO_ROOT / "SKILL.md", fixture / "SKILL.md")
        return fixture

    def test_current_architecture_is_valid(self) -> None:
        self.assertEqual(validate(REPO_ROOT), [])

    def test_missing_required_skill_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            shutil.rmtree(
                fixture
                / "plugins"
                / "apple-ui-design"
                / "skills"
                / "apple-ui-review"
            )

            errors = validate(fixture)
            self.assertTrue(any("must be exactly" in error for error in errors))

    def test_per_skill_reference_copy_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            local_references = (
                fixture
                / "plugins"
                / "apple-ui-design"
                / "skills"
                / "apple-ui-direction"
                / "references"
            )
            local_references.mkdir()
            (local_references / "copied.md").write_text("copy", encoding="utf-8")

            errors = validate(fixture)
            self.assertTrue(
                any("not a local references directory" in error for error in errors)
            )

    def test_repository_document_inside_package_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            package_readme = (
                fixture / "plugins" / "apple-ui-design" / "README.md"
            )
            package_readme.write_text("repository docs", encoding="utf-8")

            errors = validate(fixture)
            self.assertIn(
                "installable package contains forbidden repository entry: README.md",
                errors,
            )

    def test_duplicate_root_reference_source_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            duplicate_root = fixture / "references"
            duplicate_root.mkdir()
            (duplicate_root / "source-registry.json").write_text(
                "{}", encoding="utf-8"
            )

            errors = validate(fixture)
            self.assertTrue(
                any("duplicates plugin shared ownership" in error for error in errors)
            )
            self.assertTrue(
                any("exactly one plugin-owned copy" in error for error in errors)
            )

    def test_wrong_marketplace_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            marketplace_path = (
                fixture / ".agents" / "plugins" / "marketplace.json"
            )
            marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
            marketplace["plugins"][0]["source"]["path"] = "./wrong"
            marketplace_path.write_text(json.dumps(marketplace), encoding="utf-8")

            errors = validate(fixture)
            self.assertIn(
                "marketplace source must point to ./plugins/apple-ui-design",
                errors,
            )

    def test_missing_delivery_contract_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            (
                fixture
                / "plugins"
                / "apple-ui-design"
                / "references"
                / "delivery-contracts.md"
            ).unlink()

            errors = validate(fixture)
            self.assertTrue(
                any("delivery-contracts.md" in error for error in errors)
            )

    def test_missing_engineering_routing_reference_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            (
                fixture
                / "plugins"
                / "apple-ui-design"
                / "references"
                / "engineering-routing.md"
            ).unlink()

            errors = validate(fixture)
            self.assertTrue(
                any("engineering-routing.md" in error for error in errors)
            )

    def test_skill_without_delivery_contract_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            review_skill = (
                fixture
                / "plugins"
                / "apple-ui-design"
                / "skills"
                / "apple-ui-review"
                / "SKILL.md"
            )
            review_contents = review_skill.read_text(encoding="utf-8")
            review_skill.write_text(
                review_contents.replace(
                    "`../../references/delivery-contracts.md`",
                    "`../../references/validation-and-review.md`",
                ),
                encoding="utf-8",
            )

            errors = validate(fixture)
            self.assertIn(
                "apple-ui-review must directly apply the shared delivery contracts",
                errors,
            )

    def test_skill_without_engineering_routing_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            review_skill = (
                fixture
                / "plugins"
                / "apple-ui-design"
                / "skills"
                / "apple-ui-review"
                / "SKILL.md"
            )
            review_contents = review_skill.read_text(encoding="utf-8")
            review_skill.write_text(
                review_contents.replace(
                    "`../../references/engineering-routing.md`",
                    "`../../references/validation-and-review.md`",
                ),
                encoding="utf-8",
            )

            errors = validate(fixture)
            self.assertIn(
                "apple-ui-review must directly apply the engineering routing rules",
                errors,
            )

    def test_implicit_invocation_policy_must_match_frontmatter(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            agent_yaml = (
                fixture
                / "plugins"
                / "apple-ui-design"
                / "skills"
                / "apple-ui-direction"
                / "agents"
                / "openai.yaml"
            )
            contents = agent_yaml.read_text(encoding="utf-8")
            agent_yaml.write_text(
                contents.replace(
                    "allow_implicit_invocation: true",
                    "allow_implicit_invocation: false",
                ),
                encoding="utf-8",
            )

            errors = validate(fixture)
            self.assertTrue(
                any("must explicitly enable implicit invocation" in error for error in errors)
            )

    def test_missing_delivery_contract_heading_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            fixture = self.make_fixture(temp_dir)
            contracts = (
                fixture
                / "plugins"
                / "apple-ui-design"
                / "references"
                / "delivery-contracts.md"
            )
            contents = contracts.read_text(encoding="utf-8")
            contracts.write_text(
                contents.replace(
                    "## Contract 5: Native Prototype",
                    "## Native Prototype",
                ),
                encoding="utf-8",
            )

            errors = validate(fixture)
            self.assertIn(
                "delivery contracts missing required heading: "
                "## Contract 5: Native Prototype",
                errors,
            )


if __name__ == "__main__":
    unittest.main()
