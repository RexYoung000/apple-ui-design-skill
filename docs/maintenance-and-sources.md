# Repository Maintenance and Current Sources

Use this repository document when updating the plugin, checking a version-sensitive rule, or adding a new Apple platform capability.

It is intentionally excluded from the installable package. Runtime source-selection rules live in `plugins/apple-ui-design/references/current-sources.md`.

## Stable vs Changeable Knowledge

Keep stable knowledge in this repository:

- product intent before implementation;
- local source-of-truth precedence;
- brand DNA and platform behavior as separate concerns;
- accessibility and localization as design inputs;
- evidence-based review;
- honest completion language;
- risk-based validation.

Verify changeable knowledge at task time:

- current Human Interface Guidelines;
- OS availability and deployment support;
- SwiftUI API behavior and deprecations;
- new platform materials and interaction capabilities;
- App Store or platform policy;
- current device and input behavior.

Do not freeze volatile API tables into the core skill unless they are actively maintained and version-labelled.

## Source Priority

For current Apple behavior:

1. Apple Developer documentation.
2. Apple Human Interface Guidelines.
3. Apple sample code and official design resources.
4. WWDC sessions and transcripts.
5. The project’s verified runtime behavior.
6. High-quality community sources only when official material is insufficient.

For product behavior, the project’s current authoritative documents and confirmed user decisions outrank external convention.

When using current web information, cite the exact official page near the claim. Distinguish source-backed facts from design inference.

Primary entry points:

- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Apple Design Resources: https://developer.apple.com/design/resources/
- SwiftUI documentation: https://developer.apple.com/documentation/swiftui/
- Apple Developer videos: https://developer.apple.com/videos/

Treat these as entry points, not as permission to apply every newest treatment. Resolve current platform guidance against the project’s minimum versions and confirmed product intent.

## Hybrid Source Registry

Use `plugins/apple-ui-design/references/source-registry.json` as the curated starting set and `plugins/apple-ui-design/references/research-and-source-evidence.md` as the research and claim-labeling method.

- Keep stable official entry points and selected public sources in the registry.
- Search live for the actual product, target user, platform, and design question.
- Use shipped products as observable precedent, not universal validation.
- Mark Web, marketing, art, and implementation references as `inspiration only`.
- Translate external inspiration through the approved product model and verify claimed Apple behavior in a native environment.
- Prefer public, no-account sources; use public previews of limited sources only when they add unique evidence.
- Do not package third-party screenshots or assets without verified reuse rights.

The registry is a map, not a frozen archive or a ranking. Run `python3 scripts/validate_source_registry.py` after changing it.

## Comparative Sources Behind This Skill

This skill was synthesized after comparing several design and SwiftUI skills. Revisit them when maintaining the corresponding area:

