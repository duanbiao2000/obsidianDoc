
## AI时代工程师转型：价值重塑与心智进化路线图

技术浪潮的涌动，不仅带来工具的更迭，更是对工程师**价值聚焦点与心智模型**的深刻挑战。在AI，特别是大模型（LLM）能力日益强大的今天，传统“工程师”角色正经历一场静默而深远的演化。那些曾被视为核心壁垒的底层实现细节、语法记忆、模板化代码，正被自动化工具以几何级数提升的效率接管。这并非工程师的末日，而是价值流向上游迁徙的清晰信号：AI正在系统性地降低“执行”的门槛，从而指数级地提升了对“设计”、“策略”、“整合”和“判断”等更高层级认知能力的需求。

这好比我们大脑的演化：底层反射和自动化处理（System 1 Thinking）负责快速、无需努力的任务，而更高层的执行功能（Executive Functions）和理性分析（System 2 Thinking）则用于规划、决策、解决新问题和处理抽象概念。AI的强大，正在外部环境中构建一个效率极高的“System 1”，替我们承担大量重复性和模式化的“计算”，从而解放我们的“System 2”，去处理那些更具创造性和战略性的任务。

因此，AI时代的优秀开发者，其核心价值不再是你记住多少API，而是你能够调用和整合多少外部“认知资源”（包括AI工具本身）去解决一个复杂问题。这要求我们刻意训练一系列新的**元技能（Meta-skills）**。

---

### **AI时代工程师转型Golden元素与实践路径**

以下Five Golden Elements代表着从“执行型”向“策略型”工程师的转型，强调的是对复杂系统设计、AI协作编排与高级认知策略的掌握。它们不仅是技术技能提升，更是心智模式的重塑，以应对AI带来的价值位移和环境变化。

---

#### 1. 抽象建模能力：将混沌塑造成结构

*   **论点支撑：** AI擅长在既定结构内填充细节和执行指令，但**结构的定义、问题的框架需要人类来完成**。这是一种将模糊的现实需求剥离表象、提炼出核心逻辑与关系、并转化为程序可执行的**结构化指令（如 JSON-Schema, Task Graph）** 的认知能力。它本质上是**信息转译**，连接人类意图与AI可理解的计算范式。
*   **心智训练：** 提升我们大脑对复杂信息进行“块化”（Chunking）和“模式识别”后，再进一步进行“结构化”（Structuring）和“形式化”（Formalization）的能力。多进行将复杂文本压缩提炼为思维导图或结构化数据的练习。

##### 工作流实践：需求-Schema-代码生成循环

此工作流展示如何将一个复杂的自然语言需求，通过抽象建模转化为AI可消费的结构化契约，进而驱动代码生成。这体现了工程师从“写代码”到“定义规约”的角色转变。

1.  **需求分析与实体/关系识别**：
    *   **任务**：阅读用户故事，识别核心实体（对象）、属性及其相互关系、操作。
    *   **工具**：Obsidian ([[需求文档]])、XMind/Whimsical (思维导图)。
    *   **产出**：初步的概念模型图、关键术语表。

2.  **结构化数据模型定义**：
    *   **任务**：将概念模型转化为规范的JSON Schema或Pydantic模型。这定义了AI在后续步骤中应处理的数据结构。
    *   **工具**：Python (Pydantic)、JSON Schema生成器。
    *   **产出**：`request.py` (Pydantic模型定义), `response.json` (期望的JSON Schema)。

3.  **AI驱动的契约校验与辅助代码生成**：
    *   **任务**：编写Prompt，指示LLM根据定义的Schema生成API接口代码，并校验其输出是否符合Schema。
    *   **工具**：OpenAI API, `PydanticOutputParser` (LangChain), `json` 模块。
    *   **产出**：符合Schema的API接口代码片段，体现了“结构化指令驱动代码生成”的能力。

