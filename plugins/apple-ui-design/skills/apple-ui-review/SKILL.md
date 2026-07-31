---
name: apple-ui-review
description: Review an existing iOS, iPadOS, or macOS design, screenshot, prototype, recording, or UI implementation. Use when the requested outcome is critique, audit, validation, acceptance review, or prioritized findings against product intent, platform behavior, accessibility, localization, craft, or runtime evidence. Do not use for a new direction, cross-platform adaptation, or implementation-only Swift, SwiftUI, UIKit, or AppKit work such as compilation, concurrency, architecture, state management, performance, API usage, CI, packaging, or release.
---

# Apple UI Review

Assess an existing artifact against its intended product outcome. Report evidence-backed findings and validation gaps without turning personal taste or Apple convention into product authority.

## Required Evidence

Before reviewing:

1. Inspect repository instructions, product intent, target users and tasks, platform scope, design system, screenshots, recordings, implementation, tests, and runtime evidence that are available.
2. Read `../../references/authority-and-principles.md`, `../../references/context-and-alignment.md`, and `../../references/engineering-routing.md`.
3. Read `../../references/delivery-contracts.md`, select the UI Review contract, and state its evidence gate.
4. Identify the exact artifact, screen, state, framework, platform, environment, and requested review depth.
5. Ask one focused question when a blocking, path-dependent uncertainty would materially change the findings. Request independent artifacts or factual evidence compactly, and follow the user’s preferred communication pace.

A user-provided screenshot or recording can support review of what it shows. Text description alone supports only unverified consultation. A build result does not prove usable interaction.

## Review Workflow

### 1. Establish the review contract

State:

- confirmed intended outcome and task;
- artifact and version reviewed;
- platforms, states, environments, and inputs represented;
- evidence available and missing;
- whether the result is a design review, implementation review, or experience-validation review.

Do not infer validated user needs or runtime behavior from appearance.

### 2. Review against shared evidence

Read `../../references/validation-and-review.md` and assess:

- product and task alignment;
- information hierarchy and interaction clarity;
- fit with user-defined platform behavior;
- product DNA and internal consistency;
- adaptivity, accessibility, and localization;
- craft and motion;
- runtime evidence and honest completion state.

Read `../../references/apple-platform-adaptation.md` when a finding depends on platform or input behavior. Read `../../references/design-system-and-dna.md` when consistency or brand expression is in scope. Read `../../references/accessibility-and-localization.md` for outcome-based accessibility and localization checks.

### 3. Classify only actionable findings

Use:

- **Blocking** for a failed core task, contradiction of confirmed intent, misleading destructive or data meaning, essential inaccessibility, or fundamental navigation, focus, or recovery failure.
- **Important** for material friction, inappropriate platform behavior, comprehension damage, significant inconsistency, or important adaptivity, localization, accessibility, motion, or state feedback failure.
- **Optimization** for non-blocking craft improvements.

Do not assign numeric scores by default. Do not inflate severity because a solution differs from reviewer taste.

Apple guidance, native components, shipped patterns, and reviewer preference are evidence or advice, not product authority. A confirmed unconventional interaction is not a finding merely because it is unconventional. Report a finding only when the supplied evidence shows a product, task, required-experience, or hard-boundary impact.

For each finding, provide:

```text
Title and severity
Observed fact:
User impact:
Evidence or affected scenario:
Recommendation:
How to verify:
```

Mark whether the recommendation is required by confirmed intent, supported by current Apple guidance, an optional optimization, or an exploration.

For a disputed recommendation, state the observed fact, user impact, recommendation, and verification path. If the product owner understands and accepts a non-hard-boundary risk, record the decision and remaining evidence gap without repeatedly escalating the same advice.

### 4. Verify claims at the right level

Use screenshots for static hierarchy, recordings for interaction and motion, accessibility inspection and audits for semantics, simulator or device runs for iOS and iPadOS, and a real Mac app for window, menu, command, and focus behavior. Do not report an audit, label check, or UI test as a VoiceOver, Voice Control, Switch Control, AssistiveTouch, Full Keyboard Access, or Pointer Control run. Name the exact technology, task, environment, and evidence behind every experience-verification claim.

Read `../../references/prototyping-and-implementation.md` when judging prototype or implementation evidence. Use `../../references/current-sources.md` and `../../references/research-and-source-evidence.md` when citing current Apple guidance or external examples. A version-sensitive finding must include the exact current Apple page and access date, separate published availability from the project’s tested runtime, and remain unverified when the source cannot be checked.

Do not claim native validation from HTML, interaction validation from a static image, or experience completion from compilation.

## Successful Result

Deliver:

- review scope and evidence status;
- findings ordered by severity and user impact;
- exact observed facts rather than generic “more Apple-like” advice;
- recommendations that preserve confirmed product ownership;
- validation methods for every actionable finding;
- unresolved risks and unrepresented scenarios;
- the strongest completion stage supported by the supplied evidence;
- a concise user acceptance path.

If there are no actionable findings, say so and name the evidence limits. Do not manufacture issues to fill a report.

## Boundaries

Route creation of a new product or visual direction to `$apple-ui-direction`. Route redesign for another Apple platform to `$apple-platform-adaptation`. Review UIKit and AppKit evidence directly without promising SwiftUI replacement. Route Swift correctness, framework API work, architecture, state management, performance, test infrastructure, CI, packaging, and release diagnosis to an applicable engineering workflow. A review may define the intended correction and verification path; it does not independently own production integration.
