---
aliases:
date: 2025-02-28 07:04
update:
categories:
  - Mindset
tags:
  - Domain/Mindset/Reflection
---
用能力有限的AI做复杂任务，老是忘事？🤔🚫

别担心！我的笔记「[[Claude开发流程]]」给你一套策略！✅🗺️

就像和记性差但聪明的助手一起搭乐高：
🧱 **拆解任务** 到AI能处理的小块！👇
🧩 **手动接力** 上下文，确保它不跑偏！➡️
🔗 用 **外部工具** 缝合、验证AI的成果！🛠️

核心就是：**分而治之** + **持续上下文** + **工具辅助**！💡🔑 帮你一步步搞定复杂项目！💪🚀

**笔记核心主题梳理**

这份笔记 [[Claude开发流程]] 的核心主题是**为使用具有有限能力（特别是记忆/上下文限制）的 AI 助手（以旧版或免费版 Claude 为代表）进行复杂软件开发或类似任务提供一套结构化的工作流程或方法论**。

它通过“与记忆力差但聪明的助手一起建造乐高模型”的比喻，阐述了以下关键策略：

1.  **任务拆解与模块化：** 将复杂任务分解为 AI 可以处理的、小而清晰的单元。
2.  **精准指令与上下文管理：** 通过精心设计的 Prompt 和持续的上下文传递，确保 AI 理解并专注于当前任务。
3.  **增量与迭代开发：** 分步骤、按顺序地完成任务，并控制每一步的输出大小。
4.  **工程化辅助：** 利用外部工具来弥补 AI 的不足，如代码整合、脚手架等。
5.  **质量控制与验证：** 对 AI 生成的每一部分进行检查和测试。
6.  **知识管理与恢复：** 记录关键信息、技巧，并建立错误恢复机制。
7.  **优化交互效率：** 提升 Prompt 设计技巧，管理对话历史。

其**核心思想**总结为：**“分而治之” + “持续上下文管理” + “工具辅助整合与验证”**。

---
## Claude工具使用策略

*   Claude's use of tools 🔧 depends on query complexity 🧠 and the real-time nature ⏰ of the required information.
*   Claude is equipped with diverse tools 🛠️ including web search 🔍, file fetching 📄, Google Drive/Calendar/Gmail access 📧, analysis tools 📊, and artifact creation ✍️.
*   Internal tools (like Google Drive and Gmail) are prioritized ✨ for accessing personal or company data 💾.
*   Tool-based responses must include proper citations 📝 using `<antml:cite>` tags.
*   Artifacts should be used for substantial content 📦 like code 💻, analysis 📊, or writing ✍️ to improve readability ✨.
*   Specific rules 📜 govern tool usage, such as handling truncated results ✂️ or not guessing email addresses 🚫📧.
*   Search tools 🔍 are used only when necessary ✅, with the number of calls varying based on complexity 🧠 and data freshness 🆕.
*   Query types are categorized 📁 (Never Search, Offer Search, Single Search, Research) to guide the search strategy 🗺️.
*   Strict adherence ✅ to copyright ⚖️ (no copying large text 🚫📄) and safety guidelines 🚨 is mandatory 💪.
*   User preferences 👍 can be considered 🤔 but not at the expense of safety 🚨 or accuracy ✅.

**主要主题和重要观点：**

这份简报回顾了 Claude 在回答查询时使用的工具和策略，强调了其在平衡自身知识、外部信息和个人/内部数据方面的能力。

1. **工具使用策略取决于查询特性：** Claude 是否以及何时使用工具取决于查询的复杂性以及所需信息的新旧程度或变化速度。

- 对于历史事实、基本概念或不随时间变化的知识，Claude 通常直接回答，无需工具。
- 对于变化缓慢的信息（如年度统计数据），Claude 会在直接回答后选择性提供搜索选项。
- 对于需要实时数据或变化非常频繁的信息（如天气、新闻、股票价格），Claude 会立即使用网络搜索或相关工具。对于用户个人或公司内部的快速变化信息，可能会使用内部工具。
- 查询的复杂性决定了需要调用多少工具。简单的查询可能只需要一次工具调用，而复杂的查询可能需要多次调用（通常在 2 到 20 次之间，甚至更多）。

1. **可用工具的多样性：** Claude 配备了多种工具来辅助回答问题，这些工具能够获取信息、分析数据并以不同格式呈现内容。

- **网络搜索 (web_search):** <antml:cite index="2-1:2">用于搜索网络上的信息，适用于当前事件、快速变化的主题或知识截止日期之后的信息。</antml:cite>
- **获取网页内容 (web_fetch):** <antml:cite index="2-4:4">用于获取指定 URL 的完整网页内容，因为网络搜索结果片段通常太短。</antml:cite>
- **Google Drive 搜索 (google_drive_search):** <antml:cite index="2-6:7">用于搜索用户的 Google Drive 文件，适用于查找公司特定文档、内部政策或个人文件等内部或个人信息。</antml:cite>
- **Google Drive 获取文件内容 (google_drive_fetch):** <antml:cite index="2-8:9">基于文档 ID 列表，用于获取 Google Drive 文档的内容，是比搜索工具更直接的读取方式。</antml:cite>
- **Google Calendar 工具 (list_gcal_calendars, fetch_gcal_event, list_gcal_events, find_free_time):** 用于列出、获取特定事件、列出或搜索事件以及查找多个日历中的空闲时间。
- **Gmail 工具 (read_gmail_profile, search_gmail_messages, read_gmail_thread):** 用于检索用户 Gmail 个人资料、列出或搜索邮件以及读取特定邮件线程。
- **Artifacts (artifacts):** <antml:cite index="2-13:14">用于创建和更新 artifact，可用于代码、文档、HTML、SVG、Mermaid 图和 React 组件等内容，可以减少消息长度并提高可读性。</antml:cite>
- **分析工具 (repl):** <antml:cite index="2-16:16">这是一个 JavaScript 环境中的代码执行工具，适用于需要高度准确性的复杂数学问题或分析用户上传的文件。</antml:cite>

