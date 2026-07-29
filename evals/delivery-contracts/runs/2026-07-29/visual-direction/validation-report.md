# Validation report

## Artifact checks

- Loaded `today-visual-directions.html` in headless Google Chrome through Playwright at a 1600 × 1100 CSS-pixel viewport and 2× device scale.
- Browser result: two direction articles and two labelled phone screens found; no console errors and no page errors.
- DOM bounds check: no visible descendant overflowed or was clipped by either 390 × 844 CSS-pixel phone frame.
- Full comparison render: `today-visual-directions.png`, 3200 × 2336 px.
- Standalone renders: `direction-a-calm-editorial.png` and `direction-b-direct-task-led.png`, each 780 × 1690 px.
- The final comparison and the standalone task-led screen were visually inspected at rendered resolution. The required greeting, date, three commitments, one completed commitment, end-of-day note, and distinct primary focus are visible.

## Static contrast checks

WCAG contrast ratios were calculated from the final rendered proposal values:

| Foreground / background | Ratio | Result for normal text |
|---|---:|---|
| `contentPrimary #292522` / `surfaceBase #F7F2EA` | 13.64:1 | Pass |
| `actionPrimary #A44E37` / `surfaceBase #F7F2EA` | 5.06:1 | Pass |
| `contentSecondary #6A625C` / `surfaceBase #F7F2EA` | 5.36:1 | Pass |
| `contentMuted #746A64` / `surfaceBase #F7F2EA` | 4.72:1 | Pass |
| `contentPrimary #292522` / proposed task surface `#F4E7DF` | 12.55:1 | Pass |
| `actionPrimary #A44E37` / proposed task surface `#F4E7DF` | 4.66:1 | Pass |
| `contentSecondary #6A625C` / proposed task surface `#F4E7DF` | 4.93:1 | Pass |

The first render exposed two ratios below 4.5:1. The proposed muted content and task-surface values were adjusted before the final render. This calculation supports color-pair review only; it is not a native accessibility audit.

## Render hashes

| Artifact | SHA-256 |
|---|---|
| `today-visual-directions.png` | `020264898c015bbd80c6a7cbc6356933b048fcb7dd375d1453aef65d86678bf9` |
| `direction-a-calm-editorial.png` | `f44d1d720260888cd9905d3c0f190f063b21f13957e2b6d99a716e6235e13ab8` |
| `direction-b-direct-task-led.png` | `23f759ac596a925a1281a247b27f4fe2cafc0bab752793d395f221f2d2542cc9` |

## Supported completion claim

The **Visual Direction artifact is complete**: two materially different Today screen hypotheses are rendered with representative content, visible tradeoffs, platform/accessibility risks, and an exact user acceptance path.

The evidence does **not** support “direction aligned,” “native prototype complete,” “code complete,” “experience verified,” or “user accepted.”

## Not validated

- User preference or final direction selection.
- Production SwiftUI implementation.
- Native iOS navigation, hit testing, completion behavior, haptics, or state persistence.
- Dynamic Type and accessibility text-size reflow.
- VoiceOver names, order, actions, and announcements.
- Small/large supported iPhone environments, appearance modes, increased contrast, localization, right-to-left layout, and long-content behavior.
- Motion and reduced-motion behavior; motion was intentionally not introduced for this static hierarchy decision.
