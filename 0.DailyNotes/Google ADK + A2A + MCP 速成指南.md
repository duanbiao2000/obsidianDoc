---
aliases:
date: 2025-09-11 21:11
tags:
source:
  - https://github.com/duanbiao2000/adk-mcp-a2a-crash-course
update:
rating:
---


## BMAD technique

从你提供的YouTube视频背景信息及技术领域常见概念来看，**BMAD technique（通常全称为“Breakdown, Map, Assign, Deliver”，即“拆解、映射、分配、交付”技术）** 是一种面向多智能体（如Claude Code子代理）协作的项目管理与任务执行方法论，核心用于将复杂开发任务高效拆解并分配给不同智能体，确保协作有序、输出连贯。其核心逻辑与视频中强调的“子代理分工协作、先设计后实现”思路有共通性，但具体框架更侧重“任务拆解-责任分配”的流程化管理，简要解析如下：

### 1. 核心理念

BMAD的核心是解决“多智能体协作混乱”问题——避免直接用大量子代理无序并行，而是通过结构化流程，让每个智能体聚焦特定细分任务，同时确保所有任务输出能整合为完整成果（如一个应用、一份方案）。这与视频中批判的“用40-50个子代理替代团队却忽略协调”的错误用法形成对比，本质都是强调“有序分工”而非“数量堆砌”。

### 2. 关键步骤（典型流程）

- **Breakdown（拆解）**：将复杂目标（如“开发YouTube社交证明小部件”）拆分为最小可执行单元，例如拆分为“PRD撰写、UI设计、YouTube API集成、ChatGPT情感分析、iframe嵌入功能开发”等独立任务，确保每个任务边界清晰、无需依赖其他任务的中间结果。
- **Map（映射）**：为每个拆解后的任务匹配“专业化智能体”，例如“UI设计任务”映射到“UI设计子代理”，“API集成任务”映射到“YouTube Data API专业子代理”。这一步的核心是“让专业代理做专业事”，避免单一代理承担跨领域任务（如让通用代理同时负责UI和API，导致效率低或错误）。
- **Assign（分配）**：明确每个智能体的任务目标、输出格式、交付时间（或依赖关系），例如要求“API子代理输出‘获取视频元数据的代码片段+接口调用文档’，并存储到指定文件夹”。同时会定义“协调器代理”，负责监控任务进度、解决任务间的依赖冲突（如确保“情感分析”任务在“获取评论数据”任务完成后再执行）。
- **Deliver（交付）**：各智能体按分配任务输出成果，协调器代理汇总所有成果并验证完整性（如检查“UI代码是否能调用API返回的数据”“iframe是否能正常嵌入”），最终整合成符合初始目标的完整产物（如可运行的应用MVP）。

### 3. 与视频中“Claude Code子代理用法”的关联

视频中提到“先设计阶段（子代理并行输出设计文档）、再实现阶段（子代理按顺序编写代码）”的流程，本质是BMAD理念的具体落地：

- 视频中的“设计阶段”对应BMAD的“Breakdown+Map”：将“设计应用”拆分为“UI设计、API文档调研、测试架构设计”等任务，分别分配给UI子代理、API子代理、测试子代理并行执行；
- 视频中的“实现阶段”对应BMAD的“Assign+Deliver”：协调器代理按设计文档，将“编写前端代码、编写API调用逻辑”等任务分配给对应子代理，按顺序执行并最终交付可运行的应用。

视频作者也提到“尚未深入研究BMAD，但计划后续对比两种方法”，可见二者都是多智能体开发中的高效方法论，核心差异可能在于BMAD更侧重“通用任务的拆解分配框架”，而视频方法更聚焦“Claude Code环境下的设计-实现闭环”。

---

下面是对 `requirements.txt` 中各依赖在你项目中的功能和作用的简要解读：

---

### 核心依赖

1. **google-adk==1.2.1**
   - **功能**：Google 的 ADK（应用开发工具包）接口库，通常用于与 Google 服务、设备或相关 API 进行交互。
   - **作用**：为项目提供与 Google 相关的集成能力，例如数据同步或硬件连接。