```python
# request.py (Pydantic模型定义)
from pydantic import BaseModel, Field
from typing import List, Optional
import json

class User(BaseModel):
    id: str = Field(..., description="Unique user identifier")
    name: str = Field(..., description="User's full name")
    email: str = Field(..., description="User's email address")

class Task(BaseModel):
    id: str = Field(..., description="Unique task identifier")
    title: str = Field(..., description="Title of the task")
    description: Optional[str] = Field(None, description="Detailed description of the task")
    status: str = Field(..., description="Current status of the task (e.g., 'pending', 'in_progress', 'completed')")
    assignee_id: Optional[str] = Field(None, description="ID of the user assigned to this task")

class TaskListRequest(BaseModel):
    user_id: str = Field(..., description="The ID of the user requesting tasks")
    filter_status: Optional[str] = Field(None, description="Filter tasks by status")
    limit: int = Field(10, description="Maximum number of tasks to return")

# 假设这个函数代表LLM的某种生成行为，它会尝试生成符合TaskListRequest模式的代码
def generate_api_code_from_schema(schema_json_str: str) -> str:
    """
    模拟LLM根据给定的JSON Schema生成API接口代码。
    在实际中，这是一个调用LLM并传入Schema作为Prompt一部分的过程。
    """
    # 真实场景中，这里会调用LLM，例如：
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system", "content": f"Generate a Python FastAPI endpoint for a request matching this JSON Schema:\n{schema_json_str}"},
    #         {"role": "user", "content": "Generate the GET /tasks endpoint code."}
    #     ]
    # )
    # return response['choices'][0]['message']['content']

    # 简化示例：直接返回一个符合预期的代码片段，表示成功抽象和生成
    return f"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class TaskListRequest(BaseModel):
    user_id: str
    filter_status: Optional[str] = None
    limit: int = 10

@app.get("/tasks")
async def get_tasks(request: TaskListRequest):
    \"\"\"
    Retrieves tasks based on user ID and optional status filter.
    Input schema: {schema_json_str}
    \"\"\"
    # Placeholder for actual task retrieval logic
    print(f"Received request for user {request.user_id} with filter {request.filter_status}")
    return {{"message": "Tasks retrieved successfully", "request_data": request.dict()}}
"""

if __name__ == "__main__":
    # 1. 将Pydantic模型转换为JSON Schema
    task_list_request_schema = json.dumps(TaskListRequest.model_json_schema(), indent=2)
    print("--- 生成的 JSON Schema ---")
    print(task_list_request_schema)

    # 2. 模拟AI根据Schema生成代码
    generated_code = generate_api_code_from_schema(task_list_request_schema)
    print("\n--- AI生成的API代码 (基于Schema) ---")
    print(generated_code)

    # 3. 可以在这里进一步执行生成的代码并测试其是否符合Schema
    # (例如，通过动态加载模块或使用pytest进行测试，此处省略具体执行逻辑)
```


---

#### 2. 提示词工程深耕：与智能系统高效沟通的艺术

*   **论点支撑：** Prompt是我们与AI这一新型智能系统交互的接口。它要求我们不仅会用自然语言，还要掌握将意图精准“编译”为AI能理解和响应的**“语义指令”**。这类似于学习如何向一位极度聪明但缺乏常识或上下文的“外星人”下达指令，需要精确选择词汇、设定角色风格、提供示例、拆解步骤。
*   **心智训练：** 训练Prompt Behavior Graph，构建一套系统性、可预测地影响AI行为的“指令语法”和“心智模型图谱”。强调对AI输出的**“可控性”**而非仅仅“生成”。

##### 工作流实践：高可靠性Prompt设计与测试

此工作流展示如何构建一个能够稳定输出特定格式数据的Prompt，并通过Pydantic进行输出校验和错误处理，从而提升与LLM交互的可靠性。

1.  **定义期望输出结构**：
    *   **任务**：使用Pydantic定义LLM响应的精确结构，包含字段、类型和描述。
    *   **工具**：Python (Pydantic)。
    *   **产出**：`article_summary_schema.py`。

2.  **构建结构化Prompt**：
    *   **任务**：结合Output Parser生成Prompt指令，要求LLM严格按照Schema输出。包含角色、任务描述、上下文和示例（如果需要）。
    *   **工具**：LangChain `PydanticOutputParser`。
    *   **产出**：可执行Prompt字符串。

