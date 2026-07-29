---
name: apple-ui-direction
description: Define or redesign Apple product UI direction for iOS, iPadOS, or macOS. Use for zero-to-one or existing products when the requested outcome is a visual direction, screen or flow, navigation model, design system, interaction or motion concept, or design-led native prototype. Do not use for cross-platform adaptation of an established experience, critique-only review, or general Swift and SwiftUI engineering.
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
5. Ask only the highest-impact unresolved question. Do not ask the user to repeat project facts.

For a small reversible change with sufficient evidence, reuse the established user and interaction model. For a major redesign, recheck whether that model still supports the intended product. For zero-to-one work, expose confirmed product intent, research status, hypotheses, and material unknowns before direction claims.

## Direction Workflow

### 1. Establish the design problem

State the user outcome, affected flow or system, target platforms, and evidence labels. Separate confirmed direction from project facts, external evidence, design inference, and unvalidated hypotheses.

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

### 5. Make the result visible

Match fidelity to the decision:

- use static visuals or lightweight HTML for early visual hypotheses;
- use an interactive prototype for flow and state questions;
- use native SwiftUI preview, simulator, or a real macOS app when claiming Apple-native behavior;
- use real project components and representative content for an existing product.

Read `../../references/prototyping-and-implementation.md`. A browser prototype does not prove native behavior, and production integration belongs to the project’s engineering workflow.

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
- remaining hypotheses, risks, and unverified scenarios;
- the exact visual and interaction acceptance path.

Do not finish with only polished prose when the request requires a visual or operable design artifact.
