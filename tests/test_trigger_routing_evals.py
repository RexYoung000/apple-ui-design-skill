from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_trigger_routing_evals import validate  # noqa: E402


class TriggerRoutingEvalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.suite_path = REPO_ROOT / "evals" / "trigger-routing" / "cases.json"
        self.suite = json.loads(self.suite_path.read_text(encoding="utf-8"))

    def validate_data(self, data: dict) -> list[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            errors, _ = validate(path)
        return errors

    def test_current_suite_is_valid(self) -> None:
        errors, coverage = validate(self.suite_path)
        self.assertEqual(errors, [])
        self.assertEqual(coverage["kind/positive"], 6)
        self.assertEqual(coverage["kind/negative"], 7)
        self.assertEqual(coverage["kind/boundary"], 6)

    def test_duplicate_case_id_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"][1]["id"] = changed["cases"][0]["id"]
        errors = self.validate_data(changed)
        self.assertTrue(any("duplicate case id" in error for error in errors))

    def test_negative_case_cannot_select_design_skill(self) -> None:
        changed = copy.deepcopy(self.suite)
        negative = next(
            case for case in changed["cases"] if case["case_kind"] == "negative"
        )
        negative["expected_primary_route"] = "apple-ui-direction"
        errors = self.validate_data(changed)
        self.assertTrue(
            any("negative case must select engineering-workflow" in error for error in errors)
        )

    def test_missing_engineering_domain_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"] = [
            case
            for case in changed["cases"]
            if case["engineering_domain"] != "concurrency"
        ]
        errors = self.validate_data(changed)
        self.assertTrue(
            any("missing engineering-negative domains" in error for error in errors)
        )

    def test_empty_forbidden_behavior_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"][0]["must_not_do"] = []
        errors = self.validate_data(changed)
        self.assertTrue(
            any("must_not_do must be a non-empty string list" in error for error in errors)
        )

    def test_framework_coverage_is_required(self) -> None:
        changed = copy.deepcopy(self.suite)
        for case in changed["cases"]:
            if case["framework"] == "appkit":
                case["framework"] = "framework-neutral"
        errors = self.validate_data(changed)
        self.assertIn("at least two appkit cases are required", errors)


if __name__ == "__main__":
    unittest.main()
