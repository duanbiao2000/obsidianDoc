---
aliases: null
date: 2025-10-30 11:45
tags: null
source: null
update: null
rating: null
---

基于代码中的注释和结构，这四个概念是 GitHub Copilot 生态系统中的不同组件类型：

## `prompts`（提示模板）

- **作用**：预定义的提示词模板，用于特定开发场景和任务
- **特点**：
  - 包含特定模式、模型和工具集的提示文本
  - 可通过 `/prompt-name` 在 VS Code 聊天中直接调用
  - 支持通过命令面板运行或在文件中点击运行按钮执行

## `instructions`（自定义指令）

- **作用**：针对特定技术栈和编码实践的团队/项目级指令，用于增强 Copilot 行为
- **特点**：
  - 通常放置在 `.github/copilot-instructions.md` 文件中
  - 可创建任务特定的 `.github/instructions/.instructions.md` 文件
  - 安装后会自动影响 Copilot 的行为

## `chatmodes`（自定义聊天模式）

- **作用**：定义 Copilot Chat 的特定行为和工具，提供上下文感知的辅助
- **特点**：
  - 为特定任务或工作流定制聊天行为
  - 需要导入到 VS Code 设置中才能使用
  - 通过 VS Code Chat 界面访问和选择

## `agents`（自定义代理）

- **作用**：通过简单的基于文件的配置来"专业化"Copilot 编码代理（CCA）
- **特点**：
  - 可能需要一个或多个 MCP 服务器支持
  - 通过 VS Code Chat 界面、CCA 分配或 Copilot CLI 使用
  - 可访问配置的 MCP 服务器提供的工具

## 比较总结

| 类型             | 作用范围  | 使用方式    | 配置复杂度 |
| -------------- | ----- | ------- | ----- |
| `prompts`      | 特定任务  | 直接调用执行  | 低     |
| `instructions` | 项目级行为 | 自动应用    | 低     |
| `chatmodes`    | 聊天交互  | 手动切换    | 中     |
| `agents`       | 专业化代理 | 需要服务器支持 | 高     |

这四种组件构成了一个完整的 Copilot 定制化体系，从简单提示到复杂代理，满足不同层次的定制需求。



以下是对 GitHub Copilot “Awesome Copilot” 项目五大模块的功能和作用分析：

