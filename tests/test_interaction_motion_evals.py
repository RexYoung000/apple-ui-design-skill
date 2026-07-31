from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_interaction_motion_evals import validate  # noqa: E402


class InteractionMotionEvalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases_path = REPO_ROOT / "evals" / "interaction-motion" / "cases.json"
        self.cases = json.loads(self.cases_path.read_text(encoding="utf-8"))

    def validate_cases(self, cases: dict) -> list[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "cases.json"
            path.write_text(json.dumps(cases), encoding="utf-8")
            errors, _ = validate(path, repo_root=REPO_ROOT)
        return errors

    def test_interaction_motion_suite_is_valid(self) -> None:
        errors, coverage = validate(self.cases_path, repo_root=REPO_ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(
            {key.removeprefix("scenario/") for key in coverage if key.startswith("scenario/")},
            {"tool", "content", "experimental"},
        )

    def test_missing_interruption_reversal_coverage_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        for case in changed["cases"]:
            case["tags"] = [
                tag for tag in case["tags"] if tag != "interruption-reversal"
            ]
        errors = self.validate_cases(changed)
        self.assertTrue(
            any("must cover tag: interruption-reversal" in error for error in errors)
        )

    def test_missing_product_scenario_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        for case in changed["cases"]:
            if case["scenario"] == "content":
                case["scenario"] = "tool"
        errors = self.validate_cases(changed)
        self.assertTrue(any("must cover scenario: content" in error for error in errors))

    def test_missing_source_marker_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["cases"][0]["source_markers"][
            "plugins/apple-ui-design/references/interaction-and-motion.md"
        ].append("marker that must not exist")
        errors = self.validate_cases(changed)
        self.assertTrue(any("source marker missing" in error for error in errors))

    def test_changed_native_evidence_set_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["preserved_evidence"]["artifacts"].pop()
        errors = self.validate_cases(changed)
        self.assertTrue(
            any("evidence paths must match the Stillpoint record" in error for error in errors)
        )

    def test_unknown_skill_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["cases"][0]["skill"] = "generic-motion-review"
        errors = self.validate_cases(changed)
        self.assertTrue(any("not a bundled Apple UI skill" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
