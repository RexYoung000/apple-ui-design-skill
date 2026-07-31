# Accessibility and Localization

## Load When

Load this reference when accessibility, localization, assistive behavior, input alternatives, visual settings, content expansion, or locale behavior affects the requested outcome or completion claim. Do not load the full method for a task with no material scenario in scope.

This is the single runtime source for the accessibility and localization method. Select scenarios by the product's core task, target users, platforms, input modes, content, and risk. Do not claim broad accessibility from one label check or one assistive technology.

## Contents

- [Outcome Contract](#outcome-contract)
- [Evidence Levels](#evidence-levels)
- [Platform Task Matrix](#platform-task-matrix)
- [Assistive Behaviors](#assistive-behaviors)
- [Visual, Motion, and Content Settings](#visual-motion-and-content-settings)
- [Custom Controls](#custom-controls)
- [Localization Matrix](#localization-matrix)
- [Reporting](#reporting)
- [Current Apple Sources](#current-apple-sources)

## Outcome Contract

A user relying on an in-scope accessibility setting, assistive technology, input method, language, or region must be able to:

- understand the screen, current state, and available actions;
- locate and operate the primary action;
- complete the core task;
- identify errors and recover;
- understand destructive consequences;
- perceive progress, selection, interruption, and completion.

Cover relevant visual, hearing, mobility, speech, and cognitive conditions without assuming one person's needs represent the whole category. Accessibility constrains task outcomes, not brand expression. Custom typography, color, shape, motion, controls, and interaction models remain valid when people can perceive, understand, operate, and recover.

If a required outcome disappears, describe the failed task and do not claim that scenario is accessible or verified. Follow `authority-and-principles.md` for hard boundaries and informed tradeoffs instead of silently imposing a replacement design.

## Evidence Levels

Keep these levels separate:

| Level | What it can establish | What it cannot establish |
| --- | --- | --- |
| Design review | Intended order, alternatives, reflow, contrast candidates, non-color meaning, and planned recovery | Runtime semantics or assistive-technology operation |
| Semantic and automated inspection | Exposed name, role, value, state, actions, focus order, and audit findings in the tested build | What VoiceOver, Voice Control, Switch Control, or Full Keyboard Access users actually experience end to end |
| Real assistive behavior run | Core-task completion with the named technology, setting, input, OS, and device | Other technologies, platforms, locales, or untested states |

An Accessibility Inspector result, `performAccessibilityAudit`, accessibility-label assertion, or UI test is semantic or automated evidence. It is not a VoiceOver run. A screen reader pass does not establish Voice Control, Switch Control, keyboard, pointer, hearing, cognitive, localization, or reduced-motion completion.

Record the exact build, OS, device or simulator, setting, input, task, states, result, and evidence artifact. If an assistive technology is unavailable in the represented environment, mark it unverified and provide a manual device path.

## Platform Task Matrix

Create a task matrix before testing. Replace generic examples with the product's actual critical path.

| Platform | Required task path | Inputs and behaviors to select by risk | Runtime evidence |
| --- | --- | --- | --- |
| iOS | Launch or resume, understand state, complete the primary touch task, handle permission/error, confirm result | Touch, Dynamic Type, VoiceOver, Voice Control, Switch Control, AssistiveTouch, Reduce Motion, Increase Contrast, Reduce Transparency | Physical device for final assistive-technology claims; simulator may support layout, settings, semantics, and automation only where the capability is actually available |
| iPadOS | Complete the task in compact and expansive windows, preserve focus through resize or scene changes, recover from interruption | Touch, hardware keyboard, Full Keyboard Access, pointer, VoiceOver, Voice Control, Switch Control, AssistiveTouch, drag alternative | Native iPad or supported simulator for represented inputs; physical device when hardware or assistive behavior is not faithfully simulated |
| macOS | Open or restore a window, navigate content and commands, complete and reverse the task, recover focus after sheets or windows | Keyboard-only path, visible focus, VoiceOver, Voice Control, Switch Control, Pointer Control, menus, shortcuts, context menus, drag alternative | Real Mac app for window, menu, command, focus, hover, pointer, and assistive-technology completion |

For every selected row, exercise:

1. entry and orientation;
2. discovery of the primary action;
3. operation and state change;
4. error, cancellation, or interruption;
5. recovery and completion;
6. confirmation of the final result.

Do not make an essential action gesture-only, drag-only, hover-only, color-only, motion-only, or spatial-position-only without an equivalent path.

## Assistive Behaviors

### VoiceOver

- Expose a meaningful name, role, value, state, and available actions.
- Use hints only when the action is not clear from the name, role, and context.
- Group fragments that express one concept; hide decorative assets from the accessibility tree.
- Preserve logical reading and focus order across reflow, sheets, errors, and responsive layouts.
- Announce important asynchronous changes only when the result would otherwise be missed.
- Complete the actual task with VoiceOver before claiming VoiceOver verification.

### Voice Control

- Give actionable elements distinct, speakable labels.
- Check that visible labels and exposed names do not conflict.
- Exercise "Show Names" or equivalent discovery when labels repeat.
- Complete primary, cancellation, correction, and destructive-confirmation paths by voice.

### Switch Control

- Verify that scanning reaches every required action in a useful order.
- Avoid interactions that depend on speed, simultaneous gestures, or an unexposed drag.
- Complete selection, activation, error recovery, and exit from modal or custom containers.

### AssistiveTouch

- Provide alternatives for multi-finger, timed, repeated, force, device-motion, and complex gestures.
- Confirm that menus, custom gestures, and dwell behavior do not hide required actions.

### Full Keyboard Access

- Complete the task without touch or pointer.
- Keep focus visible and ordered; preserve it through updates, sheets, windows, and recovery.
- Do not override system accessibility shortcuts.
- Make custom controls reachable and operable with expected activation and escape behavior.

### Pointer Control

- Keep required actions usable without precise movement, hover-only discovery, or drag-only completion.
- Verify target stability, selection, context actions, and a non-drag alternative.

## Visual, Motion, and Content Settings

### Information and contrast

- Never use color as the only indicator of state, category, error, progress, or selection.
- Pair meaningful color changes with text, shape, iconography, position, or accessible semantics.
- Check contrast on actual backgrounds, materials, disabled states, overlays, charts, and selections.
- Apply the current Apple HIG guidance checked on 2026-07-30: 17 pt and smaller regular text uses at least 4.5:1; 18 pt and larger text and bold text use at least 3:1.
- If the default design does not meet the stated minimum, at least provide the higher-contrast result when Increase Contrast is enabled. Verify both light and dark appearances when supported.

### Reduce Transparency

When Reduce Transparency is enabled, replace semitransparent backgrounds that carry legibility or hierarchy with an opaque treatment. Preserve grouping, elevation meaning, state, and brand character rather than mechanically removing every material.

### Reduce Motion

Reduce automatic, repetitive, zooming, scaling, parallax, and spatial motion that can cause discomfort or obscure state. Preserve meaning and feedback with immediate state changes, fades, reduced distance or intensity, color, haptics, or audio as appropriate. Do not remove required feedback by disabling all animation.

### Text and cognitive load

- Use scalable semantic text roles unless the content is genuinely fixed-format.
- Test task-relevant accessibility text sizes, multiline content, and reachable actions after reflow.
- Avoid fixed-height containers around meaningful user-visible text.
- Use plain, consistent labels and explicit recovery messages for consequential actions.
- Test interruption, timeout, progress, destructive confirmation, and resumed state.

### Hearing

- Do not make audio the only carrier of instructions, status, error, or completion.
- Provide visible or haptic equivalents for meaningful sounds when the task requires them.
- Verify captions or transcripts for in-scope spoken media.

## Custom Controls

A custom control does not need to resemble a system control. Verify the experience contract:

- role: what kind of thing it is;
- name: what it represents;
- value and state: what is currently true;
- actions: what a user can do, including an alternative to custom gestures;
- focus and order: how it is reached and left;
- result: whether the intended task actually changes state and completes;
- recovery: how cancellation, error, and reversal work.

Judge the control by exposed meaning and task results, not visual similarity to a default component. Native components are often lower-risk because they inherit semantics and behaviors, but they are evidence-informed implementation candidates rather than a mandatory visual skin.

## Localization Matrix

Do not validate localization with translated screenshots alone. Run the app in each supported language and region that materially affects the task.

| Scenario | What to exercise | Failure to catch |
| --- | --- | --- |
| Long content and pseudolanguages | Double-Length, Accented, Bounded String, and Tall pseudolanguages as relevant | Truncation, overlap, hidden actions, broken vertical rhythm |
| RTL | Right-to-Left pseudolanguage plus a real target language | Wrong navigation direction, paragraph alignment, focus order, mixed-direction text, or mechanical mirroring of numbers, logos, and universal symbols |
| Plurals | Zero, one, two, few, many, and other forms supported by target languages | English-only singular/plural assumptions |
| Grammatical variation | Gender, person, inflection, and ambiguous translator context where the language requires it | Concatenated fragments or grammatically invalid UI |
| Region formats | Dates, times, numbers, currency, measurements, durations, addresses, and lists | Hardcoded order, separators, units, or symbols |
| CJK | Realistic Chinese, Japanese, and Korean content, mixed Latin text, line wrapping, input, and large text | Inappropriate line breaks, clipped glyphs, excessive fixed height, or Latin-only density assumptions |

Use project localization systems; do not hardcode user-visible strings or manually concatenate translated sentence fragments. Provide translator context for ambiguous text. Avoid embedding essential text in raster images.

For RTL, let system components mirror where appropriate. Mirror directional navigation and progress when meaning changes with direction. Do not mechanically reverse digit order, logos, or universal symbols. Align paragraphs according to their text language.

For verification:

1. use pseudolanguages early to expose structural failures;
2. run each supported App Language and App Region combination that changes the task;
3. use locale-aware APIs for dates, numbers, currency, measurements, durations, and lists;
4. review real translated content with appropriate language expertise before release.

## Reporting

Describe the failed or completed task, not a checklist label.

Prefer:

> On iPadOS 18.5 with Full Keyboard Access, focus reaches the custom duration control, Space activates it, Escape returns to the session, and the completion state remains announced. Evidence: recording and test log.

Avoid:

> Accessibility passed.

For every result, state:

- platform, OS, build, device, and input or setting;
- task and states exercised;
- evidence level: design review, semantic/automated, or real assistive behavior;
- observed result and evidence link;
- remaining untested technologies, locales, and risks.

Use `design-reviewed`, `semantics-checked`, or `<named technology>-experience-verified` only when the corresponding evidence exists. Never collapse these into a broad "accessible" claim.

## Current Apple Sources

Exact Apple pages checked on 2026-07-30:

- [Accessibility, Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/accessibility) - contrast, non-color meaning, VoiceOver, Voice Control, mobility-related assistive technologies, Full Keyboard Access, Switch Control, and Reduce Motion guidance.
- [Right to left, Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/right-to-left) - mirroring, paragraph direction, navigation, numbers, logos, and symbols.
- [Testing localizations when running your app](https://developer.apple.com/documentation/xcode/testing-localizations-when-running-your-app) - run every supported language and region; select App Language and App Region independently.
- [Preparing your interface for localization](https://developer.apple.com/documentation/xcode/preparing-your-interface-for-localization) - nonlocalized-string diagnostics and Xcode pseudolanguages including Double-Length, RTL, Accented, Bounded String, and Tall.
- [Localizing strings that contain plurals](https://developer.apple.com/documentation/xcode/localizing-strings-that-contain-plurals) - language-specific plural variants and string catalogs.
- [Unlock the power of grammatical agreement](https://developer.apple.com/videos/play/wwdc2023/10153) - Foundation grammatical agreement guidance and multilingual examples.
- [`accessibilityReduceTransparency`](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducetransparency) - published setting behavior and availability.
- [`performAccessibilityAudit(for:_:)`](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/performaccessibilityaudit(for:_:)) - automated XCTest accessibility audit API.
- [`XCUIVoiceOverService`](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice) - programmatic VoiceOver control is currently Beta and published for iOS/iPadOS/macOS 27.0+; do not use it as evidence for older represented runtimes.

Recheck version-sensitive wording and availability at task time using `current-sources.md`.
