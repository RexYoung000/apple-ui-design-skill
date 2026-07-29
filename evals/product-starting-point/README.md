# Product Starting-Point Evaluations

This suite checks how the skill distinguishes:

1. a small change to an existing product;
2. a major redesign with conflicting project evidence;
3. a zero-to-one direction with no user research.

`cases.json` contains the fixed user requests, raw fixture paths, mode-contract inputs, and manual `must_do` / `must_not_do` assertions. The fixtures intentionally contain enough evidence to reveal whether the skill repeats known questions, preserves an existing interface without review, invents a persona, or overstates validation.

## Structural validation

Run:

```bash
python3 scripts/validate_product_starting_point_evals.py
python3 -m unittest discover -s tests -v
```

The validator checks schema integrity, fixture availability, assertion presence, and coverage of all three decision branches. It does not pretend to grade natural-language quality.

## Forward-test protocol

For each case:

1. start a fresh agent with no prior conversation;
2. tell it to use `plugins/apple-ui-design/skills/apple-ui-direction/SKILL.md`;
3. provide only the case request and the listed raw fixtures;
4. do not expose `cases.json` or its assertions;
5. preserve the raw response;
6. review every `must_do` and `must_not_do` assertion;
7. if a case fails, update the smallest relevant skill rule and rerun only that case with another fresh agent.

The latest development run is preserved under `runs/`. These responses are behavioral evidence, not canonical wording or a golden output. Issue #3 can consume `mode_contract_inputs` when defining mode-level delivery contracts; Issue #4 can import the requests, fixtures, and assertions into the broader regression runner.
