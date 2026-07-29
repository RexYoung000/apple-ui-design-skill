---
name: apple-platform-adaptation
description: Adapt an established product experience between iOS, iPadOS, and macOS while preserving shared product DNA and defining platform-specific hierarchy, navigation, windowing, density, and input behavior. Use when an existing screen, flow, or product must work on another supported Apple platform or across multiple Apple platforms. Do not use for a zero-to-one visual direction, critique-only review, or general SwiftUI engineering.
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

If platform roles or feature relationships are unresolved and would change the information architecture, ask one highest-impact question. Never impose primary, peer, or companion labels.

Read `../../references/authority-and-principles.md`, `../../references/context-and-alignment.md`, `../../references/delivery-contracts.md`, and `../../references/apple-platform-adaptation.md` before defining the adaptation. Select the Platform Adaptation contract and state its artifact and evidence gate.

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

Read `../../references/design-system-and-dna.md` to preserve shared product DNA without redesigning it by default.

### 3. Map platform expressions

Define representative layouts and behaviors for:

- iOS touch, safe areas, navigation, sheets, keyboard, and interruption;
- iPadOS compact and expansive windows, columns, sidebars, inspectors, pointer, keyboard, drag and drop, and reflow;
- macOS window sizes, menus, commands, shortcuts, pointer, hover, focus, selection, context menus, and multiple-window behavior.

Read `../../references/current-sources.md` and use current official Apple sources for version-sensitive platform claims. Use platform convention as evidence, not as automatic ownership of visual style.

### 4. Preserve accessibility, localization, and task meaning

Read `../../references/accessibility-and-localization.md`. Define equivalent completion paths for relevant touch, keyboard, pointer, VoiceOver, focus, content expansion, locale, and reduced-motion scenarios.

Platform-specific presentation may differ; the confirmed outcome and state meaning may not disappear.

### 5. Prototype and validate the differences

Read `../../references/prototyping-and-implementation.md` and `../../references/validation-and-review.md`.

Use visible layout evidence for each material size class or window state. Exercise input and window behavior in native environments before claiming platform adaptation is verified. Pair with an engineering skill when production implementation is requested.

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

Route a new brand, new product, or broad visual-system exploration to `$apple-ui-direction`. Route formal critique of an existing adaptation to `$apple-ui-review`. Route Swift architecture, state refactoring, debugging, performance, CI, packaging, and release work to an applicable engineering workflow.