2. **a2a-sdk==0.2.5**
   - **功能**：A2A（Application-to-Application）通信 SDK，支持应用间数据交换和消息传递。
   - **作用**：实现项目内部或与外部服务的互通，适用于自动化流程或集成场景。

3. **fastapi==0.115.12**
   - **功能**：高性能 Web 框架，基于 ASGI，用于构建 API 服务。
   - **作用**：用于项目后端的接口开发，支持异步处理和自动文档生成。

4. **litellm==1.72.0**
   - **功能**：轻量级 LLM（大语言模型）接口库，简化与各种 LLM 服务（如 OpenAI、Claude）的集成。
   - **作用**：项目中如需调用大模型能力（AI问答、推理），此库可统一接口和调用方式。

5. **uvicorn[standard]==0.34.3**
   - **功能**：ASGI 服务器，适用于 FastAPI 等异步 Web 框架。
   - **作用**：作为项目的 Web 服务运行环境，负责高效处理 HTTP 请求。

6. **streamlit==1.45.1**
   - **功能**：可视化 Web 前端框架，快速构建仪表盘和交互式工具。
   - **作用**：用于项目的前端原型或数据展示，便于非开发者操控和演示功能。

7. **python-dotenv==1.1.0**
   - **功能**：用于加载 `.env` 文件中的环境变量。
   - **作用**：管理敏感配置（如 API 密钥、数据库地址），确保安全和灵活的环境切换。

8. **httpx==0.28.1**
   - **功能**：异步 HTTP 客户端，比 requests 更适合现代异步应用。
   - **作用**：项目中如需与第三方服务进行 HTTP 通信（如 API 调用），此库可支持高并发场景。

---

### 开发依赖（测试与代码质量）

1. **black==25.1.0**
   - **功能**：自动化 Python 代码格式化工具。
   - **作用**：统一代码风格，提升代码质量和可维护性。

2. **isort==6.0.1**
   - **功能**：自动整理 import 顺序。
   - **作用**：保持代码整洁，避免 import 混乱。

3. **mypy==1.16.0**
   - **功能**：静态类型检查工具。
   - **作用**：提升代码健壮性，及早发现类型错误。

4. **pytest==8.4.0**
   - **功能**：主流 Python 单元测试框架。
   - **作用**：编写和运行测试用例，保障代码质量。

5. **pytest-asyncio==1.0.0**
   - **功能**：支持 asyncio 协程测试的 pytest 插件。
   - **作用**：便于测试异步代码（如 FastAPI 路由、httpx 请求）。

6. **pytest-cov==6.1.1**
   - **功能**：测试覆盖率统计工具。
   - **作用**：衡量测试的全面性，发现未覆盖的代码分支。

---

### 总结建议

- **核心依赖**：负责项目的业务逻辑、后端服务、前端展示与第三方服务集成。
- **开发依赖**：保障团队开发效率、代码规范与质量。

如需更深入的使用示例或集成建议，可以针对具体库提问！

---

好的，以下是对 `utils/custom_adk_patches.py` 主要类和函数的执行流程总结（涵盖函数功能、输入、处理逻辑与输出），并采用简体中文说明，结构化便于开发者快速理解：

---

## 1. CustomMcpSessionManager 类

### 主要功能
为 MCP（Model Context Protocol）连接的会话管理提供自定义超时（主要针对 `StdioServerParameters`），解决原生 ADK 超时硬编码的问题。

---

### 1.1 `__init__`

- **功能**：初始化自定义会话管理器实例。
- **输入**：
  - `connection_params`：连接参数（可以是 StdioServerParameters/SseServerParams/StreamableHTTPServerParams）。
  - `errlog`：错误日志输出流，默认为 `sys.stderr`。
- **处理逻辑**：
  - 保存连接参数和错误日志。
  - 初始化退出栈和会话为 `None`。
- **输出**：无，创建实例并设置初始状态。

---

### 1.2 `async def create_session(self) -> ClientSession`

