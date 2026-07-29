# OrbitCut platform adaptation decision matrix

## Source and target scope

| Item | iPhone source | iPad target | Mac target |
|---|---|---|---|
| Product role | Established complete editor | Complete editor in compact and expansive windows | Complete windowed editor |
| Required tasks | Import, arrange, preview, export | Same tasks independently completable | Same tasks independently completable |
| Material environments | Existing product; not reproduced in this package | Compact 744 × 900; expansive 1366 × 1024 | Minimum 900 × 640; expanded 1440 × 900 |
| First-class inputs | Touch | Touch, Pencil, pointer, keyboard | Pointer, keyboard |
| Evidence in this package | Fixture description only | Static browser layouts | Static browser layouts |

The product brief does not define minimum iPadOS or macOS versions. This adaptation therefore avoids version-gated materials or APIs and records version selection as an implementation prerequisite. All exact dimensions, colors, type sizes, spacing, and radii shown here are rendered proposals for visual acceptance.

## Shared versus platform-specific decisions

| Decision area | Shared product DNA and task meaning | iPad expression | Mac expression | Evidence / status |
|---|---|---|---|---|
| Primary model | The radial timeline communicates temporal relationship and remains the primary editing surface. Selection, playhead position, duration, and loop boundary retain the same meaning. | Ring owns the center of the workspace. Compact mode moves secondary controls below rather than shrinking the ring into a sidebar. Expansive mode adds simultaneous library and inspector context. | Ring owns the center work area. Sidebars and inspector support it; they never replace it with a linear timeline. | Visible in all four rendered layouts; interaction unverified. |
| Core completion | Import, arrange, preview, and export are independently completable. | Import and Export remain in the top bar. Arrange controls live next to the ring or in the selected-clip sheet. Preview remains in persistent transport. | Import and Export remain in the toolbar. Arrange has contextual inspector and keyboard commands. Preview remains in persistent transport. | Actions are visibly present in all layouts; task execution unverified. |
| Navigation | Project, media, current selection, and export state use shared terminology. | Compact: one workspace with a mode switch for Clips / Edit; selected clip details appear in an anchored bottom inspector. Expansive: library, canvas, and inspector coexist. | Window uses sidebar, center canvas, and inspector. Sidebar and inspector can collapse to protect canvas width. | Static hierarchy rendered. Collapse behavior unverified. |
| Density | Temporal readability outranks showing every control. | Touch-friendly controls and fewer simultaneous fields in compact mode; expanded mode exposes clip library and inspector together. | Denser metadata, smaller pointer targets, hover affordances, and persistent keyboard hints. | Static density rendered. Input suitability unverified. |
| Selection | Selected segment is identified by color, outline, label, and inspector title; color is not the only cue. | Tap or Pencil tap selects; pointer click selects; selection opens/updates the inspector. | Click selects; Shift-click extends selection only if multi-select is approved during native implementation. Focus and selection remain visually distinct. | Visual selected state rendered; semantics unverified. |
| Arrange | Direct manipulation of the ring remains central. Explicit numeric editing is an equivalent path, not a replacement. | One-finger rotate, Pencil drag, pointer drag; keyboard nudges selected clip. Pinch changes timeline scale, not clip duration. | Drag around ring; arrow-key nudge; inspector fields for exact start and duration. Scroll-wheel zoom requires modifier to avoid accidental edits. | Mapping specified; no native input run. |
| Preview | Playhead movement retains spatial meaning. Preview never hides selection. | Space bar when hardware keyboard is present; prominent play/pause transport for touch. | Space toggles preview while canvas has editing focus; menu command remains discoverable. | Controls rendered; playback unverified. |
| Undo / redo | Edit history is explicit and reversible. | Toolbar Undo/Redo plus Command-Z / Shift-Command-Z. Disabled state must be announced. | Edit menu commands, toolbar Undo/Redo, shortcuts, and visible history state. | Controls rendered; command wiring unverified. |
| Import | Adds clips without replacing the current project. | Import control accepts system picker and drag/drop where supported. Dropped items preview insertion before committing. | Toolbar and File menu import; drag/drop onto library or ring with explicit insertion feedback. | Control/drop zones rendered; system integration unverified. |
| Export | Export is a clear, independent completion action and preserves current edits. | Top trailing action opens export configuration as a sheet/popover appropriate to width. | Toolbar and File menu command opens a document-modal sheet; export progress remains attached to the project window. | Action rendered; presentation/export unverified. |
| Windowing | Project state survives resize and restoration. | Compact mode reflows: inspector moves below canvas, library becomes a switchable panel, transport remains reachable. Expansive mode shows three contexts. Separate project windows are optional and not claimed. | Minimum window collapses inspector before reducing radial canvas below its readable floor. Expanded window shows three contexts. Each project can occupy an independent window; this is a proposed implementation decision. | Four fixed environments rendered; live resize/restoration unverified. |
| Menus / commands | Command names and enabled states match visible actions. | Hardware keyboard commands: Space preview; arrows nudge; Command-Z undo; Shift-Command-Z redo; Command-I import; Command-E export. Command discoverability should use keyboard shortcut hints in menus. | File, Edit, Clip, View, and Playback menus expose the same task model. Context menu: split, duplicate, replace, remove; destructive remove is separated. | Hints rendered; native menu/command behavior unverified. |
| Hover / focus | Hover never carries unique information; focus is visible and independent from selection. | Pointer hover reveals resize/grab affordance but does not hide touch controls. Keyboard focus ring follows logical task order. | Hover reveals segment handle and concise metadata. Keyboard focus ring is persistent when navigating; Escape returns from inspector to canvas without clearing selection. | Visual examples rendered; pointer/focus traversal unverified. |
| Accessibility | VoiceOver and keyboard-equivalent paths must complete import, arrange, preview, and export. Ring exposes an ordered clip list plus adjustable selected clip semantics. | Rotor/group structure: toolbar, radial timeline, clip list, inspector, transport. Adjustable action changes start time; named actions move before/after neighboring clip. | Same semantic grouping; menu commands and inspector fields provide exact equivalents. Full keyboard path and visible focus are mandatory. | Requirements specified only; accessibility tree not implemented. |
| Motion | Timeline movement communicates temporal position. Selection and playhead remain perceptible. | Direct manipulation follows input. With Reduce Motion, use a short cross-fade/state update and minimal angular travel rather than a full ring sweep. | Pointer/keyboard edits update position with restrained interpolation. With Reduce Motion, avoid large rotational travel; retain playhead and selection transition. | Static before/after intent only; native recording required. |
| Localization | User-visible strings and time values remain localizable. Layout tolerates longer labels and RTL where required. | Compact actions may use icon plus accessible name only when width is constrained; critical Export keeps text where practical. Ring ordering follows time, while surrounding chrome mirrors for RTL. | Menus and inspector labels allow expansion; numeric fields use locale-aware formatting; shortcut meaning does not depend on label width. | English representative content rendered; pseudo-localization/RTL unverified. |
| Continuity | Project content may move between devices; sync is outside this prototype. | Opening a transferred project restores clip order, timings, loop length, and last valid selection when available. | Same data meaning. Window geometry is device-local and does not travel with the project. | Data contract proposed; transfer not implemented. |
| Errors and recovery | Failed import/export never corrupts the arrangement; user can retry or cancel. | Error appears near the initiating sheet plus persistent project state. | Sheet or window-attached alert retains project focus and offers retry/reveal details. | Specified, not rendered in the representative normal state. |

