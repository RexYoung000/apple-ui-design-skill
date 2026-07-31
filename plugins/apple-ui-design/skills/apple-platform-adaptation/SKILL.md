---
name: apple-platform-adaptation
description: Adapt an established iOS, iPadOS, or macOS product experience to another Apple platform or a multi-platform model. Use when the requested outcome is platform-specific hierarchy, navigation, windowing, density, input, continuity, or a shared-versus-specific adaptation decision. Do not use for zero-to-one direction, critique-only review, or implementation-only Swift, SwiftUI, UIKit, or AppKit work such as compilation, concurrency, architecture, state management, performance, API usage, CI, packaging, or release.
---

# Apple Platform Adaptation

Translate an established product model across Apple platforms. Preserve what makes the product itself while redesigning the parts that should respond to platform role, available space, windowing, input, and learned behavior.

## Required Inputs

Derive from the project before asking:

- source experience and current evidence;
- target user and core task;
- source and target platforms;
- product role and feature scope on each platform;
- minimum versions, windows, orientations, and input modes;
- shared product DNA and confirmed interaction decisions.

If unresolved platform roles or feature relationships would block and materially change the information architecture, ask one focused, path-dependent question. Gather independent platform facts compactly or in parallel, follow the user’s preferred pace, and never impose primary, peer, or companion labels.

Read `../../references/authority-and-principles.md`, `../../references/context-and-alignment.md`, `../../references/engineering-routing.md`, `../../references/delivery-contracts.md`, and `../../references/apple-platform-adaptation.md` before defining the adaptation. Select the Platform Adaptation contract and state its artifact and evidence gate. Decide whether the result stops at design evidence, includes a bounded design-led prototype, or requires engineering partnership.

## Adaptation Workflow

### 1. Inspect the source experience

Inspect current requirements, UI, navigation, states, assets, components, strings, platform conditionals, deployment targets, and runtime behavior. Treat shipped behavior as evidence, not automatic correctness.

If no established experience exists, route direction definition to `$apple-ui-direction` before continuing.

### 2. Define what is shared and what changes

Record:

- shared user outcome, content model, terminology, brand character, and semantic states;
- platform-specific task priority, hierarchy, navigation, density, window behavior, and input;
- capabilities that are equal, overlapping, or intentionally different;
- continuity requirements between devices.

Do not create an iPad or Mac experience by stretching the iPhone layout. Do not replace a distinctive product interaction merely because a system control exists.

When a confirmed interaction differs from common Apple behavior, state the observed platform fact, user impact, recommendation, and native verification path. If the product owner knowingly retains the choice and no hard boundary remains, record the tradeoff and adapt it faithfully rather than repeatedly substituting the conventional control.

Read `../../references/design-system-and-dna.md` to preserve shared product DNA without redesigning it by default.
Read `../../references/interaction-and-motion.md` when behavior is material. Preserve the confirmed interaction contract and motion purposes, then translate their expression rather than reopening the product model by default.

### 3. Map platform expressions

Define representative layouts and behaviors for:

- iOS touch, safe areas, navigation, sheets, keyboard, and interruption;
- iPadOS compact and expansive windows, columns, sidebars, inspectors, pointer, keyboard, drag and drop, and reflow;
- macOS window sizes, menus, commands, shortcuts, pointer, hover, focus, selection, context menus, and multiple-window behavior.

Map the confirmed operation to touch, Pencil, keyboard, pointer, focus, commands, windows, and system events that are relevant on each target platform. Preserve state meaning, feedback, interruption, reversal, recovery, and final intent even when the surface control or navigation expression changes.

Read `../../references/current-sources.md` and use exact current Apple pages for version-sensitive platform claims. Keep the project minimum version, newer enhancement version, fallback, and represented runtime evidence separate. Mark unavailable or unsupported conclusions unverified. Use platform convention as evidence, not as automatic ownership of visual style.

### 4. Preserve accessibility, localization, and task meaning

Read `../../references/accessibility-and-localization.md`. Define a core-task matrix for each target platform and equivalent completion paths for the relevant touch, keyboard, pointer, VoiceOver, Voice Control, Switch Control, AssistiveTouch, focus, visual-setting, content-expansion, locale, and reduced-motion scenarios. Keep design review, semantic automation, and named assistive-technology runs as separate evidence levels.

Platform-specific presentation may differ; the confirmed outcome and state meaning may not disappear.

### 5. Prototype and validate the differences

Read `../../references/prototyping-and-implementation.md` and `../../references/validation-and-review.md`.

Use visible layout evidence for each material size class or window state. Exercise input and window behavior in native environments before claiming platform adaptation is verified. Pair with an engineering skill when production implementation is requested.

UIKit and AppKit products remain valid adaptation inputs. Preserve their actual architecture and framework unless the user has separately approved a migration. Do not promise SwiftUI production integration for them, and do not use an iOS-shaped SwiftUI mockup as proof of AppKit window, menu, command, focus, or multi-window behavior.

## Successful Result

Deliver:

- source and target platform scope;
- a shared-versus-platform-specific decision matrix;
- representative layouts, states, navigation, and input behavior for each target platform;
- preserved product DNA and explicitly changed interaction decisions;
- minimum-version and fallback implications;
- accessibility, localization, continuity, and reduced-motion behavior in scope;
- visible or native evidence matched to each claim;
- the strongest completion stage supported by that evidence;
- remaining platform risks and an exact acceptance path.

Do not redefine the whole product direction unless the adaptation reveals a material conflict and the user confirms that expansion.

## Boundaries

Route a new brand, new product, or broad visual-system exploration to `$apple-ui-direction`. Route formal critique of an existing adaptation to `$apple-ui-review`. Route Swift correctness, framework API work, architecture, state refactoring, debugging, performance, tests, CI, packaging, and release to an applicable engineering workflow. Keep platform experience decisions and acceptance criteria in this skill when the task is mixed.
