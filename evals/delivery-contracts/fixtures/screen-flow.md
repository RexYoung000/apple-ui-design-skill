# FrameKeep First-Run Import

Status: zero-to-one flow with confirmed scope

- Platform hypothesis: iPhone.
- Product purpose: privately organize selected personal photos into small reference collections.
- First-run goal: choose photos, grant the minimum necessary access, import selected items, and reach the first collection.
- Privacy rule: never imply access before the user selects or grants it.
- Required states: welcome, explanation, system-permission handoff, denied, limited access, selection, importing, recoverable failure, retry, cancellation, and completion.
- The prototype may mock the system picker and permission result, but it must label those boundaries.
- The user has approved explicit buttons as the primary path; no gesture-only controls.
- Visual direction is intentionally minimal for this test. The decision being tested is flow clarity and recovery.
- No native permission implementation exists.
