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

## Verified Workflow Examples

These examples are preserved repository outputs, not aspirational mockups. Each one identifies the artifact, implementation boundary, and strongest validation claim supported by its evidence.

### UI direction: Today

**Example request:** Use `$apple-ui-direction` to turn an approved commitment model into visibly distinct iPhone directions without losing warmth.

**Evidence label:** Design — two rendered visual hypotheses. Prototype — static HTML only. Product code — none. Experience validation — not run; visual choice remains unaccepted.

![Two rendered Today visual-direction hypotheses](plugins/apple-ui-design/assets/screenshot-direction.png)

The result makes the hierarchy and product-emphasis tradeoff visible instead of presenting recolors as separate directions. Review the [full direction rationale](evals/delivery-contracts/runs/2026-07-29/visual-direction/README.md) and [render validation](evals/delivery-contracts/runs/2026-07-29/visual-direction/validation-report.md).

### Platform adaptation: OrbitCut

**Example request:** Use `$apple-platform-adaptation` to carry an established radial iPhone editor to iPad and Mac without stretching the phone layout.

**Evidence label:** Design — shared-versus-specific decisions and four rendered layouts. Prototype — static HTML only. Product code — none. Experience validation — native windowing, input, focus, and accessibility were not run.

![OrbitCut Mac expanded adaptation layout](plugins/apple-ui-design/assets/screenshot-adaptation.png)

The result keeps the radial timeline central while changing surrounding hierarchy and density for compact iPad, expansive iPad, minimum Mac, and expanded Mac environments. Review the [decision matrix](evals/delivery-contracts/runs/2026-07-29/platform-adaptation/decision-matrix.md) and [validation boundary](evals/delivery-contracts/runs/2026-07-29/platform-adaptation/validation.md).

### UI review: LedgerDesk

**Example request:** Use `$apple-ui-review` to prioritize only findings supported by a text implementation packet for a high-trust macOS reconciliation task.

**Evidence label:** Review/validation result — one Blocking and one Important finding. Prototype — none. Product code — none. Experience validation — not supported because screenshots and runtime access were absent.

![LedgerDesk evidence-bounded UI review excerpt](plugins/apple-ui-design/assets/screenshot-review.png)

The result reports supported findings without inventing visual defects, then separates keyboard, VoiceOver, window, localization, and recovery gaps into an exact acceptance path. Review the [complete finding report](evals/delivery-contracts/runs/2026-07-29/ui-review/review.md) and [source packet](evals/delivery-contracts/fixtures/ui-review.md).

## Trigger and Engineering Boundaries

The requested outcome—not the presence of words such as Apple, SwiftUI, UIKit, or AppKit—determines whether a bundled skill should run.

- Direction, screen, flow, design-system, interaction, motion, and design-led prototype requests route to `$apple-ui-direction`.
- Translation of an established product between Apple platforms routes to `$apple-platform-adaptation`.
- Critique, audit, validation, acceptance review, and prioritized UI findings route to `$apple-ui-review`.
- Compilation, concurrency, state management, architecture, performance, API usage, testing infrastructure, CI, packaging, and release route to an applicable engineering workflow.

The design skills may create a disposable native prototype or make a bounded presentation-layer SwiftUI change when code is required to answer an approved design question and existing architecture remains intact. Production integration, business logic, data, dependencies, broad refactors, and engineering correctness remain outside their independent ownership.

UIKit and AppKit products remain valid design, adaptation, and review targets. The plugin inspects their actual evidence and produces framework-aware decisions, but it does not promise SwiftUI implementation, silently migrate frameworks, or claim UIKit/AppKit production integration without an applicable engineering workflow and native verification.

The three bundled skills keep implicit invocation enabled because their outcomes are now distinct. Each `agents/openai.yaml` declares the same policy explicitly. The legacy root compatibility router remains explicit-only.

## Core Principles

1. **Product intent comes first.** Confirmed decisions define the intended experience, while evidence labels keep known user needs separate from hypotheses.
2. **Project context is the local source of truth.** Existing requirements, design systems, components, assets, and platform targets are inspected before new decisions are made.
3. **The user owns product direction.** The skill explains platform, usability, and accessibility implications without silently replacing confirmed interaction or motion decisions.
4. **Native does not mean generic.** Native validation checks behavior and semantics, not resemblance to Apple system apps. Custom visuals and controls remain valid.
5. **Platforms are adapted, not enlarged.** iPhone, iPad, and Mac experiences may share a product while differing in hierarchy, density, navigation, and input.
6. **Accessibility and localization protect outcomes, not a default skin.** They are designed and validated without erasing brand expression.
7. **Visual and motion quality require evidence.** Compilation alone is not experience validation; important states and real interactions should be rendered and tested.

