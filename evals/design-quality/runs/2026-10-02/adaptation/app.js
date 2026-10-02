"use strict";

// Disposable browser design artifact. No media decoding, storage, or export service.
const clips = [
  { name:"Golden Hour", start:0.0, duration:3.8, color:"#E8A75D" },
  { name:"Boardwalk", start:3.8, duration:4.6, color:"#D56F64" },
  { name:"Ocean Foam", start:8.4, duration:4.6, color:"#36BFC1" },
  { name:"Shell Detail", start:13.0, duration:3.1, color:"#9E8AC7" },
  { name:"Sunset Ride", start:16.1, duration:4.2, color:"#E87953" },
  { name:"Night Lights", start:20.3, duration:3.7, color:"#5978B8" }
];
const byId = id => document.getElementById(id);
const ns = "http://www.w3.org/2000/svg";
const shell = byId("appShell");
const timeline = byId("timeline");
const fields = { start:byId("startField"), end:byId("endField") };
const handles = { start:byId("startHandle"), end:byId("endHandle") };
const undoStack = [], redoStack = [];
const fieldSnapshots = new Map();
let selected = 2;
let range = { start:8.4, end:13.0 };
let playhead = 8.4;
let drag = null;
let previewTimer = null;
let dialogReturn = null;
const round = value => Math.round(value * 10) / 10;
const clipEnd = clip => round(clip.start + clip.duration);
const snap = () => ({ selected, start:range.start, end:range.end });
const same = (a,b) => a.selected === b.selected && a.start === b.start && a.end === b.end;
const clock = value => `00:${value.toFixed(1).padStart(4,"0")}`;
const point = (seconds,radius=188) => {
  const angle = seconds / 24 * Math.PI * 2 - Math.PI / 2;
  return { x:280 + Math.cos(angle)*radius, y:280 + Math.sin(angle)*radius };
};
const arc = (start,end,radius=188) => {
  const a = point(start,radius), b = point(end,radius);
  return `M ${a.x} ${a.y} A ${radius} ${radius} 0 ${end-start>12 ? 1 : 0} 1 ${b.x} ${b.y}`;
};
function status(message) { byId("statusText").textContent = message; }
function stopPreview() {
  if (previewTimer !== null) clearInterval(previewTimer);
  previewTimer = null;
  byId("playButton").textContent = "▶";
  byId("playButton").setAttribute("aria-label","Preview selected range");
}
function remember(before) {
  if (!same(before,snap())) { undoStack.push(before); redoStack.length = 0; }
  render();
}
function restore(state) {
  stopPreview(); selected = state.selected;
  range = { start:state.start, end:state.end }; playhead = range.start;
  byId("fieldError").textContent = "";
  fieldSnapshots.set("start",snap()); fieldSnapshots.set("end",snap());
  render(true);
}
function selectClip(index) {
  if (drag) cancelDrag();
  stopPreview(); selected = index;
  range = { start:clips[index].start, end:clipEnd(clips[index]) };
  playhead = range.start;
  byId("fieldError").textContent = "";
  fieldSnapshots.set("start",snap()); fieldSnapshots.set("end",snap());
  render(true);
  status(`${clips[index].name} selected · ${range.start.toFixed(1)}–${range.end.toFixed(1)} sec`);
}
function validValue(kind,value) {
  const clip = clips[selected];
  return Number.isFinite(value) && value >= clip.start && value <= clipEnd(clip) &&
    (kind === "start" ? value <= round(range.end-.1) : value >= round(range.start+.1));
}
function setValue(kind,value,{clamp=false}={}) {
  const clip = clips[selected];
  if (clamp) value = kind === "start"
    ? Math.max(clip.start,Math.min(value,round(range.end-.1)))
    : Math.max(round(range.start+.1),Math.min(value,clipEnd(clip)));
  value = round(value);
  if (!validValue(kind,value)) {
    byId("fieldError").textContent = `Keep Start before End, within ${clip.start.toFixed(1)}–${clipEnd(clip).toFixed(1)} seconds.`;
    byId("exportButton").disabled = true;
    return false;
  }
  range[kind] = value;
  playhead = range.start;
  byId("fieldError").textContent = "";
  render();
  return true;
}
function render(forceFields=false) {
  const clip = clips[selected];
  document.querySelectorAll(".clip-row").forEach((row,index) => {
    row.setAttribute("aria-pressed",String(index===selected));
    row.querySelector("small").textContent = `${clips[index].start.toFixed(1)} sec · ${clips[index].duration.toFixed(1)}s${index===selected ? " · selected" : ""}`;
  });
  document.querySelectorAll(".segment").forEach((segment,index) => segment.classList.toggle("is-selected",index===selected));
  byId("rangeOutline").setAttribute("d",arc(range.start,range.end,211));
  for (const kind of ["start","end"]) {
    const p = point(range[kind]);
    handles[kind].setAttribute("transform",`translate(${p.x} ${p.y})`);
    handles[kind].setAttribute("aria-valuenow",range[kind].toFixed(1));
    handles[kind].setAttribute("aria-valuetext",`${clip.name}, ${kind} ${range[kind].toFixed(1)} seconds`);
    handles[kind].setAttribute("aria-valuemin",kind==="start" ? clip.start : round(range.start+.1));
    handles[kind].setAttribute("aria-valuemax",kind==="start" ? round(range.end-.1) : clipEnd(clip));
    fields[kind].min = kind==="start" ? clip.start : round(range.start+.1);
    fields[kind].max = kind==="start" ? round(range.end-.1) : clipEnd(clip);
    if (forceFields || document.activeElement!==fields[kind]) fields[kind].value = range[kind].toFixed(1);
  }
  byId("canvasTime").textContent = clock(playhead);
  byId("transportTime").textContent = clock(playhead);
  byId("canvasRange").textContent = `${range.start.toFixed(1)} — ${range.end.toFixed(1)} s`;
  byId("selectedName").textContent = clip.name;
  byId("selectedRange").textContent = `${range.start.toFixed(1)}–${range.end.toFixed(1)} sec · ${round(range.end-range.start).toFixed(1)} sec selected`;
  byId("inspectorName").textContent = clip.name;
  byId("previewName").textContent = clip.name;
  byId("clipNumber").textContent = String(selected+1).padStart(2,"0");
  byId("durationValue").textContent = `${round(range.end-range.start).toFixed(1)} s`;
  byId("sourceRange").textContent = `${clip.start.toFixed(1)}–${clipEnd(clip).toFixed(1)} s`;
  byId("previewTile").style.background = `linear-gradient(0deg,#08101ccb,transparent),radial-gradient(circle at 22% 20%,#d8f7ed99,transparent 26%),${clip.color}`;
  byId("playhead").setAttribute("transform",`rotate(${playhead/24*360} 280 280)`);
  byId("timelineTitle").textContent = `${clip.name}, selected ${range.start.toFixed(1)} to ${range.end.toFixed(1)} seconds`;
  byId("undoButton").disabled = undoStack.length===0;
  byId("redoButton").disabled = redoStack.length===0;
  byId("exportButton").disabled = byId("fieldError").textContent!=="";
}
clips.forEach((clip,index) => {
  const row = document.createElement("button");
  row.type = "button"; row.className = "clip-row";
  row.setAttribute("aria-label",`${index+1}. ${clip.name}, ${clip.duration.toFixed(1)} seconds`);
  row.title = clip.name;
  row.innerHTML = `<span class="clip-thumb" style="--clip:${clip.color}" aria-hidden="true"></span><span class="clip-copy"><strong>${clip.name}</strong><small></small></span>`;
  row.addEventListener("click",()=>selectClip(index));
  row.addEventListener("keydown",event=>{
    if (event.key==="ArrowDown" || event.key==="ArrowUp") {
      event.preventDefault(); const next = Math.max(0,Math.min(clips.length-1,index+(event.key==="ArrowDown" ? 1 : -1)));
      selectClip(next); byId("clipList").children[next].focus();
    }
  });
  byId("clipList").append(row);
  const segment = document.createElementNS(ns,"path");
  segment.setAttribute("d",arc(clip.start+.06,clipEnd(clip)-.06));
  segment.setAttribute("class","segment"); segment.setAttribute("stroke",clip.color);
  segment.addEventListener("click",()=>selectClip(index));
  byId("segmentLayer").append(segment);
});
for (let i=0;i<24;i++) {
  const a=point(i,i%4===0 ? 218 : 223), b=point(i,230);
  const tick=document.createElementNS(ns,"line");
  for (const [key,value] of Object.entries({x1:a.x,y1:a.y,x2:b.x,y2:b.y})) tick.setAttribute(key,String(value));
  tick.setAttribute("class",i%4===0 ? "tick major" : "tick"); byId("tickLayer").append(tick);
}
function commitField(kind) {
  const before = fieldSnapshots.get(kind) || snap();
  const entered = fields[kind].value.trim()==="" ? NaN : Number(fields[kind].value);
  if (setValue(kind,entered)) {
    remember(before); fieldSnapshots.set(kind,snap()); fields[kind].value=range[kind].toFixed(1);
    status(`Range committed · ${range.start.toFixed(1)}–${range.end.toFixed(1)} sec`);
  }
}
function nudge(kind,amount) {
  stopPreview();
  setValue(kind,range[kind]+amount,{clamp:true});
  fields[kind].value=range[kind].toFixed(1);
  status(`${kind} ${range[kind].toFixed(1)} sec · Enter commits, Esc cancels`);
}
for (const kind of ["start","end"]) {
  fields[kind].addEventListener("focus",()=>fieldSnapshots.set(kind,snap()));
  handles[kind].addEventListener("focus",()=>fieldSnapshots.set(kind,snap()));
  fields[kind].addEventListener("blur",()=>commitField(kind));
  handles[kind].addEventListener("blur",()=>commitField(kind));
  fields[kind].addEventListener("input",()=>{
    const value = fields[kind].value.trim()==="" ? NaN : Number(fields[kind].value);
    stopPreview(); setValue(kind,value);
  });
  fields[kind].addEventListener("change",()=>commitField(kind));
  const onKey = event=>{
    if (["ArrowUp","ArrowDown","ArrowLeft","ArrowRight"].includes(event.key)) {
      event.preventDefault(); const direction=["ArrowUp","ArrowRight"].includes(event.key) ? 1 : -1;
      nudge(kind,direction*(event.shiftKey ? 1 : .1));
    } else if (event.key==="Enter") {
      event.preventDefault(); commitField(kind);
    } else if (event.key==="Escape") {
      event.preventDefault(); event.stopPropagation(); if (drag) cancelDrag();
      else if (fieldSnapshots.has(kind)) { restore(fieldSnapshots.get(kind)); status("Range edit cancelled"); }
    }
  };
  fields[kind].addEventListener("keydown",onKey);
  handles[kind].addEventListener("keydown",onKey);
  handles[kind].addEventListener("pointerdown",event=>{
    if (event.button!==0) return;
    event.preventDefault(); stopPreview(); handles[kind].focus();
    drag={kind,before:snap(),pointerId:event.pointerId};
    handles[kind].classList.add("is-dragging"); timeline.setPointerCapture(event.pointerId);
    status(`Adjusting ${kind} · Esc cancels`);
  });
}
function pointerSeconds(event) {
  const p=timeline.createSVGPoint(); p.x=event.clientX; p.y=event.clientY;
  const local=p.matrixTransform(timeline.getScreenCTM().inverse());
  let angle=Math.atan2(local.y-280,local.x-280)+Math.PI/2;
  if (angle<0) angle+=Math.PI*2;
  let seconds=angle/(Math.PI*2)*24;
  if (selected===0 && seconds>23) seconds=0;
  // The final clip crosses the zero seam visually; keep its end at 24.
  if (selected===clips.length-1 && seconds<1) seconds=24;
  return seconds;
}
timeline.addEventListener("pointermove",event=>{
  if (!drag || event.pointerId!==drag.pointerId) return;
  setValue(drag.kind,pointerSeconds(event),{clamp:true});
});
timeline.addEventListener("pointerup",event=>{
  if (!drag || event.pointerId!==drag.pointerId) return;
  setValue(drag.kind,pointerSeconds(event),{clamp:true});
  const completed=drag; drag=null;
  handles[completed.kind].classList.remove("is-dragging");
  if (timeline.hasPointerCapture(event.pointerId)) timeline.releasePointerCapture(event.pointerId);
  remember(completed.before);
  fieldSnapshots.set(completed.kind,snap());
  status(`Range committed · ${range.start.toFixed(1)}–${range.end.toFixed(1)} sec`);
});
function cancelDrag() {
  if (!drag) return;
  const cancelled=drag; drag=null;
  handles[cancelled.kind].classList.remove("is-dragging");
  if (timeline.hasPointerCapture(cancelled.pointerId)) timeline.releasePointerCapture(cancelled.pointerId);
  restore(cancelled.before); status("Drag cancelled · original range restored");
}
timeline.addEventListener("pointercancel",cancelDrag);
timeline.addEventListener("lostpointercapture",cancelDrag);
window.addEventListener("blur",()=>{ cancelDrag(); stopPreview(); });
function undo() {
  if (drag) cancelDrag();
  if (!undoStack.length) return;
  redoStack.push(snap()); restore(undoStack.pop()); status("Previous range restored");
}
function redo() {
  if (!redoStack.length) return;
  undoStack.push(snap()); restore(redoStack.pop()); status("Range change restored");
}
byId("undoButton").addEventListener("click",undo);
byId("redoButton").addEventListener("click",redo);
function preview() {
  if (drag) return;
  if (previewTimer!==null) { stopPreview(); status("Illustrative preview paused"); return; }
  playhead=range.start;
  byId("playButton").textContent="Ⅱ"; byId("playButton").setAttribute("aria-label","Pause illustrative preview");
  status("Illustrative preview · no video or audio playback");
  previewTimer=setInterval(()=>{
    playhead=round(playhead+.1);
    if (playhead>=range.end) { playhead=range.end; stopPreview(); status("Illustrative preview ended · range preserved"); }
    render();
  },100);
}
byId("playButton").addEventListener("click",preview);
function closeInspector(returnFocus=true) {
  delete shell.dataset.inspector; byId("inspectButton").setAttribute("aria-expanded","false");
  if (returnFocus && shell.dataset.layout==="compact") byId("inspectButton").focus();
}
byId("inspectButton").addEventListener("click",()=>{
  if (shell.dataset.inspector==="open") closeInspector();
  else { shell.dataset.inspector="open"; byId("inspectButton").setAttribute("aria-expanded","true"); fields.start.focus(); }
});
byId("closeInspector").addEventListener("click",()=>closeInspector());
function setLayout(layout) {
  const inspectorHasFocus=byId("inspectorPanel").contains(document.activeElement);
  shell.dataset.layout=layout; closeInspector(false);
  byId("compactMode").setAttribute("aria-pressed",String(layout==="compact"));
  byId("wideMode").setAttribute("aria-pressed",String(layout==="wide"));
  byId("layoutLabel").textContent=`Mac · ${layout} layout`;
  if (layout==="compact" && inspectorHasFocus) byId("inspectButton").focus();
}
byId("compactMode").addEventListener("click",()=>setLayout("compact"));
byId("wideMode").addEventListener("click",()=>setLayout("wide"));
byId("reduceMotion").addEventListener("change",event=>document.body.classList.toggle("reduce-motion",event.target.checked));
function boundaryDialog(type,opener) {
  stopPreview(); dialogReturn=opener;
  byId("dialogTitle").textContent=type==="export" ? "Export Loop" : "Import clips";
  byId("dialogBody").textContent=type==="export"
    ? "Design preview only. In the Mac app, this action hands your current loop to the native save path. No video has been exported here. Returning keeps your selected clip and range."
    : "Design preview only. In the Mac app, Import opens the native file selection path. No files have been imported here; the six source clips are representative content.";
  byId("boundaryDialog").showModal();
}
byId("exportButton").addEventListener("click",()=>boundaryDialog("export",byId("exportButton")));
byId("importButton").addEventListener("click",()=>boundaryDialog("import",byId("importButton")));
byId("dismissDialog").addEventListener("click",()=>byId("boundaryDialog").close());
byId("boundaryDialog").addEventListener("close",()=>{ if (dialogReturn) dialogReturn.focus(); });
document.addEventListener("keydown",event=>{
  if (byId("boundaryDialog").open) return;
  const inField=event.target instanceof HTMLInputElement;
  if (event.key==="Escape" && drag) { event.preventDefault(); cancelDrag(); }
  else if (event.key==="Escape" && shell.dataset.inspector==="open" && !inField) { event.preventDefault(); closeInspector(); }
  else if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase()==="z" && !inField) {
    event.preventDefault(); event.shiftKey ? redo() : undo();
  } else if (event.code==="Space" && !inField && !(event.target instanceof HTMLButtonElement) && !event.metaKey && !event.ctrlKey && !event.altKey) {
    event.preventDefault(); preview();
  }
});
const requestedMode = new URLSearchParams(location.search).get("mode");
setLayout(requestedMode==="compact" ? "compact" : "wide");
render(true);
