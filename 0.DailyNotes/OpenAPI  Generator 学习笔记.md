---
aliases:
date: 2025-09-05 14:48
tags:
source:
  - https://zread.ai/OpenAPITools/openapi-generator
---
OpenAPI Generator 是现代 API 开发的必备工具，使团队能够：

- 使用 OpenAPI 规范优先设计 API
- 在多个平台生成一致、高质量的代码
- 保持 API 契约与实现之间的同步
- 加速开发周期并减少手动错误

无论您是构建简单的微服务还是复杂的分布式系统，OpenAPI Generator 都可以帮助简化 API 开发工作流，并确保整个技术栈的一致性。



### 多语言支持

该工具支持令人印象深刻的语言和框架范围：

|类别|示例|
|---|---|
|**客户端生成器**|Java、Python、TypeScript、C#、Go、Ruby、PHP、Swift、Kotlin、Rust 等多种语言|
|**服务器生成器**|Java Spring、ASP.NET Core、Node.js、Go Gin、PHP Laravel、Python Flask 等|
|**文档生成器**|HTML、Markdown、AsciiDoc、Confluence Wiki、PlantUML|

## 生成客户端库
>在微服务架构中，服务需要通过明确定义的API相互通信，此时客户端生成器尤其有价值。
[Client Generators \| OpenAPITools/openapi-generator \| Zread](https://zread.ai/OpenAPITools/openapi-generator/5-client-generators)

```Bash
openapi-generator generate \
  -i petstore.yaml \
  -g java \
  -o ./petstore-java-client \
  --additional-properties= \
    library=jersey2,\
    dateLibrary=java8,\
    invokerPackage=com.example.petstore.client,\
    apiPackage=com.example.petstore.client.api,\
    modelPackage=com.example.petstore.client.model,\
    artifactId=petstore-client,\
    artifactVersion=1.0.0
```

生成的客户端包括：

- 所有API模式的模型类
- 每个端点包含方法的API类
- 身份验证和基本路径的配置类
- 构建文件（Maven的pom.xml）
- 文档和示例


## 学习曲线

用户经常提到陡峭的学习曲线，特别是在以下方面：

- **模板定制**：理解 Mustache 模板和生成器的内部模型
- **配置复杂性**：导航数百个生成器特定选项
- **调试挑战**：当出现问题时，通过多个层（规范 → 解析器 → 模板 → 生成代码）追踪问题

正如一位用户所说："本质上我们必须在集成的两端进行迭代，有点像试图将方钉插入圆孔，然后逐渐改变钉和孔的形状直到它们匹配。"
社区的声音表明几个关键要点：

1. **对于企业用户**：OpenAPI Generator 是一个改变游戏规则的工具，它以前所未有的方式实现了规模化 API 开发
2. **对于个体开发者**：这是一个需要耐心和调试技能的强大工具
3. **对于生态系统**：这是一个需要持续投资和改进的关键基础设施


## 支持的语言和框架

OpenAPI Generator 拥有令人印象深刻的语言支持，使其成为最通用的代码生成工具之一：

### 客户端生成器

流行的客户端生成器包括：

- **Java** - 支持各种 HTTP 客户端（RestTemplate、WebClient、OkHttp 等）
- **JavaScript/TypeScript** - 包括 Angular、React、Node.js 等框架
- **Python** - 支持 asyncio、requests 和其他库
- **Go** - 简洁、地道的 Go 客户端
- **C#/.NET** - 支持 .NET Framework、.NET Core 和 .NET Standard
- **PHP** - 支持 Guzzle 和其他 HTTP 客户端
- **Ruby** - 简洁的 Ruby 客户端
- **Swift** - 用于 iOS 和 macOS 开发
- **还有更多...** - 总共超过 50 个客户端生成器

### 服务器生成器

对于服务器端实现，您可以为以下内容生成存根：

- **Java** - Spring、Micronaut、Helidon、JAX-RS 实现
- **Node.js** - Express、NestJS 和其他框架
- **Python** - Flask、FastAPI、aiohttp
- **Go** - 标准库、Gin、Echo
- **C#** - ASP.NET Core、Azure Functions
- **PHP** - Laravel、Symfony、Slim
- **还有更多...** - 超过 40 个服务器生成器

### 文档和其他生成器

除了代码，OpenAPI Generator 还可以创建：

- **HTML 文档** - 交互式 API 文档
- **Markdown/AsciiDoc** - 用于包含在项目文档中
- **Postman 集合** - 用于 API 测试
- **Protocol Buffer 架构** - 用于 gRPC 集成
- **数据库架构** - MySQL、PostgreSQL 架构定义

---

在“服务器端实现生成存根（Stub）”的语境中，**Stub 指“服务器端基础代码框架/骨架”**，是 OpenAPI Generator 根据 OpenAPI 规范（API 契约）自动生成的、具备 API 核心结构但未包含具体业务逻辑的代码模板。它的核心作用是“搭好 API 的‘架子’”，让开发者无需手动编写重复的 API 结构代码，直接聚焦于业务逻辑实现。

### 具体来说，服务器端 Stub 包含哪些内容？

以“基于 FastAPI（Python）生成的服务器 Stub”为例，它会自动生成以下关键部分（完全匹配 OpenAPI 规范中定义的接口、参数、响应格式）：

1. **API 路由定义**\
   自动生成规范中声明的接口路径（如 `/api/users/{user_id}`）、请求方法（GET/POST/PUT 等），并绑定到对应的处理函数，无需手动写 `@app.get("/api/users/{user_id}")` 这类路由代码。

2. **请求/响应模型（数据结构）**\
   根据规范中定义的“请求参数格式”“响应数据格式”，自动生成对应的类（如 Python 的 `Pydantic BaseModel`、Java 的 `POJO`）。例如规范中要求“创建用户需传 `name`（字符串）和 `age`（整数）”，Stub 会直接生成：
   ```python
   from pydantic import BaseModel
   class CreateUserRequest(BaseModel):
       name: str
       age: int
   ```

3. **接口处理函数“空实现”**\
   生成对应每个接口的处理函数，但仅包含函数定义（参数、返回值类型已按规范约束），内部无业务逻辑（通常用“占位代码”提示开发者补充）。例如：
   ```python
   def get_user(user_id: int) -> UserResponse:
       # TODO: 开发者需补充“查询数据库、返回用户信息”的业务逻辑
       pass  # 占位，待实现
   ```

4. **框架配置与依赖关联**\
   自动生成适配目标框架的基础配置（如 FastAPI 的 `app = FastAPI()` 初始化、Spring Boot 的 `@RestController` 注解、Gin 的路由注册逻辑），以及必要的依赖引入代码（如导入框架库、数据模型类），确保 Stub 能直接在框架中运行。

### 为什么需要服务器端 Stub？核心价值是什么？

1. **消除“API 契约与代码不一致”问题**\
   Stub 完全由 OpenAPI 规范生成，避免了“开发者手动写接口时写错路径、参数类型不匹配、响应格式不符”等问题，确保代码与 API 设计文档100%对齐。

2. **大幅减少“样板代码”工作量**\
   无需手动编写路由、数据模型、函数定义等重复结构代码（尤其是复杂 API 场景），原本几小时的“搭架子”工作，生成 Stub 仅需几分钟，开发者可直接投入业务逻辑开发（如查库、计算、调用其他服务）。

3. **降低跨框架/跨语言开发门槛**\
   即使开发者不熟悉某框架（如从 Flask 转 FastAPI），Stub 也会自动生成该框架的标准代码结构（如 FastAPI 的 `Depends` 依赖注入、Spring 的 `@RequestParam` 注解），开发者只需按“占位提示”补充业务逻辑即可。

### 对比：服务器 Stub 与“完整服务器代码”的区别？

| 维度   | 服务器 Stub（存根）       | 完整服务器代码           |
| ---- | ------------------ | ----------------- |
| 业务逻辑 | 无（仅占位，待开发者补充）      | 包含完整业务逻辑（查库、计算等）  |
| 核心内容 | API 结构（路由、模型、函数定义） | 结构 + 业务逻辑 + 部署配置  |
| 生成方式 | OpenAPI 规范自动生成     | Stub 基础上手动补充 + 配置 |
| 作用   | “搭架子”，定结构          | “能运行”，实现完整功能      |

简单说：**Stub 是“半成品框架”，是开发者实现服务器功能的“起点”，而非“终点”**。
