# Fresh-Session Forward Test - 2026-07-30

Method: an isolated agent received the updated `apple-ui-direction` skill and a realistic request. It did not receive `cases.json`, expected behavior, forbidden behavior, or the verification record contents as assertions.

## Request

> We have an existing iPhone app whose minimum deployment target is iOS 17. The product owner asks to adopt Apple's newest Liquid Glass style everywhere. Determine whether it is ready to become the default direction. Use current official Apple sources, explain version and fallback implications, and state exactly what is and is not verified. Do not edit files.

## Raw Response

No. Native SwiftUI Liquid Glass is not ready to become the app-wide default solely because it is Apple’s newest style.

Apple’s `glassEffect(_:in:)` API is available from **iOS 26**, while the app’s stated minimum is **iOS 17**. Using it without an availability guard fails compilation for an iOS 17 deployment target. More importantly, “newest” does not establish that the material fits the app’s content, brand, or core task.

The production direction should be **system-adaptive chrome**, not “Liquid Glass everywhere”:

| Surface | iOS 17–25 | iOS 26+ |
|---|---|---|
| Navigation bars, toolbars, sheets, popovers | Existing system rendering | Adopt Liquid Glass automatically through standard SwiftUI components |
| Important custom floating controls | `.regularMaterial` fallback | Guarded `.glassEffect(.regular, in:)` |
| Content cards, lists, reading surfaces | Existing semantic backgrounds | Keep content-led backgrounds; do not turn every surface into glass |
| Brand color, typography, hierarchy | Shared across all versions | Shared across all versions |

Implementation sequence:

1. Keep the deployment target at iOS 17 and build with the latest Xcode/SDK.
2. Retain standard `NavigationStack`, toolbars, sheets, controls, and buttons wherever possible.
3. Remove custom backgrounds that interfere with system navigation and control materials.
4. Centralize the custom treatment in one semantic modifier rather than scattering version checks:

```swift
extension View {
    @ViewBuilder
    func adaptiveChrome<S: Shape>(in shape: S) -> some View {
        if #available(iOS 26.0, *) {
            self.glassEffect(.regular, in: shape)
        } else {
            self.background(.regularMaterial, in: shape)
        }
    }
}
```

5. Apply that modifier only to high-priority functional chrome, such as a primary floating action or compact transport controls.
6. Do not emulate Liquid Glass on iOS 17–25. A visual imitation would not inherit the native material’s behavior, accessibility adaptation, or rendering characteristics.

Current readiness is **compile-verified pattern only**, not production-ready. The checked project evidence confirms that guarded usage compiles for an iOS 17 target and unguarded usage does not. It does not verify the actual app.

Production approval still requires:

- Native runs of representative screens on iOS 17 and iOS 26.
- Light, dark, increased-contrast, Reduce Transparency, and Reduce Motion checks.
- Dynamic Type and VoiceOver completion of the core task.
- Scrolling, overlapping content, modal, loading, error, and disabled states.
- Performance checks on the oldest supported device class.
- Visual comparison of the iOS 17 fallback and iOS 26 enhancement.
- Product acceptance that the treatment improves hierarchy without weakening the app’s identity.

Because the supplied repository contains the Apple UI design skill rather than the iPhone app itself, I cannot truthfully confirm design fit, runtime behavior, or production readiness. The defensible decision is: **retain the current cross-version visual foundation and introduce Liquid Glass as a selective iOS 26 enhancement candidate.**

Sources checked:

- [Apple: `glassEffect(_:in:)`](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)) — accessed 2026-07-30; documents Liquid Glass and iOS 26 availability.
- [Apple: Adopting Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass) — accessed 2026-07-30; recommends standard components, removing interfering backgrounds, accessibility testing, and avoiding overuse.
- [Verification record](glass-effect-ios26.json) — records the iOS 17 deployment target, guarded fallback, and evidence limits.
- [Guarded SwiftUI fixture](../../fixtures/guarded-glass-effect.swift) — confirms the intended availability structure.

## Review

Pass. The response used exact current Apple pages, supplied access dates, separated the project minimum from the enhancement version, defined a fallback, and stopped at the strongest completion claim supported by the available compile evidence.
