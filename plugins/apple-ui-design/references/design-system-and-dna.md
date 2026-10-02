# Design System and Product DNA

## Load When

Load this reference when defining visual direction, semantic tokens, components, durable product DNA, or meaningfully different visual alternatives. Use its focused UI or terminology sections when assessing consistency or resolving an informal description that changes a design decision. Skip it when established project rules already resolve a small adjustment.

This is the single runtime source for the visual-system and product-DNA method, including observable UI criteria and informal-term translation. Direction owns changes; adaptation and review preserve or assess established DNA. `validation-and-review.md` owns the quality-lens map and acceptance checks.

## Contents

- Three layers of product expression
- Observable UI criteria
- Semantic tokens
- Typography, color, and materials
- Components
- Informal descriptions and candidate terms
- Interaction and motion language
- Meaningful direction exploration
- Minimal decision profile

## Three Layers

### 1. Product principles

Capture the user promise, core task, mental model, trust/control boundaries, content voice, and what the product must never imply. These constrain design without prescribing pixels.

### 2. Shared design DNA

Define recognizable character through semantic color, typography/reading behavior, spacing/grouping, shape/surfaces, imagery, density, motion, and component behavior. Avoid universal prescriptions such as mandatory 8-point spacing, a fixed type family, a required warm accent, or a compulsory effect. Derive the system from the product and validate consistency.

### 3. Platform expression

Translate shared DNA through navigation/presentation, touch/keyboard/focus/pointer, commands, columns/inspectors/tables/windows, system materials, and version-gated enhancement/fallback. Platform expression can differ without fragmenting identity.

## Observable UI Criteria

First distinguish confirmed project choices, experience baselines, and current platform guidance through `authority-and-principles.md`. Aesthetic preference is not a platform requirement. Use real content and affected states; check only criteria that can change the scoped outcome.

| Criterion | Observable good result | Problem to investigate |
|---|---|---|
| Hierarchy | Core task, next action, and result remain distinguishable | Primary and destructive actions compete with equal emphasis |
| Legibility | Labels and values remain readable on actual surfaces | Muted text disappears over a translucent background |
| Content fit | Realistic long, empty, and unusual content preserves meaning | A polished short placeholder hides clipping of a real Chinese title |
| State clarity | Selection, focus, disabled state, and error are perceptible | Color alone distinguishes selected and unselected items |
| Adaptation | Content reflows; required actions stay reachable | Large text or a compact window hides completion controls |
| Coherence | Repeated roles behave and look consistently | Identical actions use conflicting hierarchy or feedback |

These examples identify risks, not automatic findings: inspect the artifact and user impact. `accessibility-and-localization.md` owns contrast, text expansion, semantic and assistive checks; `apple-platform-adaptation.md` owns window/input translation. A screenshot can establish visible state, not successful use.

## Semantic Tokens

Prefer reusable intent over raw visual names: `contentPrimary`, `contentCritical`, `surfaceBase`, `surfaceSelection`, `actionDestructive`, `focusRing`, `spacingRelated`, `contentMeasure`, `motionFeedback`, `motionReduced`.

Values may vary by appearance, contrast, platform, size, or environment. Avoid tokens for every one-off value; record project values or unverified proposals honestly.

## Typography

Choose for language coverage and voice, scalable text, expected size/density, availability/license, numeric alignment, and hierarchy under expansion. System typography is valid, not mandatory. Custom fonts need fallbacks and accessibility behavior.

## Color and Materials

Define semantic roles before values. Inspect contrast on changing backgrounds, appearance modes, transparency/vibrancy, selected/focused/disabled/critical states, non-color redundancy, and competing chart or brand content.

Reject gradients, glass, shadows, or pure tones when unjustified, illegible, inconsistent, or overused—not categorically. Confirm minimum versions and fallback before using version-specific materials.

## Components

Define purpose and limits, content hierarchy, states/transitions, platform inputs, sizing/adaptation, accessibility, localization, and relationship to shared DNA. Do not force identical geometry when another native structure better serves the task. Show representative states in an actual product application.

## Informal Descriptions and Candidate Terms

Translate only when naming helps select behavior, research, or implementation. Preserve the user's description and offer candidates; clarify only ambiguity that changes the next decision. A term is neither a requirement nor proof of an API.

| User description | Candidate terms | Behavior and platform distinction |
|---|---|---|
| “从底下出来一层” | 底部面板 / bottom sheet; 弹出层 / popover | Modal task versus anchored context; an iPhone sheet may need a popover, panel, or window on iPad/Mac |
| “点卡片展开细节” | 渐进披露 / progressive disclosure; 展开控件 / disclosure | Inline detail differs from navigating elsewhere; preserve focus, state, and return meaning on each platform |
| “拖起来跟手，松开回弹” | 直接操纵 / direct manipulation; 弹簧动效 / spring motion | Continuous input plus settling; touch/Pencil and pointer/keyboard need equivalent task results |
| “页面像同一块东西变过去” | 共享元素转场 / shared-element transition; 形变 / morphing | Preserve object continuity versus change shape; neither implies a particular SwiftUI API |
| “背景跟着滚动慢一点” | 视差 / parallax; 滚动联动 / scroll-linked motion | Relative movement versus any scroll-driven effect; scrolling inputs and Reduce Motion expression differ |

Explain stable vocabulary from known behavior without mandatory browsing. Verify unfamiliar meanings when needed; verify exact Apple component names, APIs, availability, and version-sensitive guidance separately through `current-sources.md`. Source examples follow `research-and-source-evidence.md`; a gallery label cannot prove native semantics.

## Interaction and Motion Language

Keep durable interaction character and semantic motion tokens in product DNA. `interaction-and-motion.md` owns behavior contracts, purposes, risks, exploration, and evidence; do not duplicate its detailed rules here.

## Meaningful Direction Exploration

When unresolved, compare two or three hypotheses differing in hierarchy, density, navigation, materials, operation, or identity. For each show product idea, visible evidence, platform implications, risks, and what it optimizes/sacrifices. Superficial recolors are not separate directions. Extend confirmed direction without manufacturing choices.

## Minimal Project Design Decision Profile

This is a **project-internal documentation template**, not an Apple document, certification, or official method. Use the project's existing format; create it only if no durable source can carry decisions:

```markdown
# Project Design Decision Profile

## Product principles
## Target platforms and minimum versions
## Shared design DNA
## Platform-specific expression
## Semantic tokens
## Core components and states
## Interaction and motion
## Accessibility and localization
## Current decisions
## Explorations not yet approved
## Validation matrix
```

The profile records decisions; it does not replace prototypes or visual validation.
