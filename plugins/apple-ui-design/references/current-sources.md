# Current Apple Source Verification

## Load When

Load this reference when a material claim depends on current Apple guidance, API or OS availability, deprecation, platform policy, hardware or input behavior, or a newly introduced design language. Do not load it for stable product decisions with no version-sensitive Apple claim.

This is the single runtime source for current Apple-source verification.

## What Stays Stable

Keep these as stable plugin principles:

- product intent before implementation;
- project evidence before broad convention;
- brand DNA and platform behavior as separate concerns;
- accessibility and localization as design inputs;
- honest evidence and risk-based validation.

Do not freeze volatile API tables into a skill.

## Verification Workflow

Before presenting a version-sensitive conclusion as verified:

1. Read the project’s deployment targets, target platforms, and represented runtime environment.
2. Open the exact current Apple page that supports the claim. A documentation homepage, search result, or remembered summary is not enough.
3. Record the page title, exact URL, access date, affected platforms, supported versions, and the part of the claim it supports.
4. Separate the project’s minimum supported version from the enhancement version that introduces the capability.
5. Define the fallback for older supported systems, or state that the capability cannot serve the current deployment target.
6. Label official documentation, project runtime evidence, and design inference separately.
7. Place the source next to the claim in the delivered artifact instead of hiding it in a generic bibliography.

Use this compact record:

```text
Claim:
Status: verified | partially verified | unverified
Official page and accessed date:
Platforms and published availability:
Project minimum versions:
Enhancement versions:
Fallback:
Project runtime evidence:
Design inference:
Remaining unverified behavior:
```

## Evidence Boundaries

- **Official source** establishes Apple’s published guidance, API signature, or availability.
- **Project runtime** establishes what the recorded build, OS, device, input, and state actually did.
- **Design inference** explains product fit or a recommendation; it is not an Apple requirement.

Compilation can verify API availability and guarded fallback code. It does not verify visual fit, interaction quality, accessibility behavior, performance, or user acceptance.

The newest capability is an enhancement candidate, not an automatic default. Resolve it against product intent, audience, release horizon, deployment support, accessibility, and fallback cost.

## Access or Coverage Failure

If the exact official source cannot be reached or does not cover the claim:

1. try another current Apple source in the same authority layer;
2. state which page or fact could not be verified;
3. mark the affected conclusion `unverified`;
4. avoid a version-specific recommendation or define the lookup as a blocking next step when it changes the artifact.

Do not reconstruct current behavior from memory. Do not silently substitute a community article for an Apple availability or policy claim.

## Official Source and Runtime Conflict

Official documentation and project runtime answer different questions. Preserve both records when they disagree.

Capture the exact toolchain, OS, device or simulator, project target, code path, and reproduction result. Reduce the conclusion to what each source proves, identify whether the difference may be a project defect, beta or SDK change, documentation gap, or environment-specific behavior, and define the next reproduction or escalation step.

Do not promote shipped behavior into an Apple rule. Do not dismiss reproducible project behavior merely because the official page describes a different expected result.

## Source Priority

For current Apple behavior:

1. Apple Developer documentation.
2. Apple Human Interface Guidelines.
3. Apple sample code and official design resources.
4. WWDC sessions and transcripts.
5. The project’s verified runtime behavior.
6. High-quality community sources only when official material is insufficient.

For product behavior, authoritative project documents and confirmed user decisions outrank external convention.

Use `source-registry.json` only as a curated starting map. Use `research-and-source-evidence.md` for external research, observations, inspiration, and reuse boundaries.
