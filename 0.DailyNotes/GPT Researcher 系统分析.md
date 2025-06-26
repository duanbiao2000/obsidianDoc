---
date: 2025-06-07 21:42
tags:
  - Domain/Creativity/Product
---

# GPT Researcher 系统分析

## 1. 主要功能

GPT Researcher 是一个开源的自主研究代理系统，专为深度研究任务设计。其核心功能包括：

- **自动化研究流程**：根据用户查询自动进行网络搜索、信息收集、分析和报告生成
- **多代理协作**：使用 LangGraph 框架实现多个专业化 AI 代理协同工作
- **深度研究报告**：生成详细、有事实依据且无偏见的研究报告，包含引用来源
- **多格式输出**：支持 PDF、Word、Markdown 等多种格式的报告导出
- **Web 和本地文档研究**：能够从互联网和本地文档中收集信息
- **智能图像处理**：为报告抓取和筛选相关图像

## 2. 实施方法

GPT Researcher 的实施基于以下关键组件：

### 后端架构

1. **基础研究引擎**：
   - 使用 Python 和 FastAPI 构建
   - 支持多种 LLM（OpenAI、Claude、Gemini、Mistral 等）
   - 支持多种搜索引擎（Tavily、Google、Bing、DuckDuckGo 等）
2. **多代理系统**（LangGraph）：
   - 基于 LangChain 的 LangGraph 框架
   - 实现了 8 个专业化代理：Chief Editor、Researcher、Editor、Reviewer、Revisor、Writer、Publisher 和 Human
   - 使用有向图定义代理之间的工作流和通信

### 前端实现

1. **轻量级界面**：
   - 基于 HTML/CSS/JavaScript 的简单界面
   - 通过 FastAPI 提供服务
2. **高级 NextJS 应用**：
   - 使用 NextJS 和 Tailwind CSS 构建
   - 实时研究进度跟踪
   - 交互式结果显示
   - 可定制的研究设置

### 部署选项

1. **本地部署**：
   - 通过 pip 安装（`pip install gpt-researcher`）
   - Docker 容器支持
   - 直接从源代码运行
2. **LangGraph 云部署**：
   - 使用 `langgraph-cli` 工具
   - 支持流式和异步端点

## 3. 新颖部分

GPT Researcher 的创新点包括：

1. **多代理协作框架**：
   - 受 [[STORM 论文]]启发，实现了专业化代理团队
   - 代理间的动态协作和反馈循环
   - 模拟人类研究团队的工作流程
2. **研究深度和质量**：
   - 能够聚合 20+ 来源形成客观结论
   - 生成超过 2,000 字的详细报告
   - 保持上下文和记忆贯穿整个研究过程
3. **模块化和可扩展设计**：
   - 支持多种 LLM 和搜索引擎
   - 可自定义研究流程和报告格式
   - 提供 API 和 SDK 供开发者集成
4. **实时反馈和人机协作**：
   - 支持人类在循环中提供反馈
   - 实时显示研究进度和中间结果

## 4. 代码工作流程

### 基本研究流程

1. **初始化**：

   Copy

   用户查询 → 创建特定领域代理 → 生成研究问题集

2. **数据收集**：

   Copy

   研究问题 → 触发爬虫代理 → 搜索相关信息 → 汇总和跟踪来源

3. **分析和报告**：

   Copy

   过滤和聚合信息 → 生成研究报告 → 导出为所需格式

### LangGraph 多代理流程

1. **规划阶段**：

   Copy

   Chief Editor 接收任务 → Browser 进行初步研究 → Editor 规划报

   告结构

2. **并行研究**：

   Copy

   对每个大纲主题：

     Researcher 深入研究 → Reviewer 验证草稿 → Revisor 根据反馈

     修改

3. **整合和发布**：

   Copy

   Writer 编写最终报告 → Publisher 以多种格式发布

### 前端与后端交互

1. **用户输入**：

   Copy

   用户提交查询 → InputArea 组件处理 → 发送到后端 API

