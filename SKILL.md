---
name: apple-ui-design
description: Legacy explicit-invocation compatibility router for the former standalone Apple UI Design skill. Use only when the user explicitly invokes $apple-ui-design from an older standalone checkout; route the request to the matching bundled workflow. Do not invoke implicitly for new Apple UI tasks.
---

# Apple UI Design Legacy Router

This root skill exists only to migrate older standalone installations. The installable plugin exposes three focused skills instead.

## Route

Choose one primary workflow:

- Product or visual direction, screen, flow, design system, interaction or motion concept, or design-led prototype: read and follow `plugins/apple-ui-design/skills/apple-ui-direction/SKILL.md`.
- Adapt an established experience between iOS, iPadOS, and macOS: read and follow `plugins/apple-ui-design/skills/apple-platform-adaptation/SKILL.md`.
- Critique, audit, validate, or prioritize findings for an existing artifact: read and follow `plugins/apple-ui-design/skills/apple-ui-review/SKILL.md`.

For a mixed request, let the requested final outcome determine the primary workflow and read another workflow only when its distinct contract is necessary.

Tell the user the new skill name once in the handoff. Do not force migration before completing the current explicitly invoked task.

Route Swift architecture, state management, debugging, performance, CI, packaging, and release work to an applicable engineering workflow. The Apple UI plugin owns product and interface decisions, not general engineering.

## Migration

Recommend installing the Plugin from the public repository and replacing future `$apple-ui-design` calls with:

- `$apple-ui-direction`
- `$apple-platform-adaptation`
- `$apple-ui-review`

Do not claim that this compatibility router is bundled in the Plugin. It is source-checkout support for the earlier standalone installation only.
