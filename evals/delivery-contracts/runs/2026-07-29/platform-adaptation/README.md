# OrbitCut radial timeline — iPad and Mac adaptation

## Outcome

This package adapts the established iPhone editing model to iPad and Mac without replacing the radial timeline. The radial canvas remains the largest and highest-contrast editing surface in every representative environment.

## Contract and evidence gate

Primary contract: **Platform Adaptation**.

This package supports **layout design complete, pending user acceptance**:

- a shared-versus-platform-specific decision matrix exists;
- representative iPad compact, iPad expansive, Mac minimum, and Mac expanded layouts are rendered;
- input, accessibility, localization, motion, continuity, fallback, and acceptance requirements are specified;
- the rendered layouts were checked as static browser artifacts.

It does **not** support “native prototype complete,” “experience verified,” or “user accepted.” No iPadOS or macOS app was built or run. Browser rendering does not verify native windows, menus, commands, focus, VoiceOver, Pencil, keyboard, pointer, drag and drop, export, or Reduce Motion behavior.

## Files

- `decision-matrix.md` — shared and platform-specific decisions, input mapping, fallbacks, and target behavior.
- `prototype/index.html` — responsive visible layout artifact.
- `prototype/styles.css` — layout and visual styling.
- `prototype/app.js` — deterministic representative data and static radial timeline rendering.
- `evidence/ipad-compact.png` — iPad compact window, 744 × 900.
- `evidence/ipad-expansive.png` — iPad expansive window, 1366 × 1024.
- `evidence/mac-minimum.png` — Mac minimum window, 900 × 640.
- `evidence/mac-expanded.png` — Mac expanded window, 1440 × 900.
- `evidence/layout-checks.json` — measured browser viewport and element visibility/bounds.
- `validation.md` — checks, evidence limits, remaining risks, and exact native/user acceptance path.

## Open the layouts

Open `prototype/index.html` with one of these query strings:

- `?mode=ipad-compact`
- `?mode=ipad-expansive`
- `?mode=mac-minimum`
- `?mode=mac-expanded`

The top-left badge identifies the rendered target environment. Exact visual values in this package are **rendered proposals**, not proven product tokens.