2. **研究执行**：

   Copy

   后端接收请求 → 启动研究流程 → 通过 WebSocket 流式返回进度和结果

3. **结果展示**：

   Copy

   前端接收流式数据 → 实时更新 UI → 显示最终报告和来源

### 关键控制流程

1. **研究代理初始化**：

   Copy

   researcher = GPTResearcher(query=query, 

   report_type="research_report")

   research_result = await researcher.conduct_research()

   report = await researcher.write_report()

2. **LangGraph 工作流**：

   Copy

   # 定义工作流图

   workflow = StateGraph(nodes=[...])

   # 定义节点间转换

   workflow.add_edge("chief_editor", "browser")

   workflow.add_edge("browser", "editor")

   # ...

   # 并行处理

   for topic in outline:

       workflow.add_parallel_tasks(...)

3. **前端状态管理**：

```javascript
   // 状态初始化

   const [promptValue, setPromptValue] = useState("");

   const [results, setResults] = useState<TResearchResult[]>

   ([]);

   // 提交处理

   const handleSubmit = async (query: string) => {

     setLoading(true);

     const response = await fetch("/api/research", { ... });

     const stream = response.body;

     // 处理流式响应...

   };
```

GPT Researcher 通过这些精心设计的组件和流程，实现了一个强大、灵活且用户友好的自动化研究系统，能够显著提高研究效率和质量。

---
# GPT Researcher 中的设计模式与算法分析

GPT Researcher 项目运用了多种设计模式和算法来实现其复杂的研究自动化功能。以下是对项目中主要设计模式和算法的详细分析：

## 设计模式

### 1. 工厂模式 (Factory Pattern)

scraper.py

gpt_researcher/scraper

Copy

def get_scraper(self, link):

    SCRAPER_CLASSES = {

        "pdf": PyMuPDFScraper,

        "arxiv": ArxivScraper,

        "bs": BeautifulSoupScraper,

        "web_base_loader": WebBaseLoaderScraper,

        "browser": BrowserScraper,

        "nodriver": NoDriverScraper,

        "tavily_extract": TavilyExtract,

        "firecrawl": FireCrawl,

    }

    scraper_key = None

    if link.endswith(".pdf"):

        scraper_key = "pdf"

    elif "arxiv.org" in link:

        scraper_key = "arxiv"

    else:

        scraper_key = self.scraper

- **实现**：`Scraper` 类中的 `get_scraper` 方法根据链接类型创建适当的爬虫实例
- **优势**：允许系统根据内容类型动态选择合适的爬虫，无需修改客户端代码

### 2. 策略模式 (Strategy Pattern)

base.py

gpt_researcher/llm_provider/generic

Copy

@classmethod

def from_provider(cls, provider, **kwargs):

    if provider == "openai":

        _check_pkg("langchain_openai")

        from langchain_openai import ChatOpenAI

        llm = ChatOpenAI(**kwargs)

    elif provider == "anthropic":

        _check_pkg("langchain_anthropic")

        from langchain_anthropic import ChatAnthropic

        llm = ChatAnthropic(**kwargs)

    # ... 其他提供商

- **实现**：`GenericLLMProvider` 类允许在运行时选择不同的 LLM 提供商
- **优势**：将 LLM 提供商的具体实现与使用代码分离，便于添加新的提供商

### 3. 观察者模式 (Observer Pattern)

websocket_manager.py

backend/server

Copy

Loading...

- **实现**：WebSocket 连接用于实时向前端推送研究进度和结果
- **优势**：实现了前端与后端的松耦合通信，支持实时更新

### 4. 命令模式 (Command Pattern)

orchestrator.py

multi_agents/agents

Copy

Loading...

- **实现**：每个代理的操作被封装为可执行的命令，由 `StateGraph` 协调执行
- **优势**：支持操作的排队、撤销和重做，便于实现复杂的工作流

### 5. 装饰器模式 (Decorator Pattern)

chat.py

