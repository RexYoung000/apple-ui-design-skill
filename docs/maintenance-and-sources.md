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

Schema 2 adds a non-empty, overlapping `design_domains` list using `ui`, `ux`, `interaction`, `motion`, and `terminology`. Keep category, access, platform, allowed use, reuse status, checked date, and curation status as separate facts. Excluded entries must retain excluded category/status, `allowed_uses: ["none"]`, and `reuse_status: "do-not-use"`.

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

## Design Quality Update — 2026-10-02

The approved update keeps UI Direction, Platform Adaptation, and UI Review as the three public workflows. UI, UX, interaction, and motion are overlapping quality lenses inside those workflows, not four new Skills. Accessibility, localization, content, design-system consistency, platform adaptation, and evidence remain shared concerns.

Implementation scope:

- Map each quality lens to observable criteria, its existing method owner, an appropriate reference layer, and a representative acceptance task. Scope checks to the requested outcome; small changes do not acquire a full product-discovery process.
- Strengthen UI standards with examples of hierarchy, legibility, real content, component states, and content/window adaptation. Separate confirmed project choices, experience baselines, and current platform guidance; do not prescribe a universal font, grid, palette, aesthetic, or numeric score.
- Translate informal descriptions into candidate component, interaction, or motion terms only when this changes the decision. Preserve product language, explain ambiguous alternatives by their behavior, and verify target-platform names/APIs separately.
- Organize source selection by design domain and evidence purpose. Add only selected UX, component-comparison, and terminology sources; preserve access, reuse, and Apple-native evidence limits. Directory/introduction inspection is not specific-case observation, code validation, or reuse permission.
- Reuse existing shared references rather than copying methods into every Skill. Keep the 2,500-word Skill-entry and 17,500-word total runtime ceilings; additions must be offset by removing redundancy, not raising limits.
- Validate the packaged and portable distributions, registry metadata and context contract, then run independent isolated tasks against the revised source. Retain actual outputs and inspected artifacts; distinguish structural checks, agent behavior, browser evidence, native evidence, and Rex's final acceptance.

This update does not publish to a plugin directory, add telemetry, adopt a component library, change production architecture, or close Roadmap #12. The three original end-to-end acceptance items remain open until the matching experience and user acceptance evidence exists. Verification results are recorded below.

### Implementation and verification result

Version 0.1.1 adds the four-lens acceptance map, six observable UI criteria, five informal-term mappings, and question/domain-based source selection. It retains the three public workflows and thirteen shared Markdown references. NN/g heuristics, Component Gallery, and NameThatUI are selected additions; current-source and reuse boundaries remain explicit.

The complete deterministic gate passed 108 unit tests, all validators and saved goldens, plus generated portable folder/ZIP checks. All three Skill-creator quick validations passed. The [independent forward run](../evals/design-quality/runs/2026-10-02/README.md) retains four requests, actual outputs, source review, browser observations, screenshots, and checksums. Browser checks covered FieldNote failure/retry/draft/focus and OrbitCut compact/wide layout, pointer/keyboard range adjustment, invalid input, cancellation, undo, and export-boundary focus. They establish only the exercised browser paths.

No native iPhone/iPad/Mac run, motion recording, named assistive-technology task, real media preview/export, or user acceptance was performed for this update. These remain explicit acceptance work; Roadmap #12 stays open. Historical native and evaluation evidence was preserved rather than relabelled.

## Public Interface Metadata and Examples

Issue #11 treats the plugin card, Skill selectors, starter prompts, and README examples as one public product surface. Their job is to explain the three workflow boundaries and the strongest evidence each example actually supports; they must not advertise production engineering, native verification, or user acceptance that the underlying artifact has not earned.

The public visual identity uses an original multi-surface and evidence-focus motif rather than an Apple logo, SF Symbol, copied app icon, or third-party artwork. `#007A6E` is the shared brand color. Its contrast is approximately 5.24:1 against white and 4.01:1 against black, so the accent remains distinguishable on both light and dark plugin surfaces. Each bundled Skill uses a related but distinct icon for direction, platform adaptation, and review. The legacy compatibility router is not a public bundled Skill and does not receive new promotional metadata.

Maintain these metadata rules:

