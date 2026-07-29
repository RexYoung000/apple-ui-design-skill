const clips = [
  { name: "Golden Hour", start: "00.0", duration: "3.8s", color: "#E8A75D" },
  { name: "Boardwalk", start: "03.8", duration: "4.6s", color: "#D56F64" },
  { name: "Ocean Foam", start: "08.4", duration: "4.6s", color: "#36BFC1", selected: true },
  { name: "Shell Detail", start: "13.0", duration: "3.1s", color: "#9E8AC7" },
  { name: "Sunset Ride", start: "16.1", duration: "4.2s", color: "#E87953" },
  { name: "Night Lights", start: "20.3", duration: "3.7s", color: "#5978B8" }
];

const modes = {
  "ipad-compact": "iPad · compact window · touch / Pencil / pointer",
  "ipad-expansive": "iPad · expansive window · touch / Pencil / pointer",
  "mac-minimum": "Mac · minimum 900 × 640 · pointer / keyboard",
  "mac-expanded": "Mac · expanded 1440 × 900 · pointer / keyboard"
};

const params = new URLSearchParams(window.location.search);
const mode = modes[params.get("mode")] ? params.get("mode") : "ipad-expansive";
document.body.classList.add(`mode-${mode}`);
document.body.dataset.mode = mode;
document.getElementById("environmentBadge").textContent = modes[mode];

const clipList = document.getElementById("clipList");
clips.forEach((clip, index) => {
  const row = document.createElement("div");
  row.className = `clip-row${clip.selected ? " is-selected" : ""}`;
  row.innerHTML = `
    <span class="clip-thumb" style="--clip:${clip.color}"></span>
    <span class="clip-copy">
      <strong>${clip.name}</strong>
      <span>${clip.start} sec</span>
    </span>
    <span class="clip-duration">${clip.duration}</span>
  `;
  row.setAttribute("aria-label", `${index + 1}. ${clip.name}, starts ${clip.start} seconds, duration ${clip.duration}${clip.selected ? ", selected" : ""}`);
  clipList.appendChild(row);
});

const svgNS = "http://www.w3.org/2000/svg";
const segmentLayer = document.getElementById("segmentLayer");
const tickLayer = document.getElementById("tickLayer");
const circumference = 2 * Math.PI * 188;
const gap = 6;

clips.forEach((clip, index) => {
  const duration = Number.parseFloat(clip.duration);
  const start = Number.parseFloat(clip.start);
  const length = circumference * (duration / 24);
  const offset = -(circumference * (start / 24)) + circumference * .25;

  const segment = document.createElementNS(svgNS, "circle");
  segment.setAttribute("cx", "280");
  segment.setAttribute("cy", "280");
  segment.setAttribute("r", "188");
  segment.setAttribute("class", `segment${clip.selected ? " is-selected" : ""}`);
  segment.setAttribute("style", `--segment-color:${clip.color}`);
  segment.setAttribute("stroke-dasharray", `${Math.max(0, length - gap)} ${circumference}`);
  segment.setAttribute("stroke-dashoffset", `${offset}`);
  segment.setAttribute("transform", "rotate(-90 280 280)");
  segmentLayer.appendChild(segment);

  if (clip.selected) {
    const outline = document.createElementNS(svgNS, "circle");
    outline.setAttribute("cx", "280");
    outline.setAttribute("cy", "280");
    outline.setAttribute("r", "209");
    outline.setAttribute("class", "segment-outline");
    outline.setAttribute("stroke-dasharray", `${Math.max(0, length - gap)} ${circumference * (209 / 188)}`);
    outline.setAttribute("stroke-dashoffset", `${offset * (209 / 188)}`);
    outline.setAttribute("transform", "rotate(-90 280 280)");
    segmentLayer.appendChild(outline);
  }
});

for (let i = 0; i < 24; i += 1) {
  const angle = (i / 24) * Math.PI * 2 - Math.PI / 2;
  const major = i % 4 === 0;
  const inner = major ? 220 : 225;
  const outer = 232;
  const tick = document.createElementNS(svgNS, "line");
  tick.setAttribute("x1", `${280 + Math.cos(angle) * inner}`);
  tick.setAttribute("y1", `${280 + Math.sin(angle) * inner}`);
  tick.setAttribute("x2", `${280 + Math.cos(angle) * outer}`);
  tick.setAttribute("y2", `${280 + Math.sin(angle) * outer}`);
  tick.setAttribute("class", `tick${major ? " major" : ""}`);
  tickLayer.appendChild(tick);
}

function visibleBounds(selector) {
  const element = document.querySelector(selector);
  if (!element) return { exists: false, visible: false, bounds: null };
  const style = window.getComputedStyle(element);
  const rect = element.getBoundingClientRect();
  const visible = style.display !== "none" && style.visibility !== "hidden" && rect.width > 0 && rect.height > 0;
  return {
    exists: true,
    visible,
    bounds: visible ? {
      x: Math.round(rect.x * 10) / 10,
      y: Math.round(rect.y * 10) / 10,
      width: Math.round(rect.width * 10) / 10,
      height: Math.round(rect.height * 10) / 10,
      right: Math.round(rect.right * 10) / 10,
      bottom: Math.round(rect.bottom * 10) / 10
    } : null
  };
}

{
  const selectors = {
    appShell: ".app-shell",
    topbar: ".topbar",
    libraryPanel: ".library-panel",
    canvasPanel: "#canvasPanel",
    inspectorPanel: "#inspectorPanel",
    radialTimeline: ".radial-timeline",
    transport: ".transport",
    importAction: ".import-button",
    exportAction: ".export-button",
    selectionCallout: ".selection-callout",
    compactSwitcher: ".compact-switcher",
    compactInspector: ".compact-inspector"
  };
  const elements = Object.fromEntries(Object.entries(selectors).map(([name, selector]) => [name, visibleBounds(selector)]));
  const timeline = elements.radialTimeline.bounds;
  const canvas = elements.canvasPanel.bounds;
  const radialCenterOffset = timeline && canvas
    ? Math.round(Math.abs((timeline.x + timeline.width / 2) - (canvas.x + canvas.width / 2)) * 10) / 10
    : null;
  const evidence = {
    mode,
    viewport: { width: window.innerWidth, height: window.innerHeight, devicePixelRatio: window.devicePixelRatio },
    document: {
      scrollWidth: document.documentElement.scrollWidth,
      scrollHeight: document.documentElement.scrollHeight,
      horizontalOverflow: document.documentElement.scrollWidth > window.innerWidth,
      verticalOverflow: document.documentElement.scrollHeight > window.innerHeight
    },
    radialCenterOffsetFromCanvas: radialCenterOffset,
    radialInsideViewport: Boolean(timeline && timeline.x >= 0 && timeline.y >= 0 && timeline.right <= window.innerWidth && timeline.bottom <= window.innerHeight),
    elements
  };
  const output = document.createElement("script");
  output.type = "application/json";
  output.id = "layout-evidence";
  output.textContent = JSON.stringify(evidence);
  document.body.appendChild(output);
}
