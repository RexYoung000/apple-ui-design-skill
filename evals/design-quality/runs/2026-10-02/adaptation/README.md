# OrbitCut Mac 适配审阅包

已产出 iPad → Mac 决策矩阵和一张可切换紧凑 / 宽窗口的浏览器代表布局。当前是设计适配稿；浏览器可见布局与真实操作检查交由主代理执行后记录，尚未达到原生 **experience verified** 或 **user accepted**。

## 打开与操作

直接用浏览器打开 `index.html`；也可在现有本地静态服务器下访问此目录。无依赖、无安装步骤、无网络资源。

- `index.html?mode=compact`：紧凑布局，素材与径向编辑共存，Inspect 打开详情。
- `index.html?mode=wide`：宽布局，素材、径向编辑与详情共存。
- 页顶“紧凑 / 宽窗口”是审阅工具；“减少动效示意”仅控制本浏览器演示。
- 素材列表选择 Ocean Foam；拖 S / E 端点。Esc 恢复操作前范围；释放提交；Undo / Redo 恢复范围。
- Tab 到端点或时间字段，箭头调整，Shift 改较大步长，Enter 提交，Esc 取消。也可直接输入起止秒数。
- Preview / Space 仅显示示意播放头；Export Loop 只展示明确边界说明，返回后保留选择和范围。

## 本次实际做过的检查

- 读取源 README、HTML、CSS、JS；查看源 iPad expansive PNG，仅作为来源，不复用其验收结论。
- `node --check app.js` 通过。
- Python 标准库检查 43 个 HTML ID 唯一，6 个 label/控件引用有效，两个本地资源存在，41 个脚本静态 ID 引用有效，CSS 大括号平衡。见 `static-checks.json`。
- 静态交互复核并修正：空字段不能被当作 0 提交；Space 不抢占按钮的默认键盘激活；键盘调整保留 Enter 提交 / Esc 恢复的操作前范围；拖动在圆环零点附近的边界处理；失焦/丢失捕获取消拖动；释放使用最终指针位置。
- 本执行者未调用浏览器、未跑原生 Mac 工程、未使用辅助技术、未输出生产 Swift 代码。

不能把上述检查写成“浏览器交互通过”或“Mac 手感验证通过”。主代理进行浏览器验收时，请另记实际窗口、路径、结果和新证据；原生验证计划在 `decision-matrix.md` 中。

## 所读来源与技能参考

源目录：`evals/delivery-contracts/runs/2026-07-29/platform-adaptation/`

实际读取：

- `README.md`
- `prototype/index.html`
- `prototype/styles.css`
- `prototype/app.js`
- `evidence/ipad-expansive.png`（看图；源设计材料）

技能：`plugins/apple-ui-design/skills/apple-platform-adaptation/SKILL.md`

参考根：`plugins/apple-ui-design/references/`

按本任务读取 `delivery-contracts.md`（开始和结束）、`apple-platform-adaptation.md`、`design-system-and-dna.md`、`interaction-and-motion.md`、`accessibility-and-localization.md`、`prototyping-and-implementation.md`、`validation-and-review.md`、`authority-and-principles.md`、`engineering-routing.md`；`content-and-sensitive-flows.md` 仅检索并读取与完成/取消/恢复和原型边界有关的开头部分。未读取外部案例目录或安装依赖。

## 待验证范围

浏览器两种窗口布局、真实指针与键盘操作、长文字和焦点恢复需主代理审阅。Mac 原生窗口、命令/菜单、触控板跟手、正常速度回弹录制、减少动态效果、VoiceOver / Voice Control / Switch Control、系统文件选择与导出、生产持久化和最低系统版本均未验证；这些不会由浏览器截图替代。
