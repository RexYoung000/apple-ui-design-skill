# Accessibility and Localization

Use this reference during design, implementation, and review. Accessibility is a product outcome, not a final annotation pass.

This is a shared plugin reference; each workflow applies only the checks relevant to its own outcome.

## Core Standard

A user relying on the assistive behaviors in scope must be able to:

- understand the screen and current state;
- locate and operate the primary action;
- complete the core task;
- identify errors and recover;
- understand destructive consequences;
- perceive progress, selection, and completion.

The visual implementation may vary. The outcome may not disappear.

Accessibility constrains task outcomes, not brand expression. Native components often inherit useful semantics, but custom typography, color, shape, motion, controls, and interaction models remain valid when the required users can perceive, understand, operate, and recover from them.

## Information and Color

- Do not use color as the only indicator of state, category, error, or progress.
- Pair important color changes with text, shape, iconography, position, or accessible semantics.
- Check contrast in actual backgrounds, materials, disabled states, overlays, charts, and selections.
- Preserve hierarchy in increased contrast and appearance modes that are in scope.

## Text and Content Expansion

- Use scalable semantic text roles unless the content is genuinely fixed-format.
- Test accessibility text sizes relevant to the task.
- Allow multiline text where truncation would hide meaning.
- Avoid fixed-height containers around user-visible text.
- Test realistic long names, large amounts, dates, validation messages, and translated strings.
- Keep critical actions reachable when content reflows.

Touch target guidance describes reliable hit areas, not mandatory visible control dimensions. Expand interaction regions without distorting hierarchy when appropriate.

## VoiceOver

- Give controls a meaningful name, role, value, state, and hint only when needed.
- Group visual fragments into a coherent accessible element when they express one concept.
- Do not make decorative assets noisy.
- Ensure custom controls expose the same meaning and action as their visual behavior.
- Announce important asynchronous state changes when the user otherwise cannot perceive them.
- Preserve a logical reading and navigation order after responsive layout changes.

## Motion

- Motion should explain change, preserve context, confirm action, or express brand character.
- Avoid motion that competes with the task or obscures state.
- Under reduced motion, preserve meaning using cross-fades, state changes, or reduced distance/intensity as appropriate.
- Do not remove required feedback merely by disabling all animation.
- Preserve suitable brand character under reduced motion through color, timing, fades, state changes, haptics, audio, or reduced distance and intensity where appropriate.

## iOS and iPadOS

When relevant, validate:

- touch target reliability and gesture alternatives;
- VoiceOver order, actions, and modal focus;
- Dynamic Type reflow;
- hardware keyboard and pointer on iPad;
- orientation or window-size changes;
- system keyboard, input accessories, and error recovery.

Do not make an essential action gesture-only without an accessible alternative.

## macOS

When relevant, validate:

- complete keyboard path and visible focus;
- logical tab order and default action;
- menu and command discoverability;
- shortcut conflicts and standard expectations;
- VoiceOver grouping and navigation;
- pointer, hover, selection, context menus, and drag alternatives;
- window resizing and focus restoration.

## Localization

- Use project localization systems; do not hardcode user-visible strings in implementation.
- Format currency, number, date, duration, measurement, and lists using locale-aware APIs.
- Do not manually concatenate translated sentence fragments.
- Account for right-to-left layout when the target locales require it.
- Provide translator context for ambiguous strings.
- Avoid embedding important text in raster images.
- Treat pseudo-localization and long-content testing as layout evidence, not optional polish.

## Review Evidence

For issues, describe the failed task rather than citing a checklist alone.

Prefer:

> At the largest supported text size, the confirmation action is pushed below an unscrollable container, so the task cannot be completed.

Avoid:

> Fails Dynamic Type.

Include the affected platform, state, content conditions, and a concrete way to re-test.
