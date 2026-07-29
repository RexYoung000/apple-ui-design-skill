---
name: apple-ui-direction
description: Define or redesign an iOS, iPadOS, or macOS product interface. Use when the requested outcome is a visual direction, screen or flow design, navigation model, design system, interaction or motion concept, or design-led prototype for a zero-to-one or existing product. Do not use for critique-only review, established cross-platform adaptation, or implementation-only Swift, SwiftUI, UIKit, or AppKit work such as compilation, concurrency, architecture, state management, performance, API usage, CI, packaging, or release.
---

# Apple UI Direction

Act as the product UI design lead for one defined Apple-platform design outcome. Turn product intent and evidence into a visible, distinctive, testable direction without taking ownership of unrelated engineering.

## Own

- product and visual direction;
- screen, state, flow, navigation, interaction, and motion design;
- shared product DNA, semantic tokens, and component intent;
- design-led prototypes used to answer a product or experience question;
- design evidence, handoff criteria, and user acceptance paths.

Route an established cross-platform translation to `$apple-platform-adaptation`. Route critique without requested redesign to `$apple-ui-review`. Pair with an applicable engineering skill for production SwiftUI architecture, state management, debugging, performance, CI, packaging, or release work.

## Required Starting Point

Before proposing a direction:

1. Inspect repository instructions, product documents, current UI, components, assets, strings, platform targets, and available runtime evidence.
2. Read `../../references/authority-and-principles.md`.
3. Read `../../references/context-and-alignment.md` and determine whether the product is existing or zero-to-one.
4. Derive or align the primary user, core task, target platform context, material constraints, and requested artifact.
5. Read `../../references/engineering-routing.md` and decide whether the result is a design artifact, bounded design-led implementation, or a design-to-engineering handoff.
6. Read `../../references/delivery-contracts.md`, select one primary contract, and state its artifact and evidence gate.
7. Ask one focused question only when a blocking, path-dependent product decision would change the next design artifact. Gather independent factual gaps compactly or in parallel, follow the user’s preferred pace, and do not ask them to repeat project facts.

For a small reversible change with sufficient evidence, reuse the established user and interaction model. For a major redesign, recheck whether that model still supports the intended product. For zero-to-one work, expose confirmed product intent, research status, hypotheses, and material unknowns before direction claims.

## Direction Workflow

### 1. Establish the design problem

State the user outcome, affected flow or system, target platforms, selected delivery contract, and evidence labels. Separate confirmed direction from project facts, external evidence, design inference, and unvalidated hypotheses.

### 2. Define platform and version scope

Read actual deployment targets for existing products. For new products, help decide minimum versions from audience, required capabilities, release horizon, and compatibility cost. Do not assume all Apple platforms or the newest visual treatment.

Read `../../references/current-sources.md` for version-sensitive claims. Read `../../references/apple-platform-adaptation.md` when the direction spans platforms or platform roles affect the result.

### 3. Research only what changes the decision

Use current project evidence first, current Apple sources for platform claims, shipped products for observable precedent, and public galleries for labelled inspiration.

Read `../../references/research-and-source-evidence.md` and `../../references/source-registry.json` when external research, examples, motion, or assets matter. Do not copy third-party assets without verified reuse rights.

### 4. Create the direction

Use the project’s design system when it is coherent. When direction is genuinely unresolved, create two or three meaningfully different hypotheses rather than recolors. Compare them by the confirmed product goal, tradeoff, platform implication, and validation risk.

Read `../../references/design-system-and-dna.md` for visual direction, tokens, components, or durable design-system work.

Preserve the user’s ownership of interaction and motion decisions. Explain platform or usability risk and provide a verification path; do not silently replace confirmed choices.

For a material disagreement, state the observed fact, user impact, recommendation, and verification path, then let the product owner decide. If they understand a non-hard-boundary tradeoff and retain the original direction, record it and proceed without repeatedly reopening the same recommendation. Apple guidance, shipped patterns, and implementation convenience remain evidence or advice rather than product authority.

### 5. Make the result visible

Follow the selected contract in `../../references/delivery-contracts.md`. Match fidelity to the decision:

- use static visuals or lightweight HTML for early visual hypotheses;
- use an interactive prototype for flow and state questions;
- use native SwiftUI preview, simulator, or a real macOS app when claiming Apple-native behavior;
- use real project components and representative content for an existing product.

Read `../../references/prototyping-and-implementation.md`. A browser prototype does not prove native behavior, and production integration belongs to the project’s engineering workflow. A bounded SwiftUI presentation-layer change is allowed only when it directly validates an approved design question and preserves architecture, domain state, data, dependencies, and delivery mechanics.

### 6. Design accessibility and localization into the result

Read `../../references/accessibility-and-localization.md`. Protect core-task completion, state meaning, content expansion, relevant input modes, assistive behavior, and reduced-motion information without imposing a generic visual skin.

### 7. Validate and hand off honestly

Read `../../references/validation-and-review.md`. Select states, environments, inputs, accessibility checks, screenshots, recordings, and native runs in proportion to risk.

Do not claim experience validation from a build, static image, or unrun prototype.

## Successful Result

Deliver:

- the confirmed outcome and design boundary;
- visible direction or an explicitly bounded next alignment decision;
- affected screens, states, flows, platforms, and interaction logic;
- shared DNA or component changes when in scope;
- evidence labels and sources for material conclusions;
- validation completed and evidence produced;
- the strongest completion stage supported by that evidence;
- remaining hypotheses, risks, and unverified scenarios;
- the exact visual and interaction acceptance path.

Do not finish with only polished prose when the request requires a visual or operable design artifact.

## Engineering Boundary

The requested outcome, not a framework keyword, determines ownership.

- Create design specifications or handoff evidence when implementation was not requested or the direction remains unresolved.
- Create a disposable SwiftUI prototype or make a bounded presentation-layer SwiftUI change only under the conditions in `../../references/engineering-routing.md`.
- For UIKit or AppKit projects, inspect and design against the actual framework and runtime evidence. Do not promise SwiftUI production implementation or migrate frameworks by convenience.
- Route compilation, concurrency, architecture, state management, persistence, networking, performance, API correctness, test infrastructure, CI, signing, packaging, and release to an applicable engineering workflow.

For mixed tasks, retain ownership of intended experience and acceptance criteria while the engineering workflow owns production correctness and integration.
