(function () {
  "use strict";
  const STORAGE_KEY = "fieldnote.direction.v1";
  const $ = id => document.getElementById(id);
  const dialog = $("editor-dialog");
  let restored = null;
  try { restored = JSON.parse(localStorage.getItem(STORAGE_KEY)); } catch (_) { /* An unavailable store will surface on save. */ }
  const store = FieldNoteState.createStore(async (note, shouldFail) => {
    // Allow browser feedback to enter before the synchronous local write. No artificial loading delay.
    await new Promise(resolve => requestAnimationFrame(resolve));
    if (shouldFail) throw { simulated: true };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(note));
  }, restored);
  let closing = false;
  let closeTimer;
  let lastPhase = store.read().phase;
  function announce(message) { $("announcement").textContent = message; }
  function reduced() { return $("reduce-motion").checked || window.matchMedia("(prefers-reduced-motion: reduce)").matches; }
  function closeSheet() {
    if (!dialog.open || closing) return;
    closing = true;
    dialog.classList.add("closing");
    const finish = () => {
      if (!closing) return;
      clearTimeout(closeTimer);
      dialog.classList.remove("closing");
      dialog.close();
      closing = false;
      $("note-card").focus({ preventScroll: true });
    };
    dialog.addEventListener("animationend", finish, { once: true });
    closeTimer = setTimeout(finish, reduced() ? 130 : 200);
  }
  function openSheet() {
    clearTimeout(closeTimer);
    closing = false;
    dialog.classList.remove("closing");
    if (!dialog.open) {
      dialog.showModal();
      $("editor-book").focus({ preventScroll: true });
    }
  }
  function render(state) {
    const saved = !!state.saved;
    $("compose-view").hidden = saved;
    $("saved-view").hidden = !saved;
    if (saved) {
      $("card-book").textContent = "《" + state.saved.book + "》";
      $("card-quote").textContent = state.saved.quote;
      $("unsaved-message").hidden = !store.hasUnsaved();
    }
    $("fail-next").checked = state.failNext;
    $("fail-next").disabled = state.phase === "saving";
    $("reset-demo").disabled = state.phase === "saving";
    ["compose", "editor"].forEach(prefix => {
      const form = $(prefix + "-form");
      form.setAttribute("aria-busy", String(state.phase === "saving"));
      ["book", "quote"].forEach(field => {
        const input = $(prefix + "-" + field);
        if (input.value !== state.draft[field]) input.value = state.draft[field];
        input.disabled = state.phase === "saving";
        const error = $(prefix + "-" + field + "-error");
        error.textContent = state.validation[field] || "";
        error.hidden = !state.validation[field];
        input.setAttribute("aria-invalid", String(!!state.validation[field]));
      });
      const errorBox = $(prefix + "-error");
      const active = prefix === "editor" ? state.editing : !saved;
      errorBox.hidden = state.phase !== "error" || !active;
      errorBox.replaceChildren();
      if (!errorBox.hidden) {
        const title = document.createElement("strong");
        title.textContent = "尚未保存，输入仍在。";
        const detail = document.createElement("span");
        detail.textContent = state.error === "simulated"
          ? "这是一次模拟失败。可直接重试；书名与摘录没有丢失。"
          : "此浏览器暂时无法写入本地存储。输入保留在当前页面；可以重试保存。";
        errorBox.append(title, detail);
      }
      const save = $(prefix + "-save");
      save.disabled = state.phase === "saving";
      const label = state.phase === "saving" ? "正在保存…" : state.phase === "error" ? "重试保存" : prefix === "editor" ? "保存修改" : "保存摘录";
      save.replaceChildren(document.createTextNode(label));
      const arrow = document.createElement("span");
      arrow.setAttribute("aria-hidden", "true");
      arrow.textContent = state.phase === "saving" ? "·" : "↗";
      save.append(arrow);
    });
    $("editor-return").disabled = state.phase === "saving";
    if (state.editing) openSheet();
    else if (dialog.open) closeSheet();
    if (lastPhase !== state.phase) {
      if (state.phase === "saved") announce("已保存到此浏览器。摘录卡片已更新。");
      if (state.phase === "saving") announce("正在保存。");
      // Error is already exposed by role=alert in the active form.
    }
    lastPhase = state.phase;
  }
  ["compose", "editor"].forEach(prefix => {
    ["book", "quote"].forEach(field => $(prefix + "-" + field).addEventListener("input", event => store.update(field, event.target.value)));
    $(prefix + "-form").addEventListener("submit", async event => {
      event.preventDefault();
      const result = await store.save();
      if (result.status === "invalid") $(prefix + "-" + result.field).focus();
      if (result.status === "saved" && prefix === "compose") $("note-card").focus({ preventScroll: true });
      if (result.status === "error") $(prefix + "-save").focus({ preventScroll: true });
    });
  });
  $("note-card").addEventListener("click", () => store.openEditor());
  $("editor-return").addEventListener("click", () => store.closeEditor());
  dialog.addEventListener("cancel", event => { event.preventDefault(); store.closeEditor(); });
  dialog.addEventListener("keydown", event => {
    if (event.key !== "Tab") return;
    const controls = [...dialog.querySelectorAll("button,input,textarea")].filter(item => !item.disabled);
    const first = controls[0], last = controls[controls.length - 1];
    if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
    else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
  });
  $("fail-next").addEventListener("change", event => store.armFailure(event.target.checked));
  $("reduce-motion").addEventListener("change", event => document.body.classList.toggle("reduce-motion", event.target.checked));
  $("reset-demo").addEventListener("click", () => {
    try { localStorage.removeItem(STORAGE_KEY); } catch (_) { /* Reset still clears in-page prototype state. */ }
    if (!store.reset()) return;
    announce("已清空这条演示摘录，可以重新输入。");
    $("compose-book").focus();
  });
  store.subscribe(render);
  render(store.read());
})();
