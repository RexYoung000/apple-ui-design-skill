---
name: apple-platform-adaptation
description: Adapt an established iOS, iPadOS, or macOS product experience to another Apple platform or a multi-platform model. Use when the requested outcome is platform-specific hierarchy, navigation, windowing, density, input, continuity, or a shared-versus-specific adaptation decision. Do not use for zero-to-one direction, critique-only review, or implementation-only Swift, SwiftUI, UIKit, or AppKit work such as compilation, concurrency, architecture, state management, performance, API usage, CI, packaging, or release.
---

# Apple Platform Adaptation

Translate an established product model across Apple platforms, preserving identity while adapting task hierarchy, space, windows, inputs, and learned behavior.

## Required Inputs

1. Inspect source requirements, UI, states, components, strings, platform conditionals, deployment targets, and runtime evidence.
2. Derive user/task, source/target platforms, roles, feature scope, inputs, continuity, DNA, and confirmed interactions.
3. Read `../../references/delivery-contracts.md`; select Platform Adaptation and its evidence gate.
4. Read `../../references/apple-platform-adaptation.md`; load other references only under matching `Load When` conditions.
5. Ask only when an unresolved platform role or feature relationship blocks the next adaptation decision.

## Adaptation Workflow

### 1. Inspect the source

Treat shipped behavior as evidence, not automatic correctness. Without an established experience, route direction definition to `$apple-ui-direction`.

Use `../../references/context-and-alignment.md` for unresolved context and `../../references/authority-and-principles.md` for material product/platform conflicts.

### 2. Preserve shared meaning

Record shared outcomes, terminology, content, DNA, and states alongside platform-specific tasks, hierarchy, navigation, density, features, and continuity. Do not create an iPad or Mac experience by stretching the iPhone layout. Do not replace a distinctive product interaction merely because a system control exists.

Use `../../references/design-system-and-dna.md` to preserve DNA, inspect UI criteria, or translate informal terms. Candidate names do not establish platform equivalence or APIs.

Use `../../references/interaction-and-motion.md` for material behavior. Preserve the confirmed interaction contract and motion purposes; translate their expression rather than reopening the model.

Use `../../references/content-and-sensitive-flows.md` for consequential flows. Preserve verified meaning and user control across platform surfaces.

### 3. Map platform expressions

Map the confirmed operation to touch, Pencil, keyboard, pointer, focus, commands, windows, and relevant system events. Preserve state, feedback, interruption, reversal, recovery, and final intent.

Translate permission, Settings, authentication, account, commerce, and support paths only where present. Do not assume an iOS system sheet, StoreKit path, or account operation behaves identically across platforms; verify relevant current sources and native behavior through `../../references/current-sources.md`.

### 4. Check shared quality

Use `../../references/validation-and-review.md` for UI, UX, interaction, and motion criteria and scoped acceptance tasks. Use `../../references/accessibility-and-localization.md` for the core-task matrix for each target platform; keep design review, automation, and named assistive runs as separate evidence levels. Platform presentation may differ; confirmed outcomes and state meaning must survive.

### 5. Prototype and validate

Use `../../references/prototyping-and-implementation.md` for prototype/code decisions. Render each material window state; Exercise input and window behavior in native environments before claiming platform adaptation is verified. A browser mock or build cannot prove native experience.

Use `../../references/engineering-routing.md` for implementation ownership. UIKit/AppKit remain valid inputs; preserve architecture unless migration is approved, and involve engineering for production integration. Do not promise SwiftUI production integration.

## Successful Result

Provide source/target scope, shared-versus-specific decision matrix, representative layouts/states/inputs, preserved DNA and changes, claim-matched evidence, supported completion stage, remaining risks, and an exact acceptance path.

Route new product/brand exploration to `$apple-ui-direction`, formal critique to `$apple-ui-review`, and production correctness/integration to engineering. Keep experience decisions and acceptance criteria in mixed tasks; broaden product direction only after resolving a material conflict with the user.