3.  **LLM调用与输出校验**：
    *   **任务**：调用LLM，并尝试解析其输出。如果输出不符合Schema，进行错误捕获并可能触发重试机制。
    *   **工具**：OpenAI API, `try-except` 语句。
    *   **产出**：经校验的结构化数据，或错误报告。

```python
# article_summary_schema.py
from pydantic import BaseModel, Field
from typing import List, Optional

class ArticleSummary(BaseModel):
    title: str = Field(..., description="The concise title of the article.")
    main_points: List[str] = Field(..., description="A list of 3-5 main points from the article.")
    sentiment: str = Field(..., description="Overall sentiment of the article (positive, neutral, negative).")
    keywords: List[str] = Field(..., description="Important keywords from the article.")

# main.py
import openai
import json
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from article_summary_schema import ArticleSummary # 导入自定义的Pydantic模型

def summarize_article_with_schema_control(article_text: str) -> Optional[ArticleSummary]:
    parser = PydanticOutputParser(pydantic_object=ArticleSummary)

    prompt_template = PromptTemplate(
        template="""You are an expert summarizer. Summarize the following article strictly following the JSON format.
{format_instructions}

Article to summarize:
{article}""",
        input_variables=["article"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    formatted_prompt = prompt_template.format(article=article_text)

    # 模拟LLM调用，实际中会是openai.ChatCompletion.create
    print("--- 发送给LLM的Prompt示例 ---")
    print(formatted_prompt)
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": formatted_prompt}
            ],
            temperature=0 # 尽量减少随机性，争取结构化输出
        )
        llm_output = response['choices'][0]['message']['content']
        print("\n--- LLM原始输出 ---")
        print(llm_output)

        # 尝试解析输出
        parsed_output = parser.parse(llm_output)
        print("\n--- 经过Pydantic解析后的结构化输出 ---")
        print(parsed_output.dict())
        return parsed_output

    except Exception as e:
        print(f"\n--- 错误: LLM输出不符合Schema或解析失败 ---")
        print(f"错误信息: {e}")
        # 在实际系统中，这里可以触发重试、人工介入或降级处理
        return None

if __name__ == "__main__":
    sample_article = """
    In a recent breakthrough, researchers at XYZ Labs have announced a new AI model capable of generating highly realistic and coherent long-form text. This model, named "Genesis," leverages a novel transformer architecture combined with a new training methodology involving adversarial networks. Early tests show Genesis surpassing previous benchmarks in creativity and factual consistency across various domains, including news reporting, creative writing, and technical documentation. While impressive, the team acknowledges the ethical implications and potential for misuse, emphasizing the need for robust safeguards and responsible deployment strategies.
    """
    
    summary = summarize_article_with_schema_control(sample_article)
    if summary:
        print("\n成功获取并解析文章摘要。")
    else:
        print("\n未能获取符合预期的文章摘要。")
```

---

#### 3. 增强智能系统构建：设计人机协作的流水线

*   **论点支撑：** 未来的AI应用是将LLM作为核心组件，与各种工具（Tool）、API、数据库、人类反馈环节有机整合而成的复杂系统。工程师的角色从编写单一模块，转变为设计和编排一个由AI和其他工具协同工作的**“智能代理”（Agent）**或“任务流水线”。这是一种将认知任务“外包”和“分布式处理”的思维。
*   **心智训练：** 学习如何管理一个项目团队，理解每个成员（AI、工具、人）的能力边界，并设计协作机制。对Planner、Executor、Memory、Tool-Invocation机制的理解是构建这种分布式认知系统所需的架构思维。

##### 工作流实践：多代理协作的RAG系统（决策与执行）

此工作流展示一个简化的检索增强生成（RAG）系统，其中包含一个决策（Planner）节点和多个工具（Executor）节点，体现了AI的“选择”能力。

1.  **定义工具集**：
    *   **任务**：封装外部API或函数为AI可调用的工具（如搜索工具、本地知识库检索工具）。
    *   **工具**：LangChain `Tool`。
    *   **产出**：可供代理使用的工具对象列表。

