import SwiftUI

@main
struct StillpointPrototypeApp: App {
    var body: some Scene {
        WindowGroup {
            SessionPrototypeView()
        }
    }
}

private enum SessionStatus: String {
    case focusing = "Focusing"
    case paused = "Paused"
    case completed = "Completed"
}

private struct SessionPrototypeView: View {
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    @State private var isExpanded: Bool
    @State private var sessionStatus: SessionStatus
    @State private var feedback = "Tap the card to reveal session actions."
    @State private var reducedMotionFeedbackVisible = false

    init() {
        let arguments = ProcessInfo.processInfo.arguments
        let requestedState = arguments.value(after: "-prototypeState") ?? "collapsed"
        _isExpanded = State(initialValue: requestedState != "collapsed")
        _sessionStatus = State(
            initialValue: requestedState == "paused"
                ? .paused
                : requestedState == "completed" ? .completed : .focusing
        )
    }

    var body: some View {
        ZStack {
            Color(red: 0.925, green: 0.914, blue: 0.878)
                .ignoresSafeArea()

            VStack(alignment: .leading, spacing: 24) {
                header

                sessionCard

                Text(feedback)
                    .font(.footnote)
                    .foregroundStyle(Color.primary.opacity(0.58))
                    .fixedSize(horizontal: false, vertical: true)
                    .accessibilityIdentifier("Feedback")

                Spacer(minLength: 16)
            }
            .padding(.horizontal, 22)
            .padding(.top, 34)
        }
    }

    private var header: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text("STILLPOINT")
                .font(.caption.weight(.semibold))
                .tracking(2.4)
                .foregroundStyle(Color(red: 0.29, green: 0.33, blue: 0.27))

            Text("A quieter place to focus.")
                .font(.title2.weight(.medium))
                .foregroundStyle(Color(red: 0.13, green: 0.15, blue: 0.12))

