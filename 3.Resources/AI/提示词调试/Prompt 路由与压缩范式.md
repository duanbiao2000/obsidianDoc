### 概念建模 (Concept Model)

概念建模旨在识别笔记中描述的核心概念及其相互关系，理解这套范式的“是什么”。

**核心概念：**

1.  **任务 (Task):** 用户提出的需要 AI 完成的复杂工作。
2.  **AI 智能体 (AI Agent):** 具备思考、规划、执行、反馈能力的 LLM，是执行任务的主体。
3.  **Prompt:** 与 LLM 交互的文本指令，驱动 AI 智能体的行为。
4.  **工具 (Tool):** AI 智能体可调用的外部能力（如搜索引擎、数据库、分析器），用于扩展 LLM 的功能边界。
5.  **工具选择 (Tool Selection):** AI 智能体根据任务需求从可用工具集中选取最合适工具的过程。
6.  **Prompt 路由 (Prompt Routing):** 指导 AI 智能体在执行过程中动态决定何时、何地、如何调用不同的 Prompt 模块或外部工具的机制。
7.  **执行轨迹/行为链元数据 (Execution Trace/Behavior Chain Metadata):** 记录 AI 智能体执行任务过程中的思考、决策、工具调用、结果等序列信息，用于回溯和分析。
8.  **路径 (Path):** AI 智能体完成任务的特定执行序列，由一系列思考、决策和工具调用组成。
9.  **路径采样 (Prompt Path Sampling):** 探索并生成完成同一任务的多种不同执行路径的过程。
10. **路径压缩 (Path Compression):** 分析成功的执行路径，提炼核心逻辑，生成更简洁高效的 Prompt 或策略的过程。
11. **反馈闭环 (Feedback Loop):** 利用执行结果或错误信息调整后续行为，提高任务成功率和鲁棒性的机制。
12. **Prompt 蒸馏 (Prompt Distillation):** 一种特殊的路径压缩技术，旨在让简单模型或短 Prompt 学习复制复杂模型或长 Prompt 的行为或策略。

**概念关系：**

*   **用户** 提出 **任务**。
*   **任务** 由 **AI 智能体** 执行。
*   **AI 智能体** 通过与 **Prompt** 交互进行思考和决策。
*   **AI 智能体** 执行任务时，可能需要调用 **工具**。
*   **Prompt 路由** 决定 **AI 智能体** 如何选择 **Prompt** 和调用 **工具** (**工具选择** 是其中一部分)。
*   每次执行步骤（思考、工具调用）都会生成 **执行轨迹** 的一部分。
*   完整的 **执行轨迹** 构成一条 **路径**。
*   **路径采样** 生成多条 **路径**。
*   对优秀的 **路径** 进行 **路径压缩**，优化 **Prompt** 或生成更高效的策略。
*   **反馈闭环** 利用 **执行轨迹** 中的结果或错误信息，调整 **AI 智能体** 的后续 **Prompt** 和决策。
*   **Prompt 蒸馏** 是实现 **路径压缩** 的一种方法。

---

### 业务骨架 (Business Skeleton)

业务骨架描述了实现这套范式所需的核心功能流程和高层操作步骤，关注“如何运作”的主要环节。

**核心业务流程：**

1.  **任务接收与解析:**
    *   接收用户输入的复杂任务。
    *   解析用户意图、识别任务的关键信息（如对象、目标、约束）。
2.  **初始规划与决策 (Prompt Routing 入口):**
    *   AI 智能体根据任务和当前上下文进行初步思考。
    *   决定下一步行动：是直接生成响应、还是需要调用工具、或是进行多步规划？
3.  **工具选择与调用 (如果需要工具):**
    *   **工具选择:** 根据任务需求和可用工具描述，选择最合适的工具。
    *   **工具行为 Prompt 生成:** 根据选定的工具，生成用于调用该工具的 Prompt（包含参数、格式要求等）。
    *   **工具执行:** 调用外部系统执行选定的工具。
    *   **结果接收与处理:** 接收工具返回的结果，进行解析和格式化。
4.  **执行追踪与日志记录:**
    *   记录整个执行过程中的每一步：AI 思考过程、决策、工具调用请求、工具返回结果、时间戳等。
    *   构建完整的执行轨迹 (Trace)。
5.  **中间结果处理与反馈:**
    *   AI 智能体整合工具结果和当前上下文，继续思考和规划。
    *   如果工具调用失败或结果异常，触发错误处理或反馈机制（如重试、换工具、调整 Prompt）。
    *   根据中间结果，决定是否需要进一步调用工具或进行其他操作。
6.  **迭代执行 (多步任务):**
    *   对于复杂任务，重复步骤 3-5，直到任务完成或达到预设条件。
    *   每次迭代都在前一步的结果基础上进行。
