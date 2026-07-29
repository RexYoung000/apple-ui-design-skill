# Research and Source Evidence

Use this reference when a task needs product research, Apple guidance, shipped examples, UI or motion inspiration, or reusable assets.

All bundled skills use this file as their single research and reuse-boundary source.

## Hybrid Research Model

Use `source-registry.json` as a maintained set of starting points, then research at task time for the actual product, target user, platform, and design question. The registry improves repeatability; live research prevents stale or generic conclusions.

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
| Shipped product observation | Show that a pattern exists and observe how it behaves | Prove that the pattern is correct for this product |
| Public UI or motion gallery | Compare visible approaches and broaden exploration | Claim Apple-native validity |
| External visual or implementation inspiration | Inspire color, material, composition, motion, or technical experiments | Copy a design or treat Web behavior as native evidence |
| Asset or component source | Supply a candidate only after license and fit checks | Reuse unknown-license material |

Mark Web-derived ideas as `inspiration only`. Before claiming Apple-native behavior, translate the idea through the confirmed product model, target platform and inputs, required accessibility outcomes, and native runtime validation.

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

Do not cite a broad homepage when a specific current page supports the claim. For version-sensitive Apple facts, record the supported OS or API version and fallback requirement.

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

## Registry Maintenance

Repository maintainers must validate `source-registry.json` with the root source-registry validator after editing it. Recheck active entries periodically and whenever a redirect, access wall, licensing change, or material content change is observed.
