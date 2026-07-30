from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_current_source_evals import validate, validate_record  # noqa: E402


class CurrentSourceEvalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases_path = REPO_ROOT / "evals" / "current-source-verification" / "cases.json"
        self.cases = json.loads(self.cases_path.read_text(encoding="utf-8"))
        self.record_path = (
            REPO_ROOT
            / "evals"
            / "current-source-verification"
            / "runs"
            / "2026-07-30"
            / "glass-effect-ios26.json"
        )
        self.record = json.loads(self.record_path.read_text(encoding="utf-8"))

    def validate_cases(self, cases: dict) -> list[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "cases.json"
            path.write_text(json.dumps(cases), encoding="utf-8")
            errors, _, _ = validate(path, repo_root=REPO_ROOT)
        return errors

    def validate_record_data(self, record: dict) -> list[str]:
        return validate_record(
            record,
            self.record_path.relative_to(REPO_ROOT),
            REPO_ROOT,
        )

    def test_current_suite_is_valid(self) -> None:
        errors, coverage, records = validate(self.cases_path, repo_root=REPO_ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(records, 1)
        self.assertEqual(
            {key.removeprefix("skill/") for key in coverage if key.startswith("skill/")},
            {
                "apple-ui-direction",
                "apple-platform-adaptation",
                "apple-ui-review",
            },
        )

    def test_broad_apple_homepage_is_rejected(self) -> None:
        changed = copy.deepcopy(self.record)
        changed["official_sources"][0]["url"] = "https://developer.apple.com/documentation/"
        errors = self.validate_record_data(changed)
        self.assertTrue(any("exact HTTPS Apple Developer page" in error for error in errors))

    def test_missing_fallback_is_rejected(self) -> None:
        changed = copy.deepcopy(self.record)
        changed["version_scope"]["fallback"] = ""
        errors = self.validate_record_data(changed)
        self.assertTrue(any("fallback must be a non-empty string" in error for error in errors))

    def test_unverified_record_requires_reason(self) -> None:
        changed = copy.deepcopy(self.record)
        changed["status"] = "unverified"
        changed["official_sources"] = []
        errors = self.validate_record_data(changed)
        self.assertTrue(any("unverified_reason is required" in error for error in errors))

    def test_missing_runtime_evidence_is_rejected(self) -> None:
        changed = copy.deepcopy(self.record)
        changed["runtime_evidence"]["checks"][0]["evidence"] = (
            "evals/current-source-verification/runs/2026-07-30/missing.log"
        )
        errors = self.validate_record_data(changed)
        self.assertTrue(any("does not exist" in error for error in errors))

    def test_missing_policy_tag_is_rejected(self) -> None:
        changed = copy.deepcopy(self.cases)
        for case in changed["cases"]:
            case["tags"] = [tag for tag in case["tags"] if tag != "runtime-conflict"]
        errors = self.validate_cases(changed)
        self.assertTrue(any("must cover tag: runtime-conflict" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
