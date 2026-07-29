# Skill Trigger and Output Regression

This is the release-level evaluation matrix for the three bundled Apple UI Design skills.

## Coverage

Each skill owns exactly one case in each scenario:

- `direct`: explicitly requests the skill or its named workflow;
- `indirect`: expresses the same outcome without a skill name;
- `incomplete`: omits evidence that must be requested or kept unresolved;
- `negative`: contains Apple framework terms but is implementation-only engineering work;
- `risk`: invites unsupported version, asset, runtime, accessibility, or completion claims.

Every case has fixed fixtures, skill-load expectations, output patterns, forbidden patterns, and human-review assertions.

## Deterministic gate

```bash
python3 scripts/run_regression_checks.py
```

This validates the matrix, fixtures, regular expressions, golden checksums, all other repository validators, and unit tests.

## Fresh-session evaluation

Run the user request and fixture material in a new session without the hidden assertions. Save the raw JSONL trace and final response, then run:

```bash
python3 scripts/evaluate_skill_regression_output.py \
  <case-id> --trace <trace.jsonl> --output <output.md>
```

The trace check expects installed plugin reads under the Codex plugin cache. Run live checks outside this repository so an agent cannot satisfy routing assertions by inspecting the test suite.

## Golden outputs

`goldens.json` records reviewed outputs and their SHA-256 checksums. A golden is a comparison baseline, not a universal template or exact-string expectation. It may change only after explicit review of the output, evidence boundary, and checksum diff.
