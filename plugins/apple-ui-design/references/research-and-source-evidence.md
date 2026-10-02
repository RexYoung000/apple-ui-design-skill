# Research and Source Evidence

## Load When

Load this reference when external research, shipped examples, UI or motion inspiration, or reusable assets can change a decision. Do not load it when project evidence already resolves the question or browsing would be ornamental.

This is the single runtime source for external-source evidence and reuse.

## Hybrid Research Model

Use `source-registry.json` as a maintained set of starting points. Select by `design_domains`, platform, access, and evidence purpose; excluded entries are never candidates. An `active` curation status is not a live availability check, and `last_checked` does not establish that every case or API was inspected.

Start with the unresolved design question, not a website quota. Follow the selected entry to a relevant example or exact guideline, inspect it, and explain which layout, behavior, vocabulary, or mechanism is applicable. A directory description supports source discovery only. If no external source changes the decision, use project evidence and continue.

Do not collect a fixed number of examples. Stop when the evidence:

- covers the meaningful directions and at least one relevant counterexample;
- is recent enough for the claim;
- distinguishes platform behavior from visual inspiration;
- lets the user compare real tradeoffs rather than repeated variations.

## Source Layers

| Layer | Valid use | Invalid use |
|---|---|---|
| User and project evidence | Define product intent, current behavior, constraints, and approved decisions | Claim external user validation without data |
| Apple official authority | Support current platform behavior, API, accessibility, and resource claims | Own the product’s brand or visual style |
| Usability reference | Suggest task-specific questions and evaluation criteria | Prove user needs, usability success, or Apple API behavior |
| Shipped product observation | Show that a pattern exists and observe how it behaves | Prove that the pattern is correct for this product |
| Public UI or motion gallery | Compare visible approaches and broaden exploration | Claim Apple-native validity |
| External visual or implementation inspiration | Inspire color, material, composition, motion, or technical experiments | Copy a design or treat Web behavior as native evidence |
| Asset or component source | Supply a candidate only after license and fit checks | Reuse unknown-license material |

Mark Web-derived ideas as `inspiration only`. Before claiming Apple-native behavior, translate the idea through the confirmed product model, target platform and inputs, required accessibility outcomes, and native runtime validation.

## Select by Question

| Question | Starting points | Inspect and translate |
|---|---|---|
| UI hierarchy, components, or real content | `apple-hig`, `ui-pocket`, `mobbin`, `component-gallery` | Relevant states and component purpose; preserve project DNA. A gallery is observation, not a quality certificate. |
| UX task clarity, navigation, or recovery | `nng-usability-heuristics`, `mobbin` | The matching heuristic or observed task path; distinguish expert judgment from research with the actual users. |
| Interaction, input, or platform adaptation | `apple-hig`, `apple-design-videos`, `component-gallery` | Inputs, states, focus, cancellation, and platform differences; verify adopted behavior in the target environment. |
| Motion purpose, continuity, or rhythm | `apple-design-videos`, `60fps-design` | Observe the actual dynamic example and interruption behavior where available; a still frame does not establish timing. |
| An unclear component or effect name | `namethatui`, `component-gallery` | Compare candidate meanings; terminology and API suggestions require platform verification. Use existing knowledge when the meaning is clear. |

Web implementation sources such as React Bits remain mechanism or visual inspiration for Apple products. Do not import their code, dependencies, or interaction assumptions into a native product merely because they demonstrate an effect.

## Claim Ledger

For material decisions, keep a compact record:

```text
Claim or decision:
Evidence label: user-confirmed | project-fact | official-source | shipped-observation | inspiration-only | design-inference | unvalidated-hypothesis
Source and observed date:
What the evidence supports:
What it does not prove:
Reuse or license status:
Required validation:
```

Record whether only an introduction, a static example, a dynamic example, or implementation documentation was inspected. Cite the exact page supporting the decision. For version-sensitive Apple facts, record the supported version and fallback.

Use `current-sources.md` as the single procedure for exact Apple pages, access dates, version splits, unavailable sources, and conflicts between published guidance and project runtime evidence.

## Observation and Reuse

Observing a public page does not grant permission to redistribute its screenshots, icons, templates, code, or brand assets.

- Link to and describe third-party examples unless reuse terms are verified.
- Prefer Apple Design Resources and SF Symbols for Apple-platform production assets, subject to their current licenses.
- Use a project’s licensed assets before searching for substitutes.
- Treat third-party icon systems as candidates, not automatic replacements for SF Symbols or product-specific art.
- Do not bundle screenshots or downloads from galleries, Pinterest, Mobbin, or software-distribution sites.
- Never make an account, subscription, or paid library a silent requirement of the core workflow.

## Access Failures

If a source is unavailable:

1. use another source in the same layer;
2. state what could not be observed;
3. avoid reconstructing the source from memory;
4. mark the affected conclusion as unverified when no equivalent evidence exists.

Use conditional sources only for their public preview. Do not ask the user to create an account unless the user explicitly wants that source and its unique value justifies the interruption.