- `frontend-design`: subject-specific visual direction, typography, structural identity, and avoiding generic template output.
- `design-dna`: separating measurable design systems, qualitative style, and effects.
- `huashu-design`: context and asset inspection, visible direction hypotheses, iterative review, and rendered evidence.
- [Wholiver/swiftui-design-skill](https://github.com/Wholiver/swiftui-design-skill): context-first direction exploration, brand assets, anti-template critique, and design review.
- [wshobson/agents](https://github.com/wshobson/agents) `mobile-ios-design`: platform conventions, responsive layout, accessibility, and native behavior.
- [dpearson2699/swift-ios-skills](https://github.com/dpearson2699/swift-ios-skills): accessibility and SwiftUI implementation depth.
- [twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill): modern SwiftUI code review and technical quality boundaries.
- [AvdLee/SwiftUI-Agent-Skill](https://github.com/AvdLee/SwiftUI-Agent-Skill): version gating, macOS coverage, localization, and trace-driven engineering workflows.

Do not copy their rules wholesale. In particular, this skill intentionally rejects:

- universal bans on colors, gradients, fonts, cards, glass, or system controls;
- mandatory serif or accent choices;
- a fixed spacing grid as a product principle;
- defaulting all new work to the newest OS;
- treating HIG as the owner of product identity;
- folding broad architecture, performance, and Instruments work into UI design;
- arbitrary numeric design scores;
- batch questionnaires when one material decision at a time is clearer.

## Updating This Plugin

When Apple introduces a new design language or platform capability:

1. determine whether it changes a stable principle or only platform expression;
2. identify supported OS versions and fallback behavior;
3. update the smallest relevant reference;
4. avoid making a new visual treatment the default without product justification;
5. add or revise realistic test prompts;
6. run structural validation;
7. inspect the diff for accidental rule conflicts;
8. version the change in Git with a concrete commit message.

## Conflict Audit

Before releasing an update, check for contradictions involving:

- project intent vs HIG;
- minimum version vs recommended API;
- native behavior vs brand expression;
- shared DNA vs platform-specific adaptation;
- accessibility outcome vs fixed visual prescription;
- design authority vs engineering convenience;
- prototype evidence vs completion claim.

Prefer a decision procedure over adding another absolute rule.

## Suggested Regression Prompts

Use realistic prompts to check the skill’s behavior. The fixed product-starting-point suite at `evals/product-starting-point/cases.json` is the repeatable source of truth for the first three branches below; validate its structure with `python3 scripts/validate_product_starting_point_evals.py`.

The plugin split and independent invocation evidence lives under `evals/plugin-split/runs/`.
The six mode-level delivery contracts live in `evals/delivery-contracts/cases.json`; validate their structure with `python3 scripts/validate_delivery_contract_evals.py`.
Trigger ownership and engineering boundaries live in `evals/trigger-routing/cases.json`; validate their structure with `python3 scripts/validate_trigger_routing_evals.py`.
The release-level trigger and output matrix lives in `evals/skill-regression/cases.json`. Run the complete deterministic gate with `python3 scripts/run_regression_checks.py`.

The unified matrix must contain exactly five scenario types for each bundled skill:

1. **direct** — explicitly names the intended workflow or outcome;
2. **indirect** — expresses the same product goal without a skill name;
3. **incomplete** — withholds evidence that would materially change the result;
4. **negative** — is an implementation-only engineering request that must not load a bundled design skill;
5. **risk** — invites unsupported version, asset, runtime, accessibility, or completion claims.

Each case must include fixed fixture paths, required and forbidden skill loads, required output-pattern groups, forbidden output patterns, and human-readable behavior assertions. Do not pass the patterns or assertions to the live model.

`evals/skill-regression/goldens.json` protects reviewed high-quality outputs with SHA-256 checksums. Changing a golden is an explicit review action: update the content, rerun its case evaluator, review the diff, then update the checksum. Do not automatically rewrite golden outputs from a live model run.

GitHub Actions runs deterministic validators, golden checks, and unit tests. It intentionally does not call Codex or any online model. To assess a model or prompt change, save the raw JSONL trace and final response from a fresh session and run:

```bash
python3 scripts/evaluate_skill_regression_output.py \
  <case-id> --trace <trace.jsonl> --output <output.md>
```

Each trigger-routing case must identify:

- whether it is a positive design intent, an implementation-only negative, or a mixed boundary;
- the requested user-visible outcome rather than relying on framework keywords;
- one expected primary route;
- any allowed supporting route;
- the permitted implementation scope;
- required routing behavior and forbidden promises.

The suite must cover each bundled design skill, pure Swift compilation and concurrency, performance and architecture, API questions, CI or release, UIKit, AppKit, bounded SwiftUI view work, and mixed design-engineering handoffs. Keep implicit invocation enabled only while fresh-session tests show that these negative engineering prompts do not load a bundled design skill.

Each delivery-contract case must identify:

- one primary contract and owning skill;
- existing-product or zero-to-one starting point;
- task-local fixture evidence;
- the user-visible artifact that must be produced;
- evidence required for the strongest allowed completion claim;
- claims that remain forbidden without additional rendering, operation, or native execution;
- one preserved raw forward-test result.

Do not pass the assertions or desired result to the forward-test agent. A contract passes only when the response produces or explicitly stops for the missing artifact instead of substituting polished prose.

1. Small existing-product adjustment — must reuse verified user and interaction facts without forcing a new intake.
2. Major existing-product redesign — must expose material evidence conflicts and ask only the highest-impact unresolved question.
3. Zero-to-one direction — must show evidence status and hypotheses before committing to a direction.
4. “Make this iPhone app work on Mac” — must ask or infer product differences, not stretch the layout.
5. “Use the newest Apple glass style” — must check minimum versions and product fit.
6. “Give me three visual options” — must create meaningful hypotheses rather than recolors.
7. “Review this screen” — must use evidence and severity, not arbitrary scores.
8. “Implement this approved design” — must preserve project architecture and route technical concerns appropriately.
9. “Make it accessible” — must explain task outcomes, not only add labels.
10. “The project has no minimum version” — must help decide rather than silently choose.

## Scope Expansion

The current scope is iOS, iPadOS, and macOS. Add watchOS, visionOS, tvOS, or other platforms only after:

- confirming user need;
- studying their distinct product and interaction model;
- adding platform-specific references;
- extending validation evidence;
- testing cross-platform ambiguity prompts.

Do not advertise unsupported platforms in the frontmatter until the reference and validation coverage exists.
