# Prototyping and Implementation

Use this reference when choosing a prototype medium, generating SwiftUI, or translating approved design into an existing app.

Bundled design skills use it to select evidence fidelity and hand work to engineering without claiming production ownership.

Read `engineering-routing.md` first when the task includes implementation code. It defines when a design artifact is sufficient, when bounded design-led SwiftUI work is allowed, and when an engineering workflow is required.

## Choose Fidelity by Decision

Use the cheapest artifact that can answer the current question:

| Question | Suitable artifact |
|---|---|
| Which visual direction fits? | Static canvas, image, or lightweight comparison |
| Is hierarchy understandable? | High-fidelity static screen with realistic content |
| Does a flow make sense? | Clickable flow or lightweight interaction prototype |
| Does Apple-native behavior work? | SwiftUI prototype in Preview, Simulator, or Mac app |
| Is production integration correct? | Real project implementation with real components and states |

Do not use a high-cost implementation to answer an early visual question. Do not use HTML to claim native behavior is verified.

## Existing Project First

Before implementation, inspect:

- deployment targets and target platforms;
- established app structure and feature boundaries;
- design tokens and reusable components;
- navigation and presentation conventions;
- localization system and string catalog;
- sample data and state models;
- accessibility patterns;
- build, test, preview, and simulator workflows.

Reuse established product language and components unless the approved design explicitly changes them.

## SwiftUI as Expression

SwiftUI should express the approved design:

- model states explicitly;
- keep view hierarchy readable;
- prefer native containers and controls when they preserve the intended behavior and reduce semantic or system-integration risk;
- customize their visuals without discarding behavior or semantics;
- use custom controls and interactions when they serve the approved product model, then provide the required roles, states, actions, input behavior, and system-setting responses;
- use availability checks and fallbacks for version-specific APIs;
- create previews for meaningful states and sizes;
- keep business logic out of presentation code.

Do not change architecture, introduce dependencies, or perform broad refactors solely to make a screen easier to style. Route architecture and performance work to the applicable engineering skill.

Native validation checks whether the intended behavior survives the real platform. It does not grade visual similarity to Apple system apps.

## UIKit and AppKit

UIKit and AppKit products remain first-class design, adaptation, and review targets. Inspect their actual view hierarchy, navigation, windows, commands, focus behavior, assets, state model, and runtime evidence.

Do not rewrite a UIKit or AppKit product into SwiftUI because SwiftUI is easier to prototype. A separate SwiftUI prototype may answer a bounded design question only when it is labelled as a prototype and does not stand in for UIKit or AppKit integration evidence.

Production UIKit and AppKit implementation, framework API correctness, interoperability, architecture, testing, packaging, and release belong to an applicable engineering workflow.

## Prototype Requirements

A native high-fidelity prototype should include only what is needed to validate the decision, but it must not fake the tested behavior.

Include as applicable:

- representative real-world content;
- normal, empty, loading, error, disabled, selected, and destructive states;
- navigation, dismissal, focus, keyboard, pointer, touch, and resizing;
- accessibility labels and scalable content;
- reduced-motion behavior;
- platform and version fallback;
- clear boundaries for mocked data or unavailable services.

## HTML and Static Exploration

HTML or static artifacts are acceptable for:

- visual direction boards;
- side-by-side variations;
- early hierarchy experiments;
- stakeholder review before native implementation.

Label them accurately. Avoid device-frame theater that hides whether the actual content adapts. An iPhone-shaped browser window is not proof of iOS behavior, and a desktop browser is not proof of macOS window or command behavior.

## Implementation Handoff

When design and implementation are separated, provide:

- product goal and primary task;
- platform scope and minimum versions;
- layout and navigation behavior by environment;
- semantic tokens rather than isolated pixel values;
- component states and content rules;
- motion purpose and reduced-motion behavior;
- accessibility and localization requirements;
- reference screens and assets;
- validation matrix and acceptance path;
- unresolved decisions.

Avoid handoff specifications that reproduce every frame but omit state transitions and behavior.

## Completion Language

Use accurate claims:

- **Direction aligned**: the user selected a visual or interaction hypothesis.
- **Design complete**: required screens, states, and specifications are produced.
- **Prototype complete**: the scoped interaction exists in a prototype.
- **Code complete**: scoped implementation is present and passes stated technical checks.
- **Experience verified**: required platforms and interactions were rendered and exercised with evidence.
- **User accepted**: the user confirmed visual and real-use behavior.

Do not collapse these stages into “done.”