2.  **构建决策代理（Planner Agent）**：
    *   **任务**：设计一个LLM代理，根据用户查询和可用工具，决定采取何种行动（如直接回答、调用搜索工具、调用知识库）。
    *   **工具**：OpenAI Function Calling LLM, LangChain `AgentExecutor`。
    *   **产出**：能够输出行动计划的代理。

3.  **编排执行流（Executor Workflow）**：
    *   **任务**：使用LangGraph构建状态图，将Planner代理、各种工具调用以及结果汇总连接起来，实现条件跳转和状态传递。
    *   **工具**：LangGraph `StateGraph`。
    *   **产出**：可执行的、具备智能决策能力的RAG工作流。

```python
# main_rag_workflow.py
import openai
from langchain.agents import AgentExecutor, Tool, create_openai_functions_agent
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List, Dict
import operator

# 1. 定义工具集
def internet_search_tool(query: str) -> str:
    """模拟互联网搜索，返回搜索结果摘要。"""
    print(f"\n--- 执行互联网搜索: {query} ---")
    if "最新AI模型" in query:
        return "最新AI模型是'Genesis'，由XYZ Labs发布，擅长生成长文本。"
    return "未找到相关互联网搜索结果。"

def local_knowledge_base_tool(query: str) -> str:
    """模拟本地知识库检索，返回相关文档片段。"""
    print(f"\n--- 执行本地知识库检索: {query} ---")
    if "XYZ Labs" in query:
        return "XYZ Labs是专注于AI研究的机构，其模型Genesis在文本生成方面表现出色。"
    return "本地知识库中未找到相关信息。"

tools = [
    Tool(name="InternetSearch", func=internet_search_tool, description="用于搜索互联网上的最新信息"),
    Tool(name="LocalKnowledgeBase", func=local_knowledge_base_tool, description="用于检索公司内部或本地知识库中的信息"),
]

# 2. 构建决策代理 (Planner Agent)
# 定义Agent的状态
class AgentState(TypedDict):
    chat_history: Annotated[List[str], operator.add]
    query: str
    intermediate_steps: Annotated[List[tuple], operator.add]

llm = ChatOpenAI(model="gpt-4-0125-preview", temperature=0) # 确保LLM支持Function Calling

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的助手，可以回答问题和使用工具。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{query}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# 创建OpenAI Function Calling Agent
agent_runnable = create_openai_functions_agent(llm, tools, prompt)

# Agent的执行器
agent_executor = AgentExecutor(agent=agent_runnable, tools=tools, verbose=True)

# 3. 编排执行流 (Executor Workflow) - 使用LangGraph
def run_agent(state: AgentState):
    """LangGraph节点：运行Agent Executor"""
    print(f"\n--- 节点: 运行Agent ---")
    agent_output = agent_executor.invoke({"query": state["query"], "chat_history": state["chat_history"]})
    return {"intermediate_steps": agent_output["intermediate_steps"], "chat_history": state["chat_history"] + [f"Agent response: {agent_output['output']}"]}

def decide_next_action(state: AgentState) -> str:
    """LangGraph节点：根据Agent的中间步骤决定下一步"""
    print(f"\n--- 节点: 决策下一步行动 ---")
    if not state["intermediate_steps"]:
        # 如果Agent没有执行任何工具，说明它直接给出了答案
        return "end"
    # 如果Agent执行了工具，并且还有后续步骤，则继续
    # 在实际复杂场景中，这里会有更复杂的逻辑来判断是否继续Agent循环或结束
    return "run_agent" # 模拟Agent可能需要多轮思考或工具调用

# 构建LangGraph图
workflow = StateGraph(AgentState)

workflow.add_node("run_agent", run_agent)
workflow.add_edge("run_agent", END) # 简化：Agent执行完直接结束

# # 更复杂的Agentic Loop示例 (如果需要多轮思考/工具调用)
# workflow.add_node("run_agent", run_agent)
# workflow.add_node("decide_next_action", decide_next_action)
# workflow.set_entry_point("run_agent")
# workflow.add_edge("run_agent", "decide_next_action")
# workflow.add_conditional_edges(
#     "decide_next_action",
#     decide_next_action,
#     {"run_agent": "run_agent", "end": END}
# )

app = workflow.compile()

if __name__ == "__main__":
    print("\n--- 启动RAG Agent Workflow ---")
    
    initial_state = {"chat_history": [], "query": "XYZ Labs最近发布了什么？"}
    final_state = app.invoke(initial_state)
    print("\n--- 第一次查询结果 ---")
    print(final_state)

    print("\n\n--- 再次查询 ---")
    initial_state = {"chat_history": [], "query": "AI的历史有哪些重要里程碑？"}
    final_state = app.invoke(initial_state)
    print("\n--- 第二次查询结果 ---")
    print(final_state)
```

