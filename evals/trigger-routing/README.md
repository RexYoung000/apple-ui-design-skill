# Trigger and Engineering Routing Evaluations

This suite protects Issue #5 routing boundaries and provides the positive, negative, and mixed cases that Issue #4 can reuse in a broader regression harness.

## What a pass means

- Product UI direction, Apple-platform adaptation, and evidence-based UI review requests select the matching bundled skill.
- Implementation-only Swift, SwiftUI, UIKit, and AppKit requests do not select a bundled design skill merely because they mention an Apple framework.
- Mixed requests keep one primary owner based on the requested final outcome and state the engineering handoff.
- Bounded design-led SwiftUI code is allowed only when it directly validates an approved interface decision and preserves architecture, domain state, data, dependencies, and delivery mechanics.
- UIKit and AppKit projects receive framework-aware design support without an implicit SwiftUI migration or unsupported production-integration promise.

## Files

- `cases.json` is the reviewable source of truth.
- `runs/` stores selected fresh-session evidence. Raw sessions must receive only the user request, not the case assertions.
- `scripts/validate_trigger_routing_evals.py` validates the suite schema and required coverage.

## Validation

```bash
python3 scripts/validate_trigger_routing_evals.py
python3 -m unittest tests.test_trigger_routing_evals -v
```

Structural validation proves coverage and consistency, not model routing by itself. Before closing a routing change, reinstall the edited plugin, start fresh ephemeral sessions, and inspect whether positive prompts load the expected skill while engineering-only negatives do not load any bundled Apple UI Design skill.
