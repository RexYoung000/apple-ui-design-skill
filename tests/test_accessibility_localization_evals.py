from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_accessibility_localization_evals import validate  # noqa: E402


class AccessibilityLocalizationEvalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases_path = REPO_ROOT / "evals" / "accessibility-localization" / "cases.json"
        self.cases = json.loads(self.cases_path.read_text(encoding="utf-8"))

    def validate_cases(self, cases: dict) -> list[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "cases.json"
            path.write_text(json.dumps(cases), encoding="utf-8")
            errors, _ = validate(path, repo_root=REPO_ROOT)
        return errors

    def test_accessibility_localization_suite_is_valid(self) -> None:
        errors, coverage = validate(self.cases_path, repo_root=REPO_ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(
            {key.removeprefix("skill/") for key in coverage if key.startswith("skill/")},
            {
                "apple-ui-direction",
                "apple-platform-adaptation",
                "apple-ui-review",
            },
        )

    def test_missing_evidence_level_coverage_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        for case in changed["cases"]:
            case["tags"] = [tag for tag in case["tags"] if tag != "evidence-levels"]
        errors = self.validate_cases(changed)
        self.assertTrue(any("must cover tag: evidence-levels" in error for error in errors))

    def test_missing_source_marker_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["cases"][0]["source_markers"][
            "plugins/apple-ui-design/references/accessibility-and-localization.md"
        ].append("marker that must not exist")
        errors = self.validate_cases(changed)
        self.assertTrue(any("source marker missing" in error for error in errors))

    def test_unknown_skill_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["cases"][0]["skill"] = "generic-accessibility"
        errors = self.validate_cases(changed)
        self.assertTrue(any("not a bundled Apple UI skill" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
