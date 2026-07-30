import SwiftUI

struct GuardedGlassEffectView: View {
    var body: some View {
        if #available(iOS 26.0, *) {
            Text("Verified")
                .padding()
                .glassEffect()
        } else {
            Text("Verified")
                .padding()
                .background(.regularMaterial, in: Capsule())
        }
    }
}
