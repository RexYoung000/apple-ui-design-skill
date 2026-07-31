# Apple Platform Adaptation

## Load When

Load this reference when more than one Apple platform or platform-specific hierarchy, navigation, windowing, input, continuity, or system behavior affects the result. Do not load it for a single-platform task with no adaptation decision.

This is the single runtime source for cross-platform translation.

## Contents

- Shared product and platform roles
- Adaptation questions
- iOS, iPadOS, and macOS expression
- Responsive and adaptive logic
- Navigation translation
- Platform fit check

## Shared Product, User-Defined Platform Roles

Start with the user’s product definition. Do not assume:

- every platform is required;
- feature parity is desirable;
- Mac is an enlarged iPad;
- iPad is an enlarged iPhone;
- one platform must be primary;
- platform differences must exist for their own sake.

Establish the shared task and data model, then decide how each target platform should express it.

## Cross-Platform Adaptation Questions

For each platform in scope, consider:

- What tasks occur most often and under what conditions?
- Is the user operating briefly, continuously, or in parallel with other work?
- How much information should be visible simultaneously?
- Which input methods must be first-class?
- Does the user need multi-window, drag and drop, menus, commands, or shortcuts?
- How does the interface resize or move between compact and expansive contexts?
- Which tasks benefit from continuity across devices?
- Which capabilities are absent by product choice rather than technical limitation?

Only ask the user when the answer changes the product. Otherwise derive the answer from current requirements and platform context.

## iOS

Common design concerns:

- one-handed and brief interactions;
- compact navigation and clear back/dismiss behavior;
- touch reliability, safe areas, keyboard avoidance, and interruption recovery;
- portrait-first or orientation-specific needs defined by the product;
- sheets, full-screen flows, tabs, search, and context menus used according to task depth;
- notifications, haptics, camera, share, and other system integrations only when in scope.

Do not reduce mobile design to stacked cards. Use hierarchy, grouping, disclosure, typography, and navigation deliberately.

## iPadOS

Treat iPad as a flexible workspace, not merely a larger canvas:

- support compact and expansive widths relevant to the product;
- consider split views, inspectors, sidebars, toolbars, and multi-window workflows;
- account for touch, keyboard, trackpad, pointer, drag and drop, and focus where applicable;
- decide which information can coexist rather than adding empty margins;
- keep primary actions reachable and understandable in changing window sizes.

Do not add columns when the product does not benefit from simultaneous context.

## macOS

Treat the Mac as a windowed, keyboard-and-pointer environment:

- define minimum, default, and useful expanded window behavior;
- design focus order, keyboard navigation, shortcuts, commands, and menu placement;
- use toolbars, sidebars, inspectors, tables, context menus, sheets, panels, and multiple windows according to task structure;
- account for hover, selection, multi-selection, drag and drop, undo/redo, and persistent workspace state when relevant;
- distinguish application commands from in-content controls;
- avoid hiding critical actions behind touch-oriented patterns.

Do not make every control permanently visible merely because space exists.

## Responsive and Adaptive Logic

Prefer semantic layout rules over device-name branching:

- content priority;
- minimum readable measure;
- available width and height;
- number of simultaneous task contexts;
- input method;
- windowing and presentation environment;
- Dynamic Type or accessibility size;
- locale and content expansion.

Use platform checks only when behavior is genuinely platform-specific.

## Navigation Translation

Preserve task structure, not screen geometry.

Examples:

- an iPhone push flow may become a sidebar-content-detail structure on iPad or Mac;
- a mobile full-screen editor may become an inspector or independent window on Mac;
- a mobile action sheet may become a menu, toolbar item, or contextual command;
- a long mobile list may become a table only when comparison, columns, or multi-selection benefits the task.

Every translation must keep state, selection, dismissal, recovery, and deep-link behavior understandable.

## Platform Fit Check

Before approval, verify:

- the platform’s intended tasks are explicit;
- interaction works with required input methods;
- navigation and presentation are predictable;
- resizing does not reveal a stretched mobile layout;
- shared brand DNA is visible without forcing identical components;
- unsupported capabilities are intentional and documented;
- minimum-version behavior remains complete.
