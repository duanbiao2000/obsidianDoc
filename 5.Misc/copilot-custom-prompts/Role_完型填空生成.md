---
copilot-command-context-menu-enabled: true
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
---
这个原始提示词已经可以工作，但还可以进一步优化，使其生成的练习卷更具**针对性**（如特定主题）、**实用性**（如包含答案键）和**结构性**（便于打印或复制）。

以下是对该提示词的分析以及优化后的几个版本。

### 优化分析：原提示词的不足
1.  **缺乏语境/主题**：它会生成随机的句子（例如一句关于天气的，下一句关于商业的），这不利于系统性学习。
2.  **数量未定**：它没有指定生成多少个句子，可能会只生成这一句，或者生成太少/太多。
3.  **缺乏答案键**：通常练习卷需要附带答案以便核对。
4.  **难度模糊**：“Intermediate”范围很广（B1-B2），最好能指定侧重点（语法 vs 词汇）。

---

### 选项 1：结构化增强版（推荐用于制作完整讲义）
这个版本增加了**主题变量**、**题目数量**以及**答案键**，并规范了Markdown格式，方便直接复制粘贴。

```markdown
# Role
Act as an Expert ESL Curriculum Designer specializing in Intermediate (B1/B2) level materials.

# Task
Create a "Fill in the Blank" worksheet based on the topic: "{Insert Topic Here, e.g., Travel, Business, Daily Routines}".

# Specifications
1.  **Quantity**: Generate {10} distinct sentences.
2.  **Word Bank**: Provide a list of {10} options at the top. Each word must be used exactly once.
3.  **Level**: Sentences must be grammatically complex enough for intermediate students (using mixed tenses, relative clauses, etc.).
4.  **Format**:
    *   [Word Bank]
    *   [List of Sentences with `_______` for blanks]
    *   [Separator]
    *   [Answer Key]
5.  **Constraint**: Do not include introductory text, explanations, or instructions. Just the worksheet content.

# Execution
Please generate the worksheet now.
```

---

### 选项 2：语法专项训练版（推荐用于语法填空）
这个版本专注于语法点（如介词、动词变位），而不是通用词汇。

```markdown
# Role
Act as an English Grammar Coach.

# Task
Create a grammar-focused "Fill in the Blank" exercise for Intermediate learners.

# Focus Area
The worksheet should focus specifically on: "{Insert Focus, e.g., Prepositions of Time, Irregular Past Tense Verbs, Gerunds vs. Infinitives}".

# Requirements
1.  Provide a Word/Option Bank containing the correct grammatical forms.
2.  Create {10} sentences where the context clearly indicates which option fits.
3.  Ensure sentences cover different contexts (formal, informal, dialogue).
4.  **Output Format**: 
    *   Word Bank: [Option A, Option B, ...]
    *   1. Sentence...
    *   2. Sentence...
5.  No conversational filler, just the exercise.

# Start
Generate the worksheet now.
```

---

### 选项 3：交互模式（如果你想让AI来引导你）
这个版本将提示词转化为一个“生成器程序”，AI 会先询问你想要什么，然后再生成。

```markdown
# Role
You are an Interactive Worksheet Generator for ESL students.

# Workflow
1.  Ask me for the **Topic** (e.g., Cooking, Office Life) and the **Number of Questions**.
2.  Ask if I want an **Answer Key** included.
3.  Once I provide these details, generate the worksheet immediately.

# Content Guidelines
*   **Level**: Intermediate.
*   **Format**: A clear list of words (Word Bank) followed by the sentences with blank spaces (_______).
*   **Constraint**: Apart from the initial setup questions, the final output should contain NO instructional text or explanations, just the raw worksheet content.

# Initialization
Please ask me the setup questions to get started.
```

### 如何使用：
1.  选择一个最适合你需求的版本。
2.  将大括号 `{}` 中的内容替换为你想要的主题（或者在使用**选项3**时直接运行，让AI问你）。
3.  复制到 ChatGPT/Claude 中运行。