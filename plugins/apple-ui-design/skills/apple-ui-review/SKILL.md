---
name: apple-ui-review
description: Review an existing iOS, iPadOS, or macOS design, screenshot, prototype, recording, or UI implementation. Use when the requested outcome is critique, audit, validation, acceptance review, or prioritized findings against product intent, platform behavior, accessibility, localization, craft, or runtime evidence. Do not use for a new direction, cross-platform adaptation, or implementation-only Swift, SwiftUI, UIKit, or AppKit work such as compilation, concurrency, architecture, state management, performance, API usage, CI, packaging, or release.
---

# Apple UI Review

Assess an existing artifact against its intended product outcome. Report evidence-backed findings and validation gaps without turning personal taste or Apple convention into product authority.

## Required Evidence

1. Inspect product intent, users and tasks, platform scope, design system, supplied artifacts, implementation, tests, and runtime evidence.
2. Identify the exact artifact, version, screen, state, framework, platform, environment, and requested review depth.
3. Read `../../references/delivery-contracts.md`, select UI Review, and state its artifact and evidence gate.
4. Read `../../references/validation-and-review.md` for the review and finding method. Load other references only when their opening `Load When` condition matches.
5. Ask one focused question only when a blocking, path-dependent uncertainty materially changes the findings.

A screenshot or recording supports only what it shows. Text alone supports unverified consultation. A build does not prove usable interaction.

## Review Workflow

### 1. Establish the review contract

State the intended outcome, reviewed artifact and version, represented platforms and states, available and missing evidence, and whether this is design review, implementation review, or experience-validation review.

Do not infer validated user needs or runtime behavior from appearance.

### 2. Review against shared evidence

Read `../../references/context-and-alignment.md` only when product intent, user/task evidence, or scope is unresolved. Read `../../references/authority-and-principles.md` only when intent, a hard boundary, Apple convention, or reviewer preference conflicts.

Read `../../references/apple-platform-adaptation.md` for platform behavior, `../../references/design-system-and-dna.md` for consistency or brand, and `../../references/accessibility-and-localization.md` for material accessibility or localization claims.
Read `../../references/interaction-and-motion.md` for material behavior and `../../references/content-and-sensitive-flows.md` for consequential content, consent, access, account data, destructive action, commerce, or professional meaning.

### 3. Classify only actionable findings

Use **Blocking**, **Important**, and **Optimization** as defined in `../../references/validation-and-review.md`. Do not assign numeric scores by default or inflate severity because a solution differs from reviewer taste.

Apple guidance, shipped patterns, and reviewer preference are evidence, not product authority. A confirmed unconventional interaction is not a finding merely because it is unconventional.

For experimental interactions, report learning, equivalent-input, limit, error, and recovery risk without replacing the model merely because it is nonstandard.

Treat a misleading permission, purchase, deletion, privacy, or professional claim as blocking when it distorts consent, cost, data, safety, or recovery. Do not call it legally compliant, medically correct, financially suitable, secure, or App Review ready from design evidence.

For each finding use the shared fact, impact, evidence, recommendation, and verification format. If the product owner accepts a non-hard-boundary risk, record the decision and remaining evidence gap without repeatedly escalating it.

### 4. Verify claims at the right level

Apply the evidence levels in `../../references/validation-and-review.md`. Do not report an audit, label check, or UI test as a VoiceOver or other assistive-technology run. Name the exact technology, task, environment, and evidence.

For material motion, inspect representative-speed native recordings and Reduce Motion. Leave rhythm and aesthetic acceptance to the user; do not infer them from timing values or build success.

For sensitive flows, match hierarchy, app, native, service, commerce, and professional claims to their corresponding evidence. Never promote a mock into a system, service, policy, or professional result.

Read `../../references/prototyping-and-implementation.md` for prototype evidence, `../../references/current-sources.md` for current Apple claims, `../../references/research-and-source-evidence.md` for external evidence, and `../../references/engineering-routing.md` when a correction crosses into implementation ownership.

Do not claim native validation from HTML, interaction validation from a static image, or experience completion from compilation.

## Successful Result

- review scope and evidence status;
- findings ordered by severity and user impact;
- exact facts, impacts, recommendations, and verification paths;
- validation methods for every actionable finding;
- unresolved risks and unrepresented scenarios;
- the strongest completion stage supported by the supplied evidence;
- a concise user acceptance path.

If there are no actionable findings, say so and name the evidence limits. Do not manufacture issues to fill a report.

Route new direction to `$apple-ui-direction`, cross-platform redesign to `$apple-platform-adaptation`, and production correctness or integration to an applicable engineering workflow. A review may define the correction and verification path; it does not own integration.