## Decision Authority and Tradeoffs

The plugin does not use one universal authority ranking. It separates:

- hard legal, safety, security, privacy, contractual, and explicitly required core-experience boundaries;
- user- or project-owner decisions about product outcomes, audience, brand, interaction, and motion;
- experience outcome baselines such as perceiving, operating, and recovering through the core task;
- Apple guidance, native behavior, shipped UI, implementation constraints, and external inspiration as differently weighted evidence or advice.

Apple guidance and native components can reveal risk and reduce implementation uncertainty, but they do not own the product’s visual identity. Existing shipped behavior is evidence, not automatic correctness. When a material choice is disputed, the plugin states the observed fact, user impact, recommendation, verification path, and recorded decision. Once an informed choice is confirmed, it proceeds unless a hard boundary remains.

Communication pace is configurable. One focused question is the default only for a blocking, path-dependent product decision; independent factual gaps may be gathered compactly or checked in parallel.

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

## Regression Testing

The repository uses two complementary regression layers:

- **Deterministic CI checks** validate plugin structure, portable-package construction, source integrity, delivery contracts, product starting points, routing rules, the fixed 15-case skill matrix, output assertions, and protected golden-output checksums.
- **Fresh-session model checks** run selected prompts without exposing their assertions, then evaluate the saved skill trace and final output against the same case definition.

Each bundled skill has one direct request, one indirect request, one incomplete-information case, one implementation-only negative, and one evidence-risk boundary case. Every case includes fixed input material, the expected loaded and forbidden skills, required output behavior, and forbidden claims.

Run the complete deterministic gate:

```bash
python3 scripts/run_regression_checks.py
```

Evaluate a saved fresh-session result:

```bash
python3 scripts/evaluate_skill_regression_output.py \
  <case-id> --trace <trace.jsonl> --output <output.md>
```

CI deliberately does not call a live model: network availability and model variation are not deterministic release gates. Live results are preserved separately and must never receive the hidden assertions in their prompts.

Issue #6 also has a seven-case decision-authority suite covering confirmed custom interactions, shipped defects, accessibility outcomes, privacy boundaries, implementation convenience, communication pace, and project-internal terminology.

Issue #9 adds a current-source verification suite covering exact Apple pages, unavailable-source degradation, minimum-versus-enhancement versions, and official-source/runtime conflicts. Its preserved Liquid Glass record verifies the iOS 26 API claim and an iOS 17 guarded fallback without treating the newest material as a default direction.

Issue #7 adds a six-case accessibility and localization suite covering platform task matrices, multiple assistive technologies, visual settings, custom controls, and localization risks. The preserved Stillpoint record establishes semantic automation and the named Reduce Motion task only; the unrun VoiceOver path remains explicitly unverified.

Issue #14 adds a fixed interaction and motion method across tool, content, and experimental products. It protects confirmed user-owned interaction direction and requires task state, input, interruption, reversal, recovery, Reduce Motion, and native recordings to establish actual behavior instead of letting common Apple patterns or system components replace product judgment.

Issue #8 adds a content and sensitive-flow method for permission, privacy, identity, account data, subscription, purchase, and regulated-domain experiences. It requires truthful content, informed user control, non-manipulative choices, explicit failure recovery, current policy sources, and professional review where the design skill cannot own the underlying legal, medical, financial, or commercial fact.

Issue #10 adds a runtime-context budget and conditional-loading contract. Skill entry files retain only role, workflow, routing, and hard evidence boundaries; detailed methods remain single-owned shared references that load only when their stated task condition applies. Skill-entry size fell from 3,382 to 2,194 words, while total runtime instructions fell from 19,083 to 17,457 words without reducing the fixed regression result. Repository history, comparison notes, and release maintenance stay outside the installable runtime path.

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

## Install the Portable Agent Skill

SkillPay and Agent Skills-compatible clients use one portable `apple-ui-design` package. It keeps UI direction, platform adaptation, and UI review as distinct internal workflows while giving users one product to install. The Codex Plugin remains the preferred Codex distribution because it exposes the three workflows separately with native Plugin metadata.

Build the portable folder and ZIP from the same canonical workflow and reference sources used by the Plugin:

```bash
python3 scripts/build_portable_skill.py
```

The command writes `dist/apple-ui-design/` for folder upload and `dist/apple-ui-design.zip` for ZIP upload. Both artifacts place `SKILL.md` at the package root, include only runtime instructions and the MIT license, and exclude repository tests, evaluations, CI configuration, and Codex-only metadata.

