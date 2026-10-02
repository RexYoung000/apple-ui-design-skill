# Design quality forward run — 2026-10-02

The update was exercised through four separate agents with no conversation history or hidden assertions. [Requests and inputs](requests.json) identify each task; generated outputs are retained under their case directories. The final runtime fingerprint is [runtime-sha256.json](runtime-sha256.json).

| Task | Preserved result | Actual verification | Result limit |
|---|---|---|---|
| FieldNote direction | [Flow, terminology and motion rationale](direction/README.md), [HTML](direction/index.html) | Primary-agent browser input/save/edit/failure/retry/draft/focus checks at desktop and 390×844 | Browser prototype only; native/assistive/user acceptance unverified |
| OrbitCut iPad→Mac | [Decision matrix](adaptation/decision-matrix.md), [HTML](adaptation/index.html) | 900×640 and 1440×900 layouts; pointer drag, keyboard adjustment, invalid input, cancel, undo, inspector/export focus, illustrative preview | Layout and selected browser paths only; no actual media export or native run |
| OrbitCut review | [Screenshot review](review/review.md) | Reviewer inspected all four inputs; primary agent checked findings and two compact inputs | Visible facts and evidence gaps; no score or runtime pass inferred |
| Inline expansion terminology/reference | [Consultation](sources/response.md) | Component Gallery → original GOV.UK guidance → operated accordion example | Behavior/vocabulary inspiration only; no Apple API or product fit asserted |

[Browser observations](browser-checks.json) enumerate exercised paths and omissions. [Source review](source-review.md) records exact pages and observation limits. [Artifact checksums](artifacts-sha256.json) protect the archived files. The FieldNote agent fixed a modal failure-control instruction and a desktop panel offset during its own checks, before the primary browser run; see [checks](direction/checks.md). These fixture repairs did not change plugin scope.

The complete deterministic gate passed 108 unit tests, all structural/contract checks, saved goldens, and generated portable folder/ZIP validation. Skill-creator quick validation passed for all three Skills. Runtime is 1,621 Skill-entry words and 17,297 total words, under the unchanged 2,500/17,500 ceilings. Registry schema 2 contains 26 curated sources with overlapping domain metadata and enforced exclusion rules.

This run is an agent-behavior and browser evidence check. It does not close Roadmap #12, establish native motion quality, prove VoiceOver or other assistive tasks, demonstrate real preview/export, validate actual user needs, or constitute user acceptance. Original historical evaluation files were left intact. Only local absolute Markdown paths in new archived outputs were normalized for portability.
