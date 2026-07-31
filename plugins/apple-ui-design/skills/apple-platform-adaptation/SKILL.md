---
name: apple-platform-adaptation
description: Adapt an established iOS, iPadOS, or macOS product experience to another Apple platform or a multi-platform model. Use when the requested outcome is platform-specific hierarchy, navigation, windowing, density, input, continuity, or a shared-versus-specific adaptation decision. Do not use for zero-to-one direction, critique-only review, or implementation-only Swift, SwiftUI, UIKit, or AppKit work such as compilation, concurrency, architecture, state management, performance, API usage, CI, packaging, or release.
---

# Apple Platform Adaptation

Translate an established product model across Apple platforms. Preserve what makes the product itself while redesigning the parts that should respond to platform role, available space, windowing, input, and learned behavior.

## Required Inputs

1. Inspect the source experience, requirements, UI, states, components, strings, platform conditionals, deployment targets, and runtime evidence.
2. Derive the target user and task, source and target platforms, platform roles, feature scope, windows, inputs, continuity, shared product DNA, and confirmed interaction decisions.
3. Read `../../references/delivery-contracts.md`, select Platform Adaptation, and state its artifact and evidence gate.
4. Read `../../references/apple-platform-adaptation.md` for the detailed translation method. Load other references only when their opening `Load When` condition matches.
5. Ask one focused question only when an unresolved platform role or feature relationship blocks and materially changes the adaptation.

## Adaptation Workflow

### 1. Inspect the source experience

Treat shipped behavior as evidence, not automatic correctness. If no established experience exists, route direction definition to `$apple-ui-direction` before continuing.

Read `../../references/context-and-alignment.md` only when the source product, user/task evidence, or platform relationship is materially unresolved. Read `../../references/authority-and-principles.md` only for a conflict involving confirmed product intent, a hard boundary, or platform convention.

### 2. Define what is shared and what changes

Record shared outcomes, content, terminology, brand, semantic states, platform-specific task priority, hierarchy, navigation, density, windows, inputs, feature differences, and continuity.

Do not create an iPad or Mac experience by stretching the iPhone layout. Do not replace a distinctive product interaction merely because a system control exists.

Read `../../references/design-system-and-dna.md` to preserve shared product DNA without redesigning it by default.
Read `../../references/interaction-and-motion.md` when behavior is material. Preserve the confirmed interaction contract and motion purposes, then translate their expression rather than reopening the product model by default.
Read `../../references/content-and-sensitive-flows.md` when the source experience includes material content, permission, privacy, identity, account-data, destructive, commerce, or regulated behavior. Preserve verified meaning and user control while translating the actual platform surface.

### 3. Map platform expressions

Map the confirmed operation to touch, Pencil, keyboard, pointer, focus, commands, windows, and system events that are relevant on each target platform. Preserve state meaning, feedback, interruption, reversal, recovery, and final intent even when the surface control or navigation expression changes.

Map app explanations, system permission handoffs, Settings recovery, authentication, account controls, purchase or subscription management, locale or storefront content, and external support surfaces only where they actually exist on the target platform. Do not assume an iOS system sheet, StoreKit path, or account operation behaves identically on iPadOS or macOS; verify current sources and native behavior.

Read `../../references/current-sources.md` only for material current Apple, version, API, policy, hardware, or platform-behavior claims.

### 4. Preserve accessibility, localization, and task meaning

Read `../../references/accessibility-and-localization.md` when accessibility, localization, input, assistive behavior, visual settings, content expansion, or reduced motion affects the outcome. Define a core-task matrix for each target platform and keep design review, automation, and named assistive-technology runs as separate evidence levels.

Platform-specific presentation may differ; the confirmed outcome and state meaning may not disappear.

### 5. Prototype and validate the differences

Read `../../references/prototyping-and-implementation.md` when producing or judging a prototype or design-led implementation. Read `../../references/validation-and-review.md` to plan evidence and acceptance.

Use visible layout evidence for each material size class or window state. Exercise input and window behavior in native environments before claiming platform adaptation is verified. Pair with an engineering skill when production implementation is requested.

Read `../../references/engineering-routing.md` when code, framework delivery, production integration, or ownership is in question. UIKit and AppKit remain valid inputs. Preserve their architecture unless migration is separately approved. Do not promise SwiftUI production integration or use an iOS-shaped mock as proof of Mac behavior.

## Successful Result

- source and target platform scope;
- a shared-versus-platform-specific decision matrix;
- representative layouts, states, navigation, and input behavior for each target platform;
- preserved product DNA and explicit changes;
- visible or native evidence matched to each claim;
- the strongest completion stage supported by that evidence;
- remaining platform risks and an exact acceptance path.

Do not redefine the whole product direction unless the adaptation reveals a material conflict and the user confirms that expansion.

Route a new brand, new product, or broad visual-system exploration to `$apple-ui-direction`. Route formal critique of an existing adaptation to `$apple-ui-review`. Route Swift correctness, framework API work, architecture, state refactoring, debugging, performance, tests, CI, packaging, and release to an applicable engineering workflow. Keep platform experience decisions and acceptance criteria in this skill when the task is mixed.