backend/chat

Copy

Loading...

- **实现**：使用 `@tool` 装饰器将函数转换为 LangChain 工具
- **优势**：动态扩展函数功能，无需修改原始代码

### 6. 适配器模式 (Adapter Pattern)

online_document.py

gpt_researcher/document

Copy

Loading...

- **实现**：为不同文档格式提供统一的加载接口
- **优势**：允许系统处理多种文档格式，而无需了解具体实现细节

## 算法

### 1. 向量相似度搜索

compression.py

gpt_researcher/context

Copy

Loading...

- **实现**：使用嵌入向量和余弦相似度计算来检索相关文档
- **复杂度**：O(n) 用于线性扫描，或 O(log n) 使用近似最近邻算法
- **应用**：在研究过程中检索相关上下文信息

### 2. 文本分块算法

chat.py

backend/chat

Copy

Loading...

- **实现**：递归字符分割器将长文本分割成重叠的小块
- **复杂度**：O(n) 其中 n 是文本长度
- **应用**：将长文档分割成适合 LLM 处理的小块

### 3. 防抖算法 (Debounce)

InputArea.tsx

frontend/nextjs/components/ResearchBlocks/elements

Copy

Loading...

- **实现**：延迟函数执行直到用户停止输入
- **复杂度**：O(1)
- **应用**：优化文本区域高度调整，减少不必要的 DOM 操作

### 4. 有向图遍历算法

editor.py

multi_agents/agents

Copy

Loading...

- **实现**：使用 LangGraph 的 `StateGraph` 实现有向图工作流
- **复杂度**：O(V+E) 其中 V 是节点数，E 是边数
- **应用**：定义和执行多代理研究工作流

### 5. 令牌计数和成本估算算法

costs.py

gpt_researcher/utils

Copy

def estimate_llm_cost(input_content: str, output_content: str) 

-> float:

    encoding = tiktoken.get_encoding(ENCODING_MODEL)

    input_tokens = encoding.encode(input_content)

    output_tokens = encoding.encode(output_content)

    input_costs = len(input_tokens) * INPUT_COST_PER_TOKEN

    output_costs = len(output_tokens) * OUTPUT_COST_PER_TOKEN

    return input_costs + output_costs

- **实现**：使用 tiktoken 库计算输入和输出的令牌数，并估算成本
- **复杂度**：O(n) 其中 n 是文本长度
- **应用**：跟踪和优化 LLM API 调用成本

### 6. 速率限制算法

base.py

gpt_researcher/llm_provider/generic

Copy

rate_limiter = InMemoryRateLimiter(

    requests_per_second=rps,

    check_every_n_seconds=0.1,

    max_bucket_size=10,

)

- **实现**：使用令牌桶算法实现 API 调用的速率限制
- **复杂度**：O(1) 用于检查和更新令牌桶
- **应用**：防止超过 API 提供商的速率限制，避免请求失败

## 总结

GPT Researcher 项目巧妙地结合了多种设计模式和算法，实现了一个灵活、可扩展且高效的自动化研究系统：

1. **设计模式**侧重于系统架构，提供了模块化、可扩展的框架
2. **算法**优化了具体操作，确保系统高效处理大量文本和复杂工作流
3. **组合使用**这些模式和算法使系统能够处理各种研究任务，同时保持代码的可维护性

这种设计使 GPT Researcher 不仅能够完成当前的研究任务，还能够轻松适应未来的扩展和改进。

---

# GPT Researcher 项目学习路线图

基于对项目的总体分析和设计模式/算法理解，以下是一个结构化的学习路线图，帮助您最快掌握 GPT Researcher 项目。

## 阶段 1: 基础架构理解（1-2 天）

### 任务 1.1: 核心组件分析

- 研究 
    
     `gpt_researcher`
    
     主模块结构
- 理解 `GPTResearcher` 类的初始化和主要方法
- 分析配置系统和环境变量设置

### 任务 1.2: LLM 集成机制

