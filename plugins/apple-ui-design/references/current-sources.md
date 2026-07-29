# Current Source Policy

Use this reference when an Apple platform, API, policy, design-resource, or public example claim may have changed.

## Stable and Changeable Knowledge

Treat these as stable plugin principles:

- product intent before implementation;
- project evidence before broad convention;
- brand DNA and platform behavior as separate concerns;
- accessibility and localization as design inputs;
- honest evidence and risk-based validation.

Verify these at task time:

- current Human Interface Guidelines;
- OS availability and deployment support;
- SwiftUI API behavior and deprecations;
- Apple platform materials and interaction capabilities;
- App Store or platform policy;
- current device and input behavior;
- public-site access, licensing, and reuse conditions.

Do not freeze volatile API tables into a skill.

## Source Priority

For current Apple behavior:

1. Apple Developer documentation.
2. Apple Human Interface Guidelines.
3. Apple sample code and official design resources.
4. WWDC sessions and transcripts.
5. The project’s verified runtime behavior.
6. High-quality community sources only when official material is insufficient.

For product behavior, current authoritative project documents and confirmed user decisions outrank external convention.

Use `source-registry.json` as a curated map, not a frozen archive or ranking. Use `research-and-source-evidence.md` to label claims, observations, inspiration, and reuse boundaries. Search live for the actual product and decision rather than citing a registry entry that does not support the claim.

Primary official entry points:

- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Apple Design Resources: https://developer.apple.com/design/resources/
- SwiftUI documentation: https://developer.apple.com/documentation/swiftui/
- Apple Developer videos: https://developer.apple.com/videos/

Resolve current platform guidance against the project’s confirmed intent and minimum supported versions. Cite the exact official page near version-sensitive claims.
