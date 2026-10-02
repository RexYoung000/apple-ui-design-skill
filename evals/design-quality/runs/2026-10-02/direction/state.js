(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.FieldNoteState = factory();
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  "use strict";
  const EMPTY = { book: "", quote: "" };
  function isNote(note) {
    return !!note && typeof note.book === "string" && typeof note.quote === "string" && !!note.book.trim() && !!note.quote.trim();
  }
  function createStore(writer, restored) {
    let saved = isNote(restored) ? { book: restored.book, quote: restored.quote } : null;
    let state = { saved, draft: saved ? { ...saved } : { ...EMPTY }, phase: saved ? "saved" : "draft", editing: false, failNext: false, validation: {}, error: "" };
    const listeners = new Set();
    const read = () => ({ ...state, saved: state.saved ? { ...state.saved } : null, draft: { ...state.draft }, validation: { ...state.validation } });
    function emit() { listeners.forEach(fn => fn(read())); }
    const store = {
      read,
      subscribe(fn) { listeners.add(fn); return () => listeners.delete(fn); },
      update(field, value) {
        if (state.phase === "saving" || !["book", "quote"].includes(field)) return;
        state.draft = { ...state.draft, [field]: String(value) };
        state.validation = { ...state.validation, [field]: "" };
        state.phase = "draft";
        state.error = "";
        emit();
      },
      openEditor() { if (!state.saved || state.phase === "saving") return; state.editing = true; emit(); },
      closeEditor() { if (state.phase === "saving") return; state.editing = false; emit(); },
      armFailure(value) { state.failNext = !!value; emit(); },
      hasUnsaved() { return !!state.saved && (state.draft.book !== state.saved.book || state.draft.quote !== state.saved.quote); },
      reset() {
        if (state.phase === "saving") return false;
        state = { saved: null, draft: { ...EMPTY }, phase: "draft", editing: false, failNext: false, validation: {}, error: "" };
        emit();
        return true;
      },
      async save() {
        if (state.phase === "saving") return { status: "busy" };
        state.validation = {
          book: state.draft.book.trim() ? "" : "请填写书名，方便认出这条摘录。",
          quote: state.draft.quote.trim() ? "" : "请写下一段想留下的文字。"
        };
        if (state.validation.book || state.validation.quote) {
          emit();
          return { status: "invalid", field: state.validation.book ? "book" : "quote" };
        }
        const note = { ...state.draft };
        const shouldFail = state.failNext;
        state.failNext = false;
        state.phase = "saving";
        state.error = "";
        emit();
        try {
          await writer({ ...note }, shouldFail);
          state.saved = note;
          state.phase = "saved";
          state.editing = false;
          emit();
          return { status: "saved", note: { ...note } };
        } catch (error) {
          state.phase = "error";
          state.error = error && error.simulated ? "simulated" : "storage";
          emit();
          return { status: "error", reason: state.error };
        }
      }
    };
    return store;
  }
  return { createStore, isNote };
});