- 研究 `llm_provider` 模块
- 了解不同 LLM 提供商的集成方式
- 分析 API 调用、流式处理和错误处理机制

### 任务 1.3: 搜索和爬虫系统

- 研究 `scraper` 模块和各种爬虫实现
- 了解搜索引擎集成（Tavily、Google 等）
- 分析网页内容提取和处理流程

## 阶段 2: 研究流程深入（2-3 天）

### 任务 2.1: 基本研究流程

- 跟踪 `conduct_research` 方法的完整执行流程
- 分析查询处理和子查询生成逻辑
- 了解上下文管理和信息聚合机制

### 任务 2.2: 报告生成系统

- 研究 `report_type` 模块中的不同报告类型
- 分析 `write_report` 方法的实现
- 了解格式化、引用和图像处理机制

### 任务 2.3: 构建简单研究代理

- 创建一个基本的研究脚本，使用 GPT Researcher 的核心功能
- 测试不同的查询类型和报告格式
- 分析结果质量和性能

## 阶段 3: 多代理系统（2-3 天）

### 任务 3.1: LangGraph 框架理解

- 研究 
    
     `multi_agents`
    
     模块结构
- 了解 `StateGraph` 的工作原理
- 分析节点和边的定义方式

### 任务 3.2: 代理角色和职责

- 研究各个代理类（Editor、Researcher、Reviewer 等）
- 分析代理间的通信和状态传递
- 了解条件转换和并行执行机制

### 任务 3.3: 构建自定义多代理工作流

- 创建一个简化的多代理研究工作流
- 测试不同的代理配置和工作流结构
- 分析结果质量和执行效率

## 阶段 4: 前端和用户交互（1-2 天）

### 任务 4.1: 基本前端理解

- 研究 HTML/JS 简单前端的实现
- 了解 WebSocket 通信机制
- 分析用户输入处理和结果展示

### 任务 4.2: NextJS 前端深入

- 研究 NextJS 应用的组件结构
- 分析状态管理和数据流
- 了解实时更新和进度显示机制

### 任务 4.3: 构建自定义 UI

- 创建一个简化的研究界面
- 实现基本的用户交互功能
- 测试不同的研究场景和结果展示

## 阶段 5: 高级功能和扩展（2-3 天）

### 任务 5.1: 深度研究模式

- 研究 `deep_research` 模块的实现
- 分析深度和广度参数的影响
- 了解进度跟踪和成本优化机制

### 任务 5.2: 详细报告系统

- 研究 `detailed_report` 模块的实现
- 分析子主题生成和并行研究机制
- 了解报告结构化和整合流程

### 任务 5.3: 自定义扩展开发

- 创建一个自定义爬虫或 LLM 提供商适配器
- 实现一个新的报告类型或研究流程
- 测试扩展的集成和性能

## 阶段 6: 部署和优化（1-2 天）

### 任务 6.1: 本地部署

- 设置完整的本地开发环境
- 配置所有必要的 API 密钥和服务
- 测试端到端的研究流程

### 任务 6.2: Docker 部署

- 研究 Docker 配置和构建流程
- 创建自定义 Docker 镜像
- 测试容器化部署的性能

### 任务 6.3: 性能优化

- 分析系统瓶颈和资源使用
- 实现缓存和并行处理优化
- 测试优化后的性能提升

## 实践项目建议

完成上述学习路径后，可以尝试以下实践项目来巩固知识：

1. **专业领域研究助手**：为特定领域（如医学、法律、金融）定制研究流程和报告格式
2. **多语言研究系统**：扩展系统支持多语言查询和报告生成
3. **交互式研究对话**：实现一个对话式研究界面，允许用户在研究过程中提供反馈和调整方向
4. **研究质量评估系统**：开发一个模块来评估研究结果的质量、全面性和准确性
5. **本地知识库集成**：扩展系统以结合本地知识库和网络搜索结果

## 学习资源

在学习过程中，可以参考以下资源：

