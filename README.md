<div align="center">

# Apple UI Design

**A product-first plugin for native, distinctive, and verifiable interfaces across iOS, iPadOS, and macOS.**

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

## Overview

Apple UI Design is a skills-only plugin for designing, adapting, and reviewing product interfaces across the Apple ecosystem.

It starts from product intent and project evidence, then combines shared product DNA with platform-appropriate interaction. Apple conventions guide the experience without forcing every product into the same visual template.

It supports both existing products and zero-to-one ideas. Existing products are read from their current evidence; new products use explicit hypotheses and public research without pretending that untested assumptions are validated user needs.

The installable plugin contains three focused skills. They share one evidence and platform-method library without competing for the same task.

## Bundled Skills

- **`$apple-ui-direction`** — product and visual direction, screens, flows, design systems, and design-led prototypes.
- **`$apple-platform-adaptation`** — translate an established product between iOS, iPadOS, and macOS without merely enlarging layouts.
- **`$apple-ui-review`** — evidence-driven review of existing designs, prototypes, and UI implementations.

Production SwiftUI architecture, debugging, performance, CI, and release work remain engineering responsibilities. These skills provide product intent, interface decisions, evidence requirements, and acceptance criteria to the applicable engineering workflow.

## Core Principles

1. **Product intent comes first.** Confirmed decisions define the intended experience, while evidence labels keep known user needs separate from hypotheses.
2. **Project context is the local source of truth.** Existing requirements, design systems, components, assets, and platform targets are inspected before new decisions are made.
3. **The user owns product direction.** The skill explains platform, usability, and accessibility implications without silently replacing confirmed interaction or motion decisions.
4. **Native does not mean generic.** Native validation checks behavior and semantics, not resemblance to Apple system apps. Custom visuals and controls remain valid.
5. **Platforms are adapted, not enlarged.** iPhone, iPad, and Mac experiences may share a product while differing in hierarchy, density, navigation, and input.
6. **Accessibility and localization protect outcomes, not a default skin.** They are designed and validated without erasing brand expression.
7. **Visual and motion quality require evidence.** Compilation alone is not experience validation; important states and real interactions should be rendered and tested.

## Delivery Contracts

Every task selects one primary contract. The contract defines the evidence required before work begins, the artifact the user receives, and the strongest completion claim the available evidence supports.

| Contract | Minimum deliverable | Evidence required to claim completion |
|---|---|---|
| Visual direction | Key screens with representative content and visibly meaningful alternatives when direction is unresolved | Rendered screens; no high-fidelity claim from prose or token values alone |
| Screen or flow | An operable path covering the necessary states, transitions, recovery, and input behavior | Interactive prototype or running implementation; static screens support appearance only |
| Design system | Semantic tokens, component intent, representative states, and application to real product screens | Rendered component states and at least one representative product application |
| Platform adaptation | Shared-versus-specific decision matrix plus representative layouts and input behavior for each target environment | Visible evidence for material sizes; native runs for windowing, input, or platform-behavior claims |
| Native prototype | Scoped SwiftUI behavior with representative states, accessibility semantics, version fallback, and reduced-motion behavior when motion is present | SwiftUI Preview, Simulator or device run, or a real macOS app; recordings for interaction and motion claims |
| UI review | Evidence status plus severity-ordered findings using fact, impact, recommendation, and verification | Findings are limited to the supplied artifact and runtime evidence; text-only input is unverified consultation |

Exact visual values must come from project evidence, a rendered artifact, or remain explicitly marked as proposed and unverified. Interaction and motion decisions remain user-owned: the plugin may recommend, prototype, and test them, but it may not silently replace confirmed product choices.

Completion is reported in distinct stages: **direction aligned**, **design complete**, **prototype complete**, **code complete**, **experience verified**, and **user accepted**. A later stage is never inferred from an earlier one.

## Install the Plugin

Add this public repository as a Codex marketplace, then install the plugin:

```bash
codex plugin marketplace add RexYoung000/apple-ui-design-skill --ref main
codex plugin add apple-ui-design@apple-ui-design
```

Start a new Codex session after installation so the three bundled skills are loaded. In the ChatGPT desktop app, restart the app, open **Plugins**, choose the **Apple UI Design** marketplace, and install **Apple UI Design**.

Refresh the marketplace and reinstall after an update:

```bash
codex plugin marketplace upgrade apple-ui-design
codex plugin add apple-ui-design@apple-ui-design
```

This GitHub marketplace is the current public installation path. Submission to OpenAI’s universal Plugins Directory is a separate publication step and is not claimed by this repository.

