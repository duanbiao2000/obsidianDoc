---
title: BMAD-METHOD/docs/enhanced-ide-development-workflow.md at main · bmad-code-org/BMAD-METHOD
source: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/enhanced-ide-development-workflow.md
author:
  - "[[GitHub]]"
published:
date: 2025-08-17
description: Breakthrough Method for Agile Ai Driven Development - BMAD-METHOD/docs/enhanced-ide-development-workflow.md at main · bmad-code-org/BMAD-METHOD
tags:
  - clippings
---
[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/bmad-code-org/BMAD-METHOD/tree/main?resume=1)

[feat: transform QA agent into Test Architect with advanced quality ca… (](https://github.com/bmad-code-org/BMAD-METHOD/commit/0b61175d98e6def508cc82bb4539e7f37f8f6e1a)

[0b61175](https://github.com/bmad-code-org/BMAD-METHOD/commit/0b61175d98e6def508cc82bb4539e7f37f8f6e1a) ·

这是一个简单的分步指南，可帮助您使用 BMad 方法有效地管理开发工作流程。该工作流在整个开发生命周期中集成了测试架构师（QA 代理），以确保质量、防止回归并保持高标准。有关此处未涵盖的任何方案，请参阅 **[用户指南](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/user-guide.md)** 。

## 创建新分支

1. **开始新分支**

## 故事创作（Scrum Master）

1. **开始新的聊天/对话**
2. **加载 SM 代理**
3. **执行** ： `*草稿 ` （运行创建下一个故事任务）
4. 在 `docs/stories/` 中 **查看生成的故事**
5. **更新状态** ：从“草稿”更改为“已批准”

## 故事实现（开发人员）

1. **开始新的聊天/对话**
2. **加载开发代理**
3. **执行** ： `*develop-story {selected-story}` （运行执行清单任务）
4. 查看 `{selected-story}` 中 **生成的报告**

## 测试架构师在整个工作流程中的集成

测试架构师 （Quinn） 在整个开发生命周期中提供全面的质量保证。以下是如何在正确的时间利用每种功能。

**命令别名：** 文档使用简短形式（ `*risk` 、 `*design` 、 `*nfr` 、 `*trace` ）来表示完整命令（ `*risk-profile` 、 `*test-design` 、 `*nfr-assess` 、 `*trace-requirements` ）。

### 快速命令参考

| **阶段** | **命令** | **目的** | **输出** | **优先权** |
| --- | --- | --- | --- | --- |
| **故事批准后** | `*risk` | 识别集成和回归风险 | `docs/qa/assessments/{epic}.{story}-risk-{YYYYMMDD}.md` | 高适用于复杂/棕地 |
|  | `*design` | 为开发人员创建测试策略 | `docs/qa/assessments/{epic}.{story}-test-design-{YYYYMMDD}.md` | 新功能高 |
| **开发过程中** | `*trace` | 验证测试覆盖率 | `docs/qa/assessments/{epic}.{story}-trace-{YYYYMMDD}.md` | 中等 |
|  | `*nfr` | 验证质量属性 | `docs/qa/assessments/{epic}.{story}-nfr-{YYYYMMDD}.md` | 高关键功能 |
| **开发后** | `*review` | 综合评估 | 故事中的 QA 结果 + `docs/qa/gates/{epic}.{story}-{slug}.yml` | **必填** |
| **事后审查** | `*gate` | 更新质量决策 | 更新 `docs/qa/gates/{epic}.{story}-{slug}.yml` | 根据需要 |

**推荐 - 为开发人员的成功做好准备：**

### 阶段 2：开发期间（实现中期检查点）

**开发人员自助服务质量检查：**

```
# 3. REQUIREMENTS TRACING (Verify coverage mid-development)
@qa *trace {story-in-progress}
# Validates:
#   - All acceptance criteria have tests
#   - No missing test scenarios
#   - Appropriate test levels
#   - Given-When-Then documentation clarity
# Run when: After writing initial tests

# 4. NFR VALIDATION (Check quality attributes)
@qa *nfr {story-in-progress}
# Assesses:
#   - Security: Authentication, authorization, data protection
#   - Performance: Response times, resource usage
#   - Reliability: Error handling, recovery
#   - Maintainability: Code quality, documentation
# Run when: Before marking "Ready for Review"
```

### 第三阶段：故事回顾（质量门评估）

**必需 - 全面的测试架构审查：**

**先决条件：** 所有测试均在本地进行绿色;lint 和类型检查通过。

```
# 5. FULL REVIEW (Standard review process)
@qa *review {completed-story}
```

**审查期间会发生什么：**

1. **深度代码分析**
	- 架构模式合规性
	- Code quality and maintainability
	- Security vulnerability scanning
	- Performance bottleneck detection
2. **Active Refactoring**
	- Improves code directly when safe
	- Fixes obvious issues immediately
	- Suggests complex refactoring for dev
3. **Test Validation**
	- Coverage at all levels (unit/integration/E2E)
	- Test quality (no flaky tests, proper assertions)
	- Regression test adequacy
4. **Gate Decision**
	- Creates: `docs/qa/gates/{epic}.{story}-{slug}.yml`
	- Adds: QA Results section to story file
	- Status: PASS/CONCERNS/FAIL/WAIVED

**Update Gate Status After Fixes:**

```
# 6. GATE UPDATE (Document final decision)
@qa *gate {reviewed-story}
# Updates: Quality gate with new status
# Use when: After addressing review feedback
# Documents: What was fixed, what was waived
```

| **Status** | **Meaning** | **Action Required** | **Can Proceed?** |
| --- | --- | --- | --- |
| **PASS** | All critical requirements met | None | ✅ Yes |
| **CONCERNS** | Non-critical issues found | Team review recommended | ⚠️ With caution |
| **FAIL** | Critical issues (security, missing P0 tests) | Must fix | ❌ No |
| **WAIVED** | Issues acknowledged and accepted | Document reasoning | ✅ With approval |

The Test Architect uses risk scoring to prioritize testing:

| **Risk Score** | **Calculation** | **Testing Priority** | **Gate Impact** |
| --- | --- | --- | --- |
| **9** | High probability × High impact | P0 - Must test thoroughly | FAIL if untested |
| **6** | Medium-high combinations | P1 - Should test well | CONCERNS if gaps |
| **4** | Medium combinations | P1 - Should test | CONCERNS if notable gaps |
| **2-3** | Low-medium combinations | P2 - Nice to have | Note in review |
| **1** | Minimal risk | P2 - Minimal | Note in review |

```
# ALWAYS run this sequence:
@qa *risk {story}    # First - identify dangers
@qa *design {story}  # Second - plan defense
# Then during dev:
@qa *trace {story}   # Verify regression coverage
@qa *nfr {story}     # Check performance impact
# Finally:
@qa *review {story}  # Deep integration analysis
```

#### Complex Integrations

- Run `*trace` multiple times during development
- Focus on integration test coverage
- Use `*nfr` to validate cross-system performance
- Review with extra attention to API contracts

#### Performance-Critical Features

- Run `*nfr` early and often (not just at review)
- Establish performance baselines before changes
- Document acceptable performance degradation
- Consider load testing requirements in `*design`

Quinn ensures all tests meet these standards:

- **No Flaky Tests**: Proper async handling, explicit waits
- **No Hard Waits**: Dynamic strategies only (polling, events)
- **Stateless**: Tests run independently and in parallel
- **Self-Cleaning**: Tests manage their own test data
- **Appropriate Levels**: Unit for logic, integration for interactions, E2E for journeys
- **Clear Assertions**: Keep assertions in tests, not buried in helpers

All Test Architect activities create permanent records:

- **Assessment Reports**: Timestamped analysis in `docs/qa/assessments/`
- **Gate Files**: Decision records in `docs/qa/gates/`
- **Story Updates**: QA Results sections in story files
- **Traceability**: Requirements to test mapping maintained
1. **Commit changes**
2. **Push to remote**
1. **SM**: Create next story → Review → Approve
2. **QA (Optional)**: Risk assessment (`*risk`) → Test design (`*design`)
3. **Dev**: Implement story → Write tests → Complete
4. **QA (Optional)**: Mid-dev checks (`*trace`, `*nfr`)
5. **Dev**: Mark Ready for Review
6. **QA (Required)**: Review story (`*review`) → Gate decision
7. **Dev (If needed)**: Address issues
8. **QA (If needed)**: Update gate (`*gate`)
9. **Commit**: All changes
10. **Push**: To remote
11. **Continue**: Until all features implemented

**Should I run Test Architect commands?**

| **Scenario** | **Before Dev** | **During Dev** | **After Dev** |
| --- | --- | --- | --- |
| **Simple bug fix** | Optional | Optional | Required `*review` |
| **New feature** | Recommended `*risk`, `*design` | Optional `*trace` | Required `*review` |
| **Brownfield change** | **Required** `*risk`, `*design` | Recommended `*trace`, `*nfr` | Required `*review` |
| **API modification** | **Required** `*risk`, `*design` | **Required** `*trace` | Required `*review` |
| **Performance-critical** | Recommended `*design` | **Required** `*nfr` | Required `*review` |
| **Data migration** | **Required** `*risk`, `*design` | **Required** `*trace` | Required `*review` + `*gate` |

### Success Metrics

The Test Architect helps achieve:

- **Zero regression defects** in production
- **100% requirements coverage** with tests
- **Clear quality gates** for go/no-go decisions
- **Documented risk acceptance** for technical debt
- **Consistent test quality** across the team
- **Shift-left testing** with early risk identification

---

# 任务类型
以下是对各任务文档的解释，涵盖其核心目标和典型应用场景：


### 1. **advanced-elicitation.md**  
- **核心目标**：通过进阶的引导技巧，从用户或相关方那里精准获取复杂、隐性或模糊的需求、信息或反馈。  
- **特点**：区别于基础提问，可能包含开放式探询、场景模拟、矛盾点挖掘等策略，适用于需求不明确的场景（如产品设计初期、用户研究）。  
- **示例**：在软件开发中，通过“如果系统崩溃，你最担心丢失什么数据？”等问题，挖掘用户对系统稳定性的潜在诉求。  


### 2. **facilitate-brainstorming-session.md**  
- **核心目标**：提供结构化流程和工具，引导团队高效开展头脑风暴，激发创意并达成共识。  
- **包含要素**：可能涉及议题设定、规则说明（如“禁止批评”）、创意收集方法（如思维导图、六顶思考帽）、成果整理步骤等。  
- **适用场景**：产品创新、问题解决方案设计、营销策略制定等需要群体创意的场景。  


### 3. **brownfield-create-epic.md**  
- **核心目标**：在“棕地项目”（已有系统或遗产项目）中，定义大型功能模块（Epic），明确其业务价值、范围和关键需求。  
- **特点**：需考虑与现有系统的兼容性、技术债务、重构约束等，区别于绿场项目（从零开始）的Epic设计。  
- **示例**：为一个老旧电商系统设计“支付流程升级”Epic，需涵盖与现有订单系统的对接、数据迁移要求等。  


### 4. **brownfield-create-story.md**  
- **核心目标**：将棕地项目中的Epic拆解为具体可执行的用户故事（User Story），描述用户需求、场景和验收标准。  
- **关注点**：需结合现有系统的技术限制、用户习惯（避免大幅变更），确保故事的可行性和最小可交付性。  
- **示例**：在“支付流程升级”Epic下，拆解出“用户可使用Apple Pay完成支付”的故事，明确需兼容现有订单数据库。  


### 5. **correct-course.md**  
- **核心目标**：当项目偏离计划（如进度滞后、需求变更、风险爆发）时，提供调整策略和执行步骤，使项目回归正轨。  
- **关键步骤**：可能包括问题诊断、影响评估、方案制定（如资源重分配、范围调整）、执行跟踪等。  
- **适用场景**：项目管理中应对突发问题（如开发延期、用户反馈不符预期）。  


### 6. **create-deep-research-prompt.md**  
- **核心目标**：设计精准、结构化的提示词，用于指导LLM或研究人员开展深度调研，获取针对性信息。  
- **设计要点**：包含研究主题、关键维度（如历史背景、现状分析、未来趋势）、信息来源要求（如学术论文、行业报告）等。  
- **示例**：为“AI在医疗诊断中的伦理风险”设计提示，明确需涵盖数据隐私、算法偏见、监管政策等子主题。  


### 7. **create-doc.md**  
- **核心目标**：生成特定类型的文档（如手册、指南、报告），包含内容框架、格式规范和写作要点。  
- **灵活性**：可适配不同场景（如技术文档、用户手册、会议纪要），明确文档的受众、目的和核心模块。  
- **示例**：制定“API接口文档”模板，包含端点说明、参数格式、错误码列表等章节。  


### 8. **document-project.md**  
- **核心目标**：系统性记录项目全生命周期的关键信息，形成可追溯的项目档案。  
- **包含内容**：可能涵盖项目目标、里程碑、决策记录、风险日志、会议纪要、成果交付物等。  
- **作用**：用于项目复盘、知识传承、 stakeholder沟通（如向管理层汇报进展）。  


### 9. **create-next-story.md**  
- **核心目标**：基于项目当前进度和优先级，规划下一个待执行的用户故事，确保与整体目标一致。  
- **依据**：需参考产品路线图、团队产能、依赖关系（如前置故事的完成情况）等因素。  
- **示例**：在电商系统开发中，完成“商品详情页展示”后，规划“加入购物车”作为下一个故事。  


### 10. **execute-checklist.md**  
- **核心目标**：按照预设的检查清单，逐项验证任务或流程的完成情况，确保无遗漏、符合标准。  
- **应用场景**：适用于重复性工作或关键节点（如发布前测试、合规审计），清单内容可能包括“代码评审通过”“用户验收完成”等。  


### 11. **generate-ai-frontend-prompt.md**  
- **核心目标**：设计用于生成前端界面（如UI组件、页面布局）的AI提示词，明确视觉风格、功能需求和技术约束。  
- **关键要素**：可能包含平台（如Web/移动端）、设计风格（如极简、拟物）、交互逻辑（如“点击按钮后弹出表单”）等。  
- **示例**：提示AI“生成一个响应式电商首页，包含轮播图、商品分类栏和用户登录入口，风格为北欧简约风”。  


### 12. **index-docs.md**  
- **核心目标**：对文档集合进行索引化处理，建立检索机制（如关键词、标签、目录结构），提高查找效率。  
- **常见方式**：可能涉及生成文档摘要、提取关键术语、构建关联图谱（如“技术文档-对应模块”映射）。  


### 13. **shard-doc.md**  
- **核心目标**：将大型文档拆分为更小的、结构化的片段（Shards），便于管理、传输或处理（如分块输入LLM）。  
- **拆分逻辑**：可按章节、主题、数据类型（如“表格部分”“文字说明部分”）划分，同时保留片段间的关联信息（如页码、引用关系）。  
- **应用**：处理超长报告、书籍时，拆分后可提升加载速度或针对性分析效率。  


这些任务多聚焦于项目管理、文档处理、需求挖掘等场景，且部分任务（如`shard-doc.md`与`index-docs.md`）常结合使用以提升信息处理效率。

---

# 文档模板

这些文件名均包含“tmpl”（即template，模板），结合前缀可推测是不同场景下的标准化文档模板，用途如下：

- **architecture-tmpl.yaml**：通用架构模板，可能用于规划软件、系统的整体架构设计，涵盖技术栈、模块划分、交互逻辑等基础架构要素。  
- **brownfield-architecture-tmpl.yaml**：“brownfield”指已有系统的改造场景，因此这是针对 legacy 系统（遗留系统）架构改造的模板，侧重兼容性、迁移策略等。  
- **brownfield-prd-tmpl.yaml**：遗留系统的产品需求文档（PRD）模板，用于在已有产品基础上迭代需求，需考虑与现有功能的衔接。  
- **competitor-analysis-tmpl.yaml**：竞争对手分析模板，用于梳理竞品的功能、优势、劣势、市场策略等，辅助自身产品决策。  
- **front-end-architecture-tmpl.yaml**：前端架构模板，专注于前端技术架构设计，如框架选择、组件库、状态管理等。  
- **front-end-spec-tmpl.yaml**：前端规格说明模板，细化前端开发的技术标准、接口规范、交互细节等。  
- **fullstack-architecture-tmpl.yaml**：全栈架构模板，整合前端、后端、数据库、服务器等全链路技术架构设计。  
- **market-research-tmpl.yaml**：市场调研模板，用于收集和分析市场规模、用户需求、趋势等信息。  
- **prd-tmpl.yaml**：产品需求文档模板，定义产品功能、目标、用户场景、验收标准等核心需求。  
- **project-brief-tmpl.yaml**：项目简报模板，概述项目背景、目标、范围、时间节点、 stakeholders 等关键信息。  
- **story-tmpl.yaml**：用户故事模板，通常以“作为[角色]，我希望[功能]，以便[价值]”的格式描述用户需求。



[BMAD-METHOD/bmad-core/agents/bmad-master.md at main · bmad-code-org/BMAD-METHOD · GitHub](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/bmad-core/agents/bmad-master.md)