1. **项目文档**：
    
     `docs`
    
     目录中的详细文档
2. **示例代码**：`examples` 目录中的示例脚本
3. **LangChain 文档**：了解 LangChain 和 LangGraph 的基础知识
4. **相关论文**：特别是 STORM 论文，了解多代理系统的理论基础
5. **社区讨论**：GitHub Issues 和 Discussions 中的问题和解决方案

按照这个路线图，您可以在约 9-15 天内全面掌握 GPT Researcher 项目，从基础组件到高级功能，再到实际部署和优化。

---
# GPT Researcher 的 `conduct_research` 方法执行流程分析

## 1. 方法概述

`conduct_research` 是 GPT Researcher 的核心方法，负责执行整个研究过程，从接收查询到生成研究上下文。以下是对其完整执行流程的详细分析。

## 2. 执行流程跟踪

### 2.1 入口点分析

agent.py

gpt_researcher

Copy

async def conduct_research(self, on_progress=None):

    await self._log_event("research", step="start", details={

        "query": self.query,

        "report_type": self.report_type,

        "agent": self.agent,

        "role": self.role

    })

    # Handle deep research separately

    if self.report_type == ReportType.DeepResearch.value and 

    self.deep_researcher:

        return await self._handle_deep_research(on_progress)

    if not (self.agent and self.role):

        await self._log_event("action", action="choose_agent")

        self.agent, self.role = await choose_agent(

            query=self.query,

            cfg=self.cfg,

            parent_query=self.parent_query,

            cost_callback=self.add_costs,

            headers=self.headers,

        )

        await self._log_event("action", 

        action="agent_selected", details={

            "agent": self.agent,

            "role": self.role

        })

    await self._log_event("research", 

    step="conducting_research", details={

        "agent": self.agent,

        "role": self.role

    })

    self.context = await self.research_conductor.

    conduct_research()

    await self._log_event("research", 

    step="research_completed", details={

        "context_length": len(self.context)

    })

    return self.context

方法执行的主要步骤：

1. 记录研究开始事件
2. 检查是否为深度研究模式
3. 如果需要，选择合适的代理和角色
4. 调用 `research_conductor.conduct_research()` 执行实际研究
5. 记录研究完成事件并返回上下文

### 2.2 深度研究处理

当报告类型为 `DeepResearch` 时，会调用专门的处理方法：

deep_research.py

gpt_researcher/skills

Copy

async def run(self, on_progress=None) -> str:

    """Run the deep research process and generate final 

    report"""

    start_time = time.time()

    # Log initial costs

    initial_costs = self.researcher.get_costs()

    follow_up_questions = await self.generate_research_plan

    (self.researcher.query)

    answers = ["Automatically proceeding with research"] * len

    (follow_up_questions)

    qa_pairs = [f"Q: {q}\nA: {a}" for q, a in zip

    (follow_up_questions, answers)]

    combined_query = f"""

    Initial Query: {self.researcher.query}\nFollow - up 

    Questions and Answers:\n

    """ + "\n".join(qa_pairs)

    results = await self.deep_research(

        query=combined_query,

        breadth=self.breadth,

        depth=self.depth,

        on_progress=on_progress

    )

    # ... 处理结果和返回上下文

    return self.researcher.context

深度研究流程：

1. 生成研究计划和跟进问题
2. 构建增强查询
3. 执行深度研究，指定广度和深度参数
4. 处理结果并返回上下文

### 2.3 标准研究流程

标准研究流程由 `Researcher` 类的 `conduct_research` 方法实现：

researcher.py

gpt_researcher/skills

Copy

