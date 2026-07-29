#!/usr/bin/env python3
"""Run every deterministic repository and skill regression gate."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    python = sys.executable
    commands = [
        [python, "scripts/validate_plugin_architecture.py"],
        [python, "scripts/validate_product_starting_point_evals.py"],
        [python, "scripts/validate_delivery_contract_evals.py"],
        [python, "scripts/validate_trigger_routing_evals.py"],
        [python, "scripts/validate_skill_regression_evals.py"],
        [python, "scripts/validate_source_registry.py"],
        [
            python,
            "scripts/evaluate_skill_regression_output.py",
            "--goldens",
        ],
        [python, "-m", "unittest", "discover", "-s", "tests", "-v"],
    ]

    for command in commands:
        print("+", " ".join(command), flush=True)
        completed = subprocess.run(command, cwd=root, check=False)
        if completed.returncode != 0:
            return completed.returncode
    print("all deterministic regression checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
