const assert = require("node:assert/strict");
const { createStore } = require("./state.js");

(async () => {
  const writes = [];
  const store = createStore(async (note, shouldFail) => {
    if (shouldFail) throw { simulated: true };
    writes.push({ ...note });
  });
  assert.equal((await store.save()).status, "invalid");
  assert.equal(writes.length, 0);
  store.update("book", "山中的一天");
  store.update("quote", "慢下来，才能看见沿途细小的变化。\n第二行仍要完整保留。");
  const original = store.read().draft;
  store.armFailure(true);
  assert.equal((await store.save()).status, "error");
  assert.deepEqual(store.read().draft, original);
  assert.equal(store.read().saved, null);
  assert.equal(store.read().failNext, false);
  assert.equal((await store.save()).status, "saved");
  assert.deepEqual(writes, [original]);

  store.openEditor();
  store.update("quote", "修改后的摘录\n保留换行与引号：“这里”。");
  const modified = store.read().draft;
  store.armFailure(true);
  assert.equal((await store.save()).status, "error");
  assert.deepEqual(store.read().saved, original);
  assert.deepEqual(store.read().draft, modified);
  assert.equal(store.read().editing, true);
  store.closeEditor();
  assert.equal(store.hasUnsaved(), true);
  store.openEditor();
  assert.deepEqual(store.read().draft, modified);
  assert.equal((await store.save()).status, "saved");
  assert.deepEqual(store.read().saved, modified);
  assert.equal(store.read().editing, false);
  assert.equal(store.hasUnsaved(), false);
  assert.equal(writes.length, 2);

  let resolveWrite;
  let writeCount = 0;
  const pending = createStore(() => {
    writeCount += 1;
    return new Promise(resolve => { resolveWrite = resolve; });
  }, original);
  pending.openEditor();
  const savePromise = pending.save();
  assert.equal((await pending.save()).status, "busy");
  pending.update("book", "不得覆盖正在保存的输入");
  pending.closeEditor();
  assert.deepEqual(pending.read().draft, original);
  assert.equal(pending.read().editing, true);
  resolveWrite();
  assert.equal((await savePromise).status, "saved");
  assert.equal(writeCount, 1);

  const unavailable = createStore(async () => { throw new Error("storage unavailable"); }, original);
  unavailable.openEditor();
  unavailable.update("book", "新书名");
  assert.equal((await unavailable.save()).reason, "storage");
  assert.equal(unavailable.read().saved.book, original.book);
  assert.equal(unavailable.read().draft.book, "新书名");
  assert.equal(createStore(async () => {}, { book: "", quote: "" }).read().saved, null);
  assert.equal(store.reset(), true);
  assert.equal(store.read().saved, null);
  console.log("PASS: validation, failure retention, retry, edit recovery, return/reopen, single pending save, storage error, restored-state guard, reset.");
})().catch(error => { console.error(error); process.exitCode = 1; });
