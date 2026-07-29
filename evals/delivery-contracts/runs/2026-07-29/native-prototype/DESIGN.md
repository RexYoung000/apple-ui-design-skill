# Stillpoint expandable session card — scoped direction

## Outcome and boundary

- **User-confirmed direction:** an existing iPhone app uses an in-place expandable session card that feels quiet, tactile, and responsive.
- **Core task:** reveal or dismiss current-session controls without leaving the focus context.
- **Platform scope:** iPhone, minimum iOS 17, touch input.
- **Primary delivery contract:** Native Prototype. The evidence gate requires an operable SwiftUI path plus recorded native execution of standard and Reduce Motion behavior before an experience-verification claim.
- **Prototype boundary:** local sample timer/session state only. Background execution, persistence, production architecture, haptics, note editing, and destructive confirmation are not implemented.

## Interaction logic

| Input | Current state | Result |
|---|---|---|
| Tap card | collapsed | expand in place and reveal pause, finish, and note actions |
| Tap card | expanded | collapse in place |
| Tap card during transition | transitioning | reverse toward the new final intent from the current presentation |
| Repeated rapid taps | any card presentation | settle according to the final tap intent |
| Tap Pause | expanded | retain controls, change session status to paused |
| Tap Finish | expanded | retain the card shell, replace timer/actions with a completed result |
| Tap Note | expanded | update local feedback only; note entry is out of scope |

The full card is a named button with an expanded/collapsed accessibility value. Nested session actions use independent buttons and at least 44-point interaction regions.

## Motion expressions

### Standard

- A short ease-in-out expansion changes the card’s layout in place and fades the controls into the revealed space.
- The animation is value-driven rather than a queued sequence, so a new tap changes the same target state and reverses from the current presentation.
- There is no spring, bounce, confetti, or celebratory effect.

### Reduce Motion

- Layout changes immediately so the new state is never ambiguous.
- A restrained card-outline fade preserves action feedback without moving or resizing content.
- State text and accessibility value change with the same semantics as the standard expression.

Exact durations and visual values are **rendered prototype proposals**, not production tokens. Their quality remains open to Rex’s visual acceptance.

## Representative evidence states

- Collapsed
- Expanded
- Reversing under rapid taps
- Paused
- Completed
- Expanded with Reduce Motion enabled

## Accessibility intent

- Semantic scalable text styles and flexible vertical layout.
- VoiceOver name, expanded/collapsed value, and expand/collapse hint on the card.
- Named Pause, Finish, and Note actions.
- Minimum 44×44-point action regions.
- State meaning is carried by text and structure, not color alone.

## Acceptance

On an iPhone simulator or device:

1. Open the prototype and tap the card once; it should expand in place.
2. Tap it again during expansion, then tap once more during reversal; it should settle expanded, matching the final tap.
3. Use Pause and Finish; each should produce an explicit textual state.
4. Enable Reduce Motion, relaunch, and tap the card; layout should change immediately with restrained fade feedback.
5. With VoiceOver, the card should announce its title, state value, and expand/collapse action; all three revealed actions should be reachable.
