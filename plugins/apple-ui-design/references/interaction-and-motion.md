# Interaction and Motion

## Load When

Load this reference when a task creates, materially changes, adapts, prototypes, or reviews interaction or motion. Do not load it for a static visual change with no behavioral consequence.

This is the single runtime source for interaction and motion contracts. The direction skill defines the language, adaptation translates it, and review assesses supplied behavior. This is a project-internal method, not an Apple framework.

## Decision Authority

Classify each rule using `authority-and-principles.md` before changing the experience:

- a hard boundary can stop the affected direction;
- a product principle or confirmed design decision remains user-owned;
- an experience baseline defines an outcome to protect, not a mandatory appearance;
- an Apple convention, native component, shipped pattern, or implementation shortcut is evidence and risk-control advice;
- an exploration remains unapproved until the user selects it.

Do not add a fallback control, remove a gesture, or replace a distinctive interaction solely because a common Apple pattern or native component is easier or more familiar. When a confirmed choice creates material risk, state the observed fact, user impact, recommendation, native verification path, and remaining gap. Record the informed decision and proceed unless a hard boundary remains.

## Interaction Contract

For every material interaction, define the smallest contract that makes the intended experience testable:

1. **Core task** — the user outcome and completion condition.
2. **Objects and states** — what the user acts on, the relevant source and destination states, and persistent state meaning.
3. **Entry and discovery** — where the interaction begins, how its affordance is learned, and whether expert or gestural paths need an equivalent discoverable path.
4. **Inputs** — touch, Pencil, keyboard, pointer, scroll, focus, commands, assistive actions, or other supported input.
5. **Operation model** — direct manipulation, explicit command, gesture, spatial navigation, selection, or another product-specific model.
6. **Feedback and result** — what changes during input, what confirms progress or completion, and what remains perceivable without color or motion alone.
7. **Interruption and reversal** — what happens when input changes, repeats, cancels, or reverses before completion; final settled state must reflect the user’s final intent.
8. **Error and recovery** — invalid input, unavailable results, retry, undo, cancellation, restoration, and protection of user data or progress.
9. **Platform expression** — how the same product meaning responds to screen, window, input, navigation, focus, and learned platform behavior.
10. **Accessibility** — equivalent task completion, semantic role and state, focus order, scalable content, relevant assistive behavior, and system visual or motion settings.
11. **Evidence** — the prototype, native environment, inputs, states, recordings, and remaining unverified claims.

Do not turn the contract into a universal checklist. Include the entries that can change the scoped task, and make omitted high-risk behavior explicit.

## Motion Language

Define motion as part of the interaction and product character, not decoration applied after layout. Capture:

- **character** — calm, precise, elastic, playful, cinematic, restrained, or another product-specific quality;
- **purpose** — functional, spatial, feedback, expressive, brand, or emotional; one motion may serve more than one purpose;
- **input relationship** — direct, continuous, triggered, programmatic, scroll-linked, or system-driven;
- **state logic** — start, progress, completion, cancellation, interruption, reversal, repetition, and final intent;
- **platform expression** — how touch, Pencil, keyboard, pointer, focus, scroll, window changes, and system events affect it;
- **comfort and settings** — how Reduce Motion or other relevant settings preserve task meaning, feedback, and suitable product character;
- **evidence status** — whether values are project values, rendered proposals, measured results, or unverified proposals.

Motion may create delight, identity, anticipation, or emotional pacing even when it does not explain a state change. It still must coexist with task completion, repeated use, user comfort, input latency, interruption, and the claimed performance envelope.

Reduce Motion is a parallel expression, not a blanket animation ban. Reduce large spatial travel, continuous parallax, or disorienting transitions as needed while retaining state, causality, feedback, completion, and appropriate brand meaning.

## Product-Specific Risk Focus

### Tool products

Prioritize speed, precision, repeat input, selection, focus, keyboard and pointer efficiency, undo or redo, interruption, reversal, error recovery, and stable final state. Expressive motion must not make repeated work wait for presentation.

### Content products

Prioritize reading or viewing continuity, place preservation, content hierarchy, navigation predictability, media state, scroll behavior, transition context, and return or restoration. Motion should support orientation without repeatedly competing with the content.

### Experimental interactions

Prioritize discoverability, learnability, feedback during manipulation, limits, cancellation, recovery, equivalent inputs, and evidence from representative users or tasks. Novelty is not a defect by itself, and convention is not permission to replace a confirmed experiment. Keep the learning and failure risk visible until tested.

## Meaningful Exploration

When the interaction or motion direction is unresolved, produce two or three operable hypotheses that differ in actual behavior, such as direct manipulation versus explicit commands, continuous spatial transition versus staged disclosure, or restrained feedback versus expressive transformation.

Do not present recolors, duration-only changes, or different easing curves as separate interaction directions. For each hypothesis, show the core task, interaction contract difference, motion purpose, platform and accessibility impact, risk, and evidence needed for selection.

When direction is already confirmed, extend and test it without manufacturing alternatives. Reopen it only when new evidence, a hard boundary, or a material product conflict warrants a decision.

## Evidence and Acceptance

Use the cheapest artifact that answers the current design question, but limit claims to what it proves:

- a state map or storyboard can specify intended behavior;
- HTML can compare and exercise browser-based hypotheses;
- a successful build establishes implementation integrity only;
- a native prototype can expose real input, layout, focus, timing, interruption, and system-setting behavior;
- a native recording can establish only the exercised environment, path, input, and motion expression;
- user or product-owner confirmation establishes final rhythm and aesthetic acceptance.

For material native motion, preserve a representative recording at normal speed and input conditions. Exercise interruptions, reversals, rapid repeat input, completion, and recovery when they affect the task. Run and record the Reduce Motion expression when motion is in scope. Record platform, OS, device or window, input, system setting, represented states, observed result, and unverified scenarios.

Do not claim native interaction or motion quality from HTML, static frames, a timing table, or compilation. Do not transfer one tool-product recording to content or experimental scenarios it never exercised.
