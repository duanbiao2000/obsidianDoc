---
share_link: https://share.note.sx/09hwcjae#EhdwdkkSqZlWulqaUP2TXP1/S2KlUa5bAXE6KXno3h4
share_updated: 2025-10-10T14:48:45+08:00
---
# 如何用AI免费将Anki闪卡制作速度提升10倍！

### 目录
- [为什么使用 Anki 和 AI](#为什么使用-anki-和-ai-content-0027)
- [教程：从 YouTube 视频生成 Anki 卡片](#教程从-youtube-视频生成-anki-卡片-content-0104)
- [教程：将生成的卡片导入 Anki](#教程将生成的卡片导入-anki-content-0329)
- [扩展应用：处理本地视频和 PDF 文件](#扩展应用处理本地视频和-pdf-文件-content-0619)
- [推荐的高效学习工作流](#推荐的高效学习工作流-content-0923)
- [AI 总结](#ai-总结)

---

## 为什么使用 Anki 和 AI [原片 @ 00:27](https://www.bilibili.com/video/BV1zhpnzwEcu?t=27)*

- **传统 Anki 卡片制作的痛点**：过去制作 Anki 卡片需要手动操作，如阅读书籍、观看视频、截图和打字，这个过程耗时且容易打断学习流。
- **AI 自动化的优势**：利用 AI 可以自动化卡片制作过程，让学习者能更专注于理解和消化知识本身，而不是机械地制作笔记。
- **选择 Anki 的理由**：
    1.  **免费**：Anki 是一款免费的开源软件。
    2.  **强大的社区支持**：Anki 拥有庞大的用户社区，开发了数以百计的插件（Add-ons），几乎可以满足任何你能想到的学习需求。
        *![](/static/screenshots/screenshot_000_122da34c-1d08-4136-92af-4d35daeb9a6f.jpg)*
    3.  **丰富的插件生态**：例如，有维基百科弹窗、自动补全、中文支持、文本转语音等各类插件，可以极大地扩展 Anki 的功能。
        *![](/static/screenshots/screenshot_001_d97aef72-606a-4d89-b57a-f51f0dd2f9c3.jpg)*

## 教程：从 YouTube 视频生成 Anki 卡片 [原片 @ 01:04](https://www.bilibili.com/video/BV1zhpnzwEcu?t=64)*

本教程将以一个关于 `Transformers` 和 `LLM` 的 YouTube 视频为例，演示如何使用 `Google AI Studio` 自动生成 Anki 闪卡。

### 1. 准备工作
- **学习材料**：找到你想要学习的 YouTube 视频。
- **工具**：打开 **Google AI Studio**。
- **Prompt**：复制视频描述中提供的专用 Prompt。
    - **注意**：该 Prompt 专为 `Google Gemini` 设计，同时也有适用于 `ChatGPT` 的版本。
    *![](/static/screenshots/screenshot_002_7d71cd12-06fa-4574-9ff2-024b8f82c3ea.jpg)*

### 2. 生成卡片
1.  **粘贴 Prompt**：将复制的 `Google Gemini` Prompt 粘贴到 `Google AI Studio` 的输入框中。
    *![](/static/screenshots/screenshot_003_db54900d-6928-44b5-81a4-1afadb8aa118.jpg)*
2.  **输入视频 URL**：将 YouTube 视频的 URL 粘贴到 Prompt 下方的消息框中。
    *![](/static/screenshots/screenshot_004_f23b1d93-010b-4b19-b748-e2f57267c7e0.jpg)*
3.  **运行 AI**：点击运行按钮，AI 会开始处理视频并生成闪卡。这个过程可能需要几分钟，具体取决于视频的长度。
    *![](/static/screenshots/screenshot_005_62077ba1-5752-4b62-893f-48da319dd7f3.jpg)*

### 3. Google AI Studio 的优势
- `Google AI Studio` (使用 Gemini) 能够真正“观看”视频，包括分析视频中的视觉元素（图表、动画等），从而生成质量更高的闪卡。
- 相比之下，`ChatGPT` 只能依赖视频的文字转录稿，无法获取视觉信息。
*![](/static/screenshots/screenshot_006_49e6f99a-6726-466a-842a-2e405cbe4ec6.jpg)*

### 4. AI 处理期间的学习策略
- 在 AI 生成卡片的同时，你应该完整地观看一遍视频。
- **核心目标**：专注于理解视频的**核心概念**和**整体框架**，建立新旧知识之间的联系。
- **避免**：频繁暂停视频来做笔记，因为 AI 正在为你完成这项工作。这种方法可以保持学习的连贯性，提升理解效率。
*![](/static/screenshots/screenshot_007_c8ca17a8-f847-49cd-997b-f5fa5b77a81f.jpg)*

## 教程：将生成的卡片导入 Anki [原片 @ 03:29](https://www.bilibili.com/video/BV1zhpnzwEcu?t=209)*

### 1. 导出与准备
1.  **复制文本**：当 AI 生成完成后，点击右上角的按钮复制所有生成的文本内容。
    *![](/static/screenshots/screenshot_008_e31a8afd-497d-41a0-a918-b754fc3d4f28.jpg)*
2.  **创建 `.txt` 文件**：Anki 无法直接粘贴文本导入，需要通过文件导入。
    - 访问 `text-editor.co` 这类在线文本编辑器网站。
    - 粘贴刚刚复制的内容。
    - 下载文件，并命名为 `flashcards.txt`。
    *![](/static/screenshots/screenshot_009_8f6b1f87-30d8-435a-9ffc-7ebefc75b0e2.jpg)*

### 2. 导入 Anki
1.  **打开 Anki**，选择 `文件 (File)` -> `导入 (Import)`。
2.  **选择文件**：选中刚刚下载的 `flashcards.txt` 文件。
    *![](/static/screenshots/screenshot_010_782a38c0-80c1-4bf5-ae8b-1c67f1e7f385.jpg)*
3.  **关键设置：字段分隔符**：
    - 在导入选项中，确保**字段分隔符 (Field separator)** 设置为 **管道符 (Pipe)**，即 `|`。
    - 这是因为我们的 Prompt 中明确指示 AI 使用 `|` 来分隔问题和答案。
    *![](/static/screenshots/screenshot_011_59f437aa-fe1b-46fd-b477-5ac6bcf55c22.jpg)*
4.  **配置导入选项**：
    - **笔记类型 (Note Type)**：选择 `Basic`。
    - **卡组 (Deck)**：选择你想要存入的卡组，例如 `Default`。
    - **添加标签 (Tags)**：可以为这批卡片添加标签，便于管理，例如 `LLM`, `3blue1brown`。
    *![](/static/screenshots/screenshot_012_fabec21e-8b67-4e1e-93f0-4de79f0c46aa.jpg)*
5.  **完成导入**：点击 `导入 (Import)` 按钮，所有卡片就会被添加到 Anki 中。

### 3. 利用时间戳优化卡片
- **时间戳功能**：Prompt 中包含一项指令，要求 AI 为每张卡片附上其内容来源在视频中的**时间戳**。
    *![](/static/screenshots/screenshot_013_9d2e76bd-b82d-4ac9-9d3c-2e832eef96fc.jpg)*
- **优化工作流**：
    1.  在复习卡片时，如果发现某张卡片需要视觉辅助（如图表、公式推导过程），可以查看其附带的时间戳。
    2.  跳转到视频的对应时间点，截取关键图像。
    3.  将截图直接粘贴 (`Ctrl+V` 或 `Cmd+V`) 到 Anki 卡片的相应字段中，极大地丰富了卡片内容。
    *![](/static/screenshots/screenshot_014_915c1164-d1b7-45b6-96d2-90d162086bfb.jpg)*
- **自定义**：如果你不需要此功能，可以在 Prompt 中删除相关指令（视频中提到是第5点）。

## 扩展应用：处理本地视频和 PDF 文件 [原片 @ 06:19](https://www.bilibili.com/video/BV1zhpnzwEcu?t=379)*

### 1. 处理本地视频文件
- 你可以将本地存储的视频文件（如大学课程录像）直接**拖拽**到 `Google AI Studio` 中。
- AI 会上传并处理该视频，后续生成卡片的步骤与处理 YouTube 视频完全相同。
*![](/static/screenshots/screenshot_015_efbecccd-93d3-470c-ab0f-3b45ff696be1.jpg)*

### 2. 处理 PDF 文档
1.  **上传 PDF**：在 `Google AI Studio` 中新建一个聊天，然后将 PDF 文件（如讲义、电子书）拖拽进去。
    *![](/static/screenshots/screenshot_016_563e6462-0b00-41f4-a243-4d964452bf22.jpg)*
2.  **修改指令**：粘贴相同的 Prompt，并在下方额外添加一条消息，指明处理对象，例如：“`Please make flashcards for the entire PDF document attached`”。
3.  **运行并生成**：AI 会逐页阅读 PDF 并生成闪卡。

#### **处理数学密集型内容的注意事项**
- **问题**：在某些学科（如量子场论）中，管道符 `|` 本身就是数学公式的一部分。如果仍用它作为分隔符，会导致 Anki 导入时格式错乱。
    *![](/static/screenshots/screenshot_017_6a8cd376-ab79-4645-99de-8f1a39992154.jpg)*
- **解决方案**：
    1.  **修改 Prompt**：在 Prompt 中，将分隔符从 `|` (Pipe) 修改为其他不常用的符号，例如**分号** (`;`)。
    2.  **添加约束**：同时在 Prompt 中明确指示 AI “**不要在其他任何地方使用分号**”，以避免混淆。
    3.  **重新生成**：修改 Prompt 后，需要重新运行 AI。
    4.  **更新 Anki 设置**：在 Anki 导入时，将字段分隔符相应地更改为分号 (`;`)。
    *![](/static/screenshots/screenshot_018_565e430a-f636-4a69-90a9-b5d2f6b7e9ce.jpg)*

## 推荐的高效学习工作流 [原片 @ 09:23](https://www.bilibili.com/video/BV1zhpnzwEcu?t=563)*

为了最大化学习效率，建议采用以下流程：

1.  **学习前：生成卡片**
    - 在观看视频或阅读文档**之前**，先将学习资料和 Prompt 输入 `Google AI Studio`，让 AI 开始生成闪卡。
    *![](/static/screenshots/screenshot_019_b7a22f45-9c6e-40ca-91b6-2410bbb0d142.jpg)*
2.  **学习中：专注理解**
    - 全神贯注地观看视频或阅读材料，目标是**理解宏观概念和知识体系**，无需分心做笔记。
3.  **学习后：回顾与优化**
    - 学习结束后，AI 生成的闪卡也已准备就绪。
    - 逐一回顾这些闪卡，这有助于巩固记忆中的细节。
    - 利用卡片上的**时间戳**，返回原文或视频，为需要视觉辅助的卡片添加截图、图表或公式。
    *![](/static/screenshots/screenshot_020_45e22525-ec52-47c8-b13d-f0caa34ca2f8.jpg)*

这种工作流将**高层次的理解**与**细节的记忆**分离开来，使整个学习过程更加流畅和高效。

## AI 总结

本视频教程详细介绍了一种利用 AI 工具（特别是 `Google AI Studio`）与 `Anki` 相结合的高效学习方法，旨在将制作闪卡的速度提升10倍。核心流程包括：使用专门设计的 Prompt，将 YouTube 视频、本地视频文件或 PDF 文档输入 AI 进行分析，自动生成格式化的问答卡片。随后，将生成的文本通过 `.txt` 文件导入 Anki。该方法不仅节省了大量手动制作卡片的时间，还通过在卡片中加入内容来源的时间戳，方便学习者后续补充截图以增强记忆。教程还特别指出了处理数学密集型内容时更换分隔符（如将 `|` 换成 `;`）的技巧，并最终提出了一套“先生成、后学习、再优化”的高效工作流，帮助学习者专注于理解，同时轻松构建起详细的知识复习库。