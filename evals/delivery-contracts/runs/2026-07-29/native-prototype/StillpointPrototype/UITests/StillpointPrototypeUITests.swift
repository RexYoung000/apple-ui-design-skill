import XCTest

final class StillpointPrototypeUITests: XCTestCase {
    override func setUpWithError() throws {
        continueAfterFailure = false
    }

    func testInterruptionReversalAndFinalIntent() throws {
        let app = XCUIApplication()
        app.launchArguments = ["-prototypeState", "collapsed"]
        app.launch()

        let card = app.buttons.matching(
            NSPredicate(format: "label == %@", "Write product brief")
        ).firstMatch
        XCTAssertTrue(card.waitForExistence(timeout: 3))
        XCTAssertEqual(card.value as? String, "Collapsed, Focusing")

        card.tap(withNumberOfTaps: 3, numberOfTouches: 1)

        let pause = app.buttons.matching(
            NSPredicate(format: "label == %@", "Pause")
        ).firstMatch
        XCTAssertTrue(pause.waitForExistence(timeout: 2))
        XCTAssertTrue(pause.isHittable)
        XCTAssertEqual(card.value as? String, "Expanded, Focusing")
        pause.tap()
        XCTAssertEqual(card.value as? String, "Expanded, Paused")

        app.buttons.matching(
            NSPredicate(format: "label == %@", "Finish")
        ).firstMatch.tap()
        XCTAssertEqual(card.value as? String, "Expanded, Completed")
    }
}