async def conduct_research(self):

    """Runs the GPT Researcher to conduct research"""

    if self.json_handler:

        self.json_handler.update_content("query", self.

        researcher.query)

    self.logger.info(f"Starting research for query: {self.

    researcher.query}")

    # Reset visited_urls and source_urls at the start of each 

    research task

    self.researcher.visited_urls.clear()

    research_data = []

    if self.researcher.verbose:

        await stream_output(

            "logs",

            "starting_research",

            f"🔍 Starting the research task for '{self.

            researcher.query}'...",

            self.researcher.websocket,

        )

        await stream_output(

            "logs",

            "agent_generated",

            self.researcher.agent,

            self.researcher.websocket

        )

    # Research for relevant sources based on source types below

    if self.researcher.source_urls:

        self.logger.info("Using provided source URLs")

        research_data = await self._get_context_by_urls(self.

        researcher.source_urls)

        # ... 处理源 URL 和补充搜索

    elif self.researcher.report_source == ReportSource.Web.

    value:

        self.logger.info("Using web search")

        research_data = await self._get_context_by_web_search

        (self.researcher.query, [], self.researcher.

        query_domains)

    elif self.researcher.report_source == ReportSource.Local.

    value:

        self.logger.info("Using local search")

        # ... 处理本地文档搜索

    # Rank and curate the sources

    self.researcher.context = research_data

    if self.researcher.cfg.curate_sources:

        self.logger.info("Curating sources")

        self.researcher.context = await self.researcher.

        source_curator.curate_sources(research_data)

    # ... 记录和返回结果

    return self.researcher.context

标准研究流程：

1. 初始化研究环境和记录
2. 根据配置选择研究来源（提供的 URL、网络搜索或本地文档）
3. 获取和处理研究数据
4. 可选地对来源进行排名和筛选
5. 返回研究上下文

## 3. 查询处理和子查询生成逻辑

### 3.1 子查询生成

子查询生成是通过 `plan_research` 方法实现的：

researcher.py

gpt_researcher/skills

Copy

async def plan_research(self, query, query_domains=None):

    self.logger.info(f"Planning research for query: {query}")

    if query_domains:

        self.logger.info(f"Query domains: {query_domains}")

    await stream_output(

        "logs",

        "planning_research",

        f"🌐 Browsing the web to learn more about the task: 

        {query}...",

        self.researcher.websocket,

    )

    search_results = await get_search_results(query, self.

    researcher.retrievers[0], query_domains)

    self.logger.info(f"Initial search results obtained: {len

    (search_results)} results")

    await stream_output(

        "logs",

        "planning_research",

        f"🤔 Planning the research strategy and subtasks...",

        self.researcher.websocket,

    )

    outline = await plan_research_outline(

        query=query,

        search_results=search_results,

        agent_role_prompt=self.researcher.role,

        cfg=self.researcher.cfg,

        parent_query=self.researcher.parent_query,

        report_type=self.researcher.report_type,

        cost_callback=self.researcher.add_costs,

    )

    self.logger.info(f"Research outline planned: {outline}")

    return outline

子查询生成流程：

1. 执行初始搜索以获取基本上下文
2. 使用 `plan_research_outline` 函数生成研究大纲
3. 大纲中的每个项目成为一个子查询

### 3.2 子查询生成的底层实现

子查询生成的核心逻辑在

`query_processing.py`

中：

query_processing.py

gpt_researcher/actions

Copy

async def generate_sub_queries(

    query: str,

    parent_query: str,

    report_type: str,

    context: List[Dict[str, Any]],

    cfg: Config,

    cost_callback: callable = None

) -> List[str]:

    """

    Generate sub-queries using the specified LLM model.

    """

    gen_queries_prompt = generate_search_queries_prompt(

        query,

        parent_query,

        report_type,

        max_iterations=cfg.max_iterations or 3,

        context=context

    )

    # ... LLM 调用和处理

    return sub_queries

async def plan_research_outline(

    query: str,

    search_results: List[Dict[str, Any]],

    agent_role_prompt: str,

    cfg: Config,

    parent_query: str,

    report_type: str,

    cost_callback: callable = None,

) -> List[str]:

    """

    Plan the research outline by generating sub-queries.

    """

    sub_queries = await generate_sub_queries(

        query,

        parent_query,

        report_type,

        search_results,

        cfg,

        cost_callback

    )

    return sub_queries

