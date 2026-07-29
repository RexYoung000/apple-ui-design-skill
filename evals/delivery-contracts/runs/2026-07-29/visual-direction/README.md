# HearthDay Today visual-direction review

## Outcome and boundary

This package supports one decision: which visual hierarchy should make the next unfinished commitment more focused while preserving HearthDay's warm, clear, non-judgmental, and private character.

In scope: Today screen hierarchy, grouping, typography, surfaces, and visual emphasis on iPhone.

Out of scope: navigation, the commitment data model, task ordering logic, completion interaction behavior, new artwork, production SwiftUI, and native runtime validation.

## Evidence state

- **User-confirmed / fixture facts:** existing iPhone product; primary user checks a small self-chosen set of daily commitments; core task is to understand what still matters and complete one item; Today contains greeting, date, three commitments with one complete, and an end-of-day note; navigation and task interactions are approved and out of scope.
- **Project values:** `surfaceBase #F7F2EA`, `contentPrimary #292522`, and `actionPrimary #A44E37`.
- **Rendered proposals:** all other exact colors, type sizes, spacing, radii, border treatments, and shadows visible in the HTML and PNGs.
- **Unvalidated hypotheses:** a large typographic pause will feel calm and focused; a raised warm task surface will feel direct without becoming judgmental.
- **External evidence:** not needed for this bounded static hierarchy comparison.

## The two rendered hypotheses

### Direction A — Calm editorial

The primary commitment receives focus through type scale, whitespace, and sequence. Secondary and completed work stay visible but quiet. It optimizes a reflective, private daily ritual and sacrifices some immediacy.

### Direction B — Direct task-led

The primary commitment receives focus through a warm raised surface and an explicit completion cue. The remaining list becomes supporting context. It optimizes quick recognition and action and sacrifices some page-like intimacy.

These are materially different hierarchy models, not color variants.

## Comparison

| Direction | Optimizes | Tradeoff | iPhone implication | Main risk | Best fit |
|---|---|---|---|---|---|
| Calm editorial | Calm focus and a reflective daily rhythm | Completion affordance is quieter | Large text must reflow without hiding the second commitment | May feel more like reading than acting | Users who open Today as a brief personal ritual |
| Direct task-led | Fast recognition and completion | Stronger task-manager energy | Focus card needs a generous hit region and explicit accessibility state | May feel too insistent for a non-judgmental product | Users who open Today for an immediate next action |

## Accessibility and localization intent

- Completion is never represented by color alone: status uses circle/check geometry, text treatment, ordering, and accessible labels in the HTML.
- Primary text and project accent combinations were checked computationally against the rendered surfaces; see `validation-report.md`.
- The layout uses system typography in the comparison artifact. A production design must use semantic Dynamic Type roles and reflow at accessibility sizes.
- Representative English content is rendered. Long strings, pseudo-localization, right-to-left layout, VoiceOver order, and real touch targets remain native implementation checks.
- No essential text is embedded in a raster-only source; the HTML is the durable semantic artifact.

## Exact acceptance path

1. Open `today-visual-directions.png` at 100% and compare only the two phone screens first.
2. Ask: on first glance, which screen makes “Walk after lunch” unmistakably primary?
3. Ask: which screen still feels warm, private, and non-judgmental rather than performance-driven?
4. Check that “Call Mum” remains easy to find and “Read 20 pages” is clearly complete without competing for attention.
5. Choose A, choose B, or name a deliberate combination (for example, A's type-led quiet with B's stronger completion affordance).
6. After selection, validate the chosen direction in SwiftUI on a small and large supported iPhone, at default and accessibility text sizes, in VoiceOver reading order, and with the actual completion interaction.

## Completion stage

The **Visual Direction contract artifact is complete**: two rendered key-screen hypotheses with representative content, visible tradeoffs, evidence labels, risks, and an acceptance path exist.

The direction is **not aligned or user accepted** until one visible hypothesis or a bounded combination is selected. No claim is made for native prototype completion, production code completion, or verified iOS experience.
