# Delivery Contracts and Evidence Gates

Use this reference at the start and end of every task. Select one primary contract, state it to the user, and use its evidence gate to limit completion claims. A task may produce supporting artifacts from another contract, but do not blur their completion criteria.

## Shared Rules

### Inputs and evidence

Before producing a direction or finding:

1. derive known product facts from the project;
2. separate confirmed decisions, observed implementation, external evidence, design inference, and unvalidated hypotheses;
3. name the artifact requested and the decision it must support;
4. ask one highest-impact question only when the missing answer would materially change the artifact;
5. pause when required source material, user approval, or runtime access is unavailable and cannot be safely substituted.

For an existing product, inspect its requirements, current interface, components, assets, content, platform targets, and available runtime behavior. Preserve confirmed boundaries unless the user approves a change.

For a zero-to-one product, keep audience, core-task, platform-capability, and visual hypotheses visibly unvalidated until evidence or user decisions support them. Do not invent a mature design system, brand asset, or tested user need.

### Exact values

A precise color, type size, spacing, radius, opacity, blur, breakpoint, spring, easing curve, or duration must be one of:

- **project value** — read from an existing token, asset, component, or approved specification;
- **rendered proposal** — used in a visible artifact and explicitly open to visual acceptance;
- **measured result** — observed in a running implementation or recorded test;
- **unverified proposal** — clearly labelled for later rendering or runtime validation.

Never present an unrendered number as proven visual quality. Prefer semantic intent before raw values.

### Interaction and motion

The user owns product, interaction, and motion decisions. Platform convention and native components are evidence and risk-reduction tools, not a visual veto.

When motion is in scope, define its purpose, input relationship, continuity, interruption, reversal, repetition, and platform expression. Deliver the reduced-motion expression as an intentional equivalent: preserve state, feedback, spatial meaning, and suitable brand character rather than mechanically disabling all animation.

Motion is visually explored through rendered prototypes and is verified only through a representative native run and recording. A duration table, static storyboard, HTML animation, or successful build does not prove native motion behavior.

### Evidence gates

| Claim | Minimum evidence |
|---|---|
| Direction aligned | The user selected or confirmed a visible hypothesis or bounded direction |
| Design complete | Required screens, states, specifications, and visible artifacts exist |
| Prototype complete | The scoped path is operable in the stated prototype medium |
| Code complete | Scoped implementation exists and passes stated technical checks |
| Experience verified | Required native environments, states, and inputs were rendered and exercised with preserved evidence |
| User accepted | The user confirmed the visual and real-use result |

Do not infer a later claim from an earlier one. A screenshot supports static appearance, an interactive prototype supports its exercised path, a native run supports the exercised platform behavior, and a recording supports the interaction or motion it visibly captures.

## Contract 1: Visual Direction

**Owner:** `$apple-ui-direction`

**Required inputs**

- product outcome, primary user or labelled audience hypothesis, and core task;
- target platform and usage context;
- project or user-confirmed constraints;
- existing design DNA and assets, or their confirmed absence;
- the decision the direction must help the user make.

**Do not infer**

- validated user preference from public inspiration;
- a complete brand system from an adjective;
- exact visual values without a project source or rendered proposal;
- user approval before visible review.

**Steps**

1. establish the evidence state and design boundary;
2. reuse the current system when direction is established;
3. when unresolved, produce two or three materially different visible hypotheses;
4. apply representative content to the key screens;
5. compare visible tradeoffs against the confirmed product goal;
6. obtain user direction before treating the hypothesis as aligned.

**Required artifact**

- rendered key screens with representative content;
- meaningful alternatives when the direction is unresolved;
- evidence labels, platform implications, risks, and an acceptance path.

**Completion**

Prose, mood words, token tables, or implementation suggestions alone do not complete this contract. Without rendered key screens, report the direction as a bounded proposal or pause for the missing asset or rendering capability.

## Contract 2: Screen or Flow

**Owner:** `$apple-ui-direction`

**Required inputs**

- entry condition, user goal, success result, and exit;
- screens and states in scope;
- navigation and data assumptions;
- relevant touch, keyboard, pointer, focus, gesture, and assistive paths;
- failure, cancellation, interruption, and recovery behavior.

**Do not infer**

- that connected static screens are operable;
- unavailable product capability or data;
- a hidden alternative interaction not approved by the user;
- successful recovery without exercising it.

**Steps**

1. map the happy path and necessary non-happy states;
2. define transitions, feedback, cancellation, recovery, and focus;
3. create an operable prototype using the cheapest medium that answers the question;
4. exercise the scoped path with representative content and inputs;
5. record missing native behavior separately from prototype findings.

**Required artifact**

- an operable path;
- state and transition map;
- representative normal, loading, empty, error, disabled, destructive, and interrupted states when relevant;
- observed results and an exact acceptance path.

