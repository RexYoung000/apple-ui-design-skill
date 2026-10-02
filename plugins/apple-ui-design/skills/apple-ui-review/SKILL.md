---
name: apple-ui-review
description: Review an existing iOS, iPadOS, or macOS design, screenshot, prototype, recording, or UI implementation. Use when the requested outcome is critique, audit, validation, acceptance review, or prioritized findings against product intent, platform behavior, accessibility, localization, craft, or runtime evidence. Do not use for a new direction, cross-platform adaptation, or implementation-only Swift, SwiftUI, UIKit, or AppKit work such as compilation, concurrency, architecture, state management, performance, API usage, CI, packaging, or release.
---

# Apple UI Review

Assess an existing artifact against its product outcome; report evidence-backed findings without promoting personal taste or convention into authority.

## Required Evidence

1. Inspect intent, users/tasks, platforms, design system, artifacts, implementation, tests, and runtime evidence.
2. Identify artifact/version, screen/state, framework, environment, and review depth.
3. Read `../../references/delivery-contracts.md`; select UI Review and its evidence gate.
4. Read `../../references/validation-and-review.md` for overlapping UI, UX, interaction, and motion lenses, scoped checks, severity, and finding format.
5. Load other references only under matching `Load When` conditions. Ask only about uncertainty that blocks and materially changes findings.

Screenshots/recordings support shown states only; text supports unverified consultation. A build does not prove usable interaction.

## Review Workflow

### 1. Establish the contract

State outcome, artifact/version, represented states/platforms, available/missing evidence, and whether reviewing design, implementation, or verified experience. Appearance cannot establish validated user needs or runtime behavior.

### 2. Apply relevant method owners

Use `../../references/context-and-alignment.md` for unresolved context and `../../references/authority-and-principles.md` for material authority conflicts.

Use `../../references/design-system-and-dna.md` for observable UI criteria, consistency, or candidate terminology; `../../references/apple-platform-adaptation.md` for platform fit; `../../references/accessibility-and-localization.md` for relevant shared checks.

Use `../../references/interaction-and-motion.md` for behavior and `../../references/content-and-sensitive-flows.md` for consequential meaning. Candidate terminology is an interpretation to check, not evidence of a platform/API choice. A small static review needs neither full discovery nor every method.

### 3. Report actionable findings

Apply the shared severity and finding method. Do not assign numeric scores by default or use taste-based severity. A confirmed unconventional interaction is not a finding merely because it is unconventional.

For experimental interactions, report learning, equivalent-input, limit, error, and recovery risk without replacing the model merely because it is nonstandard.

Misleading consent, cost, data, safety, or recovery can be blocking. Design evidence cannot establish legal compliance, medical correctness, financially suitable advice, security, or App Review readiness.

If the owner accepts an informed non-hard-boundary risk, record the decision and remaining gap rather than repeatedly escalating it.

### 4. Verify claims

Match claims to the shared evidence levels. Do not report an audit, label check, or UI test as a VoiceOver or other assistive run. Name the exact technology, task, environment, and evidence.

Inspect representative-speed native recordings and Reduce Motion for material motion. Leave rhythm and aesthetic acceptance to the user; do not infer them from timing values or build success.

Never promote a mock into a system, service, policy, or professional result. Do not claim native validation from HTML; static images cannot prove interaction.

Use `../../references/prototyping-and-implementation.md` for prototype evidence, `../../references/current-sources.md` for current Apple claims, `../../references/research-and-source-evidence.md` for external evidence, and `../../references/engineering-routing.md` for implementation ownership.

## Successful Result

Provide scope/evidence status, findings ordered by impact/severity with facts and verification paths, remaining risks/unrepresented scenarios, supported completion stage, and a concise acceptance path. If there are no actionable findings, say so; do not invent issues.

Route new direction to `$apple-ui-direction`, adaptation to `$apple-platform-adaptation`, and production correctness/integration to engineering. Review owns correction and verification guidance, not integration.
