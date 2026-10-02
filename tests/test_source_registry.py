from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_source_registry import validate  # noqa: E402


class SourceRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry_path = (
            REPO_ROOT
            / "plugins"
            / "apple-ui-design"
            / "references"
            / "source-registry.json"
        )
        self.registry = json.loads(self.registry_path.read_text(encoding="utf-8"))

    def validate_data(self, data: dict) -> tuple[list[str], list[str]]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "registry.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            errors, warnings, _ = validate(path, max_age_days=180)
        return errors, warnings

    def test_current_registry_is_valid(self) -> None:
        errors, warnings, _ = validate(self.registry_path, max_age_days=180)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_schema_requires_domain_metadata(self) -> None:
        changed = copy.deepcopy(self.registry)
        changed["schema_version"] = 1
        errors, _ = self.validate_data(changed)
        self.assertIn("schema_version must equal 2", errors)

        changed["schema_version"] = 2
        del changed["sources"][0]["design_domains"]
        errors, _ = self.validate_data(changed)
        self.assertIn("sources[0] missing fields: design_domains", errors)

    def test_domains_can_overlap(self) -> None:
        changed = copy.deepcopy(self.registry)
        changed["sources"][0]["design_domains"] = ["ui", "ux", "interaction", "motion", "terminology"]
        errors, _ = self.validate_data(changed)
        self.assertEqual(errors, [])

    def test_invalid_domains_are_rejected(self) -> None:
        for domains in ([], None, "ui", ["UI"], ["ui", "engineering"], ["ui", 3], ["ui", "ui"]):
            with self.subTest(domains=domains):
                changed = copy.deepcopy(self.registry)
                changed["sources"][0]["design_domains"] = domains
                errors, _ = self.validate_data(changed)
                self.assertTrue(any("design_domains" in error for error in errors))

    def test_duplicate_url_is_rejected(self) -> None:
        changed = copy.deepcopy(self.registry)
        duplicate = copy.deepcopy(changed["sources"][0])
        duplicate["id"] = "duplicate-source"
        changed["sources"].append(duplicate)

        errors, _ = self.validate_data(changed)
        self.assertTrue(any("duplicate URL" in error for error in errors))

    def test_excluded_source_cannot_allow_reuse(self) -> None:
        changed = copy.deepcopy(self.registry)
        excluded = next(source for source in changed["sources"] if source["status"] == "excluded")
        excluded["allowed_uses"] = ["visual-inspiration"]

        errors, _ = self.validate_data(changed)
        self.assertTrue(any("must allow only 'none'" in error for error in errors))

    def test_excluded_category_cannot_be_enabled_for_selection(self) -> None:
        changed = copy.deepcopy(self.registry)
        excluded = next(source for source in changed["sources"] if source["status"] == "excluded")
        excluded.update(status="active", allowed_uses=["screen-observation"], reuse_status="reference-only")

        errors, _ = self.validate_data(changed)
        self.assertTrue(any("excluded category must use excluded status" in error for error in errors))

    def test_excluded_status_cannot_claim_an_eligible_category(self) -> None:
        changed = copy.deepcopy(self.registry)
        excluded = next(source for source in changed["sources"] if source["status"] == "excluded")
        excluded["category"] = "observable-gallery"

        errors, _ = self.validate_data(changed)
        self.assertTrue(any("excluded status must use excluded category" in error for error in errors))

    def test_excluded_source_must_forbid_reuse(self) -> None:
        changed = copy.deepcopy(self.registry)
        excluded = next(source for source in changed["sources"] if source["status"] == "excluded")
        excluded["reuse_status"] = "observe-and-link-only"

        errors, _ = self.validate_data(changed)
        self.assertTrue(any("excluded source must use do-not-use" in error for error in errors))

    def test_active_source_cannot_carry_excluded_use_metadata(self) -> None:
        for field, value in (("allowed_uses", ["none", "screen-observation"]), ("reuse_status", "do-not-use")):
            with self.subTest(field=field):
                changed = copy.deepcopy(self.registry)
                changed["sources"][0][field] = value
                errors, _ = self.validate_data(changed)
                self.assertTrue(any("must be excluded" in error for error in errors))

    def test_future_review_date_is_rejected(self) -> None:
        changed = copy.deepcopy(self.registry)
        changed["last_reviewed"] = f"{date.today().year + 1}-01-01"

        errors, _ = self.validate_data(changed)
        self.assertIn("last_reviewed cannot be in the future", errors)


if __name__ == "__main__":
    unittest.main()
