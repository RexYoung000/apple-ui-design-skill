<div align="center">

# Apple UI Design

**面向 iOS、iPadOS 与 macOS 的产品优先型 UI 设计 Skill，强调原生、独特与可验证。**

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

## 项目简介

Apple UI Design 是一个用于 Apple 生态产品界面设计、适配、实现与评审的 Agent Skill。

它从产品意图和项目证据出发，将共享的产品 DNA 与符合平台习惯的交互方式结合起来。Apple 设计规范用于指导体验，但不会把所有产品都塑造成同一种视觉模板。

它同时覆盖已有产品与从零产品。已有产品从当前项目证据中理解；从零产品使用明确假设和公开研究推进，但不会把未经测试的判断冒充已经验证的用户需求。

## 能力范围

- Apple 平台产品与视觉方向探索
- 页面、状态、流程和导航设计
- 共享设计系统与平台差异化表达
- iOS、iPadOS 与 macOS 的跨平台适配
- 面向 SwiftUI 的原生原型与界面实现
- 可访问性、本地化、动效与自适应布局决策
- 基于真实证据的设计与实现评审

## 核心原则

1. **产品意图优先。** 已确认的决策定义预期体验，同时通过证据标签区分已知用户需求与假设。
2. **项目上下文是本地事实依据。** 在作出新决定前，先检查现有需求、设计系统、组件、资产与平台目标。
3. **用户拥有产品方向决策权。** Skill 会说明平台、可用性和无障碍影响，但不会静默替换用户已经确认的交互或动效方案。
4. **原生不等于千篇一律。** 原生验证检查行为和语义，而不是检查界面是否像 Apple 系统 App；自定义视觉与控件仍然有效。
5. **跨平台需要适配，而不是放大。** iPhone、iPad 与 Mac 可以共享同一产品，但在层级、密度、导航和输入方式上应合理变化。
6. **可访问性与本地化保护体验结果，而非统一皮肤。** 它们从设计阶段进入验证，同时保留品牌表达。
7. **视觉与动效质量需要证据。** 编译成功不等于体验通过；重要状态和真实交互需要经过渲染与验证。

## 工作模式

Skill 会根据当前任务选择合适的处理深度：

- **方向探索**——建立或探索产品的视觉与交互方向
- **页面或流程设计**——设计页面、状态集合或端到端任务
- **设计系统**——定义或扩展共享 DNA、语义化 Token 与组件
- **跨平台适配**——将现有体验转化到另一个 Apple 平台
- **原生原型或实现**——在明确需要时创建 SwiftUI 原型或生产界面
- **评审与迭代**——依据已确认的产品意图评估现有设计或实现

## 作为独立 Skill 安装

个人本地使用时，将仓库克隆到当前用户级 Skills 目录：

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/RexYoung000/apple-ui-design-skill.git "$HOME/.agents/skills/apple-ui-design"
```

Codex 会自动检测 Skill 变化。如果没有出现，请重启 Codex 或 ChatGPT 桌面应用。

更新已有安装：

```bash
git -C "$HOME/.agents/skills/apple-ui-design" pull --ff-only
```

如需移除但不永久删除源码，可以将它移出会被扫描的 `skills` 目录：

```bash
mkdir -p "$HOME/.agents/skill-backups"
mv "$HOME/.agents/skills/apple-ui-design" "$HOME/.agents/skill-backups/apple-ui-design"
```

如果目标备份目录已经存在，请使用另一个备份名称。

对于仓库级团队协作，可以将 Skill 放在项目内的 `.agents/skills/apple-ui-design`。Codex 会从当前工作目录向上扫描到仓库根目录中的 `.agents/skills`。

当前独立安装方式用于本地使用和源码开发。OpenAI 建议将面向公开分发的可复用能力包装为 Plugin。本项目的 Plugin 包装与迁移由 [Issue #2](https://github.com/RexYoung000/apple-ui-design-skill/issues/2) 跟踪；当前 README 不会把尚未完成的仓库结构描述成可安装 Plugin。

当前官方说明参见 [构建 Skills](https://learn.chatgpt.com/docs/build-skills) 与 [包装 Plugins](https://developers.openai.com/plugins/build/plugins)。

## 在 Codex 中使用

使用 `$` 明确调用 Skill：

```text
使用 $apple-ui-design 为这个 iPad 应用设计新用户引导流程。
```

Codex 也可以在请求与 Skill 描述匹配时自动选择它：

```text
评审这个 macOS 界面的信息层级、键盘操作、可访问性，
以及它与现有产品设计系统的一致性。
```

## 在 ChatGPT 桌面应用中使用

先在侧栏打开 **Skills**，确认 Apple UI Design 已经出现。在聊天输入框中键入 `@`，选择 **Apple UI Design**，然后描述任务：

```text
使用 Apple UI Design 将这个现有 iPhone 流程适配到 iPad 和 Mac。
```

独立 Skills 可用于 ChatGPT 桌面应用、Codex CLI 和 Codex IDE 扩展。共享 Plugins Directory 的安装方式将在 Issue #2 完成后补充。

Skill 会先检查项目中已有的证据，再提出问题。当某项决定会实质影响产品时，它会一次只确认一个关键问题，并说明推荐方向及理由。

对于已有产品，Skill 会从当前证据提取目标用户、核心任务、设计 DNA 和交互模型。对于从零产品，Skill 会明确区分用户确认、外部证据、设计推断与待验证假设。

## 研究与灵感

Skill 使用混合研究模式：

- 内置经过分类的 Apple 官方来源、真实案例、公开 UI 与动效网站、灵感站点和素材来源索引；
- 根据当前产品与设计问题进行实时研究；
- 明确区分权威依据、可观测案例、纯灵感与待验证假设。

60fps、Recent、Awwwards、React Bits、Magic UI 等 Web 来源可以启发视觉与动效方向，但不能证明 Apple 原生行为。第三方截图和素材默认只进行观察和链接；未核验复用权利时不会打包进仓库。

## 仓库结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
    ├── accessibility-and-localization.md
    ├── apple-platform-adaptation.md
    ├── authority-and-principles.md
    ├── context-and-alignment.md
    ├── design-system-and-dna.md
    ├── maintenance-and-sources.md
    ├── prototyping-and-implementation.md
    ├── research-and-source-evidence.md
    ├── source-registry.json
    └── validation-and-review.md
├── scripts/
    └── validate_source_registry.py
└── tests/
    └── test_source_registry.py
```

- `SKILL.md` 定义角色、范围、工作流程、评审方法与任务分流规则。
- `agents/openai.yaml` 提供展示信息与默认调用提示词。
- `references/` 存放按当前任务需要加载的专项设计指导。
- `references/source-registry.json` 是经过校验的官方、案例、灵感、受限与排除来源地图。
- `scripts/validate_source_registry.py` 用于检查必填元数据、重复来源、HTTPS 地址和核验日期。
- `tests/test_source_registry.py` 用于保护资源校验器必须识别的错误场景。

## 边界

该 Skill 负责产品意图、视觉层级、Apple 平台行为、设计系统决策和体验验收标准。

它不能替代 Swift 架构、并发、性能分析、CI、打包或发布等专项工程流程。当这些内容成为主要任务时，应将本 Skill 与相应的工程工作流配合使用。

## 维护原则

稳定的设计原则保存在 Skill 中。当某项决策依赖具体版本时，应通过 Apple 当前官方资料核对 API、平台行为与 Human Interface Guidelines。

维护策略与回归测试提示详见 [`references/maintenance-and-sources.md`](references/maintenance-and-sources.md)。

## 开源协议

本项目采用 [MIT License](LICENSE)。
