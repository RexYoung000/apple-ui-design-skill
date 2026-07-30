# Liquid Glass Source Verification - 2026-07-30

## Question

Can an existing app with an iOS 17.0 deployment target treat SwiftUI Liquid Glass as an available enhancement, and does that availability justify making it the default visual direction?

## Official Source

- Page: [glassEffect(_:in:) | Apple Developer Documentation](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:))
- Accessed: 2026-07-30
- Published claim used: the modifier applies Liquid Glass to a view and is available on iOS 26.0 and newer.
- Published behavior also observed: the default uses regular glass with a capsule shape.

This exact API page supports availability and API behavior. It does not establish product fit, visual quality, accessibility, performance, or user acceptance.

## Project and Runtime Scope

- Project minimum: iOS 17.0
- Enhancement availability: iOS 26.0+
- Toolchain: Xcode 26.6 (17F113)
- SDK: iPhoneSimulator 26.5
- Compile target: arm64-apple-ios17.0-simulator

The unguarded fixture failed type checking with the expected iOS 26 availability error. The guarded fixture passed type checking with:

- `if #available(iOS 26.0, *)`;
- `glassEffect()` in the enhanced branch;
- a regular-material capsule in the fallback branch.

## Decision

The API claim and guarded fallback are compile-verified. Liquid Glass remains an optional enhancement candidate rather than the default direction because API availability does not answer whether the material fits the product or its users.

## Remaining Evidence

This run does not verify:

- rendered appearance on representative content;
- behavior on iOS 17.5 and iOS 26.5 simulators;
- Reduce Transparency, contrast, accessibility, motion, or input behavior;
- performance or user acceptance.
