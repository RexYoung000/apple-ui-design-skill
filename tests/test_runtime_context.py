from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_runtime_context import validate  # noqa: E402


class RuntimeContextTests(unittest.TestCase):
    def setUp(self) -> None:
        self.contract_path = REPO_ROOT / "evals" / "runtime-context" / "contract.json"

    def make_fixture(self, temp_dir: str) -> tuple[Path, Path]:
        root = Path(temp_dir)
        shutil.copytree(
            REPO_ROOT / "plugins" / "apple-ui-design",
            root / "plugins" / "apple-ui-design",
        )
        contract_dir = root / "evals" / "runtime-context"
        contract_dir.mkdir(parents=True)
        contract = json.loads(self.contract_path.read_text(encoding="utf-8"))
        fixture_contract = contract_dir / "contract.json"
        fixture_contract.write_text(json.dumps(contract), encoding="utf-8")
        run_dir = contract_dir / "runs"
        run_dir.mkdir()
        (run_dir / "2026-07-31.md").write_text(
            "small-static-direction\nbehavioral-platform-adaptation\n",
            encoding="utf-8",
        )
        return root, fixture_contract

    def test_current_runtime_context_is_valid(self) -> None:
        errors, metrics = validate(self.contract_path, repo_root=REPO_ROOT)
        self.assertEqual(errors, [])
        contract = json.loads(self.contract_path.read_text(encoding="utf-8"))
        self.assertEqual(metrics, contract["current"])
        self.assertEqual(contract["limits"]["skill_words"], 2500)
        self.assertEqual(contract["limits"]["total_words"], 17500)
        self.assertLessEqual(metrics["skills"]["words"], 2500)
        self.assertLessEqual(metrics["total"]["words"], 17500)

    def test_invalid_measurement_date_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root, contract_path = self.make_fixture(temp_dir)
            contract = json.loads(contract_path.read_text(encoding="utf-8"))
            contract["measured_at"] = "2026-02-30"
            contract_path.write_text(json.dumps(contract), encoding="utf-8")
            errors, _ = validate(contract_path, repo_root=root)
        self.assertTrue(any("measured_at" in error for error in errors))

    def test_recorded_measurement_drift_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root, contract_path = self.make_fixture(temp_dir)
            contract = json.loads(contract_path.read_text(encoding="utf-8"))
            contract["current"]["total"]["words"] += 1
            contract_path.write_text(json.dumps(contract), encoding="utf-8")
            errors, _ = validate(contract_path, repo_root=root)
        self.assertTrue(any("current.total" in error for error in errors))

    def test_missing_load_condition_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root, contract_path = self.make_fixture(temp_dir)
            reference = root / "plugins" / "apple-ui-design" / "references" / "current-sources.md"
            source = reference.read_text(encoding="utf-8").replace("## Load When", "## Usage")
            reference.write_text(source, encoding="utf-8")
            errors, _ = validate(contract_path, repo_root=root)
        self.assertTrue(any("missing Load When" in error for error in errors))

    def test_long_reference_without_contents_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root, contract_path = self.make_fixture(temp_dir)
            reference = root / "plugins" / "apple-ui-design" / "references" / "authority-and-principles.md"
            source = reference.read_text(encoding="utf-8").replace("## Contents", "## Overview")
            reference.write_text(source, encoding="utf-8")
            errors, _ = validate(contract_path, repo_root=root)
        self.assertTrue(any("long reference missing Contents" in error for error in errors))

    def test_duplicate_ownership_marker_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root, contract_path = self.make_fixture(temp_dir)
            skill = root / "plugins" / "apple-ui-design" / "skills" / "apple-ui-direction" / "SKILL.md"
            skill.write_text(
                skill.read_text(encoding="utf-8")
                + "\nsingle runtime source for decision authority and tradeoff resolution\n",
                encoding="utf-8",
            )
            errors, _ = validate(contract_path, repo_root=root)
        self.assertTrue(any("ownership marker must appear once" in error for error in errors))

    def test_repository_maintenance_text_is_rejected_from_runtime(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root, contract_path = self.make_fixture(temp_dir)
            reference = root / "plugins" / "apple-ui-design" / "references" / "research-and-source-evidence.md"
            reference.write_text(
                reference.read_text(encoding="utf-8") + "\n## Registry Maintenance\n",
                encoding="utf-8",
            )
            errors, _ = validate(contract_path, repo_root=root)
        self.assertTrue(any("repository-only marker" in error for error in errors))

    def test_skill_budget_overrun_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root, contract_path = self.make_fixture(temp_dir)
            skill = root / "plugins" / "apple-ui-design" / "skills" / "apple-ui-review" / "SKILL.md"
            skill.write_text(
                skill.read_text(encoding="utf-8") + ("\nextra context" * 400),
                encoding="utf-8",
            )
            errors, _ = validate(contract_path, repo_root=root)
        self.assertTrue(any("word budget" in error for error in errors))

    def test_missing_reference_contract_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root, contract_path = self.make_fixture(temp_dir)
            contract = json.loads(contract_path.read_text(encoding="utf-8"))
            contract["reference_contracts"].pop()
            contract_path.write_text(json.dumps(contract), encoding="utf-8")
            errors, _ = validate(contract_path, repo_root=root)
        self.assertTrue(any("cover every Markdown reference" in error for error in errors))

    def test_duplicate_reference_contract_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root, contract_path = self.make_fixture(temp_dir)
            contract = json.loads(contract_path.read_text(encoding="utf-8"))
            contract["reference_contracts"].append(contract["reference_contracts"][0])
            contract_path.write_text(json.dumps(contract), encoding="utf-8")
            errors, _ = validate(contract_path, repo_root=root)
        self.assertTrue(any("duplicate reference contract path" in error for error in errors))

    def test_forward_test_record_must_name_both_scenarios(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root, contract_path = self.make_fixture(temp_dir)
            run_path = root / "evals" / "runtime-context" / "runs" / "2026-07-31.md"
            run_path.write_text("small-static-direction\n", encoding="utf-8")
            errors, _ = validate(contract_path, repo_root=root)
        self.assertTrue(any("forward-test record missing scenario" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