---

#### 4. 思维链优化：优化智能系统的决策过程

*   **论点支撑：** 对于复杂的推理或执行任务，AI也需要一个“思考过程”。设计Prompt Tree或Prompt Trace，是在为AI构建一个**“模块化的思维路径”**，将大问题分解为逻辑上相互关联的子问题，并引导AI一步步解决。通过结构性Prompt或Control Tokens压缩路径深度，则是在追求效率，类似于人类经过训练后，能将复杂推理过程内化、自动化。
*   **心智训练：** 提升我们将复杂的思维过程转化为AI可执行的、高效的计算流程的能力。学习人类解决复杂问题时使用的递归思维、分解策略、决策树等高级认知策略。

##### 工作流实践：自反思与迭代优化的推理链

此工作流展示如何构建一个包含“规划-执行-反思”循环的Agentic推理链，引导LLM进行更深层次、更健壮的复杂问题解决。

1.  **定义思考阶段Prompt**：
    *   **任务**：为AI的“思考”（Planner）、“执行”（Executor）、“反思”（Reflector）等阶段设计特定Prompt。
    *   **工具**：LangChain `PromptTemplate`。
    *   **产出**：多阶段Prompt模板。

2.  **构建Agentic循环**：
    *   **任务**：使用LangGraph构建一个循环，LLM首先提出计划，然后尝试执行，再根据结果进行反思和调整。
    *   **工具**：LangGraph `StateGraph`, `add_conditional_edges`。
    *   **产出**：具备自纠错和迭代优化能力的推理工作流。

