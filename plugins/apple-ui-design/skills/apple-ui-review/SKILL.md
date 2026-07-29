---
name: apple-ui-review
description: Review an existing iOS, iPadOS, or macOS design, prototype, or UI implementation against confirmed product intent, platform behavior, accessibility, localization, craft, and runtime evidence. Use for critique, audit, validation, acceptance review, or prioritizing UI findings. Do not use when the primary request is to create a new direction, perform cross-platform adaptation, or debug general Swift code.
---

# Apple UI Review

Assess an existing artifact against its intended product outcome. Report evidence-backed findings and validation gaps without turning personal taste or Apple convention into product authority.

## Required Evidence

Before reviewing:

1. Inspect repository instructions, product intent, target users and tasks, platform scope, design system, screenshots, recordings, implementation, tests, and runtime evidence that are available.
2. Read `../../references/authority-and-principles.md` and `../../references/context-and-alignment.md`.
3. Identify the exact artifact, screen, state, platform, environment, and requested review depth.
4. Ask only for missing evidence that would materially change the findings.

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

### 4. Verify claims at the right level

Use screenshots for static hierarchy, recordings for interaction and motion, accessibility inspection for semantics, simulator or device runs for iOS and iPadOS, and a real Mac app for window, menu, command, and focus behavior.

Read `../../references/prototyping-and-implementation.md` when judging prototype or implementation evidence. Use `../../references/current-sources.md` and `../../references/research-and-source-evidence.md` when citing current Apple guidance or external examples.

Do not claim native validation from HTML, interaction validation from a static image, or experience completion from compilation.

## Successful Result

Deliver:

- review scope and evidence status;
- findings ordered by severity and user impact;
- exact observed facts rather than generic “more Apple-like” advice;
- recommendations that preserve confirmed product ownership;
- validation methods for every actionable finding;
- unresolved risks and unrepresented scenarios;
- a concise user acceptance path.

If there are no actionable findings, say so and name the evidence limits. Do not manufacture issues to fill a report.

## Boundaries

Route creation of a new product or visual direction to `$apple-ui-direction`. Route redesign for another Apple platform to `$apple-platform-adaptation`. Route Swift correctness, architecture, performance, CI, packaging, and release diagnosis to an applicable engineering workflow.
