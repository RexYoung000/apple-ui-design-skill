# Accessibility and Localization Regression Suite

This suite protects the outcome, platform, evidence, and localization contract introduced for Issue #7.

It verifies that the installable plugin:

- selects accessibility scenarios by platform, core task, user need, input, and risk;
- covers VoiceOver, Voice Control, Switch Control, AssistiveTouch, Full Keyboard Access, and Pointer Control without treating one as universal proof;
- keeps design review, semantic automation, and real assistive-technology runs as separate evidence levels;
- evaluates custom controls by role, state, actions, task result, and recovery instead of system-default appearance;
- covers Increase Contrast, Reduce Transparency, Reduce Motion, and non-color state meaning;
- covers RTL, plurals, grammatical variation, regional formats, pseudolanguages, and CJK content;
- prevents an audit or label check from being reported as a VoiceOver run.

Run:

```bash
python3 scripts/validate_accessibility_localization_evals.py
```

For a fresh-session check, give the model only a case's `prompt` and fixture paths. Do not pass `expected_behavior`, `forbidden_behavior`, or `source_markers`.

The preserved native run establishes semantic automation and the named Reduce Motion task only. The product owner did not require a live assistive-technology run to close the method work; this scope decision does not convert the unverified VoiceOver path into evidence.
