# Interaction and Motion Regression Suite

This suite protects the user-led interaction and motion method introduced for Issue #14.

It verifies that the installable plugin:

- preserves confirmed product interaction and motion decisions across direction, adaptation, and review;
- defines material behavior through a testable interaction contract;
- treats motion as functional, spatial, feedback, expressive, brand, or emotional product language;
- applies different risk emphasis to tool, content, and experimental products;
- maps confirmed behavior to platform inputs without silently replacing the product model;
- covers interruption, reversal, rapid repeat input, recovery, final intent, and Reduce Motion;
- distinguishes meaningful behavioral exploration from recolors or timing-only variants;
- refuses native interaction or motion claims based on HTML, static frames, timing tables, or build success.

Run:

```bash
python3 scripts/validate_interaction_motion_evals.py
```

For a fresh-session check, give the model only a case's `prompt` and any named source artifact. Do not pass `expected_behavior`, `forbidden_behavior`, or `source_markers`.

The preserved Stillpoint native evidence establishes the named tool-product path only: expansion, interruption, reversal, final intent, Pause, Finish, and the recorded standard and Reduce Motion expressions on the represented simulator. The content and experimental cases protect method behavior; they are not native experience evidence.