- **功能**：创建 MCP 客户端会话，并针对 StdioServerParameters 应用自定义超时。
- **输入**：无（使用类实例属性）。
- **处理逻辑**：
  1. 如果已有会话，直接返回。
  2. 初始化异步退出栈（清理资源用）。
  3. 根据连接参数类型，分别调用对应的客户端初始化方法：
     - 若为 StdioServerParameters，则调用 `stdio_client`，后续应用自定义超时。
     - 若为 SseServerParams，则调用 `sse_client`。
     - 若为 StreamableHTTPServerParams，则调用 `streamablehttp_client`。
     - 否则抛出异常。
  4. 进入客户端的异步上下文，获得 transports。
  5. 对 StdioServerParameters，创建 ClientSession 时设置 `read_timeout_seconds` 为自定义值（180 秒）。
  6. 其他类型用默认逻辑创建 ClientSession。
  7. 初始化会话，并保存到实例属性。
- **输出**：返回已初始化的会话对象 `ClientSession`。

---

### 1.3 `async def close(self)`

- **功能**：关闭会话并清理资源。
- **输入**：无。
- **处理逻辑**：
  1. 若有退出栈，执行异步关闭。
  2. 关闭过程中异常会记录但不阻塞流程。
  3. 清空退出栈和会话引用。
- **输出**：无。

---

## 2. CustomMCPToolset 类

### 主要功能
重载默认 MCP 工具集，使用自定义会话管理器，从而支持自定义超时逻辑。

---

### 2.1 `__init__`

- **功能**：初始化工具集，替换原生 MCPToolset 的会话管理器。
- **输入**：
  - `connection_params`：连接参数。
  - `tool_filter`：工具筛选条件，可选。
  - `errlog`：错误日志流，默认 `sys.stderr`。
- **处理逻辑**：
  1. 直接调用 MCPToolset 父类的初始化（跳过 MCPToolset 的默认初始化，避免原生会话管理器被创建）。
  2. 用自定义会话管理器 `CustomMcpSessionManager` 替换原有管理器。
  3. 初始化工具配置、加载状态、关闭状态等属性。
- **输出**：无。

---

### 2.2 `@property def _session(self)` 和 `@_session.setter`

- **功能**：为工具集提供统一的会话访问和设置接口，代理到自定义会话管理器。
- **输入**：
  - getter：无。
  - setter：需要设置的新会话对象。
- **处理逻辑**：
  - getter：返回会话管理器中的 `_session`。
  - setter：将新会话对象赋值给会话管理器的 `_session` 属性。
- **输出**：
  - getter：返回当前会话实例或 None。
  - setter：无。

---

## 总结要点

- 该模块通过继承和方法重载，解决了 ADK 对 MCP 连接超时的硬编码限制，允许开发者根据实际需求调整超时（如模型下载、TTS 操作）。
- 主要涉及会话的创建、初始化和清理过程，兼容原有工具集的调用方式。
- 输入参数灵活，支持多种 MCP 连接类型，处理时有异常保护，保障资源安全释放。
- 输出主要为已初始化的 MCP 客户端会话或工具集实例，便于后续进行业务逻辑调用。

如需具体代码片段或用法建议，请随时告知！

---

下面是对 `ui/a2a_app.py` 的代码执行流程和主要函数的功能（涵盖入参、核心业务逻辑、出参）的简明分步说明：

---

## 一、整体执行流程

1. **入口**：`main()` 是应用入口，通过 `if __name__ == "__main__": main()` 启动 Streamlit Web UI。
2. **环境初始化**：
   - 加载环境变量（`load_dotenv()`），配置 Host Agent 地址等参数。
   - 初始化 Streamlit 的 session_state（如会话ID、历史、音频文件等）。
3. **UI 展示**：
   - 设置页面标题、说明、侧边栏（会话、架构、音频展示）。
   - 展示历史消息和工具交互。
   - 用户输入消息后，调用异步 A2A 交互流程。

---

## 二、核心函数功能

### 1. `create_send_message_payload`

