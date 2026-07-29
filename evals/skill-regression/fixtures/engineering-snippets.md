# Implementation-only engineering requests

## SwiftUI compilation

An existing view fails with `Type of expression is ambiguous without a type annotation` inside a generic `ViewBuilder`. The user wants the compiler error diagnosed and fixed.

## AppKit performance

An `NSWindowController` and its view model remain alive after every window closes. The user wants the retain cycle located with memory diagnostics.

## XCTest infrastructure

UI tests fail during launch because the test target cannot find its host application. The user wants the Xcode target and CI configuration repaired.

No product, visual, adaptation, or review outcome is requested in these cases.
