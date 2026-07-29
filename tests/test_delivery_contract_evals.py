from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_delivery_contract_evals import validate  # noqa: E402


class DeliveryContractEvalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.suite_path = REPO_ROOT / "evals" / "delivery-contracts" / "cases.json"
        self.suite = json.loads(self.suite_path.read_text(encoding="utf-8"))

    def validate_data(self, data: dict) -> list[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "cases.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            errors, _ = validate(path, repo_root=REPO_ROOT)
        return errors

    def test_current_suite_is_valid(self) -> None:
        errors, coverage = validate(self.suite_path, repo_root=REPO_ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(sum(coverage.values()), 6)
        self.assertTrue(all(count == 1 for count in coverage.values()))

    def test_missing_contract_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"] = [
            case for case in changed["cases"] if case["contract"] != "screen-flow"
        ]

        errors = self.validate_data(changed)
        self.assertIn("missing required contract: screen-flow", errors)

    def test_duplicate_contract_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        duplicate = copy.deepcopy(changed["cases"][0])
        duplicate["id"] = "another-visual-direction"
        changed["cases"].append(duplicate)

        errors = self.validate_data(changed)
        self.assertIn(
            "contract must have exactly one evaluation case: visual-direction=2",
            errors,
        )

    def test_wrong_owner_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"][3]["owner_skill"] = "apple-ui-direction"

        errors = self.validate_data(changed)
        self.assertTrue(any("owner_skill must be" in error for error in errors))

    def test_missing_artifact_contract_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"][4]["expected_artifacts"] = []

        errors = self.validate_data(changed)
        self.assertTrue(
            any("expected_artifacts must be a non-empty" in error for error in errors)
        )

    def test_missing_fixture_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"][5]["fixture_paths"] = [
            "evals/delivery-contracts/fixtures/missing.md"
        ]

        errors = self.validate_data(changed)
        self.assertTrue(any("fixture does not exist" in error for error in errors))

    def test_fixture_outside_suite_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"][0]["fixture_paths"] = ["README.md"]

        errors = self.validate_data(changed)
        self.assertTrue(
            any("must stay in evals/delivery-contracts/fixtures" in error for error in errors)
        )

    def test_missing_run_evidence_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"][0]["run_evidence_paths"] = [
            "evals/delivery-contracts/runs/missing.png"
        ]

        errors = self.validate_data(changed)
        self.assertTrue(
            any("run evidence does not exist" in error for error in errors)
        )

    def test_run_evidence_outside_suite_is_rejected(self) -> None:
        changed = copy.deepcopy(self.suite)
        changed["cases"][0]["run_evidence_paths"] = ["README.md"]

        errors = self.validate_data(changed)
        self.assertTrue(
            any(
                "must stay in evals/delivery-contracts/runs" in error
                for error in errors
            )
        )


if __name__ == "__main__":
    unittest.main()