1. each bundled `agents/openai.yaml` includes a user-facing name, a 25–64 character short description, small and large local icon paths, the shared brand color, a one-sentence starter prompt that explicitly names its `$skill`, and the explicit implicit-invocation policy;
2. the plugin manifest names the same three capabilities without implying production Swift ownership, and exposes at most three short starter prompts mapped one-to-one to direction, adaptation, and review;
3. plugin icons, light and dark logos, and screenshots resolve to files inside the installable package; repository evaluation material is not pulled into the installed runtime by path;
4. the English and Simplified Chinese READMEs preserve the same workflow order, artifact type, evidence label, limitations, and source links even when prose is localized rather than translated literally;
5. public examples come from preserved repository runs, identify whether the artifact is a design, operable prototype, code, or review/validation result, and link to their full evidence boundary;
6. screenshots may present or crop a preserved result for browsing, but presentation work must not upgrade its completion claim.

The initial public examples are the Today visual-direction comparison, the OrbitCut iPhone-to-iPad-and-Mac adaptation, and the LedgerDesk macOS UI review. They intentionally cover all three bundled Skills. The Today and OrbitCut images support rendered visual or layout decisions only. The LedgerDesk result is a text-evidence review with two prioritized findings and explicitly does not claim visual or runtime validation.

Run `python3 scripts/validate_public_interface.py` whenever public metadata, assets, starter prompts, or either README changes. The validator checks asset paths and PNG signatures, prompt routing, description length, brand-color contrast, manifest boundaries, three-workflow example parity, links back to preserved evidence, and the three-scenario first-use record under `evals/public-interface/`. It supplements rather than replaces the plugin-creator validator and the complete regression gate.

## Portable Agent Skill Distribution

The Codex Plugin and the portable Agent Skill are two distributions of the same product, not separate method forks.

- Keep the three bundled Plugin Skills and `plugins/apple-ui-design/references/` as the canonical runtime sources.
- Generate the portable `apple-ui-design` package at build time. Do not commit copied runtime references as a second editable source tree.
- Expose one portable Skill that routes UI direction, platform adaptation, and UI review internally. Keep the three separate Plugin Skills for the richer Codex installation surface.
- Use only Agent Skills-standard frontmatter in the portable entry. Keep `agents/openai.yaml`, `.codex-plugin`, marketplace metadata, invocation policy, and other client-specific fields out of the portable package.
- Rewrite every workflow reference to a package-root-relative `references/...` path and reject any path that escapes the generated package.
- Include `SKILL.md`, generated workflow references, shared runtime references, and `LICENSE` only. Do not package repository README files, tests, evaluations, CI files, or maintenance documentation.
- Produce both `dist/apple-ui-design/` for SkillPay folder upload and `dist/apple-ui-design.zip` for ZIP upload. `SKILL.md` must be at the root of each artifact, and the ZIP must remain below SkillPay's 20 MB per-file limit.
- Describe the SkillPay product as a paid convenience distribution of the public MIT project. Do not imply encryption, exclusivity, private source access, or functionality that differs from the generated artifact.

Run the portable validator after every workflow, reference, license, packaging, or portable-entry change. The complete deterministic regression gate must build and validate the portable artifact in addition to protecting the Codex Plugin.

## Runtime Context Architecture

Issue #10 separates repository maintenance from instructions needed during a product task. The installable runtime path contains only the three `SKILL.md` entry files, shared Markdown references, and `source-registry.json`. Repository comparison notes, creation history, evaluation fixtures, release procedures, and source-registry maintenance belong in this document or under `evals/`, never in a runtime reference.

Use three disclosure levels:

1. Skill metadata decides whether one focused workflow should activate.
2. The selected `SKILL.md` keeps only role, core workflow, reference routing, output, and hard evidence boundaries.
3. A shared reference loads only when its opening `Load When` condition matches the current task.

Every stable rule has one runtime owner. Skill entry files route to that owner instead of restating its detailed method. Each reference must state both the condition that loads it and the rule family it owns. Markdown references longer than 100 lines must include a concise `Contents` section near the top.

The runtime-context contract lives under `evals/runtime-context/`. Its validator measures the installable instruction files, rejects missing or duplicate ownership markers, verifies explicit load conditions, requires browseable long references, and enforces budgets without counting repository-only documentation or evaluation records.

### Pre-optimization baseline

Measured on 2026-07-31 before Issue #10 changes with whitespace-delimited words and physical lines:

| Runtime group | Files included | Lines | Words | Bytes |
| --- | --- | ---: | ---: | ---: |
| Skill entry instructions | `plugins/apple-ui-design/skills/*/SKILL.md` | 324 | 3,382 | 26,535 |
| Shared references | `plugins/apple-ui-design/references/*.md` and `source-registry.json` | 2,186 | 15,701 | 118,476 |
| Total | Both groups above | 2,510 | 19,083 | 145,011 |