- **Awesome Agents（代理）**  
    作用：这类 agent 是专为特定工作流和工具设计的 Copilot 定制代理，能接入 MCP Server。  
    功能：通过集成 MCP（Meta Copilot Platform）服务器，扩展 Copilot 能力，实现自动分配任务、自动化处理多种工作流（如 DevOps、数据库、安全、云原生等），让 Copilot 可针对具体场景智能响应和支持工具链。例如在 VS Code、命令行或 Copilot Agent Session 中激活后可直接分派更复杂的任务，提升效率和专业性。[github](https://github.com/duanbiao2000/awesome-copilot)​
    
- **Awesome Prompts（提示词）**  
    作用：为 Copilot 提供各种任务细分、场景化的高质量 prompt。  
    功能：通过 `/` 命令或合集，用户可以快速调用这些预设提示，实现代码生成、文档、测试等的高效自动化。同时能规范 Copilot 对应输入，提高输出针对性和准确性，非常适合开发者在不同语言或框架下的细粒度高效开发。[github](https://github.com/duanbiao2000/awesome-copilot)​
    
- **Awesome Instructions（指令集）**  
    作用：自动应用于相关文件，实现公认的代码标准和最佳实践。  
    功能：可为不同类型的工程文件、项目目录等自动指定 Coding Standard，并在编码过程中为 Copilot 提供附加指导。这样保证项目始终遵循社区最佳实践和风格一致性，减少低级错误，方便团队协作。[github](https://github.com/duanbiao2000/awesome-copilot)​
    
- **Awesome Chat Modes（聊天模式）**  
    作用：为 Copilot 提供多种 AI Persona，对应不同角色和业务场景。  
    功能：激活对应模式后，Copilot 可扮演如架构师、DBA、安全专家等角色，为用户提供针对性的专家知识和建议。适合在协作、咨询、方案讨论等场景中，为各类技术决策和问题提供结构化、专业的智能对话体验。[github](https://github.com/duanbiao2000/awesome-copilot)​
    
- **Awesome Collections（合集）**  
    作用：主题化整理上面所有资源，形成按场景分组的工具包。  
    功能：将 Prompts、Instructions、Chat Modes、Agents 按技术领域或工作流进行打包和分类，方便用户查找、引入和批量配置。例如 DevOps、云原生、前端开发等合集，帮助提升项目启动和日常工作效率，保有最高复用性。[github](https://github.com/duanbiao2000/awesome-copilot)​
    

**总结**：  
该项目通过“代理、提示词、指令集、聊天模式、合集”五大板块，实现 Copilot 的深度专业化扩展。开发者可根据自身技术栈和场景，快速获得智能化、集成化、高效化的 Copilot AI 增强体验。[github](https://github.com/duanbiao2000/awesome-copilot)​

1. [https://github.com/duanbiao2000/awesome-copilot](https://github.com/duanbiao2000/awesome-copilot)

---

当前页面的 `testing-automation.collection.yml` 工作流详解如下：

- **核心作用**：本 collection 专为覆盖测试编写与自动化场景，包括单元测试、集成测试、端到端测试及 TDD（测试驱动开发）等，为开发者全面提供测试设计、自动化、AI 工程安全等多环节智能辅助。
    

**主要内容分组说明：**

- **TDD Chat Modes（TDD 聊天模式）**
    
    - `tdd-red.chatmode.md`：TDD“Red”阶段，聚焦编写失败测试用例，引导开发者明确需求和测试目标。
        
    - `tdd-green.chatmode.md`：TDD“Green”阶段，提醒只实现让测试通过的最简单代码，控流程进度。
        
    - `tdd-refactor.chatmode.md`：TDD“Refactor”阶段，专注提示重构代码、优化测试和实现的结构。
        
    - `playwright-tester.chatmode.md`：辅助 Playwright 测试工具用例生成与调试，适合端到端测试。
        
- **Testing Instructions（测试标准指导）**
    
    - `playwright-typescript.instructions.md`：TypeScript + Playwright 测试开发规范与最佳实践引导。
        
    - `playwright-python.instructions.md`：Python + Playwright 自动化测试使用说明，实现多语言测试一致性。
        
- **Testing Prompts（测试生成与分析提示）**
    
    - `playwright-explore-website.prompt.md`：用于分析和探查网站交互流程，提升自动化脚本覆盖率。
        
    - `playwright-generate-test.prompt.md`：一键生成 Playwright 测试脚本，加速端到端测试开发。
        
    - `csharp-nunit.prompt.md`：专为 C# NUnit 框架场景提供有用的测试用例/代码生成提示。
        
    - `java-junit.prompt.md`：面向 Java JUnit 测试框架的代码和用例编写指令。
        
    - `ai-prompt-engineering-safety-review.prompt.md`：专注于 AI prompt 的安全性工程审核，适合 AI 驱动场景下的测试合规性评审。
        

**应用场景举例**：

- 支持前后端、端到端功能全流程自动化测试环境搭建。
    
- 推动团队采用 TDD/BDD 开发流程，全流程自动规范和安全检测。
    
- 助力跨语言、多框架（如 Python/TS/C#/Java）的测试生成、复用与协同。
    

本 collection 打通测试自动化工具链（如 Playwright、NUnit、JUnit）和现代 AI 安全标准，为项目提供一站式智能测试解决方案。[github](https://github.com/duanbiao2000/awesome-copilot/blob/main/collections/testing-automation.collection.yml)​

1. [https://github.com/duanbiao2000/awesome-copilot/blob/main/collections/testing-automation.collection.yml](https://github.com/duanbiao2000/awesome-copilot/blob/main/collections/testing-automation.collection.yml)

在该句子中，“enabler”指的是能够推动或支持某个主要功能实现的辅助性功能或条件。它通常用于敏捷开发或产品规划语境中，表示那些虽然不是最终交付给用户的核心功能，但为实现更高层次的功能目标所必需的支撑性能力。因此，“feature or enabler”这一固定搭配中的“enabler”意指为实现关键功能而必须先完成的使能性需求或技术准备，即帮助主功能得以实现的基础性组件或条件。