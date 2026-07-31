# Delivery Contracts and Evidence Gates

## Load When

Load this reference at the start and end of every activated Apple UI design task. Select one primary contract, use its artifact and evidence gate to plan the work, and limit completion claims to the evidence actually produced.

This is the single runtime source for delivery artifacts and evidence gates.

## Contents

- Shared evidence rules
- Contract selection
- Visual Direction
- Screen or Flow
- Design System
- Platform Adaptation
- Native Prototype
- UI Review

## Shared Evidence Rules

Inspect project evidence before proposing work. Keep user-confirmed decisions, project facts, external evidence, design inference, and unvalidated hypotheses distinct. Do not make the user repeat facts that can be verified locally.

Every task selects one primary contract. Supporting artifacts may use another contract, but their completion criteria remain separate.

### Exact values

Treat exact visual values as one of:

- existing project tokens or measured values;
- values visible in a rendered artifact;
- proposed values explicitly awaiting visual acceptance.

Do not present an unrendered number as polished or approved design. Prefer semantic roles over disconnected constants.

### Cross-cutting scope

When interaction or motion is material, apply `interaction-and-motion.md`. When content, consent, protected access, account data, purchase, deletion, recovery, or professional meaning is material, apply `content-and-sensitive-flows.md`. Apply the accessibility and localization scenarios that can affect the core task or completion claim.

Rendered content can establish hierarchy and visible control. Mocked permission, authentication, service, data, commerce, or professional behavior cannot establish native operation, service completion, policy compliance, or expert approval.

### Evidence gates

| Claim | Minimum evidence |
| --- | --- |
| Visual direction is visible | Rendered screen or canvas with representative content |
| Screen or flow is operable | Exercised interactive prototype or running implementation |
| Design system is usable | Rendered representative states and a real product application |
| Platform layout is adapted | Visible evidence at each material size or window state |
| Platform behavior works | Native run in each claimed environment and input path |
| Interaction or motion works | Representative-speed native run; recording for behavior or quality claims |
| Accessibility semantics exist | Inspection or automation of the represented build |
| Assistive technology works | Named end-to-end run for that technology and task |
| Sensitive system or service flow works | Matching native, sandbox, service, or professional evidence |
| Experience is accepted | User confirmation after inspecting the actual result |

A build does not prove a usable interface. A screenshot does not prove interaction. HTML does not prove Apple-native behavior. Earlier evidence never implies a later completion stage.

Use only these completion stages: **direction aligned**, **design complete**, **prototype complete**, **code complete**, **experience verified**, and **user accepted**.

## Contract Selection

| Requested outcome | Primary contract |
| --- | --- |
| Establish or compare visible product expression | Visual Direction |
| Define and exercise a stateful task | Screen or Flow |
| Define reusable tokens and components | Design System |
| Translate an established product across Apple platforms | Platform Adaptation |
| Validate scoped behavior in an Apple runtime | Native Prototype |
| Assess an existing artifact and prioritize findings | UI Review |

## Contract 1: Visual Direction

**Required artifact**

- rendered key screens with representative content;
- two or three visibly meaningful alternatives when direction is unresolved;
- comparison against the confirmed product goal and an exact acceptance path.

Alternatives must differ in hierarchy, composition, product emphasis, interaction stance, or visual language, not only color, font, duration, or easing.

**Evidence gate**

Rendered artifacts support visible comparison. Direction becomes aligned only after the user selects or combines an option. Static work does not verify native behavior.

## Contract 2: Screen or Flow

**Required artifact**

- state and transition map for the scoped task;
- an operable happy path and material non-happy paths;
- representative content, inputs, feedback, cancellation, failure, and recovery;
- exact user acceptance steps.

When sensitive decisions are present, include consequential content, informed choices, system boundaries, decline or defer behavior, and honest recovery.

**Evidence gate**

Exercise the scoped path and preserve the observed result. Static screens prove appearance only. Record mocked system, service, policy, and professional behavior as unverified.

## Contract 3: Design System

**Required artifact**

- product principles and shared design DNA in scope;
- semantic tokens linked to existing or rendered evidence;
- component intent, anatomy, states, interaction, accessibility, and platform variation;
- rendered representative states and at least one real product screen using the system.

**Evidence gate**

A token table or isolated swatches do not complete a design system. Show realistic content, state combinations, content expansion, and the product context the system must support.

## Contract 4: Platform Adaptation

**Required artifact**

- source and target platform scope;
- shared-versus-platform-specific decision matrix;
- representative layouts for each material size or window state;
- navigation, input, focus, command, continuity, accessibility, and fallback behavior in scope.

**Evidence gate**

Rendered layouts establish visible adaptation. Native runs establish only the exercised window, input, focus, command, system, or continuity behavior. Do not infer platform completion from an enlarged phone layout.

## Contract 5: Native Prototype

**Required artifact**

- runnable, narrowly scoped Apple-platform prototype;
- representative states, content, semantics, fallback, failure, and recovery;
- standard and Reduce Motion behavior when motion is present;
- validation record naming environment, path, observed result, and mocked boundaries.

**Evidence gate**

Use SwiftUI Preview, Simulator or device, or a real macOS app as appropriate. Preserve recordings for material interaction or motion claims. Compilation alone proves neither behavior nor experience quality, and prototype completeness does not imply production integration.

## Contract 6: UI Review

**Required artifact**

- review scope and evidence statement;
- actionable findings ordered by Blocking, Important, and Optimization;
- observed fact, user impact, evidence, recommendation, and verification for each finding;
- missing scenarios and concise user acceptance path.

**Evidence gate**

Limit findings to the supplied artifact and represented states. Text-only input supports unverified consultation. A screenshot supports visible facts, a recording supports shown behavior, and native or service evidence supports only the exercised environment and path. If no actionable findings exist, say so without inventing issues.
