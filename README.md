<div align="center">

# Apple UI Design

**A product-first design skill for native, distinctive, and verifiable interfaces across iOS, iPadOS, and macOS.**

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

## Overview

Apple UI Design is an agent skill for designing, adapting, implementing, and reviewing product interfaces across the Apple ecosystem.

It starts from product intent and project evidence, then combines shared product DNA with platform-appropriate interaction. Apple conventions guide the experience without forcing every product into the same visual template.

## What It Covers

- Product and visual direction for Apple-platform experiences
- Screen, state, flow, and navigation design
- Shared design systems and platform-specific expression
- Cross-platform adaptation for iOS, iPadOS, and macOS
- SwiftUI-oriented native prototypes and interface implementation
- Accessibility, localization, motion, and adaptive-layout decisions
- Evidence-based design and implementation reviews

## Core Principles

1. **Product intent comes first.** Confirmed user needs determine what the interface must accomplish.
2. **Project context is the local source of truth.** Existing requirements, design systems, components, assets, and platform targets are inspected before new decisions are made.
3. **Native does not mean generic.** Apple conventions guide interaction, while brand and product DNA preserve a distinctive identity.
4. **Platforms are adapted, not enlarged.** iPhone, iPad, and Mac experiences may share a product while differing in hierarchy, density, navigation, and input.
5. **Accessibility and localization are designed in.** They are part of the interface definition, not a final checklist.
6. **Visual quality requires evidence.** Compilation alone is not experience validation; important states and real interactions should be rendered and tested.

## Operating Modes

The skill selects the appropriate depth for the request:

- **Direction** — establish or explore a visual and interaction direction
- **Screen or flow design** — design a page, state set, or end-to-end task
- **Design system** — define or extend shared DNA, semantic tokens, and components
- **Cross-platform adaptation** — translate an existing experience to another Apple platform
- **Native prototype or implementation** — create SwiftUI prototypes or production UI when requested
- **Review and iteration** — assess an existing design or implementation against confirmed intent

## Installation

Clone this repository into your personal Codex skills directory:

```bash
git clone https://github.com/RexYoung000/apple-ui-design-skill.git ~/.codex/skills/apple-ui-design
```

If you already have a local copy, update it with:

```bash
git -C ~/.codex/skills/apple-ui-design pull --ff-only
```

## Usage

Invoke the skill explicitly:

```text
Use $apple-ui-design to design the onboarding flow for this iPad app.
```

Or describe an Apple UI task naturally:

```text
Review this macOS interface for hierarchy, keyboard use, accessibility,
and consistency with the product's existing design system.
```

The skill will inspect available project evidence before asking questions. When a decision materially affects the product, it asks one focused question at a time and explains the recommended direction.

## Repository Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── accessibility-and-localization.md
    ├── apple-platform-adaptation.md
    ├── authority-and-principles.md
    ├── context-and-alignment.md
    ├── design-system-and-dna.md
    ├── maintenance-and-sources.md
    ├── prototyping-and-implementation.md
    └── validation-and-review.md
```

- `SKILL.md` defines the role, scope, workflow, review method, and routing rules.
- `agents/openai.yaml` provides the display metadata and default invocation prompt.
- `references/` contains focused guidance loaded only when relevant to the current task.

## Scope

This skill owns product intent, visual hierarchy, Apple-platform behavior, design-system decisions, and experience-validation criteria.

It does not replace specialized engineering workflows for Swift architecture, concurrency, performance profiling, CI, packaging, or release operations. When those are the primary task, use the appropriate engineering workflow alongside this skill.

## Maintenance

Stable design principles live in the skill. Version-specific Apple APIs, platform behavior, and Human Interface Guidelines should be verified against current official Apple sources when they affect a decision.

See [`references/maintenance-and-sources.md`](references/maintenance-and-sources.md) for the maintenance policy and regression prompts.

## License

This project is available under the [MIT License](LICENSE).
