# Authority and Design Principles

Use this reference when project sources disagree, when Apple convention appears to conflict with product identity, or when an implementation shortcut would change the experience.

All bundled skills use this file as their single authority and design-principle source.

## Authority Order

Resolve decisions in this order unless the project explicitly defines a stronger order:

1. Confirmed product, interaction, and motion decisions.
2. Current repository instructions and authoritative product/design documents.
3. Verified target-user, task, and usage-context evidence.
4. Established UI behavior and design system in the shipping product.
5. Accessibility, localization, privacy, safety, and interaction outcomes that the project requires.
6. Current Apple platform guidance and native behavior.
7. Team conventions and implementation patterns.
8. External examples, inspiration, and general design taste.

Historical screenshots, archived documents, concept prototypes, and competitor behavior are evidence, not authority.

User authority determines intended product direction. It does not convert a hypothesis into validated user need, erase an observed accessibility failure, or prove that an interaction works. When a decision carries a material risk, state the fact, impact, recommendation, and validation method. After the user understands the tradeoff, preserve their decision unless it conflicts with a higher legal, safety, or explicit project requirement.

When two authoritative sources conflict:

1. state the exact conflict;
2. determine whether one source is newer or explicitly higher priority;
3. stop only the affected work;
4. ask one decision question if the conflict cannot be resolved from the project;
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
