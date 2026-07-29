from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_product_starting_point_evals import validate  # noqa: E402


class ProductStartingPointEvalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.suite_path = (
            REPO_ROOT / "evals" / "product-starting-point" / "cases.json"
        )
        self.suite = json.loads(self.suite_path.read_text(encoding="utf-8"))

    def validate_data(self, data: dict) -> list[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            errors, _ = validate(path, repo_root=REPO_ROOT)
        return errors

    def test_current_suite_is_valid(self) -> None:
        errors, scenarios = validate(self.suite_path, repo_root=REPO_ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(sum(scenarios.values()), 3)

    def test_duplicate_case_id_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"][1]["id"] = changed["cases"][0]["id"]

        errors = self.validate_data(changed)
        self.assertTrue(any("duplicate case id" in error for error in errors))

    def test_missing_fixture_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"][0]["fixture_paths"] = [
            "evals/product-starting-point/fixtures/missing.md"
        ]

        errors = self.validate_data(changed)
        self.assertTrue(any("fixture does not exist" in error for error in errors))

    def test_missing_required_scenario_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"] = [
            case
            for case in changed["cases"]
            if case["decision_scale"] != "major-redesign"
        ]

        errors = self.validate_data(changed)
        self.assertIn(
            "missing required scenario: existing-product/major-redesign", errors
        )

    def test_empty_negative_assertions_are_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"][2]["assertions"]["must_not_do"] = []

        errors = self.validate_data(changed)
        self.assertTrue(
            any("assertions.must_not_do must be a non-empty" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
