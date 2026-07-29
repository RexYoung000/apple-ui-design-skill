const { chromium } = require("playwright-core");
const fs = require("fs");
const path = require("path");
const { pathToFileURL } = require("url");

const runRoot = path.resolve(__dirname, "..");
const prototypeUrl = pathToFileURL(path.join(runRoot, "prototype", "index.html")).href;
const evidenceDir = path.join(runRoot, "evidence");
const chromePath = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const results = [];
let browser;

function record(pathName, operation, expected, observed) {
  results.push({
    path: pathName,
    operation,
    expected,
    observed,
    passed: expected === observed
  });
}

async function expectState(page, pathName, expected) {
  await page.waitForFunction(value => {
    const app = document.querySelector("#app");
    return app && app.dataset.state === value;
  }, expected);
  const observed = await page.locator("#app").getAttribute("data-state");
  record(pathName, `Reach ${expected}`, expected, observed);
}

async function reset(page) {
  await page.getByRole("button", { name: "Reset", exact: true }).click();
  await expectState(page, "setup", "welcome");
}

async function capture(page, filename) {
  await page.waitForTimeout(260);
  await page.screenshot({ path: path.join(evidenceDir, filename), fullPage: true });
}

async function reachPermission(page, pathName) {
  await page.getByRole("button", { name: "Get started" }).click();
  await expectState(page, pathName, "explanation");
  await page.getByRole("button", { name: "Choose photos" }).click();
  await expectState(page, pathName, "permission");
}

async function allowToSelection(page, pathName) {
  await page.getByRole("button", { name: "Allow selected photos" }).click();
  await expectState(page, pathName, "limited");
  await page.getByRole("button", { name: "Continue" }).click();
  await expectState(page, pathName, "selection");
}

async function selectPhotos(page, pathName, ids) {
  const disabled = await page.getByRole("button", { name: /Import selected/ }).isDisabled();
  record(pathName, "Import action before selection", "disabled", disabled ? "disabled" : "enabled");
  for (const id of ids) {
    await page.getByRole("button", { name: `Reference photo ${id}` }).click();
  }
  const summary = await page.locator("#selection-summary").textContent();
  record(pathName, "Selection count", `${ids.length} selected`, summary.trim());
}

async function importAndWait(page, pathName, expectedEnd) {
  await page.getByRole("button", { name: /Import \d+ selected/ }).click();
  await expectState(page, pathName, "importing");
  await expectState(page, pathName, expectedEnd);
}