子查询生成的关键点：

1. 使用初始查询和搜索结果作为输入
2. 生成专门的提示以引导 LLM 创建子查询
3. 考虑报告类型和父查询（如果有）
4. 返回子查询列表用于后续研究

## 4. 上下文管理和信息聚合机制

### 4.1 网络搜索和上下文获取

researcher.py

gpt_researcher/skills

Copy

async def _get_context_by_web_search(self, query, 

scraped_data: list | None = None, query_domains: list | None = 

None):

    """

    Generates the context for the research task by searching 

    the query and scraping the results

    """

    self.logger.info(f"Starting web search for query: {query}")

    if scraped_data is None:

        scraped_data = []

    if query_domains is None:

        query_domains = []

    # Generate Sub-Queries including original query

    sub_queries = await self.plan_research(query, 

    query_domains)

    self.logger.info(f"Generated sub-queries: {sub_queries}")

    # If this is not part of a sub researcher, add original 

    query to research for better results

    if self.researcher.report_type != "subtopic_report":

        sub_queries.append(query)

    # Using asyncio.gather to process the sub_queries 

    asynchronously

    try:

        context = await asyncio.gather(

            *[

                self._process_sub_query(sub_query, 

                scraped_data, query_domains)

                for sub_query in sub_queries

            ]

        )

        # ... 处理和返回结果

    except Exception as e:

        self.logger.error(f"Error during web search: {e}", 

        exc_info=True)

        return []

网络搜索流程：

1. 生成子查询列表
2. 对每个子查询并行执行 `_process_sub_query`
3. 聚合所有子查询的结果
4. 处理异常并返回上下文

### 4.2 子查询处理

researcher.py

gpt_researcher/skills

Copy

