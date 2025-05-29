
```python
# LangGraph Flow Prototype: 结构化笔记 AI Agent（含状态记忆、图谱导出、AgentLoop）

from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import json
import os

# ------ ENV 配置 ------
os.environ["GOOGLE_API_KEY"] = "your_gemini_api_key_here"
llm = ChatGoogleGenerativeAI(model="gemini-pro")
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = FAISS.from_documents([Document(page_content="init")], embedding_model)
retriever = vectorstore.as_retriever()

# ------ 状态图记忆容器 ------
memory_state = defaultdict(list)

# ------ Prompts ------
parse_prompt = ChatPromptTemplate.from_template(
    """
笔记内容如下："{note}"
请抽取其中的核心概念、关系对、相关主题，输出：
- 概念清单
- 三元组列表（如：A, 关系, B）
- 推荐知识图谱节点
"""
)

reflect_prompt = ChatPromptTemplate.from_template(
    """
图谱上下文如下："{context}"
新笔记："{note}"
请判断：
- 是否存在重复或冲突？
- 是否出现新连接或理解链？
- 推荐的图谱更新方式
"""
)

summarize_prompt = ChatPromptTemplate.from_template(
    "总结当前知识图谱的主要主题和结构。"
)

next_task_prompt = ChatPromptTemplate.from_template(
    "基于当前图谱内容，总结下一个值得深入的问题或延展笔记主题：\n{reflection}"
)

# ------ Runnable Chains ------
parse_chain = parse_prompt | llm | StrOutputParser()
reflect_chain = reflect_prompt | llm | StrOutputParser()
summarize_chain = summarize_prompt | llm | StrOutputParser()
next_task_chain = next_task_prompt | llm | StrOutputParser()

# ------ 知识图谱可视化 ------
def update_graph(triples, output_file="kg_graph.png"):
    G = nx.DiGraph()
    for t in triples:
        if len(t) == 3:
            G.add_edge(t[0], t[2], label=t[1])
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="gray", node_size=2000, font_size=12)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("知识图谱结构图")
    plt.savefig(output_file)
    plt.close()

# ------ Node Functions ------
def ingest_note(state):
    note = state["note"]
    vectorstore.add_documents([Document(page_content=note)])
    memory_state["notes"].append(note)
    return {"note": note}

def parse_knowledge(state):
    parsed = parse_chain.invoke({"note": state["note"]})
    memory_state["parsed"].append(parsed)
    try:
        triples = []
        for line in parsed.split("\n"):
            if line.strip().startswith("(") and "," in line:
                t = line.strip("() ").split(",")
                triples.append(tuple(x.strip() for x in t))
        memory_state["triples"].extend(triples)
        update_graph(memory_state["triples"], output_file="knowledge_graph.png")
    except Exception as e:
        print("[Parse Error]", e)
    return {"parsed": parsed}

def reflect_and_update(state):
    docs = retriever.get_relevant_documents(state["note"])
    context = "\n".join([d.page_content for d in docs])
    reflection = reflect_chain.invoke({"note": state["note"], "context": context})
    memory_state["reflections"].append(reflection)
    return {"reflection": reflection}

def summarize_graph(state):
    summary = summarize_chain.invoke({})
    memory_state["summary"] = summary
    return {"summary": summary}

def suggest_next_task(state):
    reflection = state.get("reflection", "")
    task = next_task_chain.invoke({"reflection": reflection})
    memory_state["next_tasks"].append(task)
    return {"note": task}  # 循环注入到下次运行

# ------ LangGraph 流程图构建 ------
graph_builder = StateGraph()

graph_builder.add_node("ingest_note", RunnableLambda(ingest_note))
graph_builder.add_node("parse_knowledge", RunnableLambda(parse_knowledge))
graph_builder.add_node("reflect_update", RunnableLambda(reflect_and_update))
graph_builder.add_node("summarize", RunnableLambda(summarize_graph))
graph_builder.add_node("next_task", RunnableLambda(suggest_next_task))

# 控制边（AgentLoop）

def loop_or_end(state):
    if len(memory_state["next_tasks"]) > 2:
        return "end"
    return "ingest_note"

graph_builder.set_entry_point("ingest_note")

graph_builder.add_edge("ingest_note", "parse_knowledge")
graph_builder.add_edge("parse_knowledge", "reflect_update")
graph_builder.add_edge("reflect_update", "summarize")
graph_builder.add_edge("summarize", "next_task")
graph_builder.add_conditional_edges("next_task", loop_or_end, {"ingest_note": "ingest_note", "end": END})

agent_graph = graph_builder.compile()

# ------ 运行示例 ------
if __name__ == "__main__":
    first_note = "Transformer 模型中的注意力机制启示我构建查询-匹配图谱结构。"
    final = agent_graph.invoke({"note": first_note})
    print("\n📌 [知识抽取]", final.get("parsed"))
    print("\n🔁 [反思更新]", final.get("reflection"))
    print("\n🧠 [图谱总结]", final.get("summary"))
    print("\n🧭 [新问题生成]", final.get("note"))

    with open("memory_state.json", "w", encoding="utf-8") as f:
        json.dump(dict(memory_state), f, indent=2, ensure_ascii=False)
        print("\n📁 状态已保存至 memory_state.json，图谱输出至 knowledge_graph.png")

```

✅ 已生成完整实现版本：

这套代码是一个具备如下核心功能的智能笔记系统原型：

- **📌 状态记忆**：`memory_state` 贯穿整个 Agent 流；
    
- **🧠 图谱导出**：自动抽取三元组并生成 `.png` 图；
    
- **🔁 Agent 循环**：总结-反思-提问自动闭环执行；
    
- **💾 本地保存**：输出 `memory_state.json` 与图谱文件；
    
- **🔗 模块结构清晰**：使用 `LangGraph + Runnable + EL + Memory` 构建标准化 Flow。
    

你可以运行它来整理一批笔记文件，实现个人知识的结构化与演化。

📍建议下一步：

- 加入本地笔记源（如 Obsidian Sync）；
    
- 增强提问生成策略（引入元认知提示词）；
    
- 引入 Markdown 总结输出和长期图谱归档。
    

需要我帮你配一个更强的提示词库或者可视化工具链也可以提。继续深入？