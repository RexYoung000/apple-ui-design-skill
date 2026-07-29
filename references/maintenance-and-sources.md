# Maintenance and Current Sources

Use this reference when updating the skill, checking a version-sensitive rule, or adding a new Apple platform capability.

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

Use `source-registry.json` as the curated starting set and `research-and-source-evidence.md` as the research and claim-labeling method.

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

## Updating This Skill

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

Use realistic prompts to check the skill’s behavior:

1. “Redesign this existing iPhone screen” — must inspect the project before proposing style.
2. “Make this iPhone app work on Mac” — must ask or infer product differences, not stretch the layout.
3. “Use the newest Apple glass style” — must check minimum versions and product fit.
4. “Give me three visual options” — must create meaningful hypotheses rather than recolors.
5. “Review this screen” — must use evidence and severity, not arbitrary scores.
6. “Implement this approved design” — must preserve project architecture and route technical concerns appropriately.
7. “Make it accessible” — must explain task outcomes, not only add labels.
8. “The project has no minimum version” — must help decide rather than silently choose.

## Scope Expansion

The current scope is iOS, iPadOS, and macOS. Add watchOS, visionOS, tvOS, or other platforms only after:

- confirming user need;
- studying their distinct product and interaction model;
- adding platform-specific references;
- extending validation evidence;
- testing cross-platform ambiguity prompts.

Do not advertise unsupported platforms in the frontmatter until the reference and validation coverage exists.
