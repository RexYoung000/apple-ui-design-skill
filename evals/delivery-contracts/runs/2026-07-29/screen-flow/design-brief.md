# FrameKeep first-run import — design brief

Date: 2026-07-29
Primary delivery contract: **Screen or Flow**

## Evidence status

- **User-confirmed product intent and constraints:** privately organize selected personal photos into small reference collections; iPhone hypothesis; explicit buttons are the primary path; the flow must cover permission denial and retry; the product must never imply access before selection or grant.
- **Project facts from the supplied fixture:** this is zero-to-one; no native permission implementation exists; system picker and permission result may be mocked when labelled; required states are welcome, explanation, system-permission handoff, denied, limited access, selection, importing, recoverable failure, retry, cancellation, and completion.
- **External evidence checked:** not researched. This prototype does not make version-sensitive Apple API claims.
- **Design inference:** a single forward path with explicit recovery actions is the cheapest artifact that can answer whether the first-run flow is understandable.
- **Unvalidated hypotheses:** the audience can understand “selected photos only”; the proposed copy, visual hierarchy, and collection naming feel trustworthy; iPhone remains the right target platform; minimum iOS version is undecided.

## Outcome and boundary

The user starts with no photo access, understands why FrameKeep asks, grants access only to selected items, imports a small set, and lands in the first collection. Permission denial and import failure must both remain recoverable without losing the user’s place.

This is an **HTML interaction prototype**. It tests flow clarity, state continuity, explicit controls, focus movement, and recovery. It does not implement or verify Photos permission, the native Photos picker, file transfer, persistent storage, VoiceOver, Dynamic Type, or iOS runtime behavior.

## Interaction decisions

1. Permission explanation precedes the simulated system handoff.
2. The simulated system handoff offers only explicit results: deny or allow selected photos.
3. Denial is a recoverable state. “Try again” repeats the permission handoff; “Not now” cancels back to welcome.
4. Limited access is acknowledged before selection so the user understands the privacy boundary.
5. The simulated picker never claims the app can see the library. It displays representative mock items only after the limited-access result.
6. Import is disabled until at least one item is selected.
7. Cancelling the picker returns to the explanation; cancelling import returns to the selection with the selection preserved.
8. Recoverable import failure preserves selection and retries directly.
9. Completion lands on a populated first collection and exposes a clear flow reset for repeated evaluation.
10. Prototype-only scenario controls sit outside the product surface and are labelled as non-product controls.

## Accessibility intent

- Every essential action is a semantic button; no gesture-only path exists.
- Selection state is conveyed with text and `aria-pressed`, not color alone.
- Modal focus moves into the permission handoff and returns to the triggering control.
- Import progress and state changes use a live region.
- Focus moves to the new screen heading after navigation.
- Layout scrolls and reflows rather than relying on fixed-height text containers.
- Reduced-motion users receive immediate state changes without losing progress or completion feedback.

## Visual direction

Minimal, quiet, and content-led. Warm neutral surfaces and an ink/leaf palette are rendered proposals for review, not approved brand tokens. The only expressive device is a small “stacked frame” mark that reinforces private collection-building without competing with the recovery flow.

## Evidence gate

The artifact can be called **prototype complete** only after the happy path, permission denial/retry, import failure/retry, and cancellation paths are operated in the browser and evidence is preserved. Apple-native behavior remains unverified.
