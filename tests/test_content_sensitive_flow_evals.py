from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_content_sensitive_flow_evals import validate  # noqa: E402


class ContentSensitiveFlowEvalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases_path = REPO_ROOT / "evals" / "content-sensitive-flows" / "cases.json"
        self.cases = json.loads(self.cases_path.read_text(encoding="utf-8"))

    def validate_cases(self, cases: dict) -> list[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "cases.json"
            path.write_text(json.dumps(cases), encoding="utf-8")
            errors, _ = validate(path, repo_root=REPO_ROOT)
        return errors

    def test_content_sensitive_flow_suite_is_valid(self) -> None:
        errors, coverage = validate(self.cases_path, repo_root=REPO_ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(
            {key.removeprefix("flow/") for key in coverage if key.startswith("flow/")},
            {
                "content-recovery",
                "permission-privacy",
                "identity-account-data",
                "commerce",
                "regulated-professional",
            },
        )

    def test_missing_commerce_transparency_coverage_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        for case in changed["cases"]:
            case["tags"] = [
                tag for tag in case["tags"] if tag != "commerce-transparency"
            ]
        errors = self.validate_cases(changed)
        self.assertTrue(
            any("must cover tag: commerce-transparency" in error for error in errors)
        )

    def test_missing_regulated_flow_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        for case in changed["cases"]:
            if case["flow"] == "regulated-professional":
                case["flow"] = "content-recovery"
        errors = self.validate_cases(changed)
        self.assertTrue(
            any("must cover flow: regulated-professional" in error for error in errors)
        )

    def test_changed_source_review_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["source_review"]["urls"].pop()
        errors = self.validate_cases(changed)
        self.assertTrue(
            any("official-source set" in error for error in errors)
        )

    def test_changed_preserved_evidence_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["preserved_evidence"]["artifacts"].pop()
        errors = self.validate_cases(changed)
        self.assertTrue(
            any("evidence paths must match the FrameKeep record" in error for error in errors)
        )

    def test_missing_forward_test_scenario_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["forward_test_record"]["scenarios"].pop()
        errors = self.validate_cases(changed)
        self.assertTrue(
            any("two Issue #8 product runs" in error for error in errors)
        )

    def test_missing_source_marker_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["cases"][0]["source_markers"][
            "plugins/apple-ui-design/references/content-and-sensitive-flows.md"
        ].append("marker that must not exist")
        errors = self.validate_cases(changed)
        self.assertTrue(any("source marker missing" in error for error in errors))

    def test_unknown_skill_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        changed["cases"][0]["skill"] = "generic-policy-review"
        errors = self.validate_cases(changed)
        self.assertTrue(any("not a bundled Apple UI skill" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
