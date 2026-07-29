<div align="center">

# Apple UI Design

**面向 iOS、iPadOS 与 macOS 的产品优先型 UI 设计 Skill，强调原生、独特与可验证。**

[English](README.md) · [简体中文](README.zh-CN.md)

</div>

## 项目简介

Apple UI Design 是一个用于 Apple 生态产品界面设计、适配、实现与评审的 Agent Skill。

它从产品意图和项目证据出发，将共享的产品 DNA 与符合平台习惯的交互方式结合起来。Apple 设计规范用于指导体验，但不会把所有产品都塑造成同一种视觉模板。

## 能力范围

- Apple 平台产品与视觉方向探索
- 页面、状态、流程和导航设计
- 共享设计系统与平台差异化表达
- iOS、iPadOS 与 macOS 的跨平台适配
- 面向 SwiftUI 的原生原型与界面实现
- 可访问性、本地化、动效与自适应布局决策
- 基于真实证据的设计与实现评审

## 核心原则

1. **产品意图优先。** 已确认的用户需求决定界面必须完成什么。
2. **项目上下文是本地事实依据。** 在作出新决定前，先检查现有需求、设计系统、组件、资产与平台目标。
3. **原生不等于千篇一律。** Apple 平台规范指导交互，品牌与产品 DNA 保留独特辨识度。
4. **跨平台需要适配，而不是放大。** iPhone、iPad 与 Mac 可以共享同一产品，但在层级、密度、导航和输入方式上应合理变化。
5. **可访问性与本地化从设计阶段开始。** 它们不是交付前才执行的检查清单。
6. **视觉质量需要证据。** 编译成功不等于体验通过；重要状态和真实交互需要经过渲染与验证。

## 工作模式

Skill 会根据当前任务选择合适的处理深度：

- **方向探索**——建立或探索产品的视觉与交互方向
- **页面或流程设计**——设计页面、状态集合或端到端任务
- **设计系统**——定义或扩展共享 DNA、语义化 Token 与组件
- **跨平台适配**——将现有体验转化到另一个 Apple 平台
- **原生原型或实现**——在明确需要时创建 SwiftUI 原型或生产界面
- **评审与迭代**——依据已确认的产品意图评估现有设计或实现

## 安装

将仓库克隆到个人 Codex Skills 目录：

```bash
git clone https://github.com/RexYoung000/apple-ui-design-skill.git ~/.codex/skills/apple-ui-design
```

如果已经安装，可以使用以下命令更新：

```bash
git -C ~/.codex/skills/apple-ui-design pull --ff-only
```

## 使用方式

可以明确调用 Skill：

```text
使用 $apple-ui-design 为这个 iPad 应用设计新用户引导流程。
```

也可以自然描述 Apple UI 任务：

```text
评审这个 macOS 界面的信息层级、键盘操作、可访问性，
以及它与现有产品设计系统的一致性。
```

Skill 会先检查项目中已有的证据，再提出问题。当某项决定会实质影响产品时，它会一次只确认一个关键问题，并说明推荐方向及理由。

## 仓库结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── accessibility-and-localization.md
    ├── apple-platform-adaptation.md
    ├── authority-and-principles.md
    ├── context-and-alignment.md
    ├── design-system-and-dna.md
    ├── maintenance-and-sources.md
    ├── prototyping-and-implementation.md
    └── validation-and-review.md
```

- `SKILL.md` 定义角色、范围、工作流程、评审方法与任务分流规则。
- `agents/openai.yaml` 提供展示信息与默认调用提示词。
- `references/` 存放按当前任务需要加载的专项设计指导。

## 边界

该 Skill 负责产品意图、视觉层级、Apple 平台行为、设计系统决策和体验验收标准。

它不能替代 Swift 架构、并发、性能分析、CI、打包或发布等专项工程流程。当这些内容成为主要任务时，应将本 Skill 与相应的工程工作流配合使用。

## 维护原则

稳定的设计原则保存在 Skill 中。当某项决策依赖具体版本时，应通过 Apple 当前官方资料核对 API、平台行为与 Human Interface Guidelines。

维护策略与回归测试提示详见 [`references/maintenance-and-sources.md`](references/maintenance-and-sources.md)。

## 开源协议

本项目采用 [MIT License](LICENSE)。