## Input and equivalent-path mapping

| Intent | iPhone precedent | iPad touch / Pencil | iPad pointer / keyboard | Mac pointer / keyboard | Accessible equivalent |
|---|---|---|---|---|---|
| Select a clip | Tap segment | Tap; Pencil tap | Click; Tab to ordered clip list then Return | Click; Tab/arrow through ordered clips | VoiceOver ordered clip list announces name, start, duration, selected state |
| Move in time | Touch rotation | Drag segment around ring; Pencil offers precision | Drag; arrows nudge; Shift-arrows coarse nudge | Drag; arrows nudge; inspector start field | Adjustable action plus “Move earlier/later” named actions |
| Change timeline scale | Pinch | Pinch canvas | Command-plus/minus; pointer zoom control | Command-plus/minus; toolbar zoom | Named Zoom In / Zoom Out actions |
| Change clip duration | Explicit editing control | Drag segment end handle or inspector field | Pointer handle; inspector field; keyboard increment | Pointer handle; inspector field; keyboard increment | Adjustable duration field with current value |
| Preview loop | Explicit control | Tap play/pause | Space or transport control | Space, Playback menu, transport control | Button announces Play/Pause and preview state |
| Undo / redo | Explicit undo | Toolbar controls | Toolbar plus shortcuts | Edit menu, toolbar, shortcuts | Named buttons and menu items with enabled state |
| Import | Explicit action | Tap Import; drop onto library | Command-I; drop onto library | File menu; Command-I; drop onto library or ring | Import button/menu opens system picker |
| Export | Explicit action | Tap Export | Command-E or Export control | File menu; Command-E; toolbar action | Export action opens labelled configuration and progress |

## Responsive layout rules

1. Protect the radial canvas before secondary panels. The layout collapses the inspector, then the library, before reducing the ring below its readable floor.
2. iPad compact uses one simultaneous secondary context: clip library or selected-clip inspector. The canvas and transport remain present.
3. iPad expansive and Mac expanded show library, canvas, and inspector simultaneously because arranging benefits from source, composition, and precise properties being visible together.
4. Mac minimum keeps the library visible, collapses the inspector, and exposes precise editing through a toolbar button or context panel.
5. Transport remains attached to the canvas in all environments so preview is not mistaken for a global project action.
6. Resizing preserves selected clip, playhead, zoom, undo history, and current editing field. No control relocation may commit or cancel an edit silently.

## Minimum-version and fallback implications

- Minimum iPadOS and macOS versions are **not supplied** and must be decided before implementation.
- Core behavior must use APIs available at the selected baselines. Newer materials, hover effects, Pencil features, or window APIs may enhance but must not gate import, arrange, preview, or export.
- When Pencil-specific hover is unavailable, selection and precision editing still work through tap/drag and the inspector.
- When multiple windows are unavailable or out of scope, a single project window remains complete.
- When drag and drop is unavailable, Import and Replace remain explicit controls.
- When Reduce Motion is enabled, direct manipulation remains immediate while programmatic movement uses minimal travel or cross-fade.
