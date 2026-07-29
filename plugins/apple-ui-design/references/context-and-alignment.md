# Context and Alignment

Use this reference for new design work, ambiguous requests, cross-platform expansion, or any change that may alter information hierarchy, navigation, brand, or a core flow.

All bundled skills use this file as their single product-starting-point and evidence-label source.

## Inspect Before Asking

Search for available evidence in this order:

1. Repository instructions and current project status.
2. Product, requirements, roadmap, feature-loop, and design documents.
3. Architecture and deployment targets when they constrain UI.
4. Current screens, screenshots, previews, navigation, strings, design tokens, asset catalogs, and reusable components.
5. Relevant tests, sample data, accessibility labels, localization catalogs, and platform conditionals.
6. Current official Apple sources when an API or platform rule may have changed.

Do not ask the user to restate facts that can be verified in the project.

## Evidence Labels

Keep these categories separate in notes, recommendations, and handoff:

- **User-confirmed decision**: the intended product direction.
- **Project fact**: verified in current documentation, assets, code, configuration, analytics, or runtime.
- **External evidence**: supported by a named official source, shipped product, study, or public observation.
- **Design inference**: a reasoned interpretation of available evidence.
- **Unvalidated hypothesis**: plausible but not yet confirmed or tested.

A user-confirmed decision has authority over direction. It does not become user research or runtime proof merely because it was approved.

For a zero-to-one product, distinguish **user-confirmed product intent** from **validated user evidence**. An audience or need supplied by the user remains a user-confirmed hypothesis unless interviews, behavioral data, market evidence, or another explicit basis validates it. Never promote a fixture, brief, or user statement to a stronger evidence level than its source label.

## Target User and Usage Context

Define only the dimensions that change the design:

- primary user and core task;
- platform, device, window, and input methods;
- usage frequency, proficiency, and environment;
- task duration, interruption, collaboration, and continuity;
- failure cost, privacy, trust, or destructive consequences;
- accessibility and localization needs in scope;
- relevant learned behaviors from the current product or comparable products.

Do not invent age, occupation, personality, or lifestyle details unless supplied by evidence and relevant to the decision.

### Existing product

Extract facts from current requirements, interface, navigation, strings, assets, implementation, runtime behavior, support data, and analytics when available. Ask only about gaps or conflicts that would change the result.

For a small reversible adjustment, reuse the established user and interaction model. For a major redesign, check whether the target user, core task, and existing model are still valid before preserving them.

Choose the response depth from the decision risk:

| Situation | Required behavior |
|---|---|
| Small, reversible adjustment with sufficient project evidence | Reuse verified project facts and proceed. Do not make the user approve a new persona or repeat facts merely to demonstrate discovery. Surface only assumptions that could materially change the adjustment. |
| Major redesign with consistent evidence | State the project facts and confirmed decisions that anchor the redesign, then proceed at the appropriate fidelity. Treat existing behavior as precedent, not proof that it must survive. |
| Major redesign with conflicting or stale evidence | Separate the conflict into labelled facts, decisions, inferences, and hypotheses. Ask the single highest-impact unresolved question before committing to a direction. |

Do not infer the intended future audience solely from the current interface. A shipped flow proves that the flow exists; it does not prove that the target user, task priority, or interaction model is still correct.

### Zero-to-one product

Start from the user’s idea, audience hypothesis, constraints, and desired outcome. Research public market, product, Apple-platform, accessibility, and comparable-task evidence where useful. Separate what is observed from what is inferred.

Before approving a high-fidelity direction, confirm at least the primary user, core task, target platform context, and material constraints. If research is absent, label the work as hypothesis-led. Never claim that a need is validated without interviews, behavioral data, market evidence, or another explicit basis.

Before the first direction proposal, expose a compact status:

```text
Confirmed product intent and constraints:
External evidence checked:
Audience and design hypotheses:
Material unknowns:
```

Use `not yet researched` rather than leaving the evidence row absent. Keep the status proportional to the task, but make it visible enough that the user can challenge the assumptions before selecting a direction.

## Starting-Point Decision Procedure

1. Determine whether the artifact is an existing product or a zero-to-one product.
2. Extract the smallest task-and-context profile needed for the current decision.
3. Label every material conclusion as a user-confirmed decision, project fact, external evidence, design inference, or unvalidated hypothesis.
4. Check for conflicts between intended direction and current evidence.
5. Choose the response:
   - proceed without a new intake for a sufficiently evidenced small change;
   - expose the material conflict and ask one question for a major redesign;
   - expose the zero-to-one evidence status before proposing a direction.

Labels belong on decisions that influence the design, not on every sentence or minor styling value. Keep internal notes and user-facing output readable while preserving traceability.

## Material Questions

Ask when the answer would change one of these:

- product goal or user mental model;
- target platform or minimum version;
- feature scope or platform relationship;
- task priority, information architecture, or navigation;
- visual direction or brand boundary;
- data/state meaning shown to the user;
- destructive, irreversible, privacy-sensitive, or permission behavior;
- expected artifact or implementation authority;
- acceptance criteria.

Do not block on a small reversible choice such as a minor spacing value when established tokens and context provide a sound answer.

## Question Strategy

When the user or repository asks for progressive alignment, each turn should:

1. lead with the observed fact;
2. name the decision and why it matters;
3. recommend one direction;
4. explain the meaningful alternative;
5. ask one question;
6. accept a custom answer.

Do not dump a generic intake questionnaire. Independent factual checks can run in parallel. Follow the project’s preferred communication rhythm when it is known, and continue asking only while a material uncertainty remains.

## Platform Definition

The user defines which platforms exist for the product and whether their positioning, features, task priorities, or interactions differ.

Useful questions, only when relevant:

- Which of iOS, iPadOS, and macOS are in scope?
- Is each platform’s feature set the same, overlapping, or different?
- Are there platform-specific primary tasks?
- What input modes and window behaviors matter?
- Is content density expected to differ?
- Which cross-device continuity behaviors are product requirements?

Do not impose “primary,” “peer,” or “companion” labels. They can be offered as thinking aids, not requirements.

## Minimum Version Definition

For an existing app, the configured deployment target is the current fact. Confirm whether documentation and targets agree.

For a new product, help the user decide separately for each platform using:

- target users’ devices and OS distribution;
- mandatory platform APIs;
- expected release date and maintenance horizon;
- compatibility, fallback, testing, and support cost;
- organizational device control;
- dependencies and build tooling.

Do not use a fixed formula such as “latest minus one.” Record:

| Platform | Minimum version | Core experience at baseline | Optional newer enhancement |
|---|---|---|---|
| iOS | Project decision | Complete core tasks | Version-gated enhancement |
| iPadOS | Project decision | Complete target tasks | Version-gated enhancement |
| macOS | Project decision | Complete target tasks | Version-gated enhancement |

## Decision Recording

Use the project’s existing source of truth. Record:

- decision;
- evidence label and source;
- reason;
- affected platforms and flows;
- rejected alternative only when the tradeoff matters later;
- validation requirement;
- date or version when the project convention calls for it.

Create a new design profile only when no current document can carry reusable decisions.