See the official OpenAI documentation for [building skills](https://learn.chatgpt.com/docs/build-skills), [packaging plugins](https://developers.openai.com/plugins/build/plugins), and [using plugins](https://learn.chatgpt.com/docs/plugins).

## Migrate from the Standalone Skill

Earlier installations cloned this repository to `$HOME/.agents/skills/apple-ui-design` and invoked `$apple-ui-design`. That root skill remains a compatibility router for explicit legacy calls, but it is not bundled in the plugin and no longer invokes implicitly.

After installing the plugin:

- replace `$apple-ui-design` with `$apple-ui-direction` for direction, screen, flow, design-system, or prototype work;
- use `$apple-platform-adaptation` for cross-platform product translation;
- use `$apple-ui-review` for critique and validation.

Remove or move the old standalone checkout after confirming the plugin works, otherwise both the legacy router and the new skills may appear in selectors.

## Use in Codex

```text
Use $apple-ui-direction to design the onboarding flow for this iPad app.
```

Codex may also select it when a request matches the skill description:

```text
Use $apple-ui-review to review this macOS interface for hierarchy,
keyboard use, accessibility, and consistency with the product system.
```

## Use in the ChatGPT Desktop App

Install **Apple UI Design** from **Plugins**. In a new chat, type `@`, select the relevant bundled skill, and describe the task:

```text
Use Apple Platform Adaptation to adapt this existing iPhone flow for iPad and Mac.
```

The selected skill inspects available project evidence before asking questions. When a decision materially affects the product, it asks one focused question at a time and explains the recommended direction.

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
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── docs/
│   └── maintenance-and-sources.md
├── evals/
│   ├── plugin-split/
│   │   └── runs/
│   ├── delivery-contracts/
│   │   ├── README.md
│   │   ├── cases.json
│   │   ├── fixtures/
│   │   └── runs/
│   └── product-starting-point/
│       ├── README.md
│       ├── cases.json
│       ├── fixtures/
│       └── runs/
├── plugins/
│   └── apple-ui-design/
│       ├── .codex-plugin/
│       │   └── plugin.json
│       ├── references/
│       └── skills/
│           ├── apple-platform-adaptation/
│           ├── apple-ui-direction/
│           └── apple-ui-review/
├── scripts/
│   ├── validate_product_starting_point_evals.py
│   ├── validate_delivery_contract_evals.py
│   ├── validate_plugin_architecture.py
│   └── validate_source_registry.py
└── tests/
    ├── test_plugin_architecture.py
    ├── test_delivery_contract_evals.py
    ├── test_product_starting_point_evals.py
    └── test_source_registry.py
```

- `plugins/apple-ui-design/` is the complete installable archive; it contains no repository README, issue history, or evaluation runs.
- `plugins/apple-ui-design/skills/` contains three independently discoverable workflows.
- `plugins/apple-ui-design/references/` is their single shared source for product, evidence, platform, accessibility, research, and validation rules.
- `.agents/plugins/marketplace.json` exposes the plugin through the public GitHub repository.
- Root `SKILL.md` and `agents/openai.yaml` provide explicit-call compatibility for legacy standalone installations only.
- `evals/plugin-split/` preserves independent forward-test and installed-session evidence for all three bundled skills.
- `evals/delivery-contracts/` defines one realistic task and observable evidence assertions for each of the six delivery contracts.
- `evals/product-starting-point/` contains fixed small-change, major-redesign, and zero-to-one evidence cases, review assertions, and preserved forward-test evidence.
- `scripts/validate_delivery_contract_evals.py` checks contract coverage, fixture integrity, required artifacts, forbidden claims, and evidence expectations.
- `scripts/validate_product_starting_point_evals.py` checks the evaluation schema, required scenarios, assertions, and fixture paths.
- `scripts/validate_plugin_architecture.py` protects skill boundaries, shared-reference ownership, and package hygiene.
- `tests/` protects the plugin architecture, evaluation, and source-registry validators.

## Scope

The plugin owns product intent, visual hierarchy, Apple-platform behavior, design-system decisions, adaptation strategy, and experience-review criteria.

It does not replace specialized engineering workflows for Swift architecture, concurrency, performance profiling, CI, packaging, or release operations. When those are the primary task, use the appropriate engineering workflow alongside the relevant bundled skill.

## Maintenance

Stable design principles live in the plugin’s shared references. Version-specific Apple APIs, platform behavior, and Human Interface Guidelines should be verified against current official Apple sources when they affect a decision.

See [`docs/maintenance-and-sources.md`](docs/maintenance-and-sources.md) for the repository maintenance policy and regression prompts.

## License

This project is available under the [MIT License](LICENSE).
