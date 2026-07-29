from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_skill_regression_evals import validate  # noqa: E402


class SkillRegressionEvalTests(unittest.TestCase):
    def setUp(self) -> None:
        suite_root = REPO_ROOT / "evals" / "skill-regression"
        self.cases_path = suite_root / "cases.json"
        self.goldens_path = suite_root / "goldens.json"
        self.cases = json.loads(self.cases_path.read_text(encoding="utf-8"))
        self.goldens = json.loads(self.goldens_path.read_text(encoding="utf-8"))

    def validate_data(
        self,
        cases: dict | None = None,
        goldens: dict | None = None,
    ) -> list[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            cases_path = temp / "cases.json"
            goldens_path = temp / "goldens.json"
            cases_path.write_text(
                json.dumps(cases or self.cases), encoding="utf-8"
            )
            goldens_path.write_text(
                json.dumps(goldens or self.goldens), encoding="utf-8"
            )
            errors, _ = validate(
                cases_path,
                goldens_path,
                repo_root=REPO_ROOT,
            )
        return errors

    def test_current_suite_is_valid(self) -> None:
        errors, coverage = validate(
            self.cases_path,
            self.goldens_path,
            repo_root=REPO_ROOT,
        )
        self.assertEqual(errors, [])
        self.assertEqual(sum(coverage[key] for key in coverage if key.startswith("scenario/")), 15)

    def test_each_skill_requires_every_scenario(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["cases"] = [
            case
            for case in changed["cases"]
            if case["id"] != "direction-incomplete-wellbeing"
        ]
        errors = self.validate_data(cases=changed)
        self.assertTrue(any("exactly one incomplete case" in error for error in errors))

    def test_negative_case_must_forbid_all_skills(self) -> None:
        changed = copy.deepcopy(self.cases)
        case = next(
            item
            for item in changed["cases"]
            if item["id"] == "review-negative-xctest-host"
        )
        case["expected_route"]["must_not_load"].remove("apple-ui-review")
        errors = self.validate_data(cases=changed)
        self.assertTrue(any("negative case must forbid all" in error for error in errors))

    def test_fixture_outside_suite_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["cases"][0]["fixture_paths"] = ["README.md"]
        errors = self.validate_data(cases=changed)
        self.assertTrue(any("must stay in evals/skill-regression/fixtures" in error for error in errors))

    def test_invalid_output_regex_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["cases"][0]["output_assertions"]["required_all"] = ["["]
        errors = self.validate_data(cases=changed)
        self.assertTrue(any("invalid regex" in error for error in errors))

    def test_missing_skill_behavior_marker_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["skill_policy_sources"]["apple-ui-review"]["required_markers"] = [
            "marker that is not present"
        ]
        errors = self.validate_data(cases=changed)
        self.assertTrue(
            any("missing required skill behavior marker" in error for error in errors)
        )

    def test_golden_checksum_change_is_rejected(self) -> None:
        changed = copy.deepcopy(self.goldens)
        changed["goldens"][0]["sha256"] = "0" * 64
        errors = self.validate_data(goldens=changed)
        self.assertTrue(any("checksum mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
