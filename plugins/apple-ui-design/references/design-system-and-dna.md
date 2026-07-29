# Design System and Product DNA

Use this reference when establishing a direction, extending a design system, comparing alternatives, or creating a durable Apple Design Profile.

The direction skill owns design-system changes; adaptation and review read this file only to preserve or assess established product DNA.

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

Treat confirmed interaction and motion decisions as product design, not as decoration added after layout.

For interaction, capture:

- the product mental model and the user’s intended way of manipulating it;
- primary, expert, gestural, spatial, or experimental interaction paths;
- what the user has explicitly approved;
- discoverability, learning, error recovery, input, and accessibility implications;
- platform conventions that support the idea or create a known tradeoff.

Platform conventions are recommendations and evidence. Do not silently add an alternative path, replace an unconventional interaction, or remove a product-specific gesture after the user has chosen it. Explain material risk and validate the chosen behavior.

For motion, define:

- character and emotional tone;
- functional, spatial, feedback, expressive, or brand purpose;
- relationship to touch, pointer, keyboard, Pencil, scroll, or system events;
- continuity, interruption, reversal, repetition, and duration logic;
- expression by platform and input method;
- reduced-motion behavior that preserves meaning and appropriate brand character.

Motion may exist for delight or identity as well as utility. Do not require every animation to explain a state change. Do require it to coexist with the task, user comfort, system settings, and the claimed performance envelope.

When motion direction is unresolved, make two or three visibly different prototypes. When it is already established, extend it without manufacturing alternatives. Validate meaningful motion through native execution and recording; a timing specification alone is not evidence.

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

## Minimal Apple Design Profile

Create only when the project lacks an appropriate durable source:

```markdown
# Apple Design Profile

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
