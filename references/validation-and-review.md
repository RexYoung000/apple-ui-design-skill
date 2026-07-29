# Validation and Review

Use this reference to plan evidence, review an interface, or determine whether a UI task is complete.

## Validation Is Risk-Based

Select checks based on the changed experience. Not every task needs every row, but every omitted high-risk scenario should be intentional.

## State Matrix

Consider:

- normal and populated;
- empty or first use;
- loading and slow response;
- partial data;
- recoverable and terminal error;
- offline or unavailable service when applicable;
- disabled, selected, focused, pressed, hovered, and editing;
- destructive confirmation and undo;
- permission denied or limited access;
- long, short, missing, or unusual content;
- large numbers, dates, and localized formats;
- interrupted and resumed flow;
- minimum-version fallback.

## Environment Matrix

### iOS

- smallest and largest relevant device sizes;
- portrait and landscape only when supported or materially different;
- keyboard shown and dismissed;
- safe areas, sheets, navigation, interruption, and restoration;
- touch and VoiceOver;
- supported text sizes and appearance modes.

### iPadOS

- compact and expansive windows relevant to the product;
- split view or stage/window behavior when in scope;
- touch, keyboard, focus, pointer, and drag and drop;
- sidebar, column, inspector, popover, and toolbar transitions;
- content reflow rather than empty enlargement.

### macOS

- minimum, default, and expanded window sizes;
- keyboard-only task path and visible focus;
- menus, commands, shortcuts, pointer, hover, and context menu;
- selection, multi-selection, drag and drop, undo/redo when applicable;
- sheets, panels, inspectors, multiple windows, and focus restoration;
- VoiceOver and text scaling behavior relevant to the app.

## Evidence

Match evidence to the claim:

- screenshot for static hierarchy and visual state;
- state-by-state preview for component coverage;
- recording for motion, navigation, resizing, keyboard, pointer, or touch;
- accessibility inspection or narrated test path for semantic behavior;
- simulator or device run for iOS/iPadOS native interaction;
- real Mac app run for window, menu, command, and focus behavior;
- build and tests for implementation integrity.

A successful build does not prove a usable interface. A screenshot does not prove interaction. A browser prototype does not prove native behavior.

## Evidence-Based Review

Assess:

1. **Product alignment**: Does the interface support the confirmed goal and mental model?
2. **Task clarity**: Can the user understand state, priority, action, result, and recovery?
3. **Platform fit**: Does it work with the platform role and required input/window model?
4. **Design DNA**: Is the product recognizable and internally coherent?
5. **Adaptivity**: Does layout respond to content, size, locale, and platform?
6. **Accessibility**: Can users complete the core task with relevant assistive behavior?
7. **Craft and motion**: Are spacing, typography, assets, transitions, and feedback intentional?
8. **Runtime evidence**: Has the claimed experience actually been exercised?

Do not assign numeric scores by default. Scores hide missing criteria and imply precision that the evidence rarely supports.

## Severity

### Blocking

Use when:

- a core task cannot be completed;
- behavior contradicts confirmed product intent;
- data meaning or destructive consequence is misleading;
- essential content or action becomes inaccessible;
- navigation, focus, or state recovery fundamentally fails.

### Important

Use when:

- hierarchy or affordance creates significant friction;
- platform behavior is notably inappropriate;
- brand or component inconsistency weakens comprehension;
- important localization, adaptivity, or accessibility conditions fail;
- motion or state feedback materially obscures the result.

### Optimization

Use for polish that improves quality without preventing the intended task.

Do not inflate severity because a recommendation differs from personal taste.

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

Ground critique in the actual artifact. Name the screen, state, platform, and environment. Avoid generic comments such as “make it more Apple-like” or “improve hierarchy.”

## Comparing Directions

Use a relative decision table rather than scores:

| Direction | Optimizes | Tradeoff | Platform implication | Risk | Best fit |
|---|---|---|---|---|---|

Compare only criteria that matter to the confirmed product goal. If the user combines directions, restate the resulting design logic before implementation.

## Handoff

Provide:

- outcome and scope;
- affected platforms;
- states and environments checked;
- evidence produced;
- blocking and important findings resolved;
- remaining risks or unverified scenarios;
- exact user acceptance path and expected behavior.

Final visual acceptance belongs to the user. If acceptance reveals a meaningful mismatch, return to alignment rather than patching symptoms blindly.
