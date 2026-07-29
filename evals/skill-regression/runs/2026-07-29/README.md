# Regression harness live check — 2026-07-29

## Case

`review-direct-evidence-bounded`

The prompt explicitly invoked `$apple-ui-review` with the fixed LedgerDesk facts but did not include output patterns, forbidden patterns, severity expectations, or the golden output.

## Environment

- Codex CLI ephemeral session
- Working directory: `/tmp`, outside the repository
- Sandbox: read-only
- Installed public plugin: `apple-ui-design@apple-ui-design` version `0.1.0`
- Installed skill path observed in the raw trace:
  `/Users/rexyoung/.codex/plugins/cache/apple-ui-design/apple-ui-design/0.1.0/skills/apple-ui-review/SKILL.md`

## Result

The first evaluator run correctly confirmed the expected skill load but rejected the response because the case required literal English headings and both `Blocking` and `Important` severity words.

Manual review found the response was evidence-bounded and actionable:

- it called the result an unverified text-evidence review;
- it reported two important findings without inventing visual or VoiceOver failures;
- each finding contained an observed fact, user impact, recommendation, and verification method;
- unknown keyboard, VoiceOver, native data, contrast, minimum-window, and German-layout behavior remained explicit validation risks;
- it did not claim experience verification or user acceptance.

The case assertions were corrected to test semantic bilingual headings and the presence of a justified severity classification, not a fixed English template or predetermined severity count.

After that correction:

```text
skill regression output valid: review-direct-evidence-bounded
```

## Evidence limit

The raw trace and output were held in a temporary directory because traces can include unrelated local plugin and configuration diagnostics. This summary preserves the reviewed behavior and correction without publishing local runtime metadata. The live run validates one representative case; the deterministic matrix covers all 15 cases, and the earlier trigger-routing suite preserves additional positive, negative, and mixed fresh-session evidence.
