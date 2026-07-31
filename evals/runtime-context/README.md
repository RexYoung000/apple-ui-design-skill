# Runtime Context Contract

This suite protects the runtime-context architecture introduced for Issue #10.

It measures only installable instructions that can enter model context:

- `plugins/apple-ui-design/skills/*/SKILL.md`;
- `plugins/apple-ui-design/references/*.md`;
- `plugins/apple-ui-design/references/source-registry.json`.

Repository documentation, evaluations, tests, release history, and `agents/openai.yaml` interface metadata are excluded from the runtime-size metric.

The contract verifies:

- each shared Markdown reference has one explicit `Load When` condition;
- each rule family has one declared runtime owner;
- references longer than 100 lines have a concise `Contents` section;
- every Skill entry remains below 100 lines;
- Skill-entry and total runtime word budgets are respected;
- recorded before-and-after measurements match the actual files;
- source-registry maintenance and other repository-only process text stay outside runtime references;
- two independent product tasks still route to the necessary references without loading unrelated methods.

Run:

```bash
python3 scripts/validate_runtime_context.py
```

The budgets are ceilings, not targets. A smaller file can still fail when it duplicates ownership or removes a behavior protected by the existing regression suites.