7.  **路径优化与策略学习 (离线/后台过程):**
    *   分析大量历史执行轨迹 (Trace) 数据。
    *   **路径采样:** 探索不同的执行路径，评估其效果（成功率、效率、成本）。
    *   **路径压缩:** 从成功的路径中提炼关键模式和高效逻辑。
    *   生成优化后的 Prompt 模板、工具使用策略或更紧凑的模型（通过 Prompt 蒸馏等）。
    *   将优化结果反馈到步骤 2 和 3，提高未来执行效率和成功率。
8.  **最终响应生成:**
    *   在任务完成后，AI 智能体根据最终整合的信息生成用户友好的最终响应。
9.  **安全与合规:**
    *   在整个流程中，确保工具调用和数据处理符合安全和合规要求。

---

### 软件架构 (Software Architecture)

软件架构描述了支撑这套范式所需的主要软件组件、它们的功能职责以及如何相互协作，关注“如何构建”的技术实现。

**核心组件：**

1.  **API Gateway/Request Handler:**
    *   负责接收外部用户请求。
    *   进行初步的请求验证和路由。
2.  **Task Management Service:**
    *   管理任务的整个生命周期。
    *   维护任务状态和上下文。
    *   协调各个子组件的执行顺序。
3.  **LLM Interaction Service:**
    *   封装与底层 LLM 的交互逻辑（Prompt 发送、结果接收）。
    *   可能负责 Prompt 的构建和管理（与 Prompt Template Repository 协作）。
4.  **Routing/Decision Engine:**
    *   实现 Prompt Routing 的核心逻辑。
    *   根据任务上下文和规则（可能是 LLM 内部逻辑或外部规则引擎）决定下一步执行哪个 Prompt 模块或调用哪个工具。
    *   调用 Tool Management Service 获取工具信息。
5.  **Tool Management Service:**
    *   维护可用工具的注册表（Tool Registry）。
    *   提供工具的元信息（名称、功能描述、输入输出规范等）。
6.  **Tool Execution Service:**
    *   负责调用实际的外部工具 API。
    *   处理工具调用的请求构建、参数传递、结果接收和初步解析。
    *   处理工具调用的同步/异步以及错误。
7.  **Trace & Logging Service:**
    *   收集并存储来自 Task Management Service, LLM Interaction Service, Tool Execution Service 的详细执行日志和轨迹数据。
    *   提供日志查询和回放功能。
8.  **Result Processing Module:**
    *   对 Tool Execution Service 返回的原始结果进行进一步处理、格式化、提取关键信息。
9.  **Feedback & Error Handling Module:**
    *   监控执行过程中的错误（如工具调用失败、LLM 输出异常）。
    *   实现重试、备选路径选择、向 Task Management Service 发送错误信号等逻辑。
10. **Optimization & Learning Service (Offline/Background):**
    *   分析 Trace & Logging Service 中的历史数据。
    *   实现路径采样算法，模拟和评估不同路径。
    *   实现路径压缩算法，识别模式并生成优化策略/Prompt。
    *   可能包含 Prompt 蒸馏模块，训练更小的模型或生成元 Prompt。
    *   将优化结果（如新的 Prompt 模板、路由规则）更新到 Prompt Template Repository 或 Routing/Decision Engine。
11. **Prompt Template Repository:**
    *   存储和管理各种可复用的 Prompt 模板（用于意图识别、工具选择、参数提取、结果格式化、工具行为定义等）。
    *   版本控制和管理 Prompt 的迭代。
12. **Security Module:**
    *   负责处理安全相关的逻辑，如输入过滤、防止 Prompt 注入、工具调用权限控制等。

**组件协作流程示例 (参考 Mermaid 图)：**

1.  用户请求到达 **API Gateway**，转发给 **Task Management Service**。
2.  **Task Management Service** 创建新任务，初始化上下文。
3.  **Task Management Service** 调用 **LLM Interaction Service** 和 **Routing/Decision Engine** 进行第一步决策。
4.  **Routing/Decision Engine** 可能根据 Prompt 决定调用工具，向 **Tool Management Service** 查询工具信息。
5.  **Routing/Decision Engine** 指示 **Tool Execution Service** 调用工具，并提供调用参数（可能由 **LLM Interaction Service** 生成）。
6.  **Tool Execution Service** 调用外部 API，并将结果返回给 **Result Processing Module**。
7.  **Result Processing Module** 处理结果后返回给 **Task Management Service** 或 **LLM Interaction Service**。
8.  所有执行步骤的详细信息发送给 **Trace & Logging Service** 进行记录。
9.  如果在执行过程中发生错误，**Feedback & Error Handling Module** 介入处理，并可能通知 **Task Management Service** 调整流程。
10. **Optimization & Learning Service** 后台分析 **Trace & Logging Service** 的数据，生成优化结果，更新 **Prompt Template Repository** 或 **Routing/Decision Engine** 的配置。
11. 任务完成后，**Task Management Service** 指示 **LLM Interaction Service** 生成最终响应，通过 **API Gateway** 返回给用户。