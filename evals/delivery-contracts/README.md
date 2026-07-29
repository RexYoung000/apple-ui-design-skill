# Delivery Contract Evaluations

This suite verifies that each mode-level contract produces the artifact needed to answer the user’s design question and limits completion claims to available evidence.

## Coverage

| Contract | Owning skill | Required artifact |
|---|---|---|
| `visual-direction` | `apple-ui-direction` | Rendered key screens |
| `screen-flow` | `apple-ui-direction` | Operable path and state map |
| `design-system` | `apple-ui-direction` | Rendered component states applied to a product screen |
| `platform-adaptation` | `apple-platform-adaptation` | Decision matrix and representative target layouts |
| `native-prototype` | `apple-ui-direction` | Native runnable prototype and runtime evidence |
| `ui-review` | `apple-ui-review` | Evidence-bounded severity findings |

## Structural validation

Run:

```bash
python3 scripts/validate_delivery_contract_evals.py
python3 -m unittest discover -s tests -v
```

The validator checks complete contract coverage, owner routing, fixture paths, preserved run-evidence paths, required artifacts, evidence requirements, forbidden claims, and behavioral assertions. It confirms that reviewable evidence remains in the repository; it does not semantically grade the artifact.

## Forward-test protocol

For every case:

1. start a fresh agent with only the named skill, request, and raw fixtures;
2. hide `cases.json`, expected artifacts, and assertions;
3. allow the agent to create its deliverable in a new temporary workspace;
4. preserve the raw response and produced artifact or runtime log;
5. check every `must_do`, `must_not_do`, evidence requirement, and forbidden claim;
6. fail the case when polished prose substitutes for the required artifact;
7. remove the temporary workspace after preserving only reviewable evidence.

Static and browser artifacts can prove visual hypotheses. Native experience claims require the target Apple runtime. User acceptance is never simulated by the evaluator.
