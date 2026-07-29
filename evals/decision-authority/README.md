# Decision Authority Regression Suite

This suite protects the public decision and clarification contract introduced for Issue #6.

It is intentionally scenario-based. Each case names a realistic conflict, the expected behavior, the behavior that would regress the contract, and exact policy markers that must remain in the installable plugin.

The suite verifies that:

- hard obligations are not silently ignored;
- confirmed product decisions are not replaced by Apple convention;
- accessibility is evaluated through core-task outcomes instead of a default visual skin;
- shipped behavior, implementation convenience, and external inspiration remain evidence rather than automatic authority;
- informed non-hard-boundary tradeoffs are recorded and honored;
- communication pace is configurable, with one-question alignment reserved for blocking, path-dependent decisions;
- project-internal terms are not presented as Apple terminology.

Run:

```bash
python3 scripts/validate_decision_authority_evals.py
```

For a fresh-session check, give the model only a case’s `prompt` and the referenced project material. Do not include `expected_behavior`, `forbidden_behavior`, or `source_markers` in the prompt.
