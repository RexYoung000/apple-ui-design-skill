# Design System and Product DNA

## Load When

Load this reference when defining visual direction, semantic tokens, components, durable product DNA, or meaningfully different visual alternatives. Do not load it for review or adaptation when no visual-system decision is in scope.

This is the single runtime source for the visual-system and product-DNA method. The direction skill owns changes; adaptation and review use it only to preserve or assess established DNA.

## Contents

- Three layers of product expression
- Semantic tokens
- Typography, color, and materials
- Components
- Interaction and motion language
- Meaningful direction exploration
- Minimal decision profile

## Three Layers

### 1. Product principles

Capture stable product meaning:

- user promise and core task;
- product mental model;
- trust and control boundaries;
- content voice;
- what the product must never imply.

These principles constrain design without prescribing exact pixels.

### 2. Shared design DNA

Define the recognizable system:

- qualitative character and emotional tone;
- semantic color roles;
- typography roles and reading behavior;
- spacing rhythm and grouping logic;
- shape and surface language;
- icon and imagery philosophy;
- information-density stance;
- motion character and feedback;
- component behavior that carries product identity.

Avoid universal prescriptions such as mandatory 8-point spacing, a fixed type family, a required warm accent, or a compulsory signature effect. Derive the system from the product and validate consistency.

### 3. Platform expression

Describe how shared DNA appears through platform-native structures:

- navigation and presentation;
- touch, keyboard, focus, pointer, commands, menus, and shortcuts;
- columns, inspectors, tables, toolbars, windows, and resizable layouts;
- system materials and visual effects;
- version-specific enhancement and fallback.

Platform expression can differ without fragmenting the brand.

## Semantic Tokens

Prefer semantic roles over raw visual names:

- `contentPrimary`, `contentSecondary`, `contentCritical`;
- `surfaceBase`, `surfaceRaised`, `surfaceSelection`;
- `actionPrimary`, `actionDestructive`, `focusRing`;
- `spacingRelated`, `spacingSection`, `contentMeasure`;
- `motionFeedback`, `motionTransition`, `motionReduced`.

Token names should explain purpose. Values may vary by appearance, contrast, platform, size, or environment.

Do not create tokens for every one-off value. A token earns existence when it expresses reusable intent.

## Typography

Choose typography based on:

- language coverage and product voice;
- Dynamic Type or scalable text needs;
- legibility at expected sizes and density;
- platform availability and licensing;
- numeric alignment or tabular needs;
- hierarchy that survives content expansion.

System typography is a valid choice, not a mandatory choice. Custom typography must include appropriate fallbacks and accessibility behavior.

## Color and Materials

Define roles before values. Check:

- contrast in real states;
- appearance modes in scope;
- vibrancy and transparency against changing backgrounds;
- selected, focused, disabled, critical, and elevated states;
- color-blind-safe redundancy;
- screenshots, charts, and branded content that may introduce competing color.

Do not ban gradients, glass, shadows, pure tones, or system colors categorically. Reject them when they are unjustified, illegible, inconsistent, or overused.

Use version-specific materials only after confirming minimum versions and fallback behavior.

## Components

A component definition should cover:

- purpose and when not to use it;
- content and hierarchy;
- states and transitions;
- input behaviors by platform;
- sizing and adaptation rules;
- accessibility semantics;
- localization and content expansion;
- relationship to shared DNA and platform expression.

Do not force the same component geometry across platforms when a native structure better serves the task.

## Interaction and Motion Language

Keep shared interaction character, semantic motion roles, and reusable motion tokens in the product DNA. Read `interaction-and-motion.md` when creating, adapting, prototyping, or reviewing material behavior; it owns the interaction contract, motion purposes, product-specific risk focus, exploration rules, and evidence boundary.

Do not duplicate detailed behavior rules here. Record only the durable product language and token intent that must stay coherent across components and platforms.

## Meaningful Direction Exploration

When direction is unresolved, create two or three hypotheses that differ in a decision users can evaluate:

- calm vs energetic hierarchy;
- sparse focus vs dense professional workspace;
- content-led vs tool-led navigation;
- restrained vs expressive material;
- direct manipulation vs explicit controls;
- typographic vs illustrative identity.

For each direction, state:

- product idea;
- visible evidence;
- platform implications;
- accessibility or implementation risks;
- what it optimizes and sacrifices.

Do not present superficial recolors as separate directions.

## Minimal Project Design Decision Profile

This profile is a **project-internal documentation template**, not an Apple document, certification, or official Apple design method. Create it only when the project lacks an appropriate durable source:

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

Use the project’s existing format when one exists. The profile records decisions; it does not replace prototypes or visual validation.
