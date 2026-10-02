你描述的最贴切名称是 **“列表项内联展开”**：点某条后，详情出现在这条摘要下方，把后续条目往下推，用户仍留在原清单里。

可以按需要使用三个候选词：

- **内联展开／可展开列表项（inline expansion / expandable row）**：最适合直接写进需求，清楚交代“原位置展开”。
- **展开控件（disclosure）／手风琴（accordion）**：前者强调单个条目的展开与收起；后者常用于一组纵向排列的可展开内容。“手风琴”本身不决定只能展开一条，还是允许同时展开多条。[The Component Gallery 的 Accordion 页面](https://component.gallery/components/accordion/)列出了这些相近名称。
- **渐进披露（progressive disclosure）**：描述“先给摘要，需要时再给详情”的信息策略，比具体组件更宽泛。

这些是沟通与检索的候选词，不能单凭名称确定某个 Apple 原生组件或实现 API。

| 方式 | 详情在哪里 | 对清单操作的影响 |
| --- | --- | --- |
| 列表项内联展开 | 原条目摘要下方，属于清单内容 | 后续条目下移；收起后恢复紧凑列表，无需返回上一页 |
| 抽屉／底部面板 | 通常从屏幕边缘进入独立面板 | 与条目所在位置分离，可能覆盖清单；是否允许操作背景，要看它是否为模态 |
| 弹窗／对话框 | 浮在当前内容之上的独立区域 | 模态对话框通常要求先完成或关闭，才能继续操作清单；“弹窗”这个泛称本身不能确定行为 |

我建议参考 **[GOV.UK Design System 的 Accordion 实例](https://design-system.service.gov.uk/components/accordion/default/)**。它是公开可操作的网页。我实际点击了第一条：详情在标题下出现，第二条随之下移，页面没有跳转；控件从“Show”变为“Hide”，焦点仍在刚操作的控件上。

适合借鉴的是 **摘要与详情的归属关系、原位置展开，以及清楚的展开／收起状态反馈**。对你的清单工具，可以理解为“摘要 → 点展开 → 同一条目下显示现有详情 → 点收起 → 摘要”。网站的字体、配色和“全部展开”按钮，不属于这次需要采用的范围。[组件说明](https://design-system.service.gov.uk/components/accordion/)也指出，隐藏内容有发现成本，是否值得采用取决于实际任务。

这份参考属于 **Web 交互启发（inspiration only）**。它证明这种网页模式存在、且示例能够展开；还不能据此认定它适合你的真实详情长度、会提高使用效率，或已经具备 iPhone 上正确的触控、滚动、VoiceOver、动态字体和减少动态效果表现。当前只有你的文字描述，没有现有界面与原生运行证据，因此结论限于设计咨询。若后续决定实施，最关键的验证是用已有的最长条目试一次“展开、继续查看下一条、收起”，检查位置感与清单操作是否仍然清楚；展开几条的规则仍需依据实际任务确定。

---

本次实际读过的技能与引用：

- [apple-ui-direction/SKILL.md](../../../../../plugins/apple-ui-design/skills/apple-ui-direction/SKILL.md)：按用户描述限定范围，使用候选词而不把名称当作 API。
- [delivery-contracts.md](../../../../../plugins/apple-ui-design/references/delivery-contracts.md)：开始与结束均读取；借用 UI Review 的文字咨询证据门槛控制结论，不声称设计、原型或原生体验已完成。
- [design-system-and-dna.md](../../../../../plugins/apple-ui-design/references/design-system-and-dna.md)：只使用“Informal Descriptions and Candidate Terms”等相关内容。
- [interaction-and-motion.md](../../../../../plugins/apple-ui-design/references/interaction-and-motion.md)：核对展开、反转、焦点与原生验证边界。
- [research-and-source-evidence.md](../../../../../plugins/apple-ui-design/references/research-and-source-evidence.md)：区分目录、具体示例、Web 启发与 Apple 原生证据。
- [source-registry.json](../../../../../plugins/apple-ui-design/references/source-registry.json)：选择 Component Gallery 作为组件和术语检索起点，再进入原始设计系统。

2026-10-02 实际访问的精确页面：

- [https://component.gallery/components/accordion/](https://component.gallery/components/accordion/)：读取组件定义与相近名称，找到 GOV.UK 的原始链接。
- [https://design-system.service.gov.uk/components/accordion/](https://design-system.service.gov.uk/components/accordion/)：读取使用条件、限制与状态说明。
- [https://design-system.service.gov.uk/components/accordion/default/](https://design-system.service.gov.uk/components/accordion/default/)：浏览器中实际查看折叠状态并点击第一条展开，检查前后布局与展开控件的状态、焦点。

未修改插件仓库，未安装依赖；本次仅保存这份咨询回答。
