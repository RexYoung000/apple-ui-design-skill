---
name: apple-ui-direction
description: Define or redesign an iOS, iPadOS, or macOS product interface. Use when the requested outcome is a visual direction, screen or flow design, navigation model, design system, interaction or motion concept, or design-led prototype for a zero-to-one or existing product. Do not use for critique-only review, established cross-platform adaptation, or implementation-only Swift, SwiftUI, UIKit, or AppKit work such as compilation, concurrency, architecture, state management, performance, API usage, CI, packaging, or release.
---

# Apple UI Direction

Lead one defined Apple-platform product UI outcome: direction, screen or flow, navigation, design system, interaction, motion, or a design-led prototype. Produce visible, testable design evidence without taking ownership of unrelated engineering.

## Required Starting Point

1. Inspect project instructions, product documents, UI, components, assets, strings, platform targets, and runtime evidence.
2. Derive the primary user, core task, platform scope, material constraints, existing-versus-zero-to-one starting point, and requested artifact.
3. Read `../../references/delivery-contracts.md`, select one primary contract, and state its artifact and evidence gate.
4. Load other shared references only when their opening `Load When` condition matches the task.
5. Ask one focused question only when a blocking, path-dependent product decision changes the next artifact. Gather independent factual gaps compactly or in parallel, follow the user’s preferred pace, and do not ask for project facts that can be inspected.

## Direction Workflow

### 1. Align the decision

Read `../../references/context-and-alignment.md` for zero-to-one work, major redesigns, ambiguous evidence, or unresolved path-dependent decisions. Reuse established facts for a small reversible change.

Read `../../references/authority-and-principles.md` only when sources, product ownership, a hard boundary, or platform convention materially conflict. Explain the fact, impact, recommendation, and verification path. After the product owner accepts a non-hard-boundary tradeoff, record it and proceed without repeatedly reopening the same recommendation.

### 2. Bound platform and implementation scope

Read configured deployment targets for existing products. Read `../../references/current-sources.md` only for material current Apple, API, OS, policy, hardware, or design-language claims. Read `../../references/apple-platform-adaptation.md` when multiple platforms or platform roles affect the direction.

Read `../../references/engineering-routing.md` when code, framework delivery, production integration, or implementation ownership is in question. Decide whether the result stops at design evidence, includes bounded design-led code, or needs engineering partnership.

### 3. Research and create only what changes the decision

Use project evidence first. Read `../../references/research-and-source-evidence.md` and then `../../references/source-registry.json` only when external research, examples, inspiration, or assets can change the result.

Read `../../references/design-system-and-dna.md` for visual direction, tokens, components, or durable product DNA. When direction is unresolved, create two or three operable hypotheses with real differences in hierarchy, operation, feedback, or product emphasis. Do not present recolors, duration-only changes, or easing changes as separate directions.

Read `../../references/interaction-and-motion.md` when behavior is material. Define the relevant interaction contract and motion language, including the intentional Reduce Motion expression and required native evidence.

Read `../../references/content-and-sensitive-flows.md` when content changes meaning, consent, protected access, identity, account data, destructive action, commerce, recovery, or a professional claim. Define the sensitive-flow contract and route missing facts to their responsible owner.

### 4. Produce and validate the artifact

Follow the selected contract. Read `../../references/prototyping-and-implementation.md` when choosing a prototype medium, creating design-led code, or handing off implementation. A browser prototype does not prove native behavior. Keep mocked system, account, data, and purchase behavior explicit.

Read `../../references/accessibility-and-localization.md` when accessibility, localization, input alternatives, assistive behavior, visual settings, or content expansion affect the outcome or claim. Read `../../references/validation-and-review.md` to select evidence and acceptance checks in proportion to risk.

Do not claim experience validation from a build, static image, or unrun prototype. Do not finish with only polished prose when the contract requires a visible or operable artifact.

## Successful Result

- the confirmed outcome and design boundary;
- the visible or operable artifact required by the selected contract;
- affected screens, states, platforms, behavior, and shared DNA in scope;
- the strongest completion stage supported by that evidence;
- remaining hypotheses, risks, and unverified scenarios;
- the exact visual and interaction acceptance path.

Route established cross-platform translation to `$apple-platform-adaptation`, critique-only work to `$apple-ui-review`, and production correctness or integration to an applicable engineering workflow. In mixed tasks, retain ownership of intended experience and acceptance criteria.