async def _process_sub_query(self, sub_query: str, 

scraped_data: list = [], query_domains: list = []):

    """Takes in a sub query and scrapes urls based on it and 

    gathers context."""

    if self.json_handler:

        self.json_handler.log_event("sub_query", {

            "query": sub_query,

            "scraped_data_size": len(scraped_data)

        })

    if self.researcher.verbose:

        await stream_output(

            "logs",

            "running_subquery_research",

            f"\n🔍 Running research for '{sub_query}'...",

            self.researcher.websocket,

        )

    try:

        if not scraped_data:

            scraped_data = await self._scrape_data_by_urls

            (sub_query, query_domains)

            self.logger.info(f"Scraped data size: {len

            (scraped_data)}")

        content = await self.researcher.context_manager.

        get_similar_content_by_query(sub_query, scraped_data)

        self.logger.info(f"Content found for sub-query: {len

        (str(content)) if content else 0} chars")

        # ... 处理和返回结果

        return content

    except Exception as e:

        self.logger.error(f"Error processing sub-query 

        {sub_query}: {e}", exc_info=True)

        return ""

子查询处理流程：

1. 如果没有预先抓取的数据，则抓取相关 URL
2. 使用上下文管理器获取与子查询相关的内容
3. 处理异常并返回内容

### 4.3 上下文相似度和筛选

上下文管理器负责根据查询筛选相关内容：

context_manager.py

gpt_researcher/skills

Copy

async def get_similar_content_by_query(self, query, pages):

    if self.researcher.verbose:

        await stream_output(

            "logs",

            "fetching_query_content",

            f"📚 Getting relevant content based on query: 

            {query}...",

            self.researcher.websocket,

        )

    context_compressor = ContextCompressor(

        documents=pages, embeddings=self.researcher.memory.

        get_embeddings()

    )

    return await context_compressor.async_get_context(

        query=query, max_results=10, cost_callback=self.

        researcher.add_costs

    )

上下文筛选机制：

1. 使用 `ContextCompressor` 类处理文档
2. 利用嵌入向量计算查询与文档的相似度
3. 选择最相关的内容（最多 10 个结果）
4. 跟踪成本并返回筛选后的上下文

### 4.4 深度研究中的上下文聚合

深度研究模式使用更复杂的上下文聚合机制：

deep_research.py

gpt_researcher/skills

Copy

async def deep_research(

        self,

        query: str,

        breadth: int,

        depth: int,

        learnings: List[str] = None,

        citations: Dict[str, str] = None,

        visited_urls: Set[str] = None,

        on_progress=None

) -> Dict[str, Any]:

    """Conduct deep iterative research"""

    # ... 初始化

    # Generate search queries

    serp_queries = await self.generate_search_queries(query, 

    num_queries=breadth)

    progress.total_queries = len(serp_queries)

    all_learnings = learnings.copy()

    all_citations = citations.copy()

    all_visited_urls = visited_urls.copy()

    all_context = []

    all_sources = []

    # Process queries concurrently with limit

    tasks = [process_query(query) for query in serp_queries]

    results = await asyncio.gather(*tasks)

    results = [r for r in results if r is not None]

    # Update breadth progress based on successful queries

    progress.current_breadth = len(results)

    if on_progress:

        on_progress(progress)

    # Collect all results

    for result in results:

        all_learnings.extend(result['learnings'])

        all_visited_urls.update(result['visited_urls'])

        all_citations.update(result['citations'])

        if result['context']:

            all_context.append(result['context'])

        if result['sources']:

            all_sources.extend(result['sources'])

        # Continue deeper if needed

        if depth > 1:

            # ... 递归研究

深度研究的上下文聚合：

1. 并行处理多个查询
2. 收集所有结果（学习、引用、URL、上下文、来源）
3. 如果深度 > 1，则递归进行更深层次的研究
4. 最终聚合所有层次的结果

## 5. 关键机制总结

### 5.1 查询处理机制

1. **分层查询结构**：
    - 原始查询 → 子查询 → 搜索查询
    - 每一层都增加特异性和覆盖范围
2. **上下文感知查询生成**：
    - 使用初始搜索结果指导子查询生成
    - 考虑报告类型和父查询
3. **并行查询处理**：
    - 使用 `asyncio.gather` 并行处理多个子查询
    - 提高研究效率和覆盖范围

### 5.2 上下文管理机制

1. **多源上下文获取**：
    - 网络搜索
    - 提供的 URL
    - 本地文档
    - 向量存储
2. **相似度筛选**：
    - 使用嵌入向量计算查询与文档的相似度
    - 选择最相关的内容
3. **上下文压缩和聚合**：
    - 合并多个来源的信息
    - 去除重复和不相关内容
    - 确保上下文在 LLM 处理限制内

### 5.3 深度研究特性

1. **广度和深度参数**：
    - 控制研究的广度（并行查询数）
    - 控制研究的深度（递归层级）
2. **学习和引用跟踪**：
    - 从每个来源提取关键学习点
    - 维护引用以确保可追溯性
3. **进度跟踪**：
    - 使用 `ResearchProgress` 类跟踪研究进度
    - 支持实时进度更新

## 6. 执行流程图

Copy

conduct_research
```
│

├── 如果是深度研究

│   └── _handle_deep_research

│       ├── 生成研究计划和问题

│       ├── 执行深度研究（breadth × depth）

│       └── 处理结果并返回上下文

│

└── 标准研究

    ├── 选择代理和角色（如果需要）

    └── research_conductor.conduct_research

        ├── 根据来源选择研究方法

        │   ├── _get_context_by_urls（提供的 URL）

        │   ├── _get_context_by_web_search（网络搜索）

        │   └── _get_context_by_vectorstore（向量存储）

        │

        ├── 对于网络搜索

        │   ├── plan_research 生成子查询

        │   ├── 并行处理每个子查询

        │   │   └── _process_sub_query

        │   │       ├── _scrape_data_by_urls 抓取数据

        │   │       └── context_manager.

        get_similar_content_by_query 筛选内容

        │   └── 聚合所有子查询结果

        │

        ├── 可选地筛选和
        
```