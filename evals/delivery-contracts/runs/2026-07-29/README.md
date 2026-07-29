# Delivery Contract Forward Test — 2026-07-29

Skill revision: working tree for Issue #3
Method: one isolated task per contract; each task received only its owning skill, directly required shared references, the user request, and one raw fixture. `cases.json` and its assertions were hidden.

## Result

| Contract | Result | Strongest supported stage | Preserved evidence |
|---|---|---|---|
| Visual Direction | Pass | Rendered proposal; direction not yet aligned | Two materially different screens, comparison render, contrast and bounds report |
| Screen or Flow | Pass | Prototype complete in browser | Operable prototype, state map, eight screenshots, 54/54 browser checks |
| Design System | Pass | Design complete as rendered proposal | Component states, realistic German product screen, contrast and semantics checks |
| Platform Adaptation | Pass | Target layouts design-complete | Shared-versus-specific matrix, four target layouts, automated bounds checks |
| Native Prototype | Pass after correction | Experience verified for the scoped simulator behavior | SwiftUI project, post-fix build/test logs, screenshots, Standard and actual Reduce Motion recordings |
| UI Review | Pass | Evidence-bounded unverified consultation | Severity findings and exact native acceptance path |

## Material correction

The first native-prototype run enabled the real Reduce Motion system setting and recorded it, but the code still animated card layout for 0.14 seconds while the design record promised immediate layout change. This was a contract failure.

The prototype was corrected so:

- Standard mode retains the approved 0.38-second spatial expansion.
- Reduce Motion changes layout inside a SwiftUI transaction with animations disabled.
- A separate 0.16-second outline fade preserves non-spatial feedback.
- The UI test sends one native three-tap event and verifies the final expanded intent, Pause, and Finish.
- Both `ReduceMotionEnabled=0` and `ReduceMotionEnabled=1` runs were rebuilt, retested, and re-recorded after the correction.

## Evidence boundaries

- Static HTML renders prove only the visible hypotheses and layouts they contain.
- The screen-flow prototype proves the operated browser paths; its permission picker and import are explicitly mocked.
- Platform-adaptation renders do not prove iPadOS or macOS windowing, input, focus, commands, VoiceOver, or production behavior.
- Native-prototype verification is limited to the iPhone 15 Pro simulator on iOS 17.5 and the scoped local session state. Background execution, persistence, production architecture, Note editing, haptics, extreme Dynamic Type, full VoiceOver use, and user acceptance remain outside the evidence.
- The review fixture contains text observations only, so the review does not claim visual or runtime validation.

## User acceptance

No forward-test agent can mark a visual direction, design system, platform adaptation, motion rhythm, or final experience as user accepted. The preserved artifacts provide concrete paths for Rex to perform that acceptance.