The first optimization budget is at most 2,500 Skill-entry words and at most 17,500 total runtime words. These are regression ceilings, not writing targets: a future change may stay below them only when every added instruction still has a unique owner and task-specific loading reason.

### Issue #10 result — 2026-07-31

Measured after the Issue #10 implementation on the same date and with the same method:

| Runtime group | Lines | Words | Bytes | Word reduction |
| --- | ---: | ---: | ---: | ---: |
| Skill entry instructions | 200 | 2,194 | 17,658 | 35.1% |
| Shared references | 2,132 | 15,263 | 114,653 | 2.8% |
| Total | 2,332 | 17,457 | 132,311 | 8.5% |

The larger reduction is intentionally concentrated in always-loaded Skill entry files. Shared references changed less because their detailed methods remain useful when a matching condition loads them. The fixed trigger, output, delivery, authority, source, accessibility, interaction, and sensitive-flow regression suites all retained their prior pass result after the reduction.

### Current quality update — 2026-10-02

Measured with the same method; the 2026-07-31 results above remain historical:

| Runtime group | Lines | Words | Bytes |
| --- | ---: | ---: | ---: |
| Skill entry instructions | 166 | 1,621 | 13,822 |
| Shared references | 2,105 | 15,676 | 121,290 |
| Total | 2,271 | 17,297 | 135,112 |

The original 2,500/17,500 ceilings remain unchanged. The contract's measurement date is a validated ISO calendar date; exact current measurements are checked against files rather than frozen to an earlier release date.

### Reference loading and ownership

Maintain these boundaries:

| Runtime source | Load only when | Owns |
| --- | --- | --- |
| `authority-and-principles.md` | sources, product authority, hard boundaries, or platform convention materially conflict | decision authority and tradeoff resolution |
| `context-and-alignment.md` | the product start, user/task evidence, major scope, or a path-dependent decision is unresolved | starting-point and evidence-label procedure |
| `engineering-routing.md` | code, framework delivery, production integration, or implementation ownership is in question | design-versus-engineering routing |
| `delivery-contracts.md` | every activated design task, to select the artifact and completion evidence | delivery artifact and evidence gates |
| `apple-platform-adaptation.md` | more than one Apple platform or platform-specific behavior affects the result | cross-platform translation method |
| `design-system-and-dna.md` | visual direction, tokens, components, DNA, observable UI quality, or a material terminology ambiguity is in scope | visual-system, UI-criteria, and candidate-term method |
| `interaction-and-motion.md` | interaction or motion is created, changed, adapted, prototyped, or reviewed | interaction and motion contracts |
| `accessibility-and-localization.md` | an accessibility, localization, input, content-expansion, or assistive scenario affects the requested outcome or claim | accessibility and localization method |
| `content-and-sensitive-flows.md` | content changes consequential meaning, consent, access, account data, payment, deletion, recovery, or professional claims | sensitive-flow content and control method |
| `prototyping-and-implementation.md` | prototype medium, design-led code, implementation handoff, or prototype evidence is in scope | prototype fidelity and design-led implementation method |
| `validation-and-review.md` | planning evidence, performing review, or deciding completion | validation matrix and finding method |
| `current-sources.md` | a material claim depends on current Apple guidance, API, OS, policy, hardware, or design language | current Apple-source verification procedure |
| `research-and-source-evidence.md` | external research, examples, inspiration, or reusable assets can change a decision | external-source evidence and reuse method |
| `source-registry.json` | the external-source method needs a curated starting point for the active question | maintained source entries and reuse metadata |

Source-registry editing, periodic rechecks, redirects, access walls, license changes, and publication steps are repository maintenance. Run `python3 scripts/validate_source_registry.py` after changing the registry; do not add this maintenance procedure back to the runtime reference.

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
The interaction and motion contract lives under `evals/interaction-motion/`; validate it with `python3 scripts/validate_interaction_motion_evals.py`.
The content and sensitive-flow contract lives under `evals/content-sensitive-flows/`; validate it with `python3 scripts/validate_content_sensitive_flow_evals.py`.

## Content and Sensitive-Flow Method

Issue #8 consolidates content design, permissions, privacy, identity, account-data control, commerce, and regulated-domain boundaries in `plugins/apple-ui-design/references/content-and-sensitive-flows.md`. Load it only when the task includes a material user decision, sensitive data or access, destructive account action, purchase consequence, or professional-domain claim.

