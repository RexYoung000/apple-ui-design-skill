# Fresh-session routing evidence — 2026-07-29

## Environment

- Codex CLI ephemeral sessions
- Working directory: `/tmp`
- Sandbox: read-only
- Plugin source: local marketplace checkout
- Installed cache version: `0.1.0+codex.20260729090555`
- Assertions from `cases.json` were not included in the prompts

The run directory records a reviewable summary rather than full session transcripts, which may contain unrelated local configuration and plugin-catalog diagnostics.

## Results

| Case | Expected | Observed installed-skill read | Result |
|---|---|---|---|
| Zero-to-one iPad direction | `apple-ui-direction` | `skills/apple-ui-direction/SKILL.md`, followed by delivery, context, authority, and engineering-routing references | Pass |
| Existing iPhone experience adapted to Mac | `apple-platform-adaptation` | `skills/apple-platform-adaptation/SKILL.md`, followed by platform, delivery, evidence, and engineering-routing references | Pass |
| Screenshot-only iOS subscription review | `apple-ui-review` | `skills/apple-ui-review/SKILL.md`, followed by review, accessibility, delivery, and engineering-routing references | Pass |
| Swift generic compilation failure | engineering workflow | No Apple UI Design skill or shared reference was loaded; response requested the minimum compile context | Pass |
| UIKit diffable-data-source crash | engineering workflow | No Apple UI Design skill or shared reference was loaded; response requested crash, stack, lifecycle, identifier, and concurrency evidence | Pass |
| UIKit-to-AppKit product adaptation with production integration | adaptation plus engineering handoff | `skills/apple-platform-adaptation/SKILL.md` and shared routing references; result assigned product and interaction decisions to adaptation and AppKit correctness and integration to engineering | Pass |

## Observed boundary behavior

- Positive prompts selected the expected skill without an explicit `$skill-name`.
- Framework keywords alone did not trigger the plugin for Swift or UIKit engineering failures.
- The mixed AppKit case did not promise SwiftUI implementation or treat a SwiftUI mockup as AppKit evidence.
- The mixed case kept platform experience decisions in the adaptation workflow and assigned menus, responder-chain implementation, window lifecycle, state consistency, tests, and release mechanics to engineering.
- The review case stopped at evidence requirements because no screenshot was supplied; it did not manufacture findings.

## Evidence limit

These six sessions validate representative positive, negative, and mixed routes. The full 19-case set is structurally validated and ready for the broader automated trigger harness in Issue #4; this run does not claim that every model or future wording variant has been exhaustively tested.
