---
title: BMAD-METHOD/docs/user-guide.md at main · bmad-code-org/BMAD-METHOD
source: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/user-guide.md
author:
  - "[[GitHub]]"
published:
date: 2025-08-17
description: Breakthrough Method for Agile Ai Driven Development - BMAD-METHOD/docs/user-guide.md at main · bmad-code-org/BMAD-METHOD
tags:
  - clippings
---
[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/bmad-code-org/BMAD-METHOD/tree/main?resume=1)

[feat: transform QA agent into Test Architect with advanced quality ca… (](https://github.com/bmad-code-org/BMAD-METHOD/commit/0b61175d98e6def508cc82bb4539e7f37f8f6e1a)

[0b61175](https://github.com/bmad-code-org/BMAD-METHOD/commit/0b61175d98e6def508cc82bb4539e7f37f8f6e1a) ·

本指南将帮助您理解并有效使用 BMad 方法进行敏捷的 AI 驱动规划和开发。

## BMad 计划和执行工作流程

首先，这是完整的标准绿地规划 + 执行工作流程。棕地非常相似，但建议先了解这个绿地，即使是在处理棕地项目之前的简单项目。BMad 方法需要安装到新项目文件夹的根目录。对于规划阶段，您可以选择使用强大的 Web 代理来执行它，这可能会以在某些代理工具中提供您自己的 API 密钥或积分时完成所需成本的一小部分来获得更高质量的结果。对于规划，强大的思维模型和更大的背景 - 以及与代理商合作将获得最佳结果。

如果您要将 BMad 方法用于棕地项目（现有项目），请查看 **[在棕地工作](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/working-in-the-brownfield.md)** 。

如果下图未呈现，请将 Markdown All in One 以及 Markdown 预览版 Mermaid 支持插件安装到 VSCode（或其中一个分叉的克隆）。使用这些插件，如果您在打开时右键单击选项卡，应该有一个打开预览选项，或查看 IDE 文档。

在开发开始之前，BMad 遵循结构化的规划工作流程，该工作流程最好在 Web UI 中完成，以提高成本效益：

```
graph TD
    A["Start: Project Idea"] --> B{"Optional: Analyst Research"}
    B -->|Yes| C["Analyst: Brainstorming (Optional)"]
    B -->|No| G{"Project Brief Available?"}
    C --> C2["Analyst: Market Research (Optional)"]
    C2 --> C3["Analyst: Competitor Analysis (Optional)"]
    C3 --> D["Analyst: Create Project Brief"]
    D --> G
    G -->|Yes| E["PM: Create PRD from Brief (Fast Track)"]
    G -->|No| E2["PM: Interactive PRD Creation (More Questions)"]
    E --> F["PRD Created with FRs, NFRs, Epics & Stories"]
    E2 --> F
    F --> F2{"UX Required?"}
    F2 -->|Yes| F3["UX Expert: Create Front End Spec"]
    F2 -->|No| H["Architect: Create Architecture from PRD"]
    F3 --> F4["UX Expert: Generate UI Prompt for Lovable/V0 (Optional)"]
    F4 --> H2["Architect: Create Architecture from PRD + UX Spec"]
    H --> Q{"Early Test Strategy? (Optional)"}
    H2 --> Q
    Q -->|Yes| R["QA: Early Test Architecture Input on High-Risk Areas"]
    Q -->|No| I
    R --> I["PO: Run Master Checklist"]
    I --> J{"Documents Aligned?"}
    J -->|Yes| K["Planning Complete"]
    J -->|No| L["PO: Update Epics & Stories"]
    L --> M["Update PRD/Architecture as needed"]
    M --> I
    K --> N["📁 Switch to IDE (If in a Web Agent Platform)"]
    N --> O["PO: Shard Documents"]
    O --> P["Ready for SM/Dev Cycle"]

    style A fill:#f5f5f5,color:#000
    style B fill:#e3f2fd,color:#000
    style C fill:#e8f5e9,color:#000
    style C2 fill:#e8f5e9,color:#000
    style C3 fill:#e8f5e9,color:#000
    style D fill:#e8f5e9,color:#000
    style E fill:#fff3e0,color:#000
    style E2 fill:#fff3e0,color:#000
    style F fill:#fff3e0,color:#000
    style F2 fill:#e3f2fd,color:#000
    style F3 fill:#e1f5fe,color:#000
    style F4 fill:#e1f5fe,color:#000
    style G fill:#e3f2fd,color:#000
    style H fill:#f3e5f5,color:#000
    style H2 fill:#f3e5f5,color:#000
    style Q fill:#e3f2fd,color:#000
    style R fill:#ffd54f,color:#000
    style I fill:#f9ab00,color:#fff
    style J fill:#e3f2fd,color:#000
    style K fill:#34a853,color:#fff
    style L fill:#f9ab00,color:#fff
    style M fill:#fff3e0,color:#000
    style N fill:#1a73e8,color:#fff
    style O fill:#f9ab00,color:#fff
    style P fill:#34a853,color:#fff
```

**关键过渡点** ：一旦采购订单确认文档对齐，您必须从 Web UI 切换到 IDE 才能开始开发工作流程：

1. 将 **文档复制到项目：** 确保 `docs/prd.md` 和 `docs/architecture.md` 位于项目的 docs 文件夹中（或您可以在安装过程中指定的自定义位置）
2. 切换 **到 IDE：** 在您首选的 Agentic IDE 中打开您的项目
3. **文档分片** ：使用 PO 代理对 PRD 进行分片，然后对架构进行分片
4. **开始开发** ：开始接下来的核心开发周期

#### 规划工件（标准路径）

```
PRD              → docs/prd.md
Architecture     → docs/architecture.md
Sharded Epics    → docs/epics/
Sharded Stories  → docs/stories/
QA Assessments   → docs/qa/assessments/
QA Gates         → docs/qa/gates/
```

### 核心开发周期 （IDE）

一旦规划完成并对文档进行分片，BMad 就会遵循结构化的开发工作流程：

```
graph TD
    A["Development Phase Start"] --> B["SM: Reviews Previous Story Dev/QA Notes"]
    B --> B2["SM: Drafts Next Story from Sharded Epic + Architecture"]
    B2 --> S{"High-Risk Story? (Optional)"}
    S -->|Yes| T["QA: *risk + *design on Draft Story"]
    S -->|No| B3
    T --> U["Test Strategy & Risk Profile Created"]
    U --> B3{"PO: Validate Story Draft (Optional)"}
    B3 -->|Validation Requested| B4["PO: Validate Story Against Artifacts"]
    B3 -->|Skip Validation| C{"User Approval"}
    B4 --> C
    C -->|Approved| D["Dev: Sequential Task Execution"]
    C -->|Needs Changes| B2
    D --> E["Dev: Implement Tasks + Tests"]
    E --> V{"Mid-Dev QA Check? (Optional)"}
    V -->|Yes| W["QA: *trace or *nfr for Early Validation"]
    V -->|No| F
    W --> X["Dev: Address Coverage/NFR Gaps"]
    X --> F["Dev: Run All Validations"]
    F --> G["Dev: Mark Ready for Review + Add Notes"]
    G --> H{"User Verification"}
    H -->|Request QA Review| I["QA: Test Architect Review + Quality Gate"]
    H -->|Approve Without QA| M["IMPORTANT: Verify All Regression Tests and Linting are Passing"]
    I --> J["QA: Test Architecture Analysis + Active Refactoring"]
    J --> L{"QA Decision"}
    L -->|Needs Dev Work| D
    L -->|Approved| M
    H -->|Needs Fixes| D
    M --> N["IMPORTANT: COMMIT YOUR CHANGES BEFORE PROCEEDING!"]
    N --> Y{"Gate Update Needed?"}
    Y -->|Yes| Z["QA: *gate to Update Status"]
    Y -->|No| K
    Z --> K["Mark Story as Done"]
    K --> B

    style A fill:#f5f5f5,color:#000
    style B fill:#e8f5e9,color:#000
    style B2 fill:#e8f5e9,color:#000
    style S fill:#e3f2fd,color:#000
    style T fill:#ffd54f,color:#000
    style U fill:#ffd54f,color:#000
    style B3 fill:#e3f2fd,color:#000
    style B4 fill:#fce4ec,color:#000
    style C fill:#e3f2fd,color:#000
    style D fill:#e3f2fd,color:#000
    style E fill:#e3f2fd,color:#000
    style V fill:#e3f2fd,color:#000
    style W fill:#ffd54f,color:#000
    style X fill:#e3f2fd,color:#000
    style F fill:#e3f2fd,color:#000
    style G fill:#e3f2fd,color:#000
    style H fill:#e3f2fd,color:#000
    style I fill:#f9ab00,color:#fff
    style J fill:#ffd54f,color:#000
    style K fill:#34a853,color:#fff
    style L fill:#e3f2fd,color:#000
    style M fill:#ff5722,color:#fff
    style N fill:#d32f2f,color:#fff
    style Y fill:#e3f2fd,color:#000
    style Z fill:#ffd54f,color:#000
```

## Prerequisites

Before installing BMad Method, ensure you have:

- **Node.js** ≥ 18, **npm** ≥ 9
- **Git** installed and configured
- **(Optional)** VS Code with "Markdown All in One" + "Markdown Preview Mermaid Support" extensions

## Installation

### Optional

If you want to do the planning on the web with Claude (Sonnet 4 or Opus), Gemini Gem (2.5 Pro), or Custom GPTs:

1. Navigate to `dist/teams/`
2. Copy `team-fullstack.txt`
3. Create new Gemini Gem or CustomGPT
4. Upload file with instructions: "Your critical operating instructions are attached, do not break character as directed"
5. Type `/help` to see available commands

## Special Agents

There are two BMad agents — in the future they'll be consolidated into a single BMad-Master.

### BMad-Master

This agent can do any task or command that all other agents can do, aside from actual story implementation. Additionally, this agent can help explain the BMad Method when on the web by accessing the knowledge base and explaining anything to you about the process.

If you don't want to bother switching between different agents aside from the dev, this is the agent for you. Just remember that as the context grows, the performance of the agent degrades, therefore it is important to instruct the agent to compact the conversation and start a new conversation with the compacted conversation as the initial message. Do this often, preferably after each story is implemented.

### BMad-Orchestrator

This agent should NOT be used within the IDE, it is a heavyweight, special-purpose agent that utilizes a lot of context and can morph into any other agent. This exists solely to facilitate the teams within the web bundles. If you use a web bundle you will be greeted by the BMad Orchestrator.

#### Dependencies System

Each agent has a YAML section that defines its dependencies:

```
dependencies:
  templates:
    - prd-template.md
    - user-story-template.md
  tasks:
    - create-doc.md
    - shard-doc.md
  data:
    - bmad-kb.md
```

**Key Points:**

- Agents only load resources they need (lean context)
- Dependencies are automatically resolved during bundling
- Resources are shared across agents to maintain consistency

#### Agent Interaction

**In IDE:**

#### Interactive Modes

- **Incremental Mode**: Step-by-step with user input
- **YOLO Mode**: Rapid generation with minimal interaction

## IDE Integration

- **Context Management**: Keep relevant files only in context, keep files as lean and focused as necessary
- **Agent Selection**: Use appropriate agent for task
- **Iterative Development**: Work in small, focused tasks
- **File Organization**: Maintain clean project structure
- **Commit Regularly**: Save your work frequently

### Overview

The QA agent in BMad is not just a "senior developer reviewer" - it's a **Test Architect** with deep expertise in test strategy, quality gates, and risk-based testing. Named Quinn, this agent provides advisory authority on quality matters while actively improving code when safe to do so.

```
@qa *risk {story}       # Assess risks before development
@qa *design {story}     # Create test strategy
@qa *trace {story}      # Verify test coverage during dev
@qa *nfr {story}        # Check quality attributes
@qa *review {story}     # Full assessment → writes gate
```

The documentation uses short forms for convenience. Both styles are valid:

```
*risk    → *risk-profile
*design  → *test-design  
*nfr     → *nfr-assess
*trace   → *trace-requirements (or just *trace)
*review  → *review
*gate    → *gate
```

### Core Capabilities

**When:** After story draft, before development begins (earliest intervention point)

Identifies and assesses implementation risks:

- **Categories**: Technical, Security, Performance, Data, Business, Operational
- **Scoring**: Probability × Impact analysis (1-9 scale)
- **Mitigation**: Specific strategies for each identified risk
- **Gate Impact**: Risks ≥9 trigger FAIL, ≥6 trigger CONCERNS (see `tasks/risk-profile.md` for authoritative rules)

**When:** After story draft, before development begins (guides what tests to write)

Creates comprehensive test strategies including:

- Test scenarios for each acceptance criterion
- Appropriate test level recommendations (unit vs integration vs E2E)
- Risk-based prioritization (P0/P1/P2)
- Test data requirements and mock strategies
- Execution strategies for CI/CD integration

**Example output:**

```
test_summary:
  total: 24
  by_level:
    unit: 15
    integration: 7
    e2e: 2
  by_priority:
    P0: 8 # Must have - linked to critical risks
    P1: 10 # Should have - medium risks
    P2: 6 # Nice to have - low risks
```

**When:** During development (mid-implementation checkpoint)

Maps requirements to test coverage:

- Documents which tests validate each acceptance criterion
- Uses Given-When-Then for clarity (documentation only, not BDD code)
- Identifies coverage gaps with severity ratings
- Creates traceability matrix for audit purposes

**When:** During development or early review (validate quality attributes)

Validates non-functional requirements:

- **Core Four**: Security, Performance, Reliability, Maintainability
- **Evidence-Based**: Looks for actual implementation proof
- **Gate Integration**: NFR failures directly impact quality gates

**When:** After development complete, story marked "Ready for Review"

When you run `@qa *review {story}`, Quinn performs:

- **Requirements Traceability**: Maps every acceptance criterion to its validating tests
- **Test Level Analysis**: Ensures appropriate testing at unit, integration, and E2E levels
- **Coverage Assessment**: Identifies gaps and redundant test coverage
- **Active Refactoring**: Improves code quality directly when safe
- **Quality Gate Decision**: Issues PASS/CONCERNS/FAIL status based on findings

**When:** After review fixes or when gate status needs updating

Manages quality gate decisions:

- **Deterministic Rules**: Clear criteria for PASS/CONCERNS/FAIL
- **Parallel Authority**: QA owns gate files in `docs/qa/gates/`
- **Advisory Nature**: Provides recommendations, not blocks
- **Waiver Support**: Documents accepted risks when needed

**Note:** Gates are advisory; teams choose their quality bar. WAIVED requires reason, approver, and expiry date. See `templates/qa-gate-tmpl.yaml` for schema and `tasks/review-story.md` (gate rules) and `tasks/risk-profile.md` for scoring.

The Test Architect provides value throughout the entire development lifecycle. Here's when and how to leverage each capability:

| **Stage** | **Command** | **When to Use** | **Value** | **Output** |
| --- | --- | --- | --- | --- |
| **Story Drafting** | `*risk` | After SM drafts story | Identify pitfalls early | `docs/qa/assessments/{epic}.{story}-risk-{YYYYMMDD}.md` |
|  | `*design` | After risk assessment | Guide dev on test strategy | `docs/qa/assessments/{epic}.{story}-test-design-{YYYYMMDD}.md` |
| **Development** | `*trace` | Mid-implementation | Verify test coverage | `docs/qa/assessments/{epic}.{story}-trace-{YYYYMMDD}.md` |
|  | `*nfr` | While building features | Catch quality issues early | `docs/qa/assessments/{epic}.{story}-nfr-{YYYYMMDD}.md` |
| **Review** | `*review` | Story marked complete | Full quality assessment | QA Results in story + gate file |
| **Post-Review** | `*gate` | After fixing issues | Update quality decision | Updated `docs/qa/gates/{epic}.{story}-{slug}.yml` |

#### Example Commands

```
# Planning Stage - Run these BEFORE development starts
@qa *risk {draft-story}     # What could go wrong?
@qa *design {draft-story}   # What tests should we write?

# Development Stage - Run these DURING coding
@qa *trace {story}          # Are we testing everything?
@qa *nfr {story}            # Are we meeting quality standards?

# Review Stage - Run when development complete
@qa *review {story}         # Comprehensive assessment + refactoring

# Post-Review - Run after addressing issues
@qa *gate {story}           # Update gate status
```

Quinn enforces these test quality principles:

- **No Flaky Tests**: Ensures reliability through proper async handling
- **No Hard Waits**: Dynamic waiting strategies only
- **Stateless & Parallel-Safe**: Tests run independently
- **Self-Cleaning**: Tests manage their own test data
- **Appropriate Test Levels**: Unit for logic, integration for interactions, E2E for journeys
- **Explicit Assertions**: Keep assertions in tests, not helpers
- **PASS**: All critical requirements met, no blocking issues
- **CONCERNS**: Non-critical issues found, team should review
- **FAIL**: Critical issues that should be addressed (security risks, missing P0 tests)
- **WAIVED**: Issues acknowledged but explicitly accepted by team

### Special Situations

**High-Risk Stories:**

- Always run `*risk` and `*design` before development starts
- Consider mid-development `*trace` and `*nfr` checkpoints

**Complex Integrations:**

- Run `*trace` during development to ensure all integration points tested
- Follow up with `*nfr` to validate performance across integrations

**Performance-Critical:**

- Run `*nfr` early and often during development
- Don't wait until review to discover performance issues

**Brownfield/Legacy Code:**

- Start with `*risk` to identify regression dangers
- Use `*review` with extra focus on backward compatibility

### Best Practices

- **Early Engagement**: Run `*design` and `*risk` during story drafting
- **Risk-Based Focus**: Let risk scores drive test prioritization
- **Iterative Improvement**: Use QA feedback to improve future stories
- **Gate Transparency**: Share gate decisions with the team
- **Continuous Learning**: QA documents patterns for team knowledge sharing
- **Brownfield Care**: Pay extra attention to regression risks in existing systems

Quick reference for where Test Architect outputs are stored:

```
*risk-profile  → docs/qa/assessments/{epic}.{story}-risk-{YYYYMMDD}.md
*test-design   → docs/qa/assessments/{epic}.{story}-test-design-{YYYYMMDD}.md
*trace         → docs/qa/assessments/{epic}.{story}-trace-{YYYYMMDD}.md
*nfr-assess    → docs/qa/assessments/{epic}.{story}-nfr-{YYYYMMDD}.md
*review        → QA Results section in story + gate file reference
*gate          → docs/qa/gates/{epic}.{story}-{slug}.yml
```

BMad includes a personalization system through the `technical-preferences.md` file located in `.bmad-core/data/` - this can help bias the PM and Architect to recommend your preferences for design patterns, technology selection, or anything else you would like to put in here.

When creating custom web bundles or uploading to AI platforms, include your `technical-preferences.md` content to ensure agents have your preferences from the start of any conversation.

## Core Configuration

The `bmad-core/core-config.yaml` file is a critical config that enables BMad to work seamlessly with differing project structures, more options will be made available in the future. Currently the most important is the devLoadAlwaysFiles list section in the yaml.

Define which files the dev agent should always load:

```
devLoadAlwaysFiles:
  - docs/architecture/coding-standards.md
  - docs/architecture/tech-stack.md
  - docs/architecture/project-structure.md
```

You will want to verify from sharding your architecture that these documents exist, that they are as lean as possible, and contain exactly the information you want your dev agent to ALWAYS load into its context. These are the rules the agent will follow.

As your project grows and the code starts to build consistent patterns, coding standards should be reduced to include only the standards the agent still needs enforced. The agent will look at surrounding code in files to infer the coding standards that are relevant to the current task.

## Getting Help

- **Discord Community**: [Join Discord](https://discord.gg/gk8jAdXWmj)
- **GitHub Issues**: [Report bugs](https://github.com/bmadcode/bmad-method/issues)
- **Documentation**: [Browse docs](https://github.com/bmadcode/bmad-method/docs)
- **YouTube**: [BMadCode Channel](https://www.youtube.com/@BMadCode)

## Conclusion

Remember: BMad is designed to enhance your development process, not replace your expertise. Use it as a powerful tool to accelerate your projects while maintaining control over design decisions and implementation details.

---
“文档分片”是BMad方法中从规划阶段过渡到开发阶段的关键步骤，具体指：  
1. 由产品负责人（PO）代理对产品需求文档（PRD）进行拆分，将其分解为更细致的内容单元（如史诗级需求、用户故事等）；  
2. 随后对架构文档进行类似拆分，将整体架构拆解为可执行的技术模块或开发任务。  

目的是将大型文档转化为适合开发周期中逐步处理的小块内容，便于团队在IDE中按分片内容有序推进开发，提升工作效率和任务聚焦性。

---
在当前项目语境中，“史诗”（Epic）和“故事”（Story，通常指用户故事）是敏捷开发或项目管理中常用的概念，二者既有联系又有明确区别，核心差异体现在**粒度、范围、目标和使用阶段**上。以下从多个维度详细说明：


### **1. 定义与核心目标**
- **史诗（Epic）**  
  是**大型、宽泛的需求集合**，通常涵盖一个完整的业务目标或用户价值方向，但内容模糊、细节不足，无法直接交付或开发。  
  核心目标：**从宏观层面规划项目方向**，将复杂的业务需求拆解为可管理的单元，避免需求遗漏。  
  例如：在电商项目中，“用户支付功能”可视为一个史诗，它包含多种支付方式、退款流程、安全验证等子需求。

- **故事（用户故事）**  
  是**具体、可执行的最小需求单元**，聚焦于单个用户场景或功能点，通常以“作为[用户角色]，我希望[做某事]，以便[实现某价值]”的格式描述，具备可交付、可测试的特性。  
  核心目标：**明确开发团队的具体任务**，确保每个故事都能独立完成并带来实际价值。  
  例如：“作为买家，我希望使用信用卡支付，以便快速完成订单”就是一个用户故事。


### **2. 粒度与范围**
| 维度       | 史诗（Epic）                          | 故事（Story）                          |
|------------|---------------------------------------|---------------------------------------|
| 粒度       | 粗粒度，范围宽泛                      | 细粒度，范围具体                      |
| 可拆分性   | 必须拆分为多个故事才能执行            | 通常不可拆分，可直接纳入迭代          |
| 时间跨度   | 覆盖多个迭代，甚至整个项目周期        | 单个迭代内可完成（通常1-5个工作日）   |
| 示例       | “搭建用户登录系统”                    | “用户通过手机号+验证码登录”            |
|            | “实现商品搜索功能”                    | “用户可按价格区间筛选搜索结果”        |


### **3. 在项目流程中的作用**
- **史诗**：  
  用于**需求规划初期**，帮助团队梳理核心业务目标和大方向。它像一个“容器”，暂时容纳尚未细化的需求，避免在早期陷入过多细节。  
  例如：在产品启动会上，团队可能先确定“用户账户管理”“订单处理”等史诗，再逐步拆解。

- **故事**：  
  用于**迭代执行阶段**，是**开发和测试的直接依据**。经过细化的故事需明确验收标准（Acceptance Criteria），确保团队理解“做什么”和“怎么做才合格”。  
  例如：迭代计划会上，团队从史诗中拆分出具体故事，估算工作量并纳入当前迭代。


### **4. 关键区别总结**
1. **抽象 vs 具体**：史诗是抽象的大需求，故事是具体的可执行任务。  
2. **容器 vs 单元**：史诗需要拆分为故事，故事是最小执行单元。  
3. **规划 vs 执行**：史诗用于前期规划，故事用于迭代执行。  


在实际项目中，二者是“父子关系”——史诗包含多个故事，故事是史诗的细化结果。合理区分二者有助于提升需求管理的清晰度和开发效率。

---

# BMAD-METHOD 用户指南网页总结

## 一、BMAD 方法概述
- 是一种用于敏捷 AI 驱动规划和开发的方法
- 分为绿地项目（新项目）和棕地项目（现有项目）的工作流程，建议先了解绿地项目流程
- 需要安装到新项目文件夹的根目录，规划阶段可选择使用强大的 Web 代理以获得更高质量结果

## 二、工作流程
### 1. 规划工作流（Web UI 或功能强大的 IDE 代理）
- 从项目构想开始，可选择进行分析师研究（包括头脑风暴、市场调研、竞争对手分析等）
- 依据是否有项目简报，分别进行快速创建 PRD 或交互式 PRD 创建
- 根据是否需要 UX，决定是否创建前端规范及生成 UI 提示
- 由架构师根据相关文档创建架构，可选择进行早期测试策略制定
- 经 PO 运行主检查表确认文档对齐后，规划完成并切换到 IDE 开始开发
- 规划工件包括 PRD、Architecture、Sharded Epics 等，并有固定存储路径

### 2. 核心开发周期（IDE）
- 从开发阶段开始，SM 回顾之前的故事开发/QA 笔记并起草下一个故事
- 对高风险故事，QA 会进行风险和设计评估并创建测试策略和风险概况
- PO 可对故事草稿进行验证，经用户批准后，开发人员执行任务并实现功能及测试
- 可选择进行中期开发 QA 检查，开发人员运行所有验证并标记为准备审查
- 经用户验证后，要么请求 QA 审查，要么直接批准（需确保所有回归测试和 linting 通过）
- QA 审查后做出决策，需修改则返回开发阶段，批准则提交更改，最后标记故事为完成

## 三、前置条件与安装
### 1. 前置条件
- Node.js ≥ 18，npm ≥ 9
- Git 已安装并配置
- （可选）VS Code 及相关扩展（"Markdown All in One" 和 "Markdown Preview Mermaid Support"）

### 2. 安装步骤
- 若要在网页上使用 Claude 等进行规划，需进入指定目录复制文件并创建相关 Gemini Gem 或 CustomGPT
- IDE 项目设置推荐使用交互式安装：`npx bmad-method install`

## 四、特殊代理
### 1. BMad-Master
- 可执行所有其他代理能做的任何任务或命令（除实际故事实现）
- 能在网页上通过访问知识库解释 BMAD 方法
- 需注意随着上下文增长，代理性能会下降，应经常压缩对话并以压缩内容作为初始消息开始新对话

### 2. BMad-Orchestrator
- 不应在 IDE 中使用，是重量级、专用代理，可变形为任何其他代理
- 仅用于促进 web 捆绑包中的团队，使用 web 捆绑包时会遇到

### 3. 代理工作方式
- 依赖系统：每个代理有定义依赖的 YAML 部分，仅加载所需资源，依赖在捆绑期间自动解析，资源在代理间共享以保持一致性
- 代理交互：在 IDE 中，部分 IDE 用 '@' 符号，部分用斜杠命令
- 交互模式：包括增量模式（逐步进行，有用户输入）和 YOLO 模式（快速生成，最小交互）

## 五、IDE 集成
- 最佳实践包括上下文管理（仅保留相关文件）、代理选择（为任务使用适当代理）、迭代开发（以小而专注的任务工作）、文件组织（保持清晰的项目结构）、定期提交（经常保存工作）

## 六、测试架构师（QA 代理）
### 1. 概述
- 不仅是“高级开发评审员”，还是在测试策略、质量门和基于风险的测试方面有深厚专业知识的测试架构师，名为 Quinn
- 在质量问题上有咨询权，在安全的情况下积极改进代码

### 2. 核心功能及命令
| 功能                | 命令          | 使用时机                  | 说明                                                                 |
|---------------------|---------------|---------------------------|----------------------------------------------------------------------|
| 风险分析            | `*risk`       | 故事草稿后，开发开始前    | 识别和评估实施风险，包括类别、评分、缓解措施和门影响                 |
| 测试设计            | `*design`     | 故事草稿后，开发开始前    | 创建全面的测试策略，包括每个验收标准的测试场景、适当的测试级别建议等 |
| 需求追踪            | `*trace`      | 开发期间（中期实施检查点）| 将需求映射到测试覆盖率，识别覆盖缺口等                               |
| NFR 评估            | `*nfr`        | 开发期间或早期审查时      | 验证非功能性需求，包括核心四个方面（安全性、性能、可靠性、可维护性） |
| 全面测试架构审查    | `*review`     | 开发完成后，故事标记为“准备审查” | 执行需求可追溯性、测试级别分析等，发布质量门决策                     |
| 质量门              | `*gate`       | 审查修复后或需要更新门状态时 | 管理质量门决策，有确定的规则、并行权限等                             |

### 3. 与 BMAD 工作流集成及输出路径
- 在故事起草、开发、审查、审查后等阶段有对应的使用场景和输出
- 各功能输出有固定的存储路径

### 4. 质量标准、门状态含义及特殊情况
- 质量标准：包括无不稳定测试、无硬等待、无状态且并行安全等
- 门状态：PASS（所有关键要求满足）、CONCERNS（发现非关键问题）、FAIL（有应解决的关键问题）、WAIVED（团队明确接受问题）
- 特殊情况：高风险故事、复杂集成、性能关键、棕地/遗留代码等有相应的处理建议

### 5. 最佳实践
- 早期参与（在故事起草期间运行 `*design` 和 `*risk`）、基于风险的关注（让风险评分驱动测试优先级）等

## 七、技术偏好系统
- 通过位于 `.bmad-core/data/` 的 `technical-preferences.md` 文件实现个性化系统，可帮助 PM 和架构师推荐偏好
- 在创建自定义 web 捆绑包或上传到 AI 平台时，包含该文件内容以确保代理从对话开始就了解偏好

## 八、核心配置
- `bmad-core/core-config.yaml` 文件是关键配置，目前最重要的是 yaml 中的 devLoadAlwaysFiles 列表部分
- 定义开发代理应始终加载的文件，需验证这些文件存在、尽可能精简且包含所需信息，随着项目增长，编码标准应精简

## 九、获取帮助渠道
- Discord 社区、GitHub Issues、文档、YouTube（BMadCode Channel）

## 十、结论
BMAD 旨在增强开发过程，而非取代专业知识，应将其用作加速项目同时保持对设计决策和实施细节控制的强大工具。

---
在交互模式中，**YOLO模式**（源自英文“You Only Live Once”的缩写，此处可理解为“一次到位、快速生成”）是一种以“高效输出、最小化交互”为核心的工作模式，强调快速交付初步成果，减少过程中的用户输入和迭代沟通。以下从核心特点、适用场景、优势与局限等方面详细解析：


# YOLO模式的核心特点
1. **快速生成，一步到位**  
   基于初始输入（如用户的需求描述、目标或基础信息），直接生成完整成果，不进行中间环节的拆分或分步确认。例如：用户要求“写一篇关于环保的短文”，YOLO模式会直接产出一篇完整短文，而非先确认结构、论点再逐步撰写。

2. **最小化交互，减少反馈循环**  
   过程中几乎不主动向用户索要额外信息或进行阶段性确认，默认用户提供的初始需求已足够明确，或允许成果存在一定“不完美”以换取速度。用户仅在成果生成后有一次反馈机会（如需修改），而非多次介入中间过程。

3. **聚焦“完成”而非“精准”**  
   优先保证输出的“存在性”和“时效性”，而非一开始就追求细节完美。成果可能包含待优化的部分，但能快速满足用户对“初步版本”“原型”或“应急方案”的需求。


### **YOLO模式的适用场景**
- **需求简单、目标明确**：例如生成一段简短的文案、一个基础的列表、一次快速的信息总结等，用户能清晰描述需求，无需额外补充细节。  
- **时间紧迫，需快速占位**：如临时需要一份会议提纲、一个活动口号，用户更在意“尽快拿到结果”而非反复打磨。  
- **探索性需求，允许试错**：例如用户想“看看某个创意的大致方向”，YOLO模式能快速提供一个起点，供用户判断是否符合预期，再决定是否深入优化。  
- **低风险场景**：成果即使存在小瑕疵，也不会造成严重影响（如个人笔记、非正式沟通内容）。


### **与增量模式的核心差异**
| 维度                | YOLO模式                          | 增量模式                          |
|---------------------|-----------------------------------|-----------------------------------|
| 交互频率            | 仅初始输入+最终输出，无中间交互   | 多轮交互，逐步细化（如“第一步确定框架，第二步补充内容”） |
| 输出节奏            | 一次性生成完整成果                | 分阶段输出，每阶段可调整方向       |
| 对需求的依赖        | 依赖初始需求的完整性              | 可通过中间交互弥补初始需求的模糊性 |
| 典型适用场景        | 简单任务、紧急需求、探索性输出    | 复杂任务、高精度需求、需要用户深度参与的场景 |


### **YOLO模式的优势与局限**
- **优势**：  
  - **效率极高**：省去中间沟通成本，快速响应需求，适合应对时间压力。  
  - **减少决策负担**：用户无需在过程中频繁反馈，适合希望“少操心”的场景。  

- **局限**：  
  - **容错率低**：若初始需求模糊或理解偏差，可能导致成果与预期差距较大，需返工。  
  - 缺乏灵活性：生成后如需大幅调整，可能比增量模式更耗时（因未经过中间校准）。  


总之，YOLO模式是一种“以速度换效率”的交互策略，核心是通过减少过程干预实现快速交付，适合简单、明确或紧急的需求场景，但在复杂或高精准度需求中，需谨慎使用以避免返工成本。

---
# 与YOLO相对的其他模式

与YOLO模式（快速生成、最小交互）相对的模式，核心是通过**增加交互深度、分阶段推进、强调过程校准**来提升成果的精准度和适配性。以下是几类典型的相对模式及其特点：


### **1. 增量模式（Incremental Mode）**
- **核心逻辑**：将任务拆解为多个连续阶段，每阶段输出部分成果并获取用户反馈，逐步迭代完善，最终形成完整结果。  
- **与YOLO的对比**：  
  - YOLO是“一步到位”，增量模式是“分步验证”。  
  - 例如：撰写一篇报告时，YOLO模式直接生成全文；增量模式则先输出大纲→用户确认后补充各章节核心观点→再细化案例和数据→最后调整格式，每步都允许用户反馈修改。  
- **适用场景**：需求复杂、用户对细节有明确要求（如方案设计、长文创作），需通过逐步校准避免方向偏差。


### **2. 迭代模式（Iterative Mode）**
- **核心逻辑**：基于初始版本，通过多轮“反馈-修改”循环优化成果，每轮迭代都可能推翻部分内容并重新设计，直至满足预期。  
- **与YOLO的对比**：  
  - YOLO强调“一次生成”，迭代模式强调“反复打磨”。  
  - 例如：设计一款logo时，YOLO模式直接生成一个方案；迭代模式则先出3个初稿→用户指出偏好和修改点→基于反馈调整细节→再出2个优化版→最终确定，过程中可能完全推翻初始设计。  
- **适用场景**：创意类任务（如设计、文案）、用户需求模糊但有明确“偏好倾向”，需通过多轮试错逼近目标。


### **3. 协作共创模式（Collaborative Co-creation Mode）**
- **核心逻辑**：用户深度参与创作过程，与执行者实时互动、共同决策，成果是双方协作的直接产物。  
- **与YOLO的对比**：  
  - YOLO是“执行者主导，用户被动接收”；协作模式是“用户主动参与，共同主导”。  
  - 例如：制定项目计划时，YOLO模式直接给出完整计划；协作模式则通过实时会议，双方一起讨论目标、拆解任务、分配责任，边沟通边形成文档。  
- **适用场景**：需要用户深度介入的任务（如战略规划、团队流程设计），或执行者对用户背景、需求细节缺乏了解的场景。


### **4. 精准定制模式（Precision Customization Mode）**
- **核心逻辑**：前期通过详细调研、需求拆解明确所有细节，再基于完整信息生成成果，追求“一次成型、无需修改”。  
- **与YOLO的对比**：  
  - YOLO是“快速输出，容忍不完美”；精准模式是“慢启动、高精准”，通过前期充分准备减少后期返工。  
  - 例如：制作一份法律合同，YOLO模式基于简单需求快速草拟；精准模式则先详细询问双方权责、特殊条款、风险点等细节，形成需求清单后再起草，确保条款无遗漏。  
- **适用场景**：高严谨性任务（如法律文件、技术规范）、错误成本高的场景，需通过前期精准调研规避风险。


### **各类模式与YOLO模式的核心差异对比**
| 模式类型       | 核心特点                          | 交互频率       | 输出速度       | 适用场景关键词                |
|----------------|-----------------------------------|----------------|----------------|-------------------------------|
| YOLO模式       | 快速生成，最小交互                | 极低（仅初始输入） | 极快           | 简单需求、紧急、低风险        |
| 增量模式       | 分步输出，阶段反馈                | 中高           | 中等           | 复杂需求、需逐步校准          |
| 迭代模式       | 多轮修改，逼近目标                | 高             | 较慢           | 创意类、需求模糊              |
| 协作共创模式   | 用户深度参与，实时互动            | 极高           | 中等           | 战略规划、团队协作            |
| 精准定制模式   | 前期调研充分，一次成型            | 集中在前期     | 慢（启动慢，后期快） | 高严谨性、错误成本高          |


这些模式的选择取决于**需求复杂度、时间压力、错误成本、用户参与意愿**等因素。实际项目中，也可能混合使用（如先以“精准定制模式”明确核心需求，再用“增量模式”分步推进），以平衡效率与质量。

---

# 测试策略与风险预估

Creating a **Test Strategy** and **Risk Profile** is critical for ensuring a structured, risk-aware approach to testing in a project. Below is a detailed breakdown of both, including their key components, purposes, and how they align to support successful delivery.


### **1. Test Strategy**  
A **Test Strategy** is a high-level document that defines the **overall approach, objectives, and scope of testing** for a project. It outlines "why," "what," "how," and "when" testing will be conducted, aligning with the project’s goals, stakeholders’ expectations, and quality standards.  

#### **Key Components of a Test Strategy**  
- **Testing Objectives**  
  - Define the primary goals of testing (e.g., "Ensure 95% of critical user stories meet acceptance criteria," "Validate compliance with data privacy regulations," "Minimize post-release defects in core functionality").  

- **Scope of Testing**  
  - **In Scope**: What will be tested (e.g., functional modules, integrations, performance under peak load, security vulnerabilities, usability for target users).  
  - **Out of Scope**: What will *not* be tested (e.g., legacy features not modified in the current release, third-party APIs with existing validation, non-critical UI polish).  

- **Testing Types & Levels**  
  - Specify the testing methods to be used, based on project needs:  
    - **Functional Testing**: Unit, integration, system, and acceptance testing (UAT).  
    - **Non-Functional Testing**: Performance (load, stress), security, usability, compatibility (devices/browsers), and reliability testing.  
    - **Specialized Testing**: If applicable (e.g., regression testing for iterative updates, exploratory testing for complex workflows).  

- **Test Environment & Tools**  
  - **Environments**: Define required setups (e.g., development, staging, production-like pre-production) and their configurations (hardware, software, data).  
  - **Tools**: List tools for test management (e.g., JIRA, TestRail), automation (e.g., Selenium, Cypress), performance testing (e.g., JMeter), and defect tracking (e.g., Bugzilla).  

- **Test Data Management**  
  - Strategy for creating, storing, and securing test data (e.g., synthetic data for privacy compliance, anonymized production data, data refresh cycles).  

- **Entry & Exit Criteria**  
  - **Entry Criteria**: Conditions that must be met to start testing (e.g., "All user stories for the sprint are developed and code-reviewed," "Test environment is stable").  
  - **Exit Criteria**: Conditions that must be met to conclude testing (e.g., "No critical or high-severity defects remain open," "90% of test cases executed," "UAT sign-off received").  

- **Responsibilities & Stakeholders**  
  - Clarify roles (e.g., testers, developers, product owners, stakeholders) and their responsibilities (e.g., developers conduct unit testing, testers lead integration testing, product owners approve UAT).  

- **Testing Schedule & Milestones**  
  - Align testing phases with the project timeline (e.g., "Unit testing completes by Sprint 3," "System testing concludes 2 weeks before release," "UAT runs in the final sprint").  


### **2. Risk Profile**  
A **Risk Profile** identifies, assesses, and prioritizes potential risks to the testing process (and broader project) and outlines mitigation strategies. It ensures proactive management of issues that could delay testing, reduce quality, or increase costs.  

#### **Key Components of a Risk Profile**  
- **Risk Identification**  
  - List potential risks relevant to testing, categorized by type:  
    - **Schedule Risks**: Delays in development leading to compressed testing windows; resource shortages (e.g., testers unavailable).  
    - **Quality Risks**: Ambiguous requirements leading to incorrect test cases; high complexity of new features increasing defect likelihood.  
    - **Environment Risks**: Unstable test environments; lack of access to required tools or data.  
    - **Skill Risks**: Testers lack expertise in new technologies (e.g., automation tools for a microservices architecture).  
    - **External Risks**: Third-party dependencies (e.g., APIs) failing; regulatory changes affecting testing criteria.  

- **Risk Assessment**  
  - Evaluate each risk using two metrics:  
    - **Impact**: Severity of consequences if the risk occurs (e.g., "High" = release delay; "Low" = minor rework).  
    - **Likelihood**: Probability of the risk occurring (e.g., "High" = >70% chance; "Low" = <30% chance).  
  - Prioritize risks using a risk matrix (e.g., "Critical" = high impact + high likelihood; "Low" = low impact + low likelihood).  

- **Risk Mitigation & Contingency Plans**  
  - For high-priority risks, define actions to:  
    - **Mitigate**: Reduce likelihood or impact (e.g., "Train testers on new tools 2 weeks before testing starts" to address skill gaps).  
    - **Transfer**: Shift risk to another party (e.g., "Hire external consultants for security testing" if in-house expertise is lacking).  
    - **Accept**: Tolerate low-priority risks (e.g., "Accept minor UI defects in non-critical features if time is constrained").  
  - Contingency plans for when risks materialize (e.g., "If test environment fails, switch to a backup environment within 4 hours").  

- **Risk Monitoring**  
  - Define how risks will be tracked (e.g., weekly risk reviews in stand-ups) and updated (e.g., new risks identified during testing).  


### **Alignment Between Test Strategy & Risk Profile**  
The Test Strategy and Risk Profile work together to ensure testing is both effective and resilient:  
- The Test Strategy’s scope and methods address known risks (e.g., including security testing in the strategy mitigates "data breach" risks).  
- The Risk Profile informs adjustments to the Test Strategy (e.g., if "compressed testing window" is a critical risk, the strategy may prioritize automation to accelerate execution).  


### **Example Summary Table**  
| **Test Strategy Element**       | **Linked Risk in Profile**                  | **Mitigation in Strategy**                          |  
|----------------------------------|----------------------------------------------|-----------------------------------------------------|  
| Inclusion of automation testing  | "Short testing window due to delays"          | Automate 70% of regression tests to save time.       |  
| UAT with end-users               | "Requirements misunderstood by testers"       | Validate test cases against user feedback in UAT.    |  
| Staging environment redundancy   | "Test environment instability"               | Maintain a backup staging environment.               |  


By combining a clear Test Strategy with a proactive Risk Profile, teams can ensure testing is focused, efficient, and prepared to handle challenges—ultimately delivering a high-quality product.

在敏捷开发或项目管理的语境中，**PO** 指的是 **Product Owner（产品负责人）**。 Product Owner 是项目中负责定义产品愿景、优先级和需求的关键角色，主要职责包括维护产品待办列表（Product Backlog）、明确用户故事（Story）的验收标准、确保团队理解业务目标等。 因此，“PO: Validate Story Against Artifacts” 可理解为：**产品负责人需对照相关工件（如需求文档、设计稿、验收标准等）验证用户故事的准确性和完整性**。

---

# 决策树

```
Do you have a large codebase or monorepo?
├─ Yes → PRD-First Approach
│   └─ Create PRD → Document only affected areas
└─ No → Is the codebase well-known to you?
    ├─ Yes → PRD-First Approach
    └─ No → Document-First Approach

Is this a major enhancement affecting multiple systems?
├─ Yes → Full Brownfield Workflow
│   └─ ALWAYS run Test Architect *risk + *design first
└─ No → Is this more than a simple bug fix?
    ├─ Yes → *create-brownfield-epic
    │   └─ Run Test Architect *risk for integration points
    └─ No → *create-brownfield-story
        └─ Still run *risk if touching critical paths

Does the change touch legacy code?
├─ Yes → Test Architect is MANDATORY
│   ├─ *risk → Identify regression potential
│   ├─ *design → Plan test coverage
│   └─ *review → Validate no breakage
└─ No → Test Architect is RECOMMENDED
    └─ *review → Ensure quality standards
```