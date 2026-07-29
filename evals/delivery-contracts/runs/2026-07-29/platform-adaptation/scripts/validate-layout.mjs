import { execFileSync } from "node:child_process";
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const runDirectory = resolve(scriptDirectory, "..");
const prototypeUrl = pathToFileURL(resolve(runDirectory, "prototype/index.html")).href;
const evidencePath = resolve(runDirectory, "evidence/layout-checks.json");
const chromePath = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

const targets = [
  { mode: "ipad-compact", width: 744, height: 900, library: false, inspector: false, compactInspector: true },
  { mode: "ipad-expansive", width: 1366, height: 1024, library: true, inspector: true, compactInspector: false },
  { mode: "mac-minimum", width: 900, height: 640, library: true, inspector: false, compactInspector: false },
  { mode: "mac-expanded", width: 1440, height: 900, library: true, inspector: true, compactInspector: false }
];

const results = targets.map((target) => {
  // On macOS, Chrome's headless dump-DOM viewport is 87 px shorter than the
  // requested screenshot/window height. Screenshot pixel dimensions are
  // verified separately with sips.
  let html = "";
  for (let attempt = 0; attempt < 2; attempt += 1) {
    html = execFileSync(chromePath, [
      "--headless=new",
      "--disable-gpu",
      "--hide-scrollbars",
      "--force-device-scale-factor=1",
      `--window-size=${target.width},${target.height}`,
      "--virtual-time-budget=1000",
      "--dump-dom",
      `${prototypeUrl}?mode=${target.mode}`
    ], { encoding: "utf8", maxBuffer: 10 * 1024 * 1024 });
    if (html.includes('id="layout-evidence"')) break;
  }

  const match = html.match(/<script type="application\/json" id="layout-evidence">([^<]+)<\/script>/);
  if (!match) throw new Error(`No layout evidence found for ${target.mode}`);
  const evidence = JSON.parse(match[1]);
  const requiredVisible = [
    "appShell",
    "topbar",
    "canvasPanel",
    "radialTimeline",
    "transport",
    "importAction",
    "exportAction",
    "selectionCallout"
  ];
  const assertions = {
    chromeViewportMatchesKnownInset: evidence.viewport.width === target.width && evidence.viewport.height === target.height - 87,
    noHorizontalOverflow: !evidence.document.horizontalOverflow,
    noVerticalOverflow: !evidence.document.verticalOverflow,
    radialInsideViewport: evidence.radialInsideViewport,
    radialCenteredInCanvas: evidence.radialCenterOffsetFromCanvas <= 1,
    requiredElementsVisible: requiredVisible.every((name) => evidence.elements[name]?.visible),
    libraryVisibilityMatches: evidence.elements.libraryPanel.visible === target.library,
    inspectorVisibilityMatches: evidence.elements.inspectorPanel.visible === target.inspector,
    compactInspectorVisibilityMatches: evidence.elements.compactInspector.visible === target.compactInspector
  };
  return {
    target: { mode: target.mode, width: target.width, height: target.height },
    pass: Object.values(assertions).every(Boolean),
    assertions,
    measurements: evidence
  };
});

const report = {
  generatedAt: new Date().toISOString(),
  renderer: "Google Chrome headless static browser render",
  evidenceBoundary: "Static HTML layout only; does not verify iPadOS or macOS native behavior.",
  allPassed: results.every((result) => result.pass),
  results
};

mkdirSync(dirname(evidencePath), { recursive: true });
writeFileSync(evidencePath, `${JSON.stringify(report, null, 2)}\n`);
process.stdout.write(`${evidencePath}\nallPassed=${report.allPassed}\n`);

if (!report.allPassed) process.exitCode = 1;
