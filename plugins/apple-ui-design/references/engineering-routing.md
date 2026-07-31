# Design and Engineering Routing

## Load When

Load this reference when code, framework delivery, production integration, or implementation ownership is in question. Do not load it for a design-only task with an already selected non-code artifact.

This is the single runtime source for design-versus-engineering routing. The Apple UI Design plugin may create bounded code artifacts when code is the cheapest honest way to validate a design decision, but it is not a general Swift engineering workflow.

## Contents

- Primary owner by requested outcome
- Three implementation levels
- Framework support
- Trigger boundaries
- Completion language

## Choose the Primary Owner by Requested Outcome

| Requested outcome | Primary owner |
|---|---|
| Define or redesign visual direction, a screen, a flow, navigation, a design system, interaction, motion, or a design-led prototype | `$apple-ui-direction` |
| Translate an established product experience between iOS, iPadOS, and macOS | `$apple-platform-adaptation` |
| Critique, audit, validate, or prioritize findings for an existing UI artifact | `$apple-ui-review` |
| Fix compilation, concurrency, state management, persistence, networking, architecture, performance, API usage, tests, CI, packaging, or release | An applicable engineering workflow |

Framework names do not determine ownership. A request about a SwiftUI view can be a design task or an engineering task; the user-visible outcome determines the route.

## Three Implementation Levels

### 1. Design artifact only

Deliver design evidence and a handoff without modifying production code when:

- the user asks for direction, review, specification, or adaptation only;
- the interaction or visual direction is not yet approved;
- project architecture or state contracts are unresolved;
- the available environment cannot verify the affected native behavior;
- production integration would require business logic, data, dependencies, or broad refactoring.

Valid artifacts include rendered screens, flows, state maps, adaptation matrices, component specifications, motion studies, and acceptance criteria.

### 2. Bounded design-led implementation

The design workflow may create or edit code when all of the following are true:

- the user requested a prototype or implementation, not only advice;
- the code directly answers a product, visual, interaction, motion, or accessibility question;
- the change is limited to presentation-layer views, styles, local interaction state, previews, fixtures, or a disposable prototype;
- existing architecture, domain state, persistence, networking, and dependency boundaries remain intact;
- the result can be rendered or run at the evidence level required by the selected delivery contract.

Examples include a focused SwiftUI prototype comparing two navigation models, a bounded view-layer adjustment that applies an already approved design, or representative previews for component states.

Label prototype code as prototype code. Do not imply that a prototype is production integration.

### 3. Engineering workflow required

Route to or pair with an applicable engineering workflow when the work includes:

- compiler errors, language semantics, generics, concurrency, actors, memory, or crashes;
- application architecture, state ownership, navigation infrastructure, dependency injection, persistence, networking, or data migration;
- performance profiling, Instruments, rendering optimization, or launch-time work;
- unfamiliar API correctness, availability implementation, SDK migration, or framework interoperability;
- unit, integration, snapshot, or UI-test infrastructure whose primary purpose is engineering correctness;
- CI, signing, packaging, App Store submission, release, or production deployment;
- production UIKit or AppKit integration beyond a clearly isolated presentation-only change.

If a task mixes design and engineering, keep one primary owner based on the requested final outcome and state the handoff:

- the design skill owns intended experience, visual and interaction decisions, evidence requirements, and acceptance criteria;
- the engineering workflow owns production architecture, correctness, integration, and delivery mechanics.

Do not silently expand a design task into production refactoring. Do not silently discard the design contract because code is involved.

## Framework Support

### SwiftUI

The plugin may inspect SwiftUI projects, create design-led prototypes, and make bounded presentation-layer changes under the conditions above. It must pair with engineering for production architecture, state management, debugging, performance, API correctness, testing infrastructure, packaging, and release.

### UIKit

The plugin may inspect UIKit screens and runtime evidence, define direction, adapt behavior, review outcomes, and deliver framework-aware design specifications. It must not promise SwiftUI implementation for a UIKit codebase or rewrite the product into SwiftUI without an explicit product and engineering decision. Route production UIKit implementation to engineering unless the change is clearly isolated presentation work and the required verification environment exists.

### AppKit

The plugin may inspect AppKit windows and runtime evidence, define macOS interaction and visual decisions, review the experience, and deliver framework-aware specifications. It must not substitute an iOS-shaped SwiftUI mockup for verified AppKit window, command, menu, focus, or multi-window behavior. Route production AppKit integration and API work to engineering.

### Mixed codebases

Inspect the actual target and framework before choosing a prototype medium. Preserve existing product and architecture boundaries. Never infer that a project should migrate frameworks because one framework is easier for the design workflow to generate.

## Trigger Boundaries

Implicitly select a bundled design skill only when the requested outcome clearly matches its design, adaptation, or review contract.

Do not implicitly select the plugin for implementation-only requests concerning:

- Swift compilation or language questions;
- concurrency or performance;
- architecture or state management;
- framework API usage;
- tests, CI, signing, packaging, or release;
- backend, networking, persistence, or data work.

When a prompt is ambiguous, identify the requested outcome from the surrounding project evidence. If the answer would materially change whether the task is design or engineering, ask one focused question. Do not claim a design skill is needed merely because the prompt contains `Apple`, `iOS`, `macOS`, `SwiftUI`, `UIKit`, or `AppKit`.

## Completion Language

Report design and engineering progress independently:

- a design can be aligned while production code remains untouched;
- a prototype can be complete while production integration remains pending;
- code can compile while the intended experience remains unverified;
- engineering verification does not imply user visual acceptance.

State which workflow produced each claim and what evidence supports it.