(async () => {
  fs.mkdirSync(evidenceDir, { recursive: true });
  browser = await chromium.launch({
    executablePath: chromePath,
    headless: true
  });
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 1,
    reducedMotion: "no-preference"
  });
  const page = await context.newPage();
  await page.goto(prototypeUrl);
  await expectState(page, "initial", "welcome");
  await capture(page, "01-welcome.png");

  // Happy path.
  await reachPermission(page, "happy path");
  const modalLabel = await page.getByRole("dialog").locator(".dialog-system-label").textContent();
  record("happy path", "Permission handoff boundary label", "Simulated iOS permission handoff", modalLabel.trim());
  await allowToSelection(page, "happy path");
  await selectPhotos(page, "happy path", [1, 2, 3]);
  await importAndWait(page, "happy path", "complete");
  const completionCopy = await page.getByText("Only the photos you selected were imported.").isVisible();
  record("happy path", "Completion privacy confirmation", "visible", completionCopy ? "visible" : "missing");
  await capture(page, "02-happy-completion.png");

  // Permission denial and retry.
  await reset(page);
  await reachPermission(page, "permission denial + retry");
  await page.getByRole("button", { name: "Don’t allow" }).click();
  await expectState(page, "permission denial + retry", "denied");
  const deniedCopy = await page.getByText("No photos were selected or imported.").isVisible();
  record("permission denial + retry", "Denial truthfulness", "visible", deniedCopy ? "visible" : "missing");
  await capture(page, "03-permission-denied.png");
  await page.getByRole("button", { name: "Try again" }).click();
  await expectState(page, "permission denial + retry", "permission");
  await allowToSelection(page, "permission denial + retry");
  await selectPhotos(page, "permission denial + retry", [2]);
  await importAndWait(page, "permission denial + retry", "complete");
  await capture(page, "04-denial-retry-completion.png");

  // Recoverable import failure and retry.
  await reset(page);
  await page.getByLabel("Choose next simulated import result").selectOption("failure");
  await reachPermission(page, "import failure + retry");
  await allowToSelection(page, "import failure + retry");
  await selectPhotos(page, "import failure + retry", [4, 5]);
  await importAndWait(page, "import failure + retry", "failure");
  const failureCopy = await page.getByText("Your 2 selections are still ready.").isVisible();
  record("import failure + retry", "Selection preserved in failure copy", "visible", failureCopy ? "visible" : "missing");
  await capture(page, "05-import-failure.png");
  await page.getByRole("button", { name: "Retry import" }).click();
  await expectState(page, "import failure + retry", "importing");
  await expectState(page, "import failure + retry", "complete");
  await capture(page, "06-failure-retry-completion.png");

  // Cancellation and state preservation.
  await reset(page);
  await reachPermission(page, "cancellation");
  await page.getByRole("button", { name: "Don’t allow" }).click();
  await page.getByRole("button", { name: "Not now" }).click();
  await expectState(page, "cancellation", "welcome");

  await reachPermission(page, "cancellation");
  await allowToSelection(page, "cancellation");
  await page.getByRole("button", { name: "Cancel", exact: true }).click();
  await expectState(page, "cancellation", "explanation");

  await page.getByRole("button", { name: "Choose photos" }).click();
  await page.getByRole("button", { name: "Allow selected photos" }).click();
  await page.getByRole("button", { name: "Continue" }).click();
  await page.getByRole("button", { name: "Reference photo 6" }).click();
  await page.getByRole("button", { name: /Import 1 selected/ }).click();
  await expectState(page, "cancellation", "importing");
  await page.getByRole("button", { name: "Cancel import" }).click();
  await expectState(page, "cancellation", "selection");
  const preserved = await page.locator("#selection-summary").textContent();
  record("cancellation", "Selection after cancelling import", "1 selected", preserved.trim());
  await capture(page, "07-cancelled-import-selection.png");

  // Keyboard/focus behavior for the mocked modal.
  await reset(page);
  await page.getByRole("button", { name: "Get started" }).click();
  const chooseButton = page.getByRole("button", { name: "Choose photos" });
  await chooseButton.focus();
  await page.keyboard.press("Enter");
  await expectState(page, "keyboard + focus", "permission");
  const focusedName = await page.evaluate(() => document.activeElement.textContent.trim());
  record("keyboard + focus", "Initial modal focus", "Allow selected photos", focusedName);
  await page.keyboard.press("Escape");
  const stateAfterEscape = await page.locator("#app").getAttribute("data-state");
  record("keyboard + focus", "Escape dismisses modal", "explanation", stateAfterEscape);
  const restoredName = await page.evaluate(() => document.activeElement.textContent.trim());
  record("keyboard + focus", "Focus returns to trigger", "Choose photos", restoredName);

  // Reduced-motion expression is active and the path remains operable.
  const reducedContext = await browser.newContext({
    viewport: { width: 390, height: 844 },
    reducedMotion: "reduce"
  });
  const reducedPage = await reducedContext.newPage();
  await reducedPage.goto(prototypeUrl);
  const animationDuration = await reducedPage.locator(".screen").evaluate(element => getComputedStyle(element).animationDuration);
  record("reduced motion", "Screen transition duration", "1e-06s", animationDuration);
  await reducedPage.getByRole("button", { name: "Get started" }).click();
  await expectState(reducedPage, "reduced motion", "explanation");
  await capture(reducedPage, "08-reduced-motion-explanation.png");
  await reducedContext.close();

  await context.close();
  await browser.close();

  const failed = results.filter(item => !item.passed);
  const report = {
    generatedAt: new Date().toISOString(),
    environment: {
      medium: "HTML interaction prototype",
      browser: "Google Chrome headless via Playwright Core",
      viewport: "390x844 CSS pixels",
      deviceScaleFactor: 1,
      nativeRuntime: false
    },
    summary: {
      checks: results.length,
      passed: results.length - failed.length,
      failed: failed.length
    },
    results
  };
  fs.writeFileSync(path.join(evidenceDir, "operations-tested.json"), JSON.stringify(report, null, 2) + "\n");

  if (failed.length) {
    console.error(JSON.stringify(failed, null, 2));
    process.exitCode = 1;
  } else {
    console.log(`All ${results.length} checks passed.`);
  }
})().catch(error => {
  console.error(error);
  if (browser) {
    browser.close().catch(() => {});
  }
  process.exitCode = 1;
});
