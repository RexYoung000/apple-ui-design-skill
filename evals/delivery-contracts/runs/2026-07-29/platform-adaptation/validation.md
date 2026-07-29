# Validation, evidence boundary, and acceptance

## Static checks completed

The four representative HTML layouts were rendered at their target viewport sizes. Automated browser checks recorded:

- target mode and viewport;
- visibility and bounds of application shell, top bar, radial editor, radial timeline, transport, Import, Export, and the selected clip label;
- absence of horizontal document overflow;
- whether the radial timeline remains inside the visible viewport;
- whether target-specific library and inspector panels match the intended responsive rule.

Results are preserved in `evidence/layout-checks.json`. Each layout also has a full-page PNG in `evidence/`.

## What the visible evidence supports

- The radial timeline is visually central and remains the primary editing surface.
- Import, arrange context, preview transport, explicit Undo/Redo, and Export are visibly represented.
- iPad compact is a deliberate reflow, not a stretched three-column desktop layout.
- iPad expansive and Mac expanded show simultaneous library, radial canvas, and inspector context.
- Mac minimum protects the radial canvas by collapsing the inspector.
- Selected clip state uses more than color: segment treatment, label, and inspector/selection text.
- The proposed layouts fit the four stated viewports without horizontal document overflow.

## What was not verified

- No native iPadOS or macOS target exists or was run.
- No real import, arrange, preview, export, undo, redo, save, restore, sync, error, or interruption behavior was exercised.
- No touch, Pencil, pointer, keyboard, menu, command, focus, hover, context menu, drag/drop, resize, or multi-window behavior was exercised natively.
- No VoiceOver accessibility tree or full keyboard path was inspected.
- No Dynamic Type, text scaling, pseudo-localization, RTL, appearance mode, increased contrast, or Reduce Motion native run was recorded.
- No minimum OS versions, framework fallbacks, performance, or export integrity were tested.
- Static HTML controls are visual evidence only and do not claim production semantics.

## Supported completion stage

**Supported:** layout design complete, pending user acceptance.

**Not supported:** direction aligned, native prototype complete, code complete for a product target, experience verified, or user accepted.

The four layouts are one bounded adaptation proposal. The user has not yet visually confirmed it.

## Native acceptance path

After minimum iPadOS and macOS versions are decided:

1. Implement the shared radial data model and four complete tasks in a scoped native prototype.
2. Run iPad compact and expansive windows in Simulator or on device. Resize between them while a clip is selected and an inspector field is being edited. Confirm selection, playhead, undo history, edit state, and transport remain intact.
3. On iPad, complete import → select → move → resize duration → undo/redo → preview → export once with touch, once with hardware keyboard and pointer, and once with VoiceOver. Exercise Pencil precision editing on supported hardware or document the unavailable hardware gap.
4. Run a real Mac app at 900 × 640, 1440 × 900, and at least one intermediate live resize. Complete the same task using pointer, then keyboard only.
5. On Mac, verify File/Edit/Clip/View/Playback menus, enabled states, shortcuts, visible focus, hover, context menus, Escape behavior, undo/redo, drag/drop alternatives, and focus restoration after sheets and window switching.
6. Enable Reduce Motion on both platforms. Record direct manipulation and a programmatic jump. Confirm temporal position, playhead, and selection remain clear without large spatial travel.
7. Run VoiceOver on both targets. Confirm the ordered clip list, current selection, start, duration, adjustable actions, transport state, errors, and export progress are announced and operable.
8. Test largest supported text size or text scaling, long localized labels, pseudo-localization, RTL if supported, increased contrast, and light/dark appearances. Confirm critical actions stay reachable.
9. Exercise failed import and failed export, cancellation, retry, interruption, project reopen, and transferred-project restoration. Confirm arrangement data is unchanged after failure.
10. Preserve screenshots for static states and recordings for resize, input, focus, commands, motion, and recovery. Only then claim the exercised environments “experience verified.”

## User visual acceptance path

Review the four PNGs in this order:

1. `ipad-compact.png`: confirm the ring still feels like the editor—not a preview above a mobile form—and that Clips/Edit switching is an acceptable compact compromise.
2. `ipad-expansive.png`: confirm library, ring, and inspector coexist without weakening the radial model.
3. `mac-minimum.png`: confirm the collapsed inspector still leaves import, precise editing access, preview, undo/redo, and export discoverable.
4. `mac-expanded.png`: confirm the denser workspace feels appropriate for sustained pointer/keyboard editing and not like an enlarged iPad.

Acceptance question: **Does this hierarchy preserve the radial timeline as OrbitCut’s central editing model while making the surrounding workspace feel native to iPad and Mac?**
