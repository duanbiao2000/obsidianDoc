---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 1761118141562
share_link: https://share.note.sx/p8kki00o#+u8OIeyQayh9bkjz9+4qIS4xr3vOhqg4dhHFT6WRzRY
share_updated: 2025-10-22T18:51:15+08:00
view-count: 8
---
# Obsidian2Anki 极简生成器

### 0. 插件正则配置
```regex
in-line QA:  ^(.*[^\n:]{1}):{2}([^\:]{1}.*)
Cloze: ((?:.+\n)*(?:.*{.*)(?:\n(?:^.{1,3}$|^.{4}(?<!<!--).*))*)
```

### 1. 核心指令 (Core Logic)
按以下优先级处理输入内容：
1.  **信息熵提取**：识别核心定义、底层逻辑、高价值洞见（删除废话）。
2.  **型态分配**：
    -   **Cloze**：用于术语耦合、逻辑链条、流程步骤。
    -   **In-line QA**：用于本质追问（Why/How）、第一性原理、方法论对冲。

### 2. 生成准则 (Rules)

| 维度 | Cloze (填空) | In-line QA (问答) |
| :--- | :--- | :--- |
| **格式要求** | `{cn:text}` (max n=3) | `问题 :: 答案` |
| **挖空策略** | 仅挖掉高密度关键词，保留上下文锚点 | 问题须具备启发性，答案须具备知识密度 |
| **逻辑约束** | 相同序号复用表意关联项 | 避免单一定义，聚焦“原理/差异/应用” |

### 3. 示例 (Minimal Examples)

-   **Cloze**: {c1:CAP定理}指出，分布式系统在{c2:分区容错性(P)}下，只能在{c3:一致性(C)}与{c1:可用性(A)}中二选一。
-   **QA**: 为什么 RAG 优于纯大模型微调？ :: RAG 提供可追溯的外部知识增强，降低幻觉风险，且无需重新训练即可实时更新知识库。

### 4. 优化选项 (Optimization)

-   **[A] 强化对抗**：增加易混淆概念对比（如：协程 vs 线程）。
-   **[B] 生产力导向**：转化理论为具体的 CLI 命令或 Code Snippet 记忆。
-   **[C] 极度压缩**：删除所有背景，仅保留公理化陈述。

---

**PROMPT TO LLM:**
`[直接粘贴上述内容 + 你的笔记]`
`执行指令：根据上述逻辑，将以下笔记转化为 Anki 卡片，追求高信号量与低冗余。`