The maintained method must preserve these boundaries:

1. content states what is happening, why it matters, what the user can choose, what changes next, and how failure is recovered;
2. product, policy, price, entitlement, retention, refund, medical, financial, and legal facts come from named owners or current authoritative sources rather than design inference;
3. permission and privacy flows request only the access needed for the task, respect denial or limited access, and expose a truthful alternative where one exists;
4. identity, export, and deletion paths make scope, consequence, progress, cancellation, and recovery explicit without adding unnecessary obstruction;
5. subscription and purchase flows present the billed amount, duration, renewal or trial consequence, entitlement, restoration, and management path supported by the actual product and current policy;
6. manipulative urgency, shame, disguised choices, hidden dismissal, repeated pressure, and false success are unacceptable evidence of conversion quality;
7. design review can assess comprehension and control, while native permission, authentication, StoreKit, data-operation, and policy-compliance claims require their own real evidence and responsible owner.

The deterministic suite must cover content and recovery, permission and privacy, identity and account data, commerce, and regulated-domain boundaries across all bundled skills. At least two independent product scenarios must be forward-tested without exposing the hidden assertions.

## Content and Sensitive-Flow Source Review

Issue #8 was reviewed against these exact Apple pages on 2026-07-31. Treat their policy and availability details as current-source claims and recheck them when a product decision depends on them.

| Apple page | Claim supported | Maintenance note |
| --- | --- | --- |
| `https://developer.apple.com/design/human-interface-guidelines/writing` | Interface words are part of the product experience | Use project voice and localization evidence; do not turn general writing guidance into one mandatory tone |
| `https://developer.apple.com/design/human-interface-guidelines/privacy` | Privacy-sensitive access requires transparency and protection | Recheck the current page before making platform-guidance claims |
| `https://developer.apple.com/design/human-interface-guidelines/in-app-purchase` | Current Apple design guidance for in-app purchase presentation | Verify the product type, storefront, OS, and current policy separately |
| `https://developer.apple.com/app-store/subscriptions/` | Subscription sign-up must clearly present the product, duration, billed renewal price, and sign-in or restore path; trials disclose duration and post-trial price | Pricing, offer eligibility, management APIs, and storefront rules can change |
| `https://developer.apple.com/app-store/review/guidelines/` | Current review rules for consent, minimization, alternative paths, account sign-in, subscriptions, sensitive data, and regulated services | Cite the current section and access date; do not let the design skill make legal-compliance conclusions |
| `https://developer.apple.com/support/offering-account-deletion-in-your-app/` | Apps with account creation must let users initiate deletion in-app; the flow should be findable, transparent, and not unnecessarily difficult | Retention and legal obligations still require project legal ownership |
| `https://developer.apple.com/app-store/app-privacy-details/` | App privacy disclosures depend on the app's and third-party partners' actual data practices | Treat App Store disclosures as product facts to verify, not copy invented by the design skill |

The stable method belongs in the shared reference; changing App Store rules, StoreKit behavior, storefront exceptions, API availability, and regulated-domain requirements remain live research. If an exact current source cannot be checked, mark the affected recommendation unverified and route the policy decision to its responsible owner.

## Interaction and Motion Method

Issue #14 consolidates interaction and motion decisions in `plugins/apple-ui-design/references/interaction-and-motion.md`. Load that reference only when a task creates, adapts, or reviews material interaction or motion behavior.

The maintained method must preserve these boundaries:

1. confirmed product interaction and motion direction remains user-owned unless a hard boundary conflicts;
2. Apple conventions and native components are classified as experience baselines, platform recommendations, or implementation evidence rather than visual vetoes;
3. interaction is specified through task, state, input, result, interruption, reversal, recovery, and accessibility behavior;
4. motion may serve functional, spatial, feedback, expressive, brand, or emotional purposes, but its task impact and system-setting response remain explicit;
5. tool, content, and experimental products receive different risk emphasis instead of one generic motion checklist;
6. HTML, storyboards, timing tables, and successful builds do not establish native interaction or motion quality;
7. native recording can establish the exercised behavior, while final rhythm and aesthetic acceptance remains with the user.

The deterministic suite must cover tool, content, and experimental interaction scenarios; direction, adaptation, and review ownership; interruption and reversal; Reduce Motion; platform inputs; and honest native-evidence claims.

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