```python
# main_self_reflect_agent.py
import openai
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
import operator

# 定义Agent的状态
class SelfReflectState(TypedDict):
    question: str
    plan: str
    steps_executed: Annotated[List[str], operator.add]
    intermediate_thoughts: Annotated[List[str], operator.add]
    final_answer: str
    reflection: str
    iteration: int

llm = ChatOpenAI(model="gpt-4-0125-preview", temperature=0.2)

# 1. 定义思考阶段Prompt
# Planner Prompt: 规划如何解决问题
planner_prompt = ChatPromptTemplate.from_messages([
    ("system", """你是一个严谨的规划者。根据用户的问题，制定一个详细的、分步骤的解决方案。
     每一步都清晰明确，包括需要获取的信息、需要执行的计算或逻辑。
     请以JSON格式输出你的计划：
     {{
        "plan": [
            {{"step": 1, "description": "...", "action_type": "search/calculate/reason"}},
            // ...
        ]
     }}
     """),
    ("user", "{question}")
])
planner_chain = planner_prompt | llm | (lambda x: {"plan": x.content}) # 简化解析

# Executor Prompt: 执行计划中的某一步骤
executor_prompt = ChatPromptTemplate.from_messages([
    ("system", """你是一个执行者。根据给定的计划步骤和目前已知的上下文，执行当前步骤并给出结果。
     如果需要进行计算，请给出详细的计算过程。
     如果需要搜索信息，请明确你正在搜索什么。
     当前已执行步骤: {steps_executed}
     目前上下文: {intermediate_thoughts}
     """),
    ("user", "执行以下步骤：{current_step_description}\n用户问题：{question}")
])
executor_chain = executor_prompt | llm | (lambda x: {"result": x.content}) # 简化解析

# Reflector Prompt: 反思执行结果并判断是否完成或需要修正
reflector_prompt = ChatPromptTemplate.from_messages([
    ("system", """你是一个反思者。根据原始问题、当前的计划、已执行的步骤和结果，判断问题是否已解决。
     如果已解决，请给出最终答案。
     如果没有，请指出当前存在的问题，并建议下一步行动或修正计划。
     请以JSON格式输出你的反思：
     {{
        "solved": true/false,
        "final_answer": "...", // 如果已解决
        "next_action": "...", // 如果未解决
        "problem_identified": "...", // 如果未解决
        "suggested_plan_correction": "..." // 可选，如果需要修正计划
     }}
     """),
    ("user", "原始问题: {question}\n当前计划: {plan}\n已执行步骤: {steps_executed}\n最新执行结果: {latest_result}")
])
reflector_chain = reflector_prompt | llm | (lambda x: x.content) # 返回原始JSON字符串，待后续解析

# LangGraph Nodes
def call_planner(state: SelfReflectState):
    print(f"\n--- 节点: 规划 (Iteration {state['iteration']}) ---")
    plan_output = planner_chain.invoke({"question": state["question"]})
    print(f"规划结果: {plan_output['plan']}")
    return {"plan": plan_output['plan'], "iteration": state["iteration"] + 1}

def call_executor(state: SelfReflectState):
    print(f"\n--- 节点: 执行步骤 (Iteration {state['iteration']}) ---")
    current_plan = json.loads(state["plan"]) # 假设plan是JSON字符串
    # 简化：只执行计划的第一步
    if not current_plan.get("plan"):
        print("无更多计划可执行。")
        return {"intermediate_thoughts": state["intermediate_thoughts"] + ["无更多计划可执行。"]}
    
    current_step_desc = current_plan["plan"][0]["description"]
    
    # 模拟执行
    if "计算" in current_step_desc:
        result = f"模拟计算结果 for '{current_step_desc}'"
    elif "搜索" in current_step_desc:
        result = f"模拟搜索结果 for '{current_step_desc}'"
    else:
        result = f"模拟执行结果 for '{current_step_desc}'"
    
    print(f"执行步骤 '{current_step_desc}', 结果: {result}")
    return {
        "steps_executed": state["steps_executed"] + [current_step_desc],
        "intermediate_thoughts": state["intermediate_thoughts"] + [result]
    }

def call_reflector(state: SelfReflectState):
    print(f"\n--- 节点: 反思 (Iteration {state['iteration']}) ---")
    latest_result = state["intermediate_thoughts"][-1] if state["intermediate_thoughts"] else ""
    reflection_output = reflector_chain.invoke({
        "question": state["question"],
        "plan": state["plan"],
        "steps_executed": state["steps_executed"],
        "latest_result": latest_result
    })
    
    # 解析反思结果
    try:
        reflection_data = json.loads(reflection_output)
    except json.JSONDecodeError:
        print(f"反思输出非JSON格式: {reflection_output}")
        reflection_data = {"solved": False, "next_action": "继续执行", "problem_identified": "反思器输出格式错误"}
    
    print(f"反思结果: {reflection_data}")
    return {"reflection": reflection_output, "final_answer": reflection_data.get("final_answer"), "solved_flag": reflection_data.get("solved", False)}

def decide_flow(state: SelfReflectState) -> str:
    print(f"\n--- 节点: 决定流程方向 (Iteration {state['iteration']}) ---")
    if state.get("solved_flag"):
        print("问题已解决，流程结束。")
        return "end"
    
    # 简化：如果未解决且迭代次数未超限，继续执行或重新规划
    if state["iteration"] < 3: # 最多迭代3次
        print("问题未解决，继续执行或重新规划。")
        # 实际中会根据反射器的next_action来决定是执行还是重新规划
        return "executor" # 简单回到执行阶段
    else:
        print("达到最大迭代次数，流程结束。")
        return "end"


# 构建LangGraph图
workflow = StateGraph(SelfReflectState)

workflow.add_node("planner", call_planner)
workflow.add_node("executor", call_executor)
workflow.add_node("reflector", call_reflector)

workflow.set_entry_point("planner") # 从规划开始

# 规划 -> 执行
workflow.add_edge("planner", "executor")
# 执行 -> 反思
workflow.add_edge("executor", "reflector")
# 反思 -> 决定下一步（是否结束或继续循环）
workflow.add_conditional_edges(
    "reflector",
    decide_flow,
    {
        "executor": "executor", # 继续执行下一轮
        "end": END # 结束流程
    }
)

app = workflow.compile()

if __name__ == "__main__":
    question = "请计算2023年全球AI芯片市场规模，并分析其主要驱动因素。"
    print(f"\n--- 启动自反思Agent工作流，问题: {question} ---")
    
    initial_state = {
        "question": question,
        "plan": "",
        "steps_executed": [],
        "intermediate_thoughts": [],
        "final_answer": "",
        "reflection": "",
        "iteration": 0,
        "solved_flag": False
    }

    final_state = app.invoke(initial_state)
    print("\n--- 最终工作流状态 ---")
    print(final_state)
```