1. **内部工具的优先使用：** 对于涉及用户个人或公司内部的信息，Claude 会优先使用内部工具（如 Google Drive 或 Gmail 工具），因为这些信息无法通过网络搜索获得。
2. **引用规范：** 如果回答基于工具返回的内容，必须使用 <antml:cite> 标签进行适当引用。

- <antml:cite index="3-3:3">每个源自搜索结果的具体声明都应包含在 <antml:cite> 标签中。</antml:cite>
- <antml:cite index="3-4:6">index 属性应是支持该声明的句子索引的逗号分隔列表，可以是单个句子或连续的句子范围。</antml:cite>
- <antml:cite index="3-8:8">引用应使用支持声明所需的最少句子数量。</antml:cite>
- <antml:cite index="3-9:10">如果搜索结果不相关，应礼貌地告知用户，并且不使用引用。</antml:cite>

1. **Artifact 的使用指南：** Artifacts 应用于实质性的代码、分析和写作内容，例如原创创意写作、深度分析内容、自定义代码、报告、结构化文档等。

- <antml:cite index="3-20:20">正确使用 artifacts 可以减少消息长度并提高可读性。</antml:cite>
- <antml:cite index="3-21:23">Artifacts 的使用应基于内容长度和类型，20 行以上且符合标准的文本应创建 artifact。</antml:cite>
- 支持的代码、文档、HTML、SVG、Mermaid 和 React 组件等类型。对于 React 组件，强调使用 Tailwind 的核心工具类进行样式设计，避免使用任意值。
- 可以使用 window.fs.readFile API 读取用户上传的文件。

1. **工具使用细则和限制：**

- <antml:cite index="3-157:158">对于 Gmail 工具，如果用户要求查找特定人员的邮件，不要猜测其电子邮件地址，而是通过搜索并请用户确认。</antml:cite>
- 如果工具结果被截断，应按照工具描述获取完整响应，<antml:cite index="3-160:160">绝不使用截断的响应得出结论，除非得到用户许可。</antml:cite>
- <antml:cite index="3-161:161">不要直接提及技术性的响应参数名称。</antml:cite>
- Google Drive Search 工具适用于用户的 Google Drive 文件，包括私人文件和公司内部文件。

1. **搜索工具的使用原则：** Claude 在必要时才使用搜索工具，并且会根据查询的复杂性调整搜索次数。

- <antml:cite index="3-169:169">如果无需工具即可回答，则不使用工具。</antml:cite>
- <antml:cite index="3-170:170">如果不确定是否需要搜索，先直接回答，然后提供搜索选项。</antml:cite> 仅对快速变化的信息（如天气、新闻）立即搜索。
- <antml:cite index="3-171:171">根据查询复杂性调整工具调用次数，从 1 次到 20 次或更多。</antml:cite>
- <antml:cite index="3-172:172">优先使用最适合查询的工具，对于个人/公司数据优先使用内部工具。</antml:cite>
- <antml:cite index="3-175:175">永不复制超过 20 个单词的搜索结果内容，以尊重版权。</antml:cite>
- <antml:cite index="3-179:182">根据信息变化速度决定是否搜索：快速变化立即搜索，适度变化回答后提供搜索，稳定信息永不搜索。</antml:cite>

1. **特定查询类型的处理：**

- <antml:cite index="3-186:196">“永不搜索”类别：信息变化慢或不变化，基本概念，通用知识。</antml:cite>
- <antml:cite index="3-198:208">“不搜索但提供”类别：信息变化较慢（每年或几年），统计数据，排名。</antml:cite>
- <antml:cite index="3-210:218">“单次搜索”类别：需要实时数据或频繁变化的信息，有单一明确答案的简单查询，简单的内部查询。</antml:cite>
- <antml:cite index="3-220:234">“研究”类别：需要 2 到 20 次工具调用，需要比较、验证或综合多个来源的信息，需要结合网络和内部信息。</antml:cite> 复杂的查询需要至少 5 次工具调用。

1. **版权和安全要求：** 必须严格遵守版权要求，<antml:cite index="3-241:242">绝不复制受版权保护的材料，包括歌词。</antml:cite> <antml:cite index="3-250:250">避免生成超过 30 个单词的搜索结果摘要。</antml:cite> 严格遵守有害内容安全要求，<antml:cite index="3-259:259">不创建有害内容的搜索查询或引用有害来源。</antml:cite>
2. **用户偏好和风格：** Claude 可以根据用户偏好和风格进行调整，但应仅在相关且不牺牲安全性、正确性、有用性、相关性或适当性的情况下应用。

这份简报提供了 Claude 在信息检索、工具使用和内容生成方面的核心原则和详细策略，特别是强调了工具选择的依据、各类工具的功能、对内部信息的处理以及版权和安全的重要性。

