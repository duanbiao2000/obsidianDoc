---
rating: 3.0
tags:
- agent-task-system
- specification-based-execution
- agent-architecture
- algorithm
- Domain/AI
- Domain/AI/PromptEngineering
- Type/Reference
view-count: 4
---

## 🔗 相关链接

**上级索引**:
- [[2.Topics\00.协议与规范\Spec\_Index_of_Rules.md|Rules]]
- [[2.Topics\00.协议与规范\_Index_of_00.协议与规范.md|00.协议与规范]]
- [[2.Topics\_Index_of_2.Topics.md|2.Topics]]

---

## 1. Agent 核心哲学（Spec → Task → 执行）

- 把 LLM 当成「高能但死板的执行引擎」，只按 **Spec + Task** 行动。  
- 不依赖常识、不猜用户意图，一切都写进 Spec。  
- 每一阶段的输出，都要转写为下一阶段的 **Task 更新或完成记录**，形成闭环。

---

## 2. Agent 主循环：六阶段 = 六类 Task 流程

### S1：Spec 解析 & 根任务创建（Initial）

**目标：** 从用户输入构造清晰的工作规格和根任务。

- 从输入中抽取并写入 Spec：  
  - `role`（期望扮演的角色）  
  - `final_goal`（终极目标）  
  - `scope`（边界/不做什么）  
  - `context`（关键背景）
- 基于 Spec 生成根任务 `T0`：  
  - `description`：用一句话说明要完成什么结果  
  - `status`：`todo`  
  - `constraints`：重要限制（字数、风格、目标对象等）

> 输出：  
> - `Spec` 块  
> - `TaskList` 初始版（至少包含一个根任务）

---

### S2：任务拆解 & 显性规划（Thinking）

**目标：** 把根任务拆成可执行子任务，并显式展示路径。

- 针对 `T0`：拆解为 3–7 个子任务 `T1..Tn`，写入：  
  - 明确动词开头的描述（如“分析…”，“生成…”，“评估…”）  
  - 输入依赖（依赖哪些 Task 的输出）  
  - 预期输出形式（文本结构、要素清单等）
- 用流程形式给出执行顺序：  
  - `T1 → T2 → T3 …`（可以包含分支，但要说清条件）

> 输出更新：  
> - `TaskList`：新增子任务，状态均为 `todo`  
> - `Plan`：用 A → B → C 概述执行步骤

---

### S3：自我评估 Task（Self-Eval）

**目标：** 每个关键产出 Task 都要有自评 Task，与之配对。

- 对每个关键执行 Task（如“生成摘要”、“给出方案”），派生一个自评 Task `Eval_Tx`：  
  - `description`：对照 Checklist 审核 `Tx` 的输出  
  - `checklist` 示例：  
    - 是否满足字数 / 结构要求？  
    - 是否覆盖所有必须要点？  
    - 是否违反了负向清单？
- 自评输出为：  
  - `pass: yes/no`  
  - `issues: […]`（缺陷列表）

> 输出更新：  
> - `TaskList`：新增若干 `Eval_*` 任务  
> - 对已完成的执行 Task，补充其 `eval_result`

---

### S4：元反思 Task（Meta-Reflect）

**目标：** 对“错在哪 / 偏在哪”做溯源，而不是只改表面。

- 针对评估未通过的 Task，为其创建 `Meta_Tx`：  
  - 重点回答：  
    - 是 Spec 理解错误？  
    - 是信息缺失？  
    - 是推理链断裂？  
    - 是约束不清/冲突？
- 输出一组「偏差原因」与「可操作调整点」。

> 输出更新：  
> - `TaskList`：新增 `Meta_*` 任务  
> - 在 `Spec` 或 `Task` 上标记需要调整的字段（如：补充约束、改写描述）

---

### S5：针对性改进 Task（Refinement）

**目标：** 不推倒重来，而是基于 S3/S4 的信息做精准修正。

- 对每个有问题的执行 Task，新建一个 `Refine_Tx`：  
  - 引用：`based_on: Tx, Eval_Tx, Meta_Tx`  
  - 明确：  
    - 需要补充哪些信息？  
    - 风格 / 结构需要如何调整？  
    - 哪些误解要避免重现？
- 用更新后的 Spec/Task 再次生成输出，标记为 `Tx_v2`。

> 输出更新：  
> - `TaskList`：`Refine_*` 完成后，将老版本标记为 `superseded`，新版本标记为 `done`  
> - 记录「从 v1 → v2 的变更点」

---

### S6：策略沉淀 & 模板更新（Update）

**目标：** 从这次执行中抽取可复用模板，写回「通用 Prompt/Task 模板库」。

- 新建 `Template_Update` 任务：  
  - 从这次流程中抽取：  
    - 哪些 Spec 字段是必须的？  
    - 哪些 Checklist 在评估中最有用？  
    - 哪些错误/偏差值得写进「负向清单」？
- 将这些内容沉淀为：  
  - 通用 Prompt 模板片段  
  - 通用 Task 模板（如统一的 `Summarize_Task`、`Eval_Task` 格式）

> 输出更新：  
> - `Templates` 区域：新增或迭代模板  
> - 为后续同类任务提供可直接复用的起点

---

## 3. Task 写作规范（面向 Agent 内部）

- **动词前置**：  
  - Task 描述统一以动词开头（如“解析 Spec…”，“生成 3 个要点…”）。  
- **结构化输出**：  
  - 结果用 Markdown 标题 + 编号列表，方便后续 Task 复用。  
- **强量化**：  
  - 在 Task 中写清：数量（3 条）、字数（150 字内/以上）、格式（表格/要点）。  
- **负向清单**：  
  - Task 中显式给出「禁止项」（如：不得提及模型名称、避免术语）。  
- **边界设定**：  
  - 明确缺失数据的处理规则（如：信息不足时输出 `N/A` 并列出需要的补充信息）。

---

## 4. 示例：摘要任务的 Agent Task 流（闭环）

1. `T0`（根任务）  
   - 目标：为输入文本生成 150 字以内摘要。

2. `T1`（规划 Task）  
   - 生成 3 个核心论点列表。

3. `T2`（执行 Task）  
   - 基于 `T1` 写出 150 字内摘要。

4. `Eval_T2`（自评）  
   - 检查：  
     - 字数是否 ≤150  
     - 3 个论点是否都覆盖  
     - 是否遵守负向清单

5. `Meta_T2`（元反思）  
   - 若不达标：分析是字数约束理解错误，还是遗漏要点。

6. `Refine_T2`（改进）  
   - 按 `Eval_T2` 和 `Meta_T2` 修正摘要，再生成 `T2_v2`。

7. `Template_Update`  
   - 更新「摘要类任务模板」：  
     - 固定增加「字数下限/上限」  
     - 固定要求先列 3 个要点再写摘要  

整个过程：  
Spec → 任务列表 → 执行 → 自评 → 元反思 → 精准改进 → 模板沉淀  
= 一个可持续迭代的 **Agent 风格 Task 系统**。