---

#### 5. 数据思维迭代：构建AI的“语义心智”

*   **论点支撑：** AI时代，“数据为王”更重要的是如何构建结构化、分层化、可迁移的**“语义知识组件”**，为AI提供高质量的“认知养料”。这包括如何有效地将非结构化数据转化为AI可用的知识表示（如 embedding memory），如何对知识进行检索和排序（vector rerank），以及如何将复杂知识提炼为简洁形式（知识 distillation）。
*   **心智训练：** 为AI建立一个高效的**“内部知识网络”或“语义地图”**，让它能够进行更精准、更有效的推理和生成。这类似于教育一个学生，提供结构化的教材、提炼的重点，并教他如何查找和关联知识。

##### 工作流实践：基于RAG的知识精炼与检索优化

此工作流展示一个更高级的RAG流程，它不仅检索，还涉及知识的精炼和检索结果的重排，以提供更准确、更相关的AI回答。

1.  **数据摄取与预处理**：
    *   **任务**：加载非结构化文档，进行清洗、分块。
    *   **工具**：`SimpleDirectoryReader`, `RecursiveCharacterTextSplitter` (LangChain)。
    *   **产出**：结构化文本块列表。

2.  **构建向量存储与索引**：
    *   **任务**：将文本块转化为向量嵌入，存储到向量数据库中。
    *   **工具**：`OpenAIEmbeddings`, `Chroma`/`Weaviate`/`Pinecone`。
    *   **产出**：可检索的向量索引。

3.  **检索与重排（Reranking）**：
    *   **任务**：根据用户查询，从向量数据库中初步检索相关文档，然后使用交叉编码器（Cross-Encoder）进行二次重排，提升相关性。
    *   **工具**：`VectorStoreRetriever`, `BgeRerank` (Langchain)。
    *   **产出**：高质量、高相关性的检索结果。

4.  **知识蒸馏（可选，高级）**：
    *   **任务**：利用LLM对检索到的多个文档片段进行概括和精炼，提取核心要点，形成更简洁的知识表示。
    *   **工具**：LLM (`MapReduceDocumentsChain`)。
    *   **产出**：精炼后的知识片段，用于喂给回答LLM。

5.  **答案生成**：
    *   **任务**：将优化后的检索结果与用户查询结合，通过LLM生成最终答案。
    *   **工具**：LLM。
    *   **产出**：基于知识的准确回答。

