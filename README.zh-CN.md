<div align="center">

# Apple UI Design

**面向 iOS、iPadOS 与 macOS 的产品优先型 UI 设计 Plugin，强调原生、独特与可验证。**

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

## 项目简介

Apple UI Design 是一个用于 Apple 生态产品界面设计、适配与评审的纯 Skills Plugin。

它从产品意图和项目证据出发，将共享的产品 DNA 与符合平台习惯的交互方式结合起来。Apple 设计规范用于指导体验，但不会把所有产品都塑造成同一种视觉模板。

它同时覆盖已有产品与从零产品。已有产品从当前项目证据中理解；从零产品使用明确假设和公开研究推进，但不会把未经测试的判断冒充已经验证的用户需求。

可安装 Plugin 包含三个聚焦的 Skill；它们共享同一套证据与平台方法，不会争抢同一类任务。

## 内置 Skills

- **`$apple-ui-direction`**——产品与视觉方向、页面、流程、设计系统和设计型原型。
- **`$apple-platform-adaptation`**——在 iOS、iPadOS 与 macOS 之间转化既有产品，而不是放大布局。
- **`$apple-ui-review`**——依据证据评审已有设计、原型与 UI 实现。

SwiftUI 生产架构、调试、性能、CI 与发布仍属于工程职责。以上 Skills 向相应工程工作流提供产品意图、界面决策、证据要求和验收标准。

## 核心原则

1. **产品意图优先。** 已确认的决策定义预期体验，同时通过证据标签区分已知用户需求与假设。
2. **项目上下文是本地事实依据。** 在作出新决定前，先检查现有需求、设计系统、组件、资产与平台目标。
3. **用户拥有产品方向决策权。** Skill 会说明平台、可用性和无障碍影响，但不会静默替换用户已经确认的交互或动效方案。
4. **原生不等于千篇一律。** 原生验证检查行为和语义，而不是检查界面是否像 Apple 系统 App；自定义视觉与控件仍然有效。
5. **跨平台需要适配，而不是放大。** iPhone、iPad 与 Mac 可以共享同一产品，但在层级、密度、导航和输入方式上应合理变化。
6. **可访问性与本地化保护体验结果，而非统一皮肤。** 它们从设计阶段进入验证，同时保留品牌表达。
7. **视觉与动效质量需要证据。** 编译成功不等于体验通过；重要状态和真实交互需要经过渲染与验证。

## 交付合同

每项任务只选择一个主要合同。合同定义开始前需要什么证据、用户最终获得什么产物，以及现有证据最多能支持哪一级完成声明。

| 合同 | 最低交付物 | 声明完成所需证据 |
|---|---|---|
| 视觉方向 | 使用代表性真实内容的关键画面；方向未确定时提供具有实质差异的可见方案 | 已渲染画面；不能只凭文字或精确参数宣称高保真方向完成 |
| 页面或流程 | 覆盖必要状态、转换、恢复和输入行为的可操作路径 | 交互原型或运行实现；静态画面只能证明外观 |
| 设计系统 | 语义 Token、组件意图、代表性状态及其在真实产品页面中的应用 | 已渲染组件状态和至少一个代表性产品应用 |
| 跨平台适配 | 共享与平台差异矩阵，以及每个目标环境的代表布局和输入行为 | 各关键尺寸的可见证据；涉及窗口、输入或平台行为的声明必须经过原生运行 |
| 原生原型 | 有明确范围的 SwiftUI 行为、代表性状态、无障碍语义、版本降级，以及有动效时的 Reduce Motion 表达 | SwiftUI Preview、模拟器或真机，或真实 macOS App；交互与动效声明需要录屏 |
| UI 评审 | 证据状态，以及按严重度排列的事实、影响、建议和验证方法 | 结论受用户提供的产物与运行证据约束；只有文字时只能提供未验证咨询 |

所有精确视觉值都必须来自项目依据、已渲染产物，或明确标记为“建议值、尚未验证”。交互与动效决定仍属于用户：Plugin 可以建议、制作原型和验证，但不能静默替换已确认的产品选择。

完成状态必须分层表达：**方向已对齐**、**设计完成**、**原型完成**、**代码完成**、**体验已验证**、**用户已验收**。不得从前一阶段自动推导后一阶段。

## 安装 Plugin

先将本公开仓库添加为 Codex Marketplace，再安装 Plugin：

```bash
codex plugin marketplace add RexYoung000/apple-ui-design-skill --ref main
codex plugin add apple-ui-design@apple-ui-design
```

安装后新建 Codex 会话，使三个内置 Skills 被加载。在 ChatGPT 桌面应用中，重启应用，打开 **Plugins**，选择 **Apple UI Design** Marketplace，然后安装 **Apple UI Design**。

仓库更新后刷新 Marketplace 并重新安装：

```bash
codex plugin marketplace upgrade apple-ui-design
codex plugin add apple-ui-design@apple-ui-design
```

GitHub Marketplace 是当前公开安装路径。本仓库不会把“已提交到 OpenAI 通用 Plugins Directory”作为已完成事实；那属于单独的正式发布步骤。

