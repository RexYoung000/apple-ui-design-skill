# Authority and Design Principles

Use this reference when project sources disagree, when Apple convention appears to conflict with product identity, or when an implementation shortcut would change the experience.

All bundled skills use this file as their single decision-authority and design-principle source. The layer names and procedures below are a **project-internal method**, not Apple terminology or an Apple-approved framework.

## Decision Layers, Not One Authority Ranking

Do not place unlike inputs into one universal ranking. Resolve each decision by identifying which layer owns it, what evidence informs it, and what remains unverified.

### 1. Hard boundaries

Applicable legal, safety, security, and privacy obligations cannot be silently ignored. Neither can an explicit contractual requirement or a core-experience outcome that the project has marked as required.

When a proposed direction conflicts with a hard boundary:

1. state the exact conflict and affected scope;
2. distinguish verified obligation from interpretation;
3. recommend a compliant path and a way to verify it;
4. stop only the affected work when no safe in-scope path exists.

Apple visual convention, native-component availability, reviewer preference, and implementation convenience are not hard boundaries by themselves.

### 2. Product decision authority

The user or the project’s designated product owner decides intended product outcomes, target users, brand expression, information hierarchy, interaction model, and motion direction. Current authoritative product and design documents carry those decisions until they are explicitly changed.

The skill may challenge a choice with evidence, but it may not silently replace a confirmed decision merely because another pattern is more common on Apple platforms. After the decision-maker understands the material usability, learning, accessibility, platform, or implementation tradeoff and confirms the choice, record it and continue unless a hard boundary remains.

A user-confirmed decision defines intent. It does not become validated user research, erase an observed failure, or prove that the interaction works.

### 3. Experience outcome baseline

Treat the core task being perceptible, understandable, operable, and recoverable for the users and assistive scenarios in scope as an outcome baseline, not as a required visual style.

If a proposal misses that baseline:

- report the affected task and user impact;
- recommend an alternative or equivalent completion path;
- define how the outcome can be tested;
- do not claim the experience or accessibility scenario is verified;
- if the baseline is an explicit project or legal requirement, treat the gap as a hard-boundary conflict;
- otherwise, let the product owner make and record the informed tradeoff.

### 4. Evidence and advice

These inputs inform a product decision but do not own it:

- verified target-user, task, and usage-context evidence;
- current Apple documentation, Human Interface Guidelines, official resources, and observed native behavior;
- shipped product behavior and the existing design system;
- accessibility and localization observations;
- team conventions, architecture, implementation cost, and maintenance constraints;
- external examples, inspiration, and general design taste.

Name the source and the claim it supports. A shipped interface proves what currently exists, not what should survive; a known defect gains no authority from release history. Apple guidance is strong platform evidence and risk-control advice, not ownership of product identity. External inspiration is a hypothesis source, not proof of fit.

## Tradeoff Procedure

For a material disagreement or risky choice, provide:

1. **Observed fact** — what is known and its source;
2. **User or product impact** — who or what may be affected;
3. **Recommendation** — the preferred path and why;
4. **Verification** — the prototype, native run, accessibility path, research, or other evidence that can resolve uncertainty;
5. **Decision** — the product owner’s choice, remaining gap, and revisit trigger.

Risk advice must stay labelled as advice. Do not silently convert it into a product requirement.

When current sources conflict:

1. state the exact conflict and evidence labels;
2. determine whether a current product source explicitly supersedes another;
3. separate intended future behavior from shipped observation;
4. ask for a decision only when the unresolved conflict is path-dependent and material;
5. record the resolution in the appropriate source of truth.

## Rule Levels

Classify guidance before enforcing it:

- **Product principle**: a stable statement about user value, mental model, trust, or brand boundary.
- **Experience baseline**: an outcome that must remain usable, understandable, accessible, and recoverable.
- **Current design decision**: the approved solution for the current version; changeable through explicit design judgment.
- **Platform recommendation**: a strong default supported by Apple conventions; may be adapted with a clear reason.
- **Exploration**: a hypothesis or reference that must not be treated as approved design.

Do not turn a recommendation into a hard law merely because it is easy to test.
Do not turn an accessibility outcome into a visual prescription when the same outcome can be achieved through custom presentation.

## Native and Distinctive

“Apple-native” means the product respects people’s learned operating model:

- navigation and dismissal are predictable;
- controls communicate their behavior;
- system capabilities integrate coherently;
- touch, pointer, keyboard, focus, menus, windows, and assistive technologies work where relevant;
- platform behaviors degrade deliberately across supported versions.

It does not require:

- default system blue;
- a system-app visual identity;
- identical layouts on every platform;
- SF Symbols for every illustration;
- the latest Apple material;
- the absence of custom typography, color, shape, or motion.

A native component is a useful way to inherit behavior, semantics, input handling, and system adaptation. It is not a requirement to keep the component’s default appearance. Custom controls and interactions are valid when they preserve the intended product model and expose the behavior needed by the target users and environments.

Native-experience priority is not native-appearance priority. Prefer reliable platform behavior and verifiable semantics; do not infer that visual conformity is required.

A distinctive product still needs a small set of recognizable decisions tied to its subject and brand. Do not force a “signature detail” when the content and interaction already create identity.

## Decision Test

For a disputed visual or interaction choice, answer:

1. What user or product problem does this solve?
2. Which project fact or confirmed decision supports it?
3. What learned platform behavior does it preserve or intentionally change?
4. Does it still work for required accessibility and localization scenarios?
5. What is the cost of the alternative?
6. How will the choice be verified in the actual interface?

If the only rationale is “it looks Apple-like,” “the framework makes this easy,” or “AI designs usually do this,” the decision is not yet justified.
