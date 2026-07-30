# Current Apple Source Verification Evaluations

This suite protects the version-sensitive claim protocol introduced for Issue #9.

## Coverage

The cases verify that the bundled skills:

- cite an exact current Apple page near a version-sensitive claim;
- mark the result unverified when the official source is unavailable or insufficient;
- separate project minimum versions from newer enhancement versions and fallbacks;
- preserve both official documentation and reproducible project runtime evidence when they disagree;
- distinguish official facts, project runtime results, and design inference.

Run the deterministic checks with:

```bash
python3 scripts/validate_current_source_evals.py
python3 -m unittest tests.test_current_source_evals -v
```

## Preserved New-Capability Record

`runs/2026-07-30/glass-effect-ios26.json` records an end-to-end verification of SwiftUI `View.glassEffect(_:in:)`.

The exact Apple documentation page was accessed on 2026-07-30 and states that the API is available on iOS 26.0 and newer. The project scenario keeps iOS 17.0 as its minimum:

- the unguarded fixture fails type checking for an iOS 17 deployment target;
- the guarded fixture type checks with an iOS 26 availability check and a regular-material fallback;
- the record keeps visual fit, runtime rendering, accessibility, performance, and user acceptance outside the compile evidence.

The saved compiler logs are macOS/Xcode evidence and are not rerun by Linux CI. CI validates the record schema, exact official URL, dates, version split, fallback, evidence labels, and referenced artifacts.
