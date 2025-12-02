LangChain 提供了多种**内置的 Agent 类型（built-in agents）**，它们封装了常见的推理模式（如 ReAct、Plan-and-Execute、Self-Ask 等），并自动配对了对应的 **提示模板（Prompt）** 和 **输出解析器（OutputParser）**。你无需从零实现推理逻辑，只需提供 LLM 和工具（Tools）即可。

---

### 📦 LangChain 自带的主要 Agent 类型（截至 LangChain 0.2+）

> 注：部分旧版 `AgentType` 枚举已弃用，推荐使用 `create_*_agent` 工厂函数 + `hub` 提示。

#### ✅ 1. **ReAct 系列（最常用）**
基于 [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) 论文，结合推理（Thought）与行动（Action）。

| 名称 | 创建方式 | 特点 |
|------|--------|------|
| **Zero-shot ReAct** | `create_react_agent(llm, tools, prompt)` | 最经典，支持多工具调用，需模型理解 ReAct 格式 |
| **Structured ReAct** | `create_structured_chat_agent(...)` | 支持聊天历史，结构化输入（常用于对话场景） |

> 🔧 配套解析器：`ReActSingleInputOutputParser` 或 `ReActJsonOutputParser`（若用 JSON 模式）

📌 使用示例：
```python
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.llms import Ollama

llm = Ollama(model="qwen:7b")
tools = [/* your tools */]

# 拉取官方 ReAct 提示（含格式指令）
prompt = hub.pull("hwchase17/react")  # 或 "langchain/structured-chat-react"

agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

---

#### ✅ 2. **OpenAI Functions Agent（仅限支持 function calling 的模型）**
- 适用于 **OpenAI GPT-4-turbo / GPT-3.5-turbo**、**Anthropic Claude**、**Google Gemini** 等支持原生函数调用的模型。
- 不依赖 ReAct 文本格式，而是通过 **JSON Schema** 声明工具，由模型直接返回结构化函数调用。

```python
from langchain.agents import create_openai_functions_agent

prompt = hub.pull("hwchase17/openai-functions-agent")
agent = create_openai_functions_agent(llm, tools, prompt)
```

> ⚠️ **不适用于普通本地模型（如 Llama、Qwen base）**，除非你用 vLLM/Ollama 启用了 function calling 仿真。

---

#### ✅ 3. **Plan-and-Execute Agent**
- 先让一个 “Planner” 制定多步计划，再由 “Executor” 逐步执行。
- 适合复杂任务，但速度慢、成本高。

```python
from langchain.agents import create_plan_and_execute_agent
```

---

#### ✅ 4. **Self-Ask with Search**
- 仅支持单个 `Intermediate Answer` 工具（通常是搜索）。
- 模型通过自问自答分解问题（如 “What is X? → First, find Y…”）。
- 现在较少使用，已被 ReAct 取代。

---

#### ✅ 5. **Tool Calling Agents（新版推荐）**
LangChain 0.2+ 推出了更统一的 **tool calling interface**，支持：
- 自动根据工具生成工具描述
- 兼容 OpenAI、Anthropic、Mistral、Groq 等原生 tool calling
- 对于不支持的模型（如 Llama），可 fallback 到 ReAct

```python
from langchain_core.messages import HumanMessage
from langchain.tools.render import render_text_description
from langchain.agents import AgentExecutor, create_tool_calling_agent

# 自动适配模型能力
agent = create_tool_calling_agent(llm, tools, prompt)
```

---

### 🆚 内置 Agent 对比表

| Agent 类型 | 是否需要 ReAct 格式 | 适用模型 | 多轮工具调用 | 备注 |
|-----------|------------------|--------|------------|------|
| `react` | ✅ 是 | 任何文本模型（Qwen, Llama, GPT等） | ✅ | 最通用 |
| `openai-functions` | ❌ 否（用 JSON） | OpenAI / Claude / Gemini | ✅ | 高效准确 |
| `structured-chat-react` | ✅ 是（带聊天历史） | 任何 | ✅ | 适合对话 |
| `plan-and-execute` | ✅ 是 | 任何 | ✅✅ | 复杂任务 |
| `tool_calling_agent` | ⚠️ 自动适配 | 支持 function calling 的优先用 JSON，否则回退 ReAct | ✅ | **推荐新项目使用** |

---

### ❓常见问题

#### Q1: 我用 Qwen/Llama，能用 `openai-functions-agent` 吗？
**不能直接用**。除非：
- 你用的是 **Qwen-Max / Qwen-Plus**（阿里云 API 支持 function calling）
- 或你用 **Ollama + function-calling 适配层**（实验性）
否则请用 `react` 或 `tool_calling_agent`（它会自动降级到 ReAct）

#### Q2: 能不用任何内置 Agent 吗？
可以！你可以：
- 直接调用 `llm.invoke(prompt)` + 自定义解析
- 实现自己的 `AgentExecutor` 循环
但会失去 LangChain 的 retry、memory、streaming 等能力。

#### Q3: 如何查看某个 Agent 的提示模板？
```python
prompt = hub.pull("hwchase17/react")
print(prompt.pretty_repr())  # 或 print(prompt.messages)
```
你会看到类似：
```
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
```

---

### ✅ 建议

- **如果你用本地模型（Qwen、Llama 等）** → 用 `create_react_agent` 或 `create_tool_calling_agent`
- **如果你用 OpenAI/Claude/Gemini** → 优先用 `create_openai_functions_agent` 或 `create_tool_calling_agent`
- **遇到解析错误** → 继承 `AgentOutputParser` 写 `CustomOutputParser`（如你之前做的）

---

需要我帮你根据你的具体模型（比如 Qwen2-7B-Instruct）和工具，生成一个完整的可运行 Agent 示例吗？