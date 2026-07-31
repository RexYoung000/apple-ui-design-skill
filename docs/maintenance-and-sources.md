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

## Version-Sensitive Apple Claim Protocol

Treat a conclusion as version-sensitive when it depends on current HIG wording, API or OS availability, deprecation, platform policy, hardware or input behavior, or a newly introduced Apple design language.

Before presenting one of these conclusions as verified:

1. inspect the project’s deployment targets and the environment represented by its runtime evidence;
2. open the exact current Apple page that supports the claim, not only a documentation homepage or search result;
3. record the page title, URL, access date, affected platforms, supported versions, and the exact part of the claim it supports;
4. separate the project’s minimum supported version from any newer enhancement version;
5. define the fallback or state that the capability cannot support the current deployment target;
6. label Apple documentation, project runtime evidence, and design inference separately.

If the exact official source cannot be reached or does not support the claim, mark the conclusion unverified. Do not reconstruct current behavior from memory, quietly substitute a community article, or recommend the newest treatment as a default.

Apple documentation and project runtime evidence answer different questions. Official documentation establishes published availability or guidance; a reproducible project run establishes what the tested build and environment actually did. When they disagree, preserve both records, capture the toolchain and runtime, reduce the claim to what each source proves, and define a reproduction or escalation step. Do not silently treat either the shipped project behavior or an implementation anomaly as a replacement for the published Apple rule.

The installable workflow lives in `plugins/apple-ui-design/references/current-sources.md`. Reviewable verification records and their deterministic validator live under `evals/current-source-verification/` and `scripts/validate_current_source_evals.py`.

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
- generic intake questionnaires that ignore whether questions are blocking, dependent, or independently verifiable.

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

The decision-layer names, evidence labels, delivery contracts, and Project Design Decision Profile in this repository are project-internal methods. Do not present them as Apple terminology, Apple certification, or an official Apple workflow.

The authority model must preserve these distinctions:

- confirmed product decisions own intended product direction;
- experience baselines define what can honestly be claimed, not a mandatory visual skin;
- Apple guidance and native components supply platform evidence and risk controls;
- shipped behavior supplies current-state evidence, including evidence of defects;
- implementation convenience and external inspiration may inform a tradeoff but never silently decide it;
- an informed user choice proceeds unless an applicable hard boundary remains.

## Suggested Regression Prompts

Use realistic prompts to check the skill’s behavior. The fixed product-starting-point suite at `evals/product-starting-point/cases.json` is the repeatable source of truth for the first three branches below; validate its structure with `python3 scripts/validate_product_starting_point_evals.py`.

The plugin split and independent invocation evidence lives under `evals/plugin-split/runs/`.
The six mode-level delivery contracts live in `evals/delivery-contracts/cases.json`; validate their structure with `python3 scripts/validate_delivery_contract_evals.py`.
Trigger ownership and engineering boundaries live in `evals/trigger-routing/cases.json`; validate their structure with `python3 scripts/validate_trigger_routing_evals.py`.
The release-level trigger and output matrix lives in `evals/skill-regression/cases.json`. Run the complete deterministic gate with `python3 scripts/run_regression_checks.py`.
The decision-authority contract lives in `evals/decision-authority/cases.json`; validate it with `python3 scripts/validate_decision_authority_evals.py`.
The current-source contract and preserved version-sensitive records live under `evals/current-source-verification/`; validate them with `python3 scripts/validate_current_source_evals.py`.
The accessibility and localization contract lives under `evals/accessibility-localization/`; validate it with `python3 scripts/validate_accessibility_localization_evals.py`.

## Accessibility and Localization Source Review

Issue #7 was reviewed against exact Apple pages on 2026-07-30. Keep the stable task-outcome method in `plugins/apple-ui-design/references/accessibility-and-localization.md`; recheck version-sensitive wording and API availability through the current-source protocol.

| Apple page | Claim supported | Maintenance note |
| --- | --- | --- |
| `https://developer.apple.com/design/human-interface-guidelines/accessibility` | Current contrast guidance, non-color meaning, VoiceOver, Voice Control, mobility-related assistive technologies, Full Keyboard Access, Switch Control, and Reduce Motion | Recheck numeric thresholds and named technologies when Apple updates the page |
| `https://developer.apple.com/design/human-interface-guidelines/right-to-left` | Directional mirroring, paragraph alignment, navigation, numbers, logos, and universal symbols | Keep real-language testing in addition to pseudolanguages |
| `https://developer.apple.com/documentation/xcode/testing-localizations-when-running-your-app` | Run every supported language and region; App Language and App Region are independently selectable | Record the combinations actually run |
| `https://developer.apple.com/documentation/xcode/preparing-your-interface-for-localization` | Xcode nonlocalized-string diagnostics and Double-Length, RTL, Accented, Bounded String, and Tall pseudolanguages | Pseudolanguages are structural evidence, not linguistic acceptance |
| `https://developer.apple.com/documentation/xcode/localizing-strings-that-contain-plurals` | Language-specific plural variants and string-catalog handling | Do not reduce plural validation to English singular versus plural |
| `https://developer.apple.com/videos/play/wwdc2023/10153` | Foundation grammatical agreement guidance | Treat the WWDC year and API availability as version-sensitive |
| `https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducetransparency` | Reduce Transparency should make mainly window backgrounds opaque | Preserve hierarchy and meaning rather than merely removing material |
| `https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/performaccessibilityaudit(for:_:)` | XCTest automated accessibility audits | An automated audit is not a VoiceOver or other assistive-technology run |
| `https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice` | Programmatic VoiceOver testing is published as Beta for OS 27.0+ | Xcode 26.6 with iOS 17.5/26.5 cannot use this as runtime evidence |

The maintained evidence boundary is:

1. design review can establish intended alternatives and layout behavior;
2. semantic inspection and automation can establish what the tested build exposes;
3. only a named assistive-technology run can establish end-to-end operation with that technology.

Never turn one layer into a broader completion claim. Preserve unavailable runtime scenarios as explicit acceptance work rather than filling the gap with labels or audit output.

For Issue #7, the product owner accepted the method, source review, deterministic suite, semantic audit, and recorded Reduce Motion task as sufficient to close the method-development scope on 2026-07-31. That product decision does not change the evidence boundary: the preserved Stillpoint run remains explicitly unverified for VoiceOver, and a future VoiceOver or broader assistive-technology completion claim still requires a named end-to-end run in a supported environment.

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
2. Major existing-product redesign — must expose material evidence conflicts and ask one focused question only when a blocking decision changes the next path.
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
