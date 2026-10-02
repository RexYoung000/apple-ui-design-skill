---
name: apple-ui-direction
description: Define or redesign an iOS, iPadOS, or macOS product interface. Use when the requested outcome is a visual direction, screen or flow design, navigation model, design system, interaction or motion concept, or design-led prototype for a zero-to-one or existing product. Do not use for critique-only review, established cross-platform adaptation, or implementation-only Swift, SwiftUI, UIKit, or AppKit work such as compilation, concurrency, architecture, state management, performance, API usage, CI, packaging, or release.
---

# Apple UI Direction

Lead a defined product-interface outcome with visible, testable evidence. UI, UX, interaction, and motion are overlapping quality lenses within this workflow, not additional workflows.

## Required Starting Point

1. Inspect instructions, product/design documents, UI, components, assets, strings, platform targets, and runtime evidence.
2. Derive user, core task, existing-versus-zero-to-one starting point, constraints, and requested artifact.
3. Read `../../references/delivery-contracts.md`; select one primary contract and its evidence gate.
4. Load references only when their `Load When` condition matches. Small static changes need neither every reference nor complete exploration.
5. Ask only about a blocking, path-dependent decision. Gather independent factual gaps compactly or in parallel, follow the user’s preferred pace; inspect available facts first.

## Direction Workflow

### 1. Align the decision

Use `../../references/context-and-alignment.md` for unresolved product context or evidence. Reuse established facts for small reversible changes.

For material authority conflicts, use `../../references/authority-and-principles.md`. Explain fact, impact, recommendation, and verification; after an informed non-hard-boundary choice, record it and proceed without repeatedly reopening the same recommendation.

### 2. Bound platform and implementation scope

Inspect deployment targets. Use `../../references/current-sources.md` for current Apple or API claims, `../../references/apple-platform-adaptation.md` for platform roles, and `../../references/engineering-routing.md` for code or ownership questions. Bound design-led code before implementation.

### 3. Create what resolves the design question

Use `../../references/design-system-and-dna.md` for visual direction, observable UI criteria, components, shared DNA, or candidate terminology. Preserve the user's language; a component term does not establish an Apple API.

Use project evidence first. Load `../../references/research-and-source-evidence.md`, then `../../references/source-registry.json`, only when external evidence can change a decision.

For unresolved direction, create two or three operable hypotheses with real differences in hierarchy, operation, feedback, or product emphasis. Do not present recolors, duration-only changes, or easing changes as separate directions. Extend confirmed choices without manufacturing alternatives.

For material behavior, use `../../references/interaction-and-motion.md`. Define the relevant interaction contract and motion language, including the intentional Reduce Motion expression and native evidence.

For consequential content, use `../../references/content-and-sensitive-flows.md`. Define the sensitive-flow contract; route missing professional or commercial facts to their owner.

### 4. Produce and validate

Follow the selected contract. Use `../../references/prototyping-and-implementation.md` for prototype/code decisions. A browser prototype does not prove native behavior. Keep mocked system, account, data, and purchase behavior explicit.

Use `../../references/validation-and-review.md` for the quality-lens map and scoped acceptance task; `../../references/accessibility-and-localization.md` owns relevant cross-cutting checks. A build, screenshot, HTML, or unrun prototype cannot establish native experience. Do not finish with only polished prose when the contract requires a visible or operable artifact.

## Successful Result

Provide outcome/scope, artifact, affected screens/states/platforms, supported completion stage, risks and unverified hypotheses, and an exact acceptance path.

Route established adaptation to `$apple-platform-adaptation`, critique to `$apple-ui-review`, and production correctness/integration to engineering. Retain intended experience and acceptance criteria in mixed tasks.
