# Context and Alignment

Use this reference for new design work, ambiguous requests, cross-platform expansion, or any change that may alter information hierarchy, navigation, brand, or a core flow.

## Inspect Before Asking

Search for available evidence in this order:

1. Repository instructions and current project status.
2. Product, requirements, roadmap, feature-loop, and design documents.
3. Architecture and deployment targets when they constrain UI.
4. Current screens, screenshots, previews, navigation, strings, design tokens, asset catalogs, and reusable components.
5. Relevant tests, sample data, accessibility labels, localization catalogs, and platform conditionals.
6. Current official Apple sources when an API or platform rule may have changed.

Do not ask the user to restate facts that can be verified in the project.

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

## One Question per Round

Each alignment turn should:

1. lead with the observed fact;
2. name the decision and why it matters;
3. recommend one direction;
4. explain the meaningful alternative;
5. ask one question;
6. accept a custom answer.

Do not dump a generic intake questionnaire. Continue asking only while a material uncertainty remains.

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
- reason;
- affected platforms and flows;
- rejected alternative only when the tradeoff matters later;
- validation requirement;
- date or version when the project convention calls for it.

Create a new design profile only when no current document can carry reusable decisions.