- **入参**：
  - `text: str` 用户输入的消息文本
  - `task_id: str | None` 任务ID（可选）
  - `context_id: str | None` 会话上下文ID（可选）
- **业务逻辑**：
  - 构造符合 A2A 协议的消息体（包括用户角色、文本、messageId）。
  - 自动补全 context_id 以保持会话连续性。
  - 按需插入 task_id、context_id 字段。
- **出参**：
  - 返回 dict 格式的消息 payload。

---

### 2. `send_message_to_agent`

- **入参**：
  - `client: A2AClient` A2A 客户端实例
  - `text: str` 用户输入内容
  - `context_id: str | None` 会话上下文ID（可选）
- **业务逻辑**：
  - 调用 `create_send_message_payload` 构造消息。
  - 封装成 `SendMessageRequest`，通过 A2AClient 发送。
  - 解析 agent 返回结构，提取 `taskId`、即时回复文本（如有）、会话上下文ID。
  - 将即时回复和 contextId 存入 `st.session_state` 以便后续流程使用。
  - 错误处理：异常时提示错误信息。
- **出参**：
  - 返回 `taskId`（str），失败时返回 `None`。

---

### 3. `poll_for_task_completion`

- **入参**：
  - `client: A2AClient` A2A 客户端实例
  - `task_id: str` 要轮询的任务ID
- **业务逻辑**：
  - 如果 session_state 有即时回复，直接返回结果。
  - 否则，循环 MAX_RETRIES 次轮询 agent 任务状态（每次间隔 RETRY_DELAY 秒）。
  - 任务完成（`completed`）时解析返回 artifacts（如文本、音频URL），失败时返回错误信息。
  - 超时则返回超时提示。
- **出参**：
  - 返回 dict，包含 `final_response`, `tool_calls`, `tool_responses`, `audio_url`, `success` 等字段。

---

### 4. `create_a2a_client`

- **入参**：无
- **业务逻辑**：
  - 用 httpx 异步客户端连接 HOST_AGENT_A2A_URL。
  - 通过 A2A SDK 获取 A2AClient 实例。
  - 异常处理与用户提示。
- **出参**：
  - 返回 A2AClient 实例，失败时返回 None。

---

### 5. `run_agent_logic_a2a`

- **入参**：
  - `prompt: str` 用户输入消息
- **业务逻辑**：
  - 创建 A2AClient。
  - 调用 `send_message_to_agent`，获取 taskId。
  - 调用 `poll_for_task_completion`，获取最终结果。
  - 错误处理与用户提示。
- **出参**：
  - 返回结果 dict（同 `poll_for_task_completion`）。

---

### 6. UI 相关辅助函数

- `initialize_session_state`：初始化 Streamlit 会话变量。
- `display_tool_calls`/`display_tool_responses`：展示工具调用和结果。
- `main`：页面布局、会话历史、用户输入、消息处理、UI渲染。

---

## 三、典型交互流程（主线）

1. 用户输入消息（如“请帮我搜索Notion”）。
2. UI将消息加入会话历史，并显示到页面。
3. 通过 `asyncio.run(run_agent_logic_a2a(prompt))` 调用 Host Agent：
   - 建立连接
   - 消息发送，获得任务ID
   - 轮询任务状态，获取最终文本或音频结果
4. 结果展示到页面，并更新会话历史、音频列表等。

---

## 总结

- **模块化**：各功能分离，便于维护和扩展。
- **异步操作**：适用于轮询和网络请求场景，提升响应效率。
- **会话管理**：通过 Streamlit session_state 保持用户数据连贯性。
- **错误处理**：用户界面友好提示，便于排查问题。

如需某个函数的详细代码解读或优化建议，可随时补充说明！

---

下面是对 `ui/app.py` 主线流程及核心类/函数的作用、入参、出参和中间业务逻辑的分步说明，便于开发者快速理解和复用：

---

## 一、主线执行流程

1. **入口函数**：`main()`  
   - Streamlit 应用启动，设置页面参数并初始化 Runner/会话。
   - 展示会话历史和音频，处理用户输入，调用智能体核心流程。

