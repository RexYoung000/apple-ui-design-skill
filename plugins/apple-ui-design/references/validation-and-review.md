# Validation and Review

## Load When

Load this reference when planning evidence, performing a formal review, or determining whether a UI task is complete. Use focused sections for a small change; do not turn every check into a full review.

This is the single runtime source for the validation matrix and actionable-finding method. Review owns formal findings; direction and adaptation use it to plan evidence and state honest completion.

## Contents

- Quality lenses and representative acceptance tasks
- Shared checks and risk-based validation
- State and sensitive-flow matrices
- Platform environment matrix
- Evidence levels
- Evidence-based review
- Severity and finding format
- Direction comparison
- Handoff

## Quality Lenses and Acceptance Tasks

UI, UX, Interaction, and Motion are overlapping lenses inside the three workflows. UX concerns the whole task experience, including interface, interaction, and motion; the columns below are navigation aids, not mutually exclusive categories. Select affected lenses and their existing owners. A narrow request does not require every task.

| Lens | Observable question | Method owner and source purpose | Minimal representative acceptance task |
|---|---|---|---|
| UI — visual interface | Are hierarchy, text, content, surfaces, and states coherent and readable? | `design-system-and-dna.md`; project rules and applicable current Apple guidance; galleries offer candidates | Render one key screen with real content, a relevant state, and long/large text; inspect priority and reachable actions |
| UX — task experience | Can the intended user understand, complete, and recover the core task? | `context-and-alignment.md`, `content-and-sensitive-flows.md`; confirmed intent and user/task evidence; observed flows suggest hypotheses | Run one core path through failure and recovery; verify preserved progress, truthful completion, and understandable return |
| Interaction — operation | Are input, discovery, feedback, cancellation, and final state reliable? | `interaction-and-motion.md`; platform input guidance and actual operation | Execute, cancel, repeat, and undo one material operation using required inputs; check final intent and focus |
| Motion — temporal expression | Do purpose, continuity, rhythm, and comfort coexist with efficient use? | `interaction-and-motion.md`; project language, current guidance, and motion observations | Record a key native transition at normal speed, interrupt/reverse/repeat it, then exercise Reduce Motion |

Sources inform a criterion; they do not establish that this product passes. Use `research-and-source-evidence.md` to select an evidence layer and inspect specific examples. Terms and candidate mappings belong to `design-system-and-dna.md`, not a new workflow.

## Validation Is Risk-Based

Select checks from the changed experience; make omitted high-risk scenarios explicit. Shared concerns cut across every lens:

- accessibility/localization: `accessibility-and-localization.md` owns equivalent completion, semantics, settings, and content/locale expansion;
- content/control: `content-and-sensitive-flows.md` owns consequential meaning and sensitive-flow contracts;
- design-system consistency: `design-system-and-dna.md` owns reusable roles, components, and identity;
- platform/adaptation: `apple-platform-adaptation.md` owns window, navigation, input, and continuity translation;
- evidence/completion: apply the levels below and the selected `delivery-contracts.md` gate.

Do not invent user research from a brief or judge quality by terminology count, number of reference sites, visual novelty, or resemblance to system apps.

## State Matrix

Select relevant populated, empty/first-use, loading/slow, partial, error, offline, disabled/selected/focused/pressed/hovered/editing, destructive/undo, denied-access, long/unusual content, locale-format, interrupted/resumed, and minimum-version states.

## Sensitive-Flow Matrix

Exercise relevant paths; name omissions:

- content/action meaning, retry, cancellation, preserved progress, and confirmed completion;
- permission not determined, allowed/limited/denied/restricted/deferred, Settings recovery, and no-access operation;
- sign-in, reauthentication/recovery/session loss, export, deletion confirmation/processing/failure/completion;
- purchase loading/pending/success/cancellation/failure, restoration, entitlement refresh/expiry/billing, and management;
- professional sources present/stale/unavailable/disputed, jurisdiction, review pending, and unverified claims.

Check false urgency, shame, disguised choices, hidden dismissal, repeated pressure, obscured price, false success, and unsupported authority.

## Environment Matrix

### iOS

Check relevant device sizes, supported orientations, keyboard/safe areas, sheets/navigation/interruption/restoration, touch/VoiceOver, text sizes, and appearances.

### iPadOS

Check compact/expansive windows, split or stage/window behavior, touch/keyboard/focus/pointer/drag and drop, sidebar/column/inspector/popover/toolbar transitions, and content reflow rather than empty enlargement.

### macOS

Check minimum/default/expanded windows, keyboard-only completion and focus, menus/commands/shortcuts/hover/context actions, selection/drag/undo, sheets/panels/inspectors/multiple windows/focus restoration, VoiceOver, and relevant text scaling.

## Evidence

Match each claim to what was actually exercised:

| Evidence | Can support |
|---|---|
| Screenshot or component preview | Visible hierarchy and represented states |
| Operable prototype | Exercised flow in that prototype's medium |
| Representative-speed native recording/run | Shown input, navigation, motion, resize, focus, and system-setting behavior |
| Semantic inspection/automation | Checked labels, roles, state, and supported automated paths |
| Named assistive-technology run | Exercised technology, task, environment, and path |
| Build/tests | Implementation integrity |
| Matching service/sandbox/professional evidence | Exercised external operation or reviewed domain claim |

A build does not prove usability; a screenshot does not prove interaction; HTML does not prove native behavior. Record simulator/device or real Mac environment. Material motion needs representative-speed recordings and its Reduce Motion expression. Timing values alone cannot prove rhythm, continuity, interruption, or comfort.

Copy review cannot prove policy compliance; mocked permission/purchase cannot prove the system path; a completion label cannot prove account/data/payment success; a generic disclaimer cannot prove professional review.

Native evidence concerns operation, not visual conformity. A custom interaction can pass when it serves confirmed tasks/inputs, while a system-looking interface can fail. Evidence reveals risk without overruling confirmed decisions; record accepted non-hard-boundary tradeoffs and remaining gaps.

## Evidence-Based Review

Use the affected quality lenses to assess product/task alignment, platform fit, shared DNA, content/size/locale adaptivity, accessibility, craft, and actual runtime evidence. Do not assign numeric scores by default: they can imply precision or conceal missing evidence.

## Severity

### Blocking

Core-task failure, contradiction of confirmed intent, misleading data/destructive consequences, inaccessible essential content/actions, or fundamental navigation/focus/recovery failure.

### Important

Material hierarchy/affordance friction, inappropriate platform behavior, incoherent identity/components, failed relevant accessibility/localization/adaptation, or obscured results/feedback.

### Optimization

Polish that improves quality without preventing the task. Do not inflate severity for taste.

## Finding Format

For every actionable finding:

```text
Title and severity
Observed fact:
User impact:
Evidence or affected scenario:
Recommendation:
How to verify:
```

Name artifact, screen/state, platform, and environment. Explain the observable problem, not “make it more Apple-like.” Mark a recommendation as a confirmed outcome requirement, current platform guidance, optional optimization, or unapproved exploration/preference. Convention does not override product authority.

## Comparing Directions

Compare criteria relevant to the confirmed goal:

| Direction | Optimizes | Tradeoff | Platform implication | Risk | Best fit |
|---|---|---|---|---|---|

If directions are combined, restate the resulting design logic before implementation.

## Handoff

Report outcome/scope, platforms, checked states/environments, evidence, resolved findings, remaining risks, and the exact acceptance path with expected behavior. Final visual acceptance belongs to the user; a meaningful mismatch returns to alignment.