            Text(reduceMotion ? "Motion: Reduce Motion" : "Motion: Standard")
                .font(.caption)
                .foregroundStyle(Color.primary.opacity(0.55))
                .accessibilityIdentifier("MotionMode")
        }
    }

    private var sessionCard: some View {
        VStack(spacing: 0) {
            Button(action: toggleExpanded) {
                HStack(spacing: 16) {
                    VStack(alignment: .leading, spacing: 8) {
                        Text(statusEyebrow)
                            .font(.caption.weight(.semibold))
                            .foregroundStyle(statusColor)

                        Text("Write product brief")
                            .font(.title3.weight(.semibold))
                            .foregroundStyle(Color(red: 0.12, green: 0.14, blue: 0.11))
                            .multilineTextAlignment(.leading)

                        if sessionStatus != .completed {
                            Text(sessionStatus == .paused ? "24:18 remaining" : "24:18")
                                .font(.system(.title, design: .rounded, weight: .medium))
                                .monospacedDigit()
                                .foregroundStyle(Color(red: 0.24, green: 0.27, blue: 0.22))
                        } else {
                            Text("Session complete")
                                .font(.headline)
                                .foregroundStyle(Color(red: 0.24, green: 0.27, blue: 0.22))
                        }
                    }

                    Spacer(minLength: 12)

                    Image(systemName: isExpanded ? "chevron.up" : "chevron.down")
                        .font(.body.weight(.semibold))
                        .foregroundStyle(Color(red: 0.29, green: 0.33, blue: 0.27))
                        .frame(width: 44, height: 44)
                }
                .contentShape(Rectangle())
                .padding(.horizontal, 20)
                .padding(.vertical, 18)
            }
            .buttonStyle(QuietPressStyle())
            .accessibilityIdentifier("SessionCard")
            .accessibilityLabel("Write product brief")
            .accessibilityValue(isExpanded ? "Expanded, \(sessionStatus.rawValue)" : "Collapsed, \(sessionStatus.rawValue)")
            .accessibilityHint(isExpanded ? "Double tap to collapse session actions." : "Double tap to reveal session actions.")

            if isExpanded {
                VStack(spacing: 16) {
                    Divider()
                        .overlay(Color.black.opacity(0.10))

                    HStack(spacing: 10) {
                        actionButton(
                            title: sessionStatus == .paused ? "Resume" : "Pause",
                            systemImage: sessionStatus == .paused ? "play.fill" : "pause.fill"
                        ) {
                            sessionStatus = sessionStatus == .paused ? .focusing : .paused
                            feedback = sessionStatus == .paused
                                ? "Session paused. Your remaining time is unchanged."
                                : "Session resumed."
                        }

                        actionButton(title: "Finish", systemImage: "checkmark") {
                            sessionStatus = .completed
                            feedback = "Session completed locally for this prototype."
                        }

                        actionButton(title: "Note", systemImage: "square.and.pencil") {
                            feedback = "Note action acknowledged; editing is outside this prototype."
                        }
                    }

                    Text(sessionStatus == .completed
                         ? "You can collapse the card when you are ready."
                         : "Session actions stay anchored to this card.")
                        .font(.footnote)
                        .foregroundStyle(Color.primary.opacity(0.58))
                        .frame(maxWidth: .infinity, alignment: .leading)
                }
                .padding(.horizontal, 20)
                .padding(.bottom, 20)
                .transition(
                    reduceMotion
                        ? .opacity
                        : .asymmetric(
                            insertion: .opacity.combined(with: .offset(y: -8)),
                            removal: .opacity.combined(with: .offset(y: -4))
                        )
                )
            }
        }
        .background(
            RoundedRectangle(cornerRadius: 28, style: .continuous)
                .fill(Color(red: 0.985, green: 0.980, blue: 0.958))
                .shadow(color: Color.black.opacity(0.08), radius: 22, y: 12)
        )
        .overlay(
            RoundedRectangle(cornerRadius: 28, style: .continuous)
                .stroke(Color(red: 0.29, green: 0.40, blue: 0.26), lineWidth: 2)
                .opacity(reducedMotionFeedbackVisible ? 0.34 : 0)
                .animation(.easeOut(duration: 0.16), value: reducedMotionFeedbackVisible)
        )
        .clipShape(RoundedRectangle(cornerRadius: 28, style: .continuous))
    }

    private var statusEyebrow: String {
        switch sessionStatus {
        case .focusing: "CURRENT FOCUS"
        case .paused: "PAUSED"
        case .completed: "COMPLETED"
        }
    }

    private var statusColor: Color {
        switch sessionStatus {
        case .focusing: Color(red: 0.29, green: 0.40, blue: 0.26)
        case .paused: Color(red: 0.55, green: 0.36, blue: 0.14)
        case .completed: Color(red: 0.20, green: 0.38, blue: 0.32)
        }
    }

    private func toggleExpanded() {
        if reduceMotion {
            var transaction = Transaction(animation: nil)
            transaction.disablesAnimations = true
            withTransaction(transaction) {
                isExpanded.toggle()
            }

            reducedMotionFeedbackVisible = true
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.03) {
                reducedMotionFeedbackVisible = false
            }
        } else {
            withAnimation(.easeInOut(duration: 0.38)) {
                isExpanded.toggle()
            }
        }

        feedback = isExpanded
            ? "Session actions revealed."
            : "Session actions hidden."
    }

    private func actionButton(
        title: String,
        systemImage: String,
        action: @escaping () -> Void
    ) -> some View {
        Button(action: action) {
            VStack(spacing: 7) {
                Image(systemName: systemImage)
                    .font(.body.weight(.semibold))
                Text(title)
                    .font(.caption.weight(.medium))
                    .lineLimit(1)
                    .minimumScaleFactor(0.8)
            }
            .frame(maxWidth: .infinity, minHeight: 52)
            .foregroundStyle(Color(red: 0.20, green: 0.24, blue: 0.19))
            .background(
                RoundedRectangle(cornerRadius: 16, style: .continuous)
                    .fill(Color(red: 0.89, green: 0.90, blue: 0.83))
            )
            .contentShape(Rectangle())
        }
        .buttonStyle(QuietPressStyle())
        .accessibilityIdentifier("\(title)Action")
        .accessibilityLabel(title)
    }
}

private struct QuietPressStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .opacity(configuration.isPressed ? 0.72 : 1)
    }
}

private extension Array where Element == String {
    func value(after flag: String) -> String? {
        guard let index = firstIndex(of: flag), indices.contains(index + 1) else {
            return nil
        }
        return self[index + 1]
    }
}
