<div align="center">

# Apple UI Design

**A product-first design skill for native, distinctive, and verifiable interfaces across iOS, iPadOS, and macOS.**

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

## Overview

Apple UI Design is an agent skill for designing, adapting, implementing, and reviewing product interfaces across the Apple ecosystem.

It starts from product intent and project evidence, then combines shared product DNA with platform-appropriate interaction. Apple conventions guide the experience without forcing every product into the same visual template.

It supports both existing products and zero-to-one ideas. Existing products are read from their current evidence; new products use explicit hypotheses and public research without pretending that untested assumptions are validated user needs.

## What It Covers

- Product and visual direction for Apple-platform experiences
- Screen, state, flow, and navigation design
- Shared design systems and platform-specific expression
- Cross-platform adaptation for iOS, iPadOS, and macOS
- SwiftUI-oriented native prototypes and interface implementation
- Accessibility, localization, motion, and adaptive-layout decisions
- Evidence-based design and implementation reviews

## Core Principles

1. **Product intent comes first.** Confirmed decisions define the intended experience, while evidence labels keep known user needs separate from hypotheses.
2. **Project context is the local source of truth.** Existing requirements, design systems, components, assets, and platform targets are inspected before new decisions are made.
3. **The user owns product direction.** The skill explains platform, usability, and accessibility implications without silently replacing confirmed interaction or motion decisions.
4. **Native does not mean generic.** Native validation checks behavior and semantics, not resemblance to Apple system apps. Custom visuals and controls remain valid.
5. **Platforms are adapted, not enlarged.** iPhone, iPad, and Mac experiences may share a product while differing in hierarchy, density, navigation, and input.
6. **Accessibility and localization protect outcomes, not a default skin.** They are designed and validated without erasing brand expression.
7. **Visual and motion quality require evidence.** Compilation alone is not experience validation; important states and real interactions should be rendered and tested.

## Operating Modes

The skill selects the appropriate depth for the request:

- **Direction** — establish or explore a visual and interaction direction
- **Screen or flow design** — design a page, state set, or end-to-end task
- **Design system** — define or extend shared DNA, semantic tokens, and components
- **Cross-platform adaptation** — translate an existing experience to another Apple platform
- **Native prototype or implementation** — create SwiftUI prototypes or production UI when requested
- **Review and iteration** — assess an existing design or implementation against confirmed intent

## Install as a Standalone Skill

For personal local use, clone this repository into the current user-level skills directory:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/RexYoung000/apple-ui-design-skill.git "$HOME/.agents/skills/apple-ui-design"
```

Codex detects skill changes automatically. If the skill does not appear, restart Codex or the ChatGPT desktop app.

To update an existing installation:

```bash
git -C "$HOME/.agents/skills/apple-ui-design" pull --ff-only
```

To remove the skill without permanently deleting the checkout, move it outside the scanned `skills` directory:

```bash
mkdir -p "$HOME/.agents/skill-backups"
mv "$HOME/.agents/skills/apple-ui-design" "$HOME/.agents/skill-backups/apple-ui-design"
```

Choose a different backup name if that destination already exists.

For a repository-scoped team workflow, place the skill at `.agents/skills/apple-ui-design` inside the repository instead. Codex scans `.agents/skills` from the current working directory up to the repository root.

This standalone installation is intended for local use and source development. OpenAI recommends packaging reusable public distribution as a plugin. Plugin packaging and migration for this project are tracked in [Issue #2](https://github.com/RexYoung000/apple-ui-design-skill/issues/2); this README does not claim that the current repository is already an installable plugin.

See the current OpenAI documentation for [building skills](https://learn.chatgpt.com/docs/build-skills) and [packaging plugins](https://developers.openai.com/plugins/build/plugins).

## Use in Codex

Invoke the skill explicitly with `$`:

```text
Use $apple-ui-design to design the onboarding flow for this iPad app.
```

Codex may also select it when a request matches the skill description:

```text
Review this macOS interface for hierarchy, keyboard use, accessibility,
and consistency with the product's existing design system.
```

## Use in the ChatGPT Desktop App

Open **Skills** in the sidebar to confirm that Apple UI Design is available. In a chat, type `@`, select **Apple UI Design**, and then describe the task:

```text
Use Apple UI Design to adapt this existing iPhone flow for iPad and Mac.
```

Standalone skills are supported in the ChatGPT desktop app, Codex CLI, and the Codex IDE extension. Plugin installation through the shared Plugins Directory will be documented after Issue #2 is complete.

The skill will inspect available project evidence before asking questions. When a decision materially affects the product, it asks one focused question at a time and explains the recommended direction.

For an existing product, it derives the user, core task, design DNA, and interaction model from current evidence. For a zero-to-one product, it separates user-confirmed decisions, external evidence, design inference, and unvalidated hypotheses.

## Research and Inspiration

The skill uses a hybrid research model:

- a curated registry of Apple official sources, shipped examples, public UI and motion galleries, inspiration sites, and asset sources;
- live research tailored to the current product and design question;
- explicit labels that separate authority, observation, inspiration, and hypothesis.

Web references such as 60fps, Recent, Awwwards, React Bits, and Magic UI may inspire visual or motion direction, but they do not prove Apple-native behavior. Third-party screenshots and assets are linked and observed rather than bundled unless reuse rights are verified.

## Repository Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── evals/
│   └── product-starting-point/
│       ├── README.md
│       ├── cases.json
│       ├── fixtures/
│       └── runs/
├── references/
│   ├── accessibility-and-localization.md
│   ├── apple-platform-adaptation.md
│   ├── authority-and-principles.md
│   ├── context-and-alignment.md
│   ├── design-system-and-dna.md
│   ├── maintenance-and-sources.md
│   ├── prototyping-and-implementation.md
│   ├── research-and-source-evidence.md
│   ├── source-registry.json
│   └── validation-and-review.md
├── scripts/
│   ├── validate_product_starting_point_evals.py
│   └── validate_source_registry.py
└── tests/
    ├── test_product_starting_point_evals.py
    └── test_source_registry.py
```

- `SKILL.md` defines the role, scope, workflow, review method, and routing rules.
- `agents/openai.yaml` provides the display metadata and default invocation prompt.
- `evals/product-starting-point/` contains fixed small-change, major-redesign, and zero-to-one evidence cases, review assertions, and preserved forward-test evidence.
- `references/` contains focused guidance loaded only when relevant to the current task.
- `references/source-registry.json` is a validated map of official, observable, inspirational, conditional, and excluded sources.
- `scripts/validate_product_starting_point_evals.py` checks the evaluation schema, required scenarios, assertions, and fixture paths.
- `scripts/validate_source_registry.py` checks required metadata, duplicate sources, HTTPS URLs, and review age.
- `tests/` protects the evaluation and source-registry validators’ required failure cases.

## Scope

This skill owns product intent, visual hierarchy, Apple-platform behavior, design-system decisions, and experience-validation criteria.

It does not replace specialized engineering workflows for Swift architecture, concurrency, performance profiling, CI, packaging, or release operations. When those are the primary task, use the appropriate engineering workflow alongside this skill.

## Maintenance

Stable design principles live in the skill. Version-specific Apple APIs, platform behavior, and Human Interface Guidelines should be verified against current official Apple sources when they affect a decision.

See [`references/maintenance-and-sources.md`](references/maintenance-and-sources.md) for the maintenance policy and regression prompts.

## License

This project is available under the [MIT License](LICENSE).