Install the generated `apple-ui-design` folder in a location supported by the target client:

| Client | Installation location |
| --- | --- |
| Claude Code | `~/.claude/skills/apple-ui-design/` |
| OpenAI Codex standalone Skill | `$CODEX_HOME/skills/apple-ui-design/`, or `~/.codex/skills/apple-ui-design/` when `CODEX_HOME` is unset |
| OpenCode | `~/.agents/skills/apple-ui-design/` or `~/.config/opencode/skills/apple-ui-design/` |
| Pi | `~/.agents/skills/apple-ui-design/` or `~/.pi/agent/skills/apple-ui-design/` |
| Harness-style repositories | `skills/apple-ui-design/`, then reference it from the repository's agent instructions when automatic discovery is unavailable |

The portable package follows the [Agent Skills specification](https://agentskills.io/specification). It uses only standard frontmatter and package-local relative references; agent-specific invocation controls, tool names, permissions, and UI metadata remain outside the shared runtime instructions.

### SkillPay positioning

The SkillPay listing is a paid convenience distribution of this public MIT-licensed project, not an exclusive or encrypted edition. The product value is the generated cross-agent package, structural validation, tested workflow routing, and continued compatibility maintenance. State that relationship in the listing so buyers understand that purchasing supports maintenance and avoids manual packaging rather than purchasing private source code.

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

The selected skill inspects available project evidence before asking questions. For a blocking, path-dependent product decision it defaults to one focused question and explains the recommendation; independent facts may be gathered together, and the user can choose a step-by-step, batch, workshop, or explicit-assumptions pace.

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
├── .github/
│   └── workflows/
│       └── validate.yml
├── docs/
│   └── maintenance-and-sources.md
├── evals/
│   ├── plugin-split/
│   │   └── runs/
│   ├── decision-authority/
│   │   ├── README.md
│   │   ├── cases.json
│   │   └── runs/
│   ├── trigger-routing/
│   │   ├── README.md
│   │   ├── cases.json
│   │   └── runs/
│   ├── skill-regression/
│   │   ├── README.md
│   │   ├── cases.json
│   │   ├── fixtures/
│   │   └── goldens.json
│   ├── delivery-contracts/
│   │   ├── README.md
│   │   ├── cases.json
│   │   ├── fixtures/
│   │   └── runs/
│   ├── current-source-verification/
│   │   ├── README.md
│   │   ├── cases.json
│   │   ├── fixtures/
│   │   └── runs/
│   ├── accessibility-localization/
│   │   ├── README.md
│   │   ├── cases.json
│   │   └── runs/
│   ├── interaction-motion/
│   │   ├── README.md
│   │   ├── cases.json
│   │   └── runs/
│   ├── content-sensitive-flows/
│   │   ├── README.md
│   │   ├── cases.json
│   │   └── runs/
│   ├── runtime-context/
│   │   ├── README.md
│   │   ├── contract.json
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
├── packaging/
│   └── portable-skill/
│       └── SKILL.md.in
├── scripts/
│   ├── build_portable_skill.py
│   ├── run_regression_checks.py
│   ├── validate_portable_skill.py
│   ├── validate_decision_authority_evals.py
│   ├── evaluate_skill_regression_output.py
│   ├── validate_skill_regression_evals.py
│   ├── validate_trigger_routing_evals.py
│   ├── validate_product_starting_point_evals.py
│   ├── validate_delivery_contract_evals.py
│   ├── validate_current_source_evals.py
│   ├── validate_accessibility_localization_evals.py
│   ├── validate_interaction_motion_evals.py
│   ├── validate_content_sensitive_flow_evals.py
│   ├── validate_runtime_context.py
│   ├── validate_plugin_architecture.py
│   └── validate_source_registry.py
└── tests/
    ├── test_accessibility_localization_evals.py
    ├── test_current_source_evals.py
    ├── test_decision_authority_evals.py
    ├── test_skill_regression_evals.py
    ├── test_skill_regression_output.py
    ├── test_trigger_routing_evals.py
    ├── test_plugin_architecture.py
    ├── test_delivery_contract_evals.py
    ├── test_content_sensitive_flow_evals.py
    ├── test_runtime_context.py
    ├── test_interaction_motion_evals.py
    ├── test_portable_skill.py
    ├── test_product_starting_point_evals.py
    └── test_source_registry.py
```

- `plugins/apple-ui-design/` is the complete installable archive; it contains no repository README, issue history, or evaluation runs.
- `plugins/apple-ui-design/skills/` contains three independently discoverable workflows.
- `plugins/apple-ui-design/references/` is their single shared source for product, evidence, platform, accessibility, research, and validation rules.
- `packaging/portable-skill/SKILL.md.in` is the provider-neutral entry template. The build derives its three workflow references and all shared references from the canonical Plugin sources.
- `dist/apple-ui-design/` and `dist/apple-ui-design.zip` are ignored generated artifacts for SkillPay and Agent Skills-compatible clients.
- `.agents/plugins/marketplace.json` exposes the plugin through the public GitHub repository.
- Root `SKILL.md` and `agents/openai.yaml` provide explicit-call compatibility for legacy standalone installations only.
- `evals/plugin-split/` preserves independent forward-test and installed-session evidence for all three bundled skills.
- `evals/trigger-routing/` separates positive design intents, implementation-only negatives, and mixed design-engineering boundary cases.
- `evals/skill-regression/` is the unified 15-case trigger-and-output matrix and golden-output registry.
- `evals/delivery-contracts/` defines one realistic task and observable evidence assertions for each of the six delivery contracts.
- `evals/current-source-verification/` protects exact Apple sources, access failure, version fallbacks, runtime conflicts, and the preserved Liquid Glass verification record.
- `evals/accessibility-localization/` protects platform task selection, assistive-technology evidence boundaries, visual settings, custom controls, and localization risks.
- `evals/interaction-motion/` protects product authority, interaction contracts, motion language, platform inputs, interruption and reversal, Reduce Motion, and native-evidence boundaries.
- `evals/content-sensitive-flows/` protects content clarity, permission and privacy control, identity and account-data paths, commerce transparency, failure recovery, professional boundaries, and honest evidence claims.
- `evals/runtime-context/` records the pre-optimization baseline and protects single ownership, conditional reference loading, browseable long references, and runtime size budgets.
- `evals/product-starting-point/` contains fixed small-change, major-redesign, and zero-to-one evidence cases, review assertions, and preserved forward-test evidence.
- `scripts/validate_current_source_evals.py` checks source-record integrity, exact Apple URLs, access dates, version splits, fallbacks, evidence labels, and referenced runtime artifacts.
- `scripts/validate_accessibility_localization_evals.py` checks Issue #7 method coverage, skill routing, and source markers across six fixed cases.
- `scripts/validate_interaction_motion_evals.py` checks Issue #14 coverage across three product scenarios and all bundled skills.
- `scripts/validate_content_sensitive_flow_evals.py` checks Issue #8 coverage across five high-risk flow families, current official sources, and all bundled skills.
- `scripts/validate_runtime_context.py` measures installable instruction size and checks reference ownership, load conditions, long-reference contents, and context budgets.
- `scripts/validate_delivery_contract_evals.py` checks contract coverage, fixture integrity, required artifacts, forbidden claims, and evidence expectations.
- `scripts/validate_trigger_routing_evals.py` checks route coverage, implementation boundaries, and the required engineering-negative domains.
- `scripts/evaluate_skill_regression_output.py` checks a saved trace and response against one case without exposing assertions to the model.
- `scripts/run_regression_checks.py` is the single deterministic local and CI entry point.
- `scripts/validate_product_starting_point_evals.py` checks the evaluation schema, required scenarios, assertions, and fixture paths.
- `scripts/validate_plugin_architecture.py` protects skill boundaries, shared-reference ownership, and package hygiene.
- `scripts/build_portable_skill.py` and `scripts/validate_portable_skill.py` build the folder and ZIP, then reject missing files, escaping references, client-specific metadata, repository-only files, and SkillPay size violations.
- `tests/` protects the Plugin architecture, portable distribution, evaluation, and source-registry validators.
- `.github/workflows/validate.yml` runs the same deterministic gate for pushes and pull requests.

## Scope

The plugin owns product intent, visual hierarchy, Apple-platform behavior, design-system decisions, adaptation strategy, and experience-review criteria.

It does not replace specialized engineering workflows for Swift architecture, concurrency, performance profiling, CI, packaging, or release operations. When those are the primary task, use the appropriate engineering workflow alongside the relevant bundled skill.

## Maintenance

Stable design principles live in the plugin’s shared references. Version-specific Apple APIs, platform behavior, and Human Interface Guidelines should be verified against current official Apple sources when they affect a decision.

See [`docs/maintenance-and-sources.md`](docs/maintenance-and-sources.md) for the repository maintenance policy and regression prompts.

## License

This project is available under the [MIT License](LICENSE).
