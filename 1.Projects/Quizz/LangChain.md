---
view-count: 10
---
# LangChain：组件化 AI 架构极简协议

## 核心范式
- **本质**：语言模型应用的组件化框架 (Building blocks for LLMs)。
- **逻辑流**：Prompt + LLM + OutputParser $\rightarrow$ Chain $\rightarrow$ Agent。

## 架构矩阵 (Components)
| 模块 | 核心类/接口 | 极简职能 |
| :--- | :--- | :--- |
| **Model** | `ChatOpenAI` / `LLM` | 逻辑执行核心。 |
| **Prompt** | `PromptTemplate` | 输入格式化与变量注入。 |
| **Parser** | `OutputParser` | 文本 $\rightarrow$ 结构化数据 (JSON/Pydantic)。 |
| **Memory** | `ConversationBufferMemory` | 对话上下文状态持久化。 |
| **Tool** | `name` + `description` + `run()` | LLM 可调用的外部函数/API。 |

## 数据增强 (RAG) 流程
- **Load**: `DocumentLoader` (读取 PDF/Web/Wiki)。
- **Storage**: `Vectorstores` (向量数据库集成)。
- **Search**: `Retriever` (相似度搜索逻辑)。
- **Chain**: `ConversationalRetrievalChain` (带记忆的检索问答)。

## 执行逻辑：Chain vs Agent
- **Chain (预定义)**：
    - `SimpleSequentialChain`：线性 A $\rightarrow$ B。
    - `RouterChain`：条件分支导航。
    - `MapReduceChain`：大规模文档摘要/聚合。
- **Agent (动态推理)**：
    - **核心循环**：ReAct 框架 (Reason + Act)。
    - **控制器**：`AgentExecutor`。
    - **决策流**：`AgentOutputParser` $\rightarrow$ `AgentAction` (调工具) 或 `AgentFinish` (给结果)。

## 生产级特性
- **LCEL (Runnable)**：统一接口，原生支持 `Async` (异步), `Batch` (批处理), `Streaming` (流式)。
- **Callbacks**：`CallbackHandler` 追踪中间过程 (on_tool_start, on_chain_end)。
- **Evaluation**：`langchain.evaluation` 自动化评估输出质量。

---
**关联笔记**
- [[个人知识管理系统]]
- [[2025-12-14-经典软件测试方法]]