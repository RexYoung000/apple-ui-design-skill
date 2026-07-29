from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_decision_authority_evals import validate  # noqa: E402


class DecisionAuthorityEvalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases_path = REPO_ROOT / "evals" / "decision-authority" / "cases.json"
        self.cases = json.loads(self.cases_path.read_text(encoding="utf-8"))

    def validate_data(self, cases: dict) -> list[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            cases_path = Path(temp_dir) / "cases.json"
            cases_path.write_text(json.dumps(cases), encoding="utf-8")
            errors, _ = validate(cases_path, repo_root=REPO_ROOT)
        return errors

    def test_current_suite_is_valid(self) -> None:
        errors, coverage = validate(self.cases_path, repo_root=REPO_ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(sum(coverage[key] for key in coverage if key.startswith("skill/")), 7)
        self.assertEqual(
            {key.removeprefix("tag/") for key in coverage if key.startswith("tag/")},
            {
                "hard-boundary",
                "product-authority",
                "experience-baseline",
                "platform-advice",
                "shipped-evidence",
                "implementation-advice",
                "communication-pace",
                "internal-terminology",
            },
        )

    def test_missing_policy_tag_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        for case in changed["cases"]:
            case["tags"] = [
                tag for tag in case["tags"] if tag != "hard-boundary"
            ]
        errors = self.validate_data(changed)
        self.assertTrue(any("must cover tag: hard-boundary" in error for error in errors))

    def test_source_outside_plugin_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["cases"][0]["source_markers"] = {
            "README.md": ["Apple UI Design"]
        }
        errors = self.validate_data(changed)
        self.assertTrue(any("must stay inside plugins/apple-ui-design" in error for error in errors))

    def test_missing_policy_marker_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        source = next(iter(changed["cases"][0]["source_markers"]))
        changed["cases"][0]["source_markers"][source] = [
            "marker that does not exist"
        ]
        errors = self.validate_data(changed)
        self.assertTrue(any("missing policy marker" in error for error in errors))

    def test_every_skill_must_be_represented(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["cases"] = [
            case
            for case in changed["cases"]
            if case["owner_skill"] != "apple-ui-review"
        ]
        errors = self.validate_data(changed)
        self.assertTrue(
            any("apple-ui-review must own at least one" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
