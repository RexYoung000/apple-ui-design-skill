from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from evaluate_skill_regression_output import (  # noqa: E402
    evaluate_case,
    evaluate_goldens,
    load_cases,
)


class SkillRegressionOutputTests(unittest.TestCase):
    def setUp(self) -> None:
        suite_root = REPO_ROOT / "evals" / "skill-regression"
        self.cases_path = suite_root / "cases.json"
        self.goldens_path = suite_root / "goldens.json"
        self.cases = load_cases(self.cases_path)

    def test_review_golden_passes_output_assertions(self) -> None:
        self.assertEqual(
            evaluate_goldens(
                self.cases_path,
                self.goldens_path,
                REPO_ROOT,
            ),
            [],
        )

    def test_missing_required_pattern_fails(self) -> None:
        case = self.cases["review-direct-evidence-bounded"]
        failures = evaluate_case(case, "A short generic review.")
        self.assertTrue(any("missing required output pattern" in item for item in failures))

    def test_forbidden_pattern_fails(self) -> None:
        case = self.cases["review-risk-score-accessibility"]
        output = (
            "Screenshot review: I cannot confirm accessibility without runtime "
            "VoiceOver and keyboard evidence.\nScore: 8"
        )
        failures = evaluate_case(case, output)
        self.assertTrue(any("matched forbidden output pattern" in item for item in failures))

    def test_expected_installed_skill_trace_passes(self) -> None:
        case = self.cases["review-direct-evidence-bounded"]
        golden_path = json.loads(
            self.goldens_path.read_text(encoding="utf-8")
        )["goldens"][0]["output_path"]
        output = (REPO_ROOT / golden_path).read_text(encoding="utf-8")
        trace = (
            "/Users/test/.codex/plugins/cache/apple-ui-design/apple-ui-design/"
            "0.1.0/skills/apple-ui-review/SKILL.md"
        )
        self.assertEqual(evaluate_case(case, output, trace), [])

    def test_wrong_installed_skill_trace_fails(self) -> None:
        case = self.cases["review-direct-evidence-bounded"]
        golden_path = json.loads(
            self.goldens_path.read_text(encoding="utf-8")
        )["goldens"][0]["output_path"]
        output = (REPO_ROOT / golden_path).read_text(encoding="utf-8")
        trace = (
            "/Users/test/.codex/plugins/cache/apple-ui-design/apple-ui-design/"
            "0.1.0/skills/apple-ui-direction/SKILL.md"
        )
        failures = evaluate_case(case, output, trace)
        self.assertTrue(any("expected installed skill was not loaded" in item for item in failures))
        self.assertTrue(any("forbidden installed skill was loaded" in item for item in failures))


if __name__ == "__main__":
    unittest.main()
