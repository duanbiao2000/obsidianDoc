
## 🎯 Agent Objective Definition: **Restaurant Recommendation Agent**

---

### ✅ 1. What problem do I want my Agent to solve?

**Primary Goal**:  
帮助用户在指定城市中根据 _菜系偏好_ 和 _预算约束_ 发现评分最高的餐厅。

**Use Cases**:

- 构建一个通过自然语言与用户交互的聊天机器人
    
- 能够根据用户的多轮输入动态理解其需求
    
- 提供个性化推荐，包括评分、评论、联系方式等关键信息
    

---

### 🤝 2. Will my Agent need to collaborate with other agents?

**Answer**: Yes, the task benefits from modular agent collaboration.

**Sub-Agent Roles**:

- **UserIntentParser Agent**：理解用户需求（菜系、预算、位置等）
    
- **DataRetrieval Agent**：调用外部 API（如 Yelp、Google Maps）查询餐厅信息
    
- **RecommendationRanker Agent**：根据评分、预算、偏好等因素进行排序和筛选
    
- **ResponseGenerator Agent**：整理最终输出并以自然语言呈现
    

**Benefits of Collaboration**:

- 各子 Agent 解耦、可复用
    
- 增强响应的准确性和灵活性
    
- 易于扩展（如后续添加“订位助手”、“评价生成器”等子 Agent）
    

---

### 🧩 3. What tasks should my Agent perform to achieve its goal?

**Task Breakdown**:

1. **接收用户请求**：通过聊天界面获取用户输入（如“我想找一家北京的川菜馆，人均150左右”）
    
2. **解析用户意图**：提取关键词：{城市、菜系、预算}
    
3. **调用外部数据源**：如 Google Places, Yelp API 获取符合条件的餐厅列表
    
4. **应用推荐策略**：按照评分、评价数量、距离、匹配度进行排序
    
5. **生成推荐响应**：提供前3家餐厅的详细信息：名称、评分、地址、联系方式、简评
    
6. **支持多轮对话**：允许用户进一步 refine（如“我想要安静一点的环境”）
    

**Input/Output Requirements**:

- **Input**: 用户自然语言请求
    
- **Output**: JSON 格式的推荐列表 + 自然语言摘要回复
    

---

### 🛠️ 4. What tools and resources will my Agent need?

**Libraries & APIs**:

- OpenAI/Gemini LLM API（对话理解、响应生成）
    
- 外部 API：Google Places API, Yelp API（实时餐厅数据）
    
- LangGraph（构建多 Agent 协作流程）
    
- 地理位置处理库（如 `geopy`）
    

**Domain Knowledge**:

- 不同菜系分类表
    
- 用户预算与餐厅价格等级之间的映射表
    
- 用户评价倾向建模（可选）
    

**Pretrained Models**:

- LLM for NLU + NLG（如 GPT-4, Gemini 1.5）
    
- 可选：RAG 机制加载本地餐饮评价语料（如点评网/小红书）
    

---

### 📦 Summary (One-liner Objective)

> A conversational Restaurant Recommendation Agent that collaborates with sub-agents to parse user preferences, query restaurant APIs, rank results, and return personalized dining suggestions, all through natural interaction.

---

如需进一步生成 Obsidian Kanban / LangGraph 架构图（如 Planner-Executor-Reviewer 三层结构），我可以直接帮你扩展。需要吗？