```python
# main_rag_optimization.py
import openai
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from langchain.retrievers.document_compressors import BgeRerank # 需要安装`sentence-transformers`
from langchain.retrievers import ContextualCompressionRetriever
import os

# 模拟一个本地知识库文件
knowledge_base_path = "data/knowledge_base.txt"
os.makedirs(os.path.dirname(knowledge_base_path), exist_ok=True)
with open(knowledge_base_path, "w", encoding="utf-8") as f:
    f.write("""
    ### 2023年AI芯片市场报告
    2023年全球AI芯片市场规模达到约500亿美元，预计到2030年将突破2000亿美元。
    主要驱动因素包括：
    1. 生成式AI的爆发式增长：OpenAI的ChatGPT等模型推动了对高性能AI推理和训练芯片的需求。
    2. 边缘AI的兴起：智能设备、物联网传感器和自动驾驶汽车对低功耗、高效率边缘AI芯片的需求增加。
    3. 云计算巨头投入：Google、Amazon、Microsoft等持续投资定制AI加速器以优化其云服务。
    4. 5G和数据中心升级：需要更强大的AI芯片来处理海量数据。
    
    ### 公司简介：XYZ Labs
    XYZ Labs是一家领先的AI研究机构，最近发布了名为“Genesis”的革命性文本生成模型。该模型采用了创新的Transformer架构和对抗网络训练方法，在创意写作和事实一致性方面设立了新标杆。
    """)

# 1. 数据摄取与预处理
loader = TextLoader(knowledge_base_path, encoding="utf-8")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
print(f"原始文档分块数量: {len(splits)}")

# 2. 构建向量存储与索引
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
vector_retriever = vectorstore.as_retriever(search_kwargs={"k": 5}) # 初始检索5个最相关块

# 结合BM25（关键词检索）和VectorStore（语义检索）
keyword_retriever = BM25Retriever.from_documents(splits)
keyword_retriever.k = 5

ensemble_retriever = EnsembleRetriever(
    retrievers=[vector_retriever, keyword_retriever], weights=[0.5, 0.5]
)

# 3. 检索与重排 (Reranking)
# 使用BGE Rerank模型进行二次重排，提升相关性
compressor = BgeRerank(top_n=3, model="BAAI/bge-reranker-base") # 选3个最相关的
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=ensemble_retriever
)
print("--- 完成向量存储和重排器配置 ---")

# 4. 答案生成链
llm = ChatOpenAI(model="gpt-4-0125-preview", temperature=0)

# 定义历史感知检索器
history_aware_retriever = create_history_aware_retriever(
    llm, compression_retriever, ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
        ("user", "根据上述对话历史，生成一个能够从知识库中检索信息的搜索查询，以便回答用户问题。"),
    ])
)

# 定义文档组合链
document_chain = create_stuff_documents_chain(
    llm, ChatPromptTemplate.from_messages([
        ("system", "你是一个专业的AI市场分析师。根据以下检索到的上下文信息，简洁准确地回答用户问题。\n\n{context}"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
    ])
)

# 结合检索器和文档组合链
retrieval_chain = create_retrieval_chain(history_aware_retriever, document_chain)

if __name__ == "__main__":
    chat_history = []
    
    # 第一次查询：RAG流程将利用重排后的知识回答
    query1 = "2023年AI芯片市场规模是多少？驱动因素有哪些？"
    print(f"\n--- 查询 1: {query1} ---")
    response1 = retrieval_chain.invoke({"input": query1, "chat_history": chat_history})
    print("\n--- 回答 1 ---")
    print(response1["answer"])
    chat_history.extend([("user", query1), ("assistant", response1["answer"])])

    # 第二次查询：体现历史感知和结合上下文检索
    query2 = "XYZ Labs是什么？它有什么新的模型？"
    print(f"\n\n--- 查询 2: {query2} ---")
    response2 = retrieval_chain.invoke({"input": query2, "chat_history": chat_history})
    print("\n--- 回答 2 ---")
    print(response2["answer"])
```

---

### **核心价值：迈向具备适应性和智能的行为**

这些实践工作流不仅仅是技术指南，更是**心智模型转型**的体现。它们指导工程师：

*   **从“写代码”到“定义规约”**：将复杂需求转化为AI可理解和执行的结构化契约。
*   **从“硬编码”到“软编程”**：通过Prompt和代理编排，让AI的行为更具柔性和可配置性。
*   **从“固定流程”到“自适应系统”**：构建能根据上下文和反馈动态调整行为的智能工作流。
*   **从“数据堆砌”到“知识精炼”**：重视高质量的语义知识构建，提升AI的“理解力”和“推理精度”。

AI的浪潮不可阻挡。它正在以前所未有的方式重塑我们所知的世界，包括“工程师”这个职业。与其抗拒或仅仅被动接受，不如积极拥抱这种变化，深入理解其背后的价值逻辑，并刻意重塑自身的心智模式和技能组合。成为一名有效的AI时代构建者，需要我们从对底层细节的执着中解放出来，将精力聚焦于更高的抽象层次、更复杂的系统协调，以及与智能工具的协同进化。这是一个充满挑战，但也充满机遇的时代。