**Completion**

Static screens support appearance review only. Interaction is prototype-complete only after the scoped path can be operated; Apple-native behavior remains unverified until exercised natively.

## Contract 3: Design System

**Owner:** `$apple-ui-direction`

**Required inputs**

- product principles and design DNA;
- target platforms, environments, appearance modes, and content needs;
- current tokens, components, assets, and known inconsistencies;
- the screens or product areas the system must serve.

**Do not infer**

- a universal spacing grid, typeface, material, or component style;
- token values from generic Apple convention;
- system completeness from an isolated component sheet;
- cross-platform equivalence from identical geometry.

**Steps**

1. define semantic roles before values;
2. separate product DNA from platform expression;
3. specify component purpose, states, content, input, adaptation, semantics, and motion;
4. render representative states;
5. apply the system to at least one real product screen;
6. record platform, accessibility, localization, and version variations.

**Required artifact**

- semantic tokens and decision rationale;
- component definitions with representative states;
- rendered component evidence;
- at least one representative product screen using the system;
- adoption boundary and unresolved exceptions.

**Completion**

A token list alone is not a complete design system. Claim design complete only when the system is visibly applied to representative product content and its necessary states are shown.

## Contract 4: Platform Adaptation

**Owner:** `$apple-platform-adaptation`

**Required inputs**

- established source experience and runtime evidence;
- source and target platforms, versions, sizes, windows, orientations, and inputs;
- shared product goal, content model, terminology, and design DNA;
- product role and feature relationship on each platform;
- confirmed interaction decisions and continuity requirements.

**Do not infer**

- that all platforms have equal feature scope;
- that enlargement is adaptation;
- that visual similarity proves equivalent behavior;
- that platform convention may silently replace a confirmed product interaction.

**Steps**

1. inspect the source experience;
2. record shared and platform-specific decisions;
3. produce representative layouts for every material target environment;
4. translate navigation, density, windowing, commands, and inputs;
5. exercise material platform behavior natively;
6. record fallbacks, continuity, accessibility, localization, and reduced-motion behavior.

**Required artifact**

- shared-versus-platform-specific decision matrix;
- representative layouts and states for material sizes or window configurations;
- input and interaction mapping;
- visible evidence for each material environment;
- native evidence for windowing, input, command, focus, or platform-behavior claims.

**Completion**

Layouts can be design-complete without native verification when labelled accurately. Claim the adaptation experience verified only for target environments and behaviors actually rendered and exercised.

## Contract 5: Native Prototype

**Owner:** `$apple-ui-direction`, paired with an engineering workflow when production architecture is requested

**Required inputs**

- the product or experience question being tested;
- target platform, minimum versions, environments, and inputs;
- approved direction and interaction boundary;
- representative data and states;
- build, Preview, Simulator, device, or macOS run path.

**Do not infer**

- production readiness from a prototype;
- native behavior from HTML;
- experience quality from compilation;
- backend, permissions, or services that are mocked.

**Steps**

1. implement only the behavior required to answer the question;
2. identify mocks and production boundaries;
3. include representative states, semantics, content expansion, version fallbacks, and input behavior;
4. run in SwiftUI Preview, Simulator or device, or a real Mac app as appropriate;
5. operate the scoped path and preserve screenshots or recordings;
6. when motion is present, run and record both standard and reduced-motion expressions.

**Required artifact**

- runnable scoped SwiftUI prototype;
- representative states and content;
- native run log and environment details;
- screenshots for static states;
- recording for interaction or motion;
- reduced-motion evidence when motion is present;
- unresolved production and service boundaries.

**Completion**

Compilation supports code-complete claims only. Prototype complete requires an operable scoped path. Experience verified requires recorded native execution of the claimed states, inputs, and motion behavior.

## Contract 6: UI Review

**Owner:** `$apple-ui-review`

**Required inputs**

- intended product outcome and core task;
- exact artifact and version;
- target platform, environment, state, content, and input represented;
- requested review depth;
- available screenshots, recordings, implementation, and runtime evidence.

**Do not infer**

- runtime behavior from appearance;
- visual contrast or layout from prose;
- user validation from reviewer preference;
- native fit from visual resemblance to Apple apps.

**Steps**

1. state the evidence boundary and review level;
2. inspect only claims supported by the artifact;
3. report actionable findings by severity and user impact;
4. use fact, impact, evidence, recommendation, and verification for each finding;
5. separate required outcomes, Apple-supported recommendations, optional optimizations, and explorations;
6. name unrepresented scenarios and the acceptance path.

**Required artifact**

- evidence and scope statement;
- severity-ordered findings;
- verification method for every actionable finding;
- unresolved risks and an exact user acceptance path.

**Completion**

Text-only input permits unverified consultation, not visual or experience validation. Do not manufacture findings when the supplied evidence supports none.