2. **会话与 Runner 初始化**  
   - 通过 `get_adk_runner()` 创建并缓存 ADK Runner 实例，保证会话与智能体上下文持久。
   - 通过 `initialize_session_state()` 初始化 Streamlit 会话变量（如 session_id、历史、音频列表）。

3. **用户交互处理**  
   - 用户输入 prompt，加入历史，并触发 agent 处理流程。
   - 通过异步 `run_agent_logic()` 获取结果并展示。

---

## 二、核心类/函数作用及参数说明

### 1. `get_adk_runner()`

- **作用**：初始化并缓存 ADK Runner，保证每个用户 session 只创建一次。
- **入参**：无
- **出参**：`Runner` 实例（已绑定 host_agent、session_service、app_name）
- **业务逻辑**：
  - 创建 InMemorySessionService（内存会话管理）
  - 调用 `create_host_agent()` 获取主 Agent
  - 实例化 Runner，作为核心智能体运行器

---

### 2. `initialize_session_state()`

- **作用**：初始化 Streamlit 的 session_state 变量，保证 UI 状态同步。
- **入参**：无
- **出参**：无（直接修改 st.session_state）
- **业务逻辑**：
  - 生成唯一 session_id
  - 初始化对话历史和音频文件列表

---

### 3. `run_agent_logic(prompt: str, session_id: str)`

- **作用**：主业务逻辑，处理用户输入，驱动 Host Agent 协同并返回结果。
- **入参**：
  - `prompt`：用户输入的消息文本
  - `session_id`：当前会话唯一标识
- **出参**：
  - dict，包含 `final_response`、`tool_calls`、`tool_responses`、`audio_url`、`success`
- **业务逻辑**：
  1. 获取 Runner 实例（缓存）
  2. 若会话未初始化，调用 Runner 的 session_service 创建会话
  3. 异步运行 Runner，传入用户 prompt
  4. 按事件流处理 Agent 返回内容：
     - 收集工具调用（function_call）、工具响应（function_response）、音频URL
     - 判断是否为最终回复、拼接文本
  5. 返回结构化结果，供 UI 展示

---

### 4. `display_tool_calls(tool_calls: List[Dict[str, Any]])`  
### 5. `display_tool_responses(tool_responses: List[Dict[str, Any]])`

- **作用**：在 UI 展示工具调用和响应（如 Notion 查询、音频生成）。
- **入参**：工具调用或响应的列表
- **出参**：无（直接渲染 Streamlit UI）
- **业务逻辑**：遍历并格式化显示工具相关信息

---

### 6. `main()`

- **作用**：Streamlit 应用入口，组织页面结构和交互逻辑。
- **入参**：无
- **出参**：无
- **业务逻辑**：
  1. 设置页面参数、初始化 Runner 和 session_state
  2. 展示侧边栏（会话ID、音频列表、会话重置按钮）
  3. 展示历史消息和工具交互
  4. 处理用户输入：加入历史、触发 agent 处理、展示结果（文本、工具、音频）
  5. 支持音频结果的持久化和多轮对话

---

## 三、业务流程梳理（开发者视角）

1. 用户输入消息后，UI 通过 `main()` 将消息送入对话历史，并调用 `run_agent_logic()`。
2. `run_agent_logic()` 用当前会话ID驱动 Runner 异步协同 Host Agent，收集事件流中的所有工具调用/响应和最终文本/音频结果。
3. 结果被格式化后，UI 展示文本、工具调用与响应、音频，历史消息实时迭代。
4. 会话和 Runner 完全持久化，支持多轮交互和上下文记忆（基于 Streamlit 的缓存和 session_state）。

---

### 推荐做法与技术要点

- **会话唯一性**：每个用户 session 独立，防止上下文污染。
- **异步事件驱动**：利用 asyncio 和事件流，提升响应效率，支持复杂任务（如长文本分析、音频生成）。
- **工具链扩展**：工具调用与响应结构化，便于后续增加更多子 agent 或外部服务。

如需针对某一部分代码、交互细节或性能优化的深度解析，请告知具体需求！