官方说明参见[构建 Skills](https://learn.chatgpt.com/docs/build-skills)、[包装 Plugins](https://developers.openai.com/plugins/build/plugins)与[使用 Plugins](https://learn.chatgpt.com/docs/plugins)。

## 从旧版独立 Skill 迁移

旧版安装方式会把本仓库克隆到 `$HOME/.agents/skills/apple-ui-design`，并调用 `$apple-ui-design`。根级 Skill 仍作为旧版显式调用兼容路由存在，但不会装进 Plugin，也不会再被自动触发。

安装 Plugin 后：

- 方向、页面、流程、设计系统或原型任务将 `$apple-ui-design` 替换为 `$apple-ui-direction`；
- 跨平台产品转化使用 `$apple-platform-adaptation`；
- 评审与验证使用 `$apple-ui-review`。

确认 Plugin 可用后，再删除或移走旧版独立 Skill；否则选择器中可能同时出现兼容路由和新 Skills。

## 在 Codex 中使用

使用 `$` 明确调用 Skill：

```text
使用 $apple-ui-direction 为这个 iPad 应用设计新用户引导流程。
```

Codex 也可以在请求与 Skill 描述匹配时自动选择它：

```text
使用 $apple-ui-review 评审这个 macOS 界面的信息层级、
键盘操作、可访问性及其与现有产品设计系统的一致性。
```

## 在 ChatGPT 桌面应用中使用

从 **Plugins** 安装 **Apple UI Design**。在新会话输入框中键入 `@`，选择对应的内置 Skill，然后描述任务：

```text
使用 Apple Platform Adaptation 将这个现有 iPhone 流程适配到 iPad 和 Mac。
```

被选中的 Skill 会先检查项目中已有的证据，再提出问题。当某项决定会实质影响产品时，它会一次只确认一个关键问题，并说明推荐方向及理由。

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
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── docs/
│   └── maintenance-and-sources.md
├── evals/
│   ├── plugin-split/
│   │   └── runs/
│   ├── delivery-contracts/
│   │   ├── README.md
│   │   ├── cases.json
│   │   ├── fixtures/
│   │   └── runs/
│   └── product-starting-point/
│       ├── README.md
│       ├── cases.json
│       ├── fixtures/
│       └── runs/
├── plugins/
│   └── apple-ui-design/
│       ├── .codex-plugin/
│       │   └── plugin.json
│       ├── references/
│       └── skills/
│           ├── apple-platform-adaptation/
│           ├── apple-ui-direction/
│           └── apple-ui-review/
├── scripts/
│   ├── validate_product_starting_point_evals.py
│   ├── validate_delivery_contract_evals.py
│   ├── validate_plugin_architecture.py
│   └── validate_source_registry.py
└── tests/
    ├── test_plugin_architecture.py
    ├── test_delivery_contract_evals.py
    ├── test_product_starting_point_evals.py
    └── test_source_registry.py
```

- `plugins/apple-ui-design/` 是完整可安装包，不包含仓库 README、Issue 历史或评测运行记录。
- `plugins/apple-ui-design/skills/` 包含三个可独立发现的工作流。
- `plugins/apple-ui-design/references/` 是产品、证据、平台、无障碍、研究与验证规则的唯一共享来源。
- `.agents/plugins/marketplace.json` 通过公开 GitHub 仓库暴露 Plugin。
- 根级 `SKILL.md` 与 `agents/openai.yaml` 只为旧版独立安装提供显式调用兼容。
- `evals/plugin-split/` 保留三个内置 Skills 的独立前向测试与安装后新会话证据。
- `evals/delivery-contracts/` 为六类交付合同分别提供一项真实任务与可观察的证据断言。
- `evals/product-starting-point/` 提供固定的小改动、重大改版与从零产品证据场景、评审断言和保留的前向测试证据。
- `scripts/validate_delivery_contract_evals.py` 用于检查合同覆盖、固定素材、必需产物、禁止声明和证据要求。
- `scripts/validate_product_starting_point_evals.py` 用于检查评测结构、必需场景、行为断言和固定素材路径。
- `scripts/validate_plugin_architecture.py` 用于保护 Skill 边界、共享规则所有权和安装包纯度。
- `tests/` 用于保护 Plugin 架构、评测与资源校验器必须识别的错误场景。

## 边界

该 Plugin 负责产品意图、视觉层级、Apple 平台行为、设计系统决策、适配策略和体验评审标准。

它不能替代 Swift 架构、并发、性能分析、CI、打包或发布等专项工程流程。当这些内容成为主要任务时，应将对应内置 Skill 与相应工程工作流配合使用。

## 维护原则

稳定的设计原则保存在 Plugin 的共享 references 中。当某项决策依赖具体版本时，应通过 Apple 当前官方资料核对 API、平台行为与 Human Interface Guidelines。

仓库维护策略与回归测试提示详见 [`docs/maintenance-and-sources.md`](docs/maintenance-and-sources.md)。

## 开源协议

本项目采用 [MIT License](LICENSE)。
