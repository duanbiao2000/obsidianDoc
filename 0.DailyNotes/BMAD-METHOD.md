---
tags:
  - Tech/DeepWiki
  - Method
  - Domain/Creativity/Product
  - Checklist-防呆清单
source:
  - https://deepwiki.com/bmadcode/BMAD-METHOD
---

## 10 Brainstorming Actions

仅从图中信息看，“10 Brainstorming Actions”（10 项头脑风暴行动 ）没有明确给出具体内容，这是一套围绕 “Interactive Refinement（交互式完善）” 流程里的步骤，通常这类 “10 项头脑风暴行动” 是结合具体项目（比如文档优化、产品需求挖掘等，因图里有 `tasks/advanced - elicitation.md` ，可能和需求启发、文档迭代相关 ）自定义的操作，以下是常见的**头脑风暴行动方向推测**（供参考，需结合实际项目补充）：  

### 1. 需求挖掘类（若关联 `advanced - elicitation.md` 的需求启发）  
-  **用户角色反转**：团队成员扮演不同用户角色（如客户、终端用户、合作方），从角色视角提需求/问题。  
-  **竞品拆解模仿**：分析同类产品功能，反向思考 “若我们做类似功能，怎么创新/优化”。  
-  **极端场景假设**：假设产品遇到极端情况（如高并发、资源匮乏、用户误操作），头脑风暴应对方案。  

### 2. 文档优化类（若围绕 `tasks/advanced - elicitation.md` 文档完善）  
-  **跨角色挑错**：开发、测试、产品、设计等不同角色，专门找文档里逻辑漏洞、描述歧义。  
-  **空白补充挑战**：针对文档模糊/未提及的部分，强制每人提出 1 种补充思路。  
-  **类比迁移**：找其他领域（如医疗、金融→ 若当前是科技产品）的类似文档结构，迁移可复用逻辑。  

### 3. 通用创意类（适配多数 “交互式完善” 场景）  
-  **反向否定法**：先假设 “现有内容全错/无效”，再推导怎么重构。  
-  **关键词联想**：提取文档核心词（如 “elicitation 需求启发” 相关词），每人围绕词自由联想新观点。  
-  **故事化重构**：把文档内容编成用户故事/案例，从故事里找优化点。  
-  **限时疯狂想**：定 5 分钟，团队成员快速抛出最激进、不考虑可行性的想法，后续再筛选。  


简单说，“10 Brainstorming Actions” 是**10 种激发创意、挖掘问题、优化内容的具体操作方法**，但因图里没给细节，实际要结合 `advanced - elicitation.md` 所属项目（比如是需求文档、产品方案等 ），才能明确这 10 项具体是什么。你可以查查项目里的流程说明文档，或问问团队里的流程设计者～


## 领域案例
### 三、Domain Examples（领域案例）  
提供**不同领域的实践参考**，覆盖 4 类场景：  
1. 游戏开发：`bmat-2d-game-dev` → 输出 `Game Designer Level Designer`（游戏设计角色）  
2. 云架构：`bmat- infrastructure-devops` → 对应 `Cloud Architect SRE Expert`（云架构师/运维专家）  
3. 创意写作：`bmat-creative-writing` → 关联 `Bio Architects Character Psychologist`（生物架构/角色心理设计）  
4. 个人发展：`bmat-personal-development` → 指向 `Life Coach Goal Strategist`（人生教练/目标策略师）  


### 四、Expansion Pack Structure（扩展包结构）  
定义**扩展包组成要素**，通过 `expansionpacks/pack- name/` 管理，包含：  
- `package.json`：扩展包基础配置文件  
- `data/`：存储数据资源（如 `expansion-agent` 相关数据）  
- `templates/`：模板文件，用于快速生成内容  
- `tasks/`：任务脚本，定义扩展包可执行的操作  
- `agents/`：代理逻辑，实现自动化功能  


### 整体逻辑  
以**“系统集成” 为核心**，通过标准化安装流程（Installation Integration）落地工具，用扩展包结构（Expansion Pack Structure）实现功能模块化，再结合多领域案例（Domain Examples）覆盖不同业务场景，形成 “**工具链搭建 → 功能扩展 → 领域落地**” 的完整协作框架 。


---

## 防呆指南
以下是 **`prd-tmpl.yaml`（产品需求文档）、`architecture-tmpl.yaml`（架构文档）、`story-tmpl.yaml`（用户故事）** 的文字示例，结合实际场景解析核心结构：


### 一、`prd-tmpl.yaml`（产品需求文档模板）  
**核心作用**：定义产品功能、业务规则、验收标准，面向产品、开发、测试。  

```yaml
# 产品需求文档模板 - 电商商品管理系统
product:
  name: 电商商品中台
  version: v1.0
  owner: 产品部
  vision: "打造统一商品管理平台，支撑多端（APP、小程序、PC）商品展示与交易"

# 功能需求（按模块拆分）
functional_requirements:
  - module: 商品基础信息管理
    description: "维护商品名称、价格、属性、上下架状态"
    features:
      - name: 商品创建
        details: |
          1. 支持上传最多5张商品图（格式：JPG/PNG，单张≤5M）  
          2. 名称长度≤50字，价格≥0.01元，库存≥0  
          3. 分类支持三级联动（如「数码→手机→智能手机」）  
        acceptance_criteria:  # 验收标准（可测试）
          - "名称为空时，弹窗提示「请输入商品名称」"
          - "价格输入字母时，自动触发格式校验并标红"
      - name: 商品上下架
        details: "支持批量操作，下架后前端隐藏商品"
        acceptance_criteria:
          - "批量下架10个商品，耗时≤3秒"
          - "下架商品的SKU无法加入购物车"

  - module: 库存管理
    description: "实时同步库存，支持预警和调拨"
    features:
      - name: 库存预警
        details: "设置阈值（如库存<10时预警），触发邮件+站内信通知"
        acceptance_criteria:
          - "阈值可配置（1-999），修改后5分钟内生效"
          - "预警通知包含「商品名称、当前库存、阈值」"

# 非功能需求
non_functional_requirements:
  - performance: "商品列表查询（1000条数据）响应时间≤500ms"
  - compatibility: "支持Chrome 90+/Safari 14+/微信浏览器"
  - security: "商品价格仅管理员角色可修改，操作需记录审计日志"
```  


### 二、`architecture-tmpl.yaml`（技术架构文档模板）  
**核心作用**：定义技术方案、模块分工、部署架构，面向架构师、开发、运维。  

```yaml
# 技术架构文档模板 - 电商商品中台
architecture:
  name: 商品中台技术架构
  version: v1.0
  overview: "基于微服务架构，实现高可用、可扩展的商品全生命周期管理"

# 技术栈选型
tech_stack:
  backend: "Spring Boot 3.2 + MySQL 8.0（分片） + Redis 7.0（缓存）"
  frontend: "Vue 3 + Element Plus + Axios"
  middleware: "RabbitMQ（异步通知） + Nginx（负载均衡）"
  infrastructure: "Kubernetes（容器化部署） + Jenkins（CI/CD）"

# 模块架构（微服务拆分）
modules:
  - name: product-service（商品服务）
    responsibility: "商品信息增删改查、上下架逻辑"
    endpoints:
      - "POST /product/create  # 创建商品（需鉴权）"
      - "GET /product/list?page=1&size=20  # 商品列表查询"
    dependencies:  # 依赖关系
      - "stock-service：创建商品时初始化库存"
      - "user-service：鉴权接口校验用户角色"

  - name: stock-service（库存服务）
    responsibility: "库存扣减、预警、调拨"
    endpoints:
      - "PUT /stock/update  # 库存变更（如采购入库）"
      - "GET /stock/alert  # 查询库存预警商品"
    dependencies:
      - "MQ（RabbitMQ）：库存变更后发消息通知product-service"

# 部署架构
deployment:
  - environment: 生产环境
    instances: "product-service: 3实例（4C8G） | stock-service: 2实例（2C4G）"
    monitoring: "Prometheus + Grafana（监控接口响应时间、吞吐量）"
    disaster_recovery: "异地容灾，主集群故障时30分钟内切换备集群"

# 数据流转示例（商品创建流程）
data_flow:
  scenario: 商品创建
  steps:
    1. 前端→product-service：提交商品信息（名称、价格、图片等）
    2. product-service→stock-service：调用库存初始化接口（默认库存=0）
    3. stock-service→MySQL：写入库存记录，同时更新Redis缓存
    4. stock-service→RabbitMQ：发送「库存初始化完成」消息
    5. product-service→前端：返回创建结果（成功/失败）

# 架构决策记录（ADR）
architecture_decisions:
  - decision: "为什么选MySQL而非MongoDB？"
    reason: "商品数据为强结构化（价格、库存等字段固定），需复杂查询（如价格区间搜索），MySQL更高效。"
  - decision: "为什么引入Redis？"
    reason: "库存数据需高频读写（如秒杀场景），Redis缓存减少DB压力，保障性能。"
```  


### 三、`story-tmpl.yaml`（用户故事模板）  
**核心作用**：敏捷开发中，描述用户场景和价值，面向开发、测试、产品负责人（PO）。  

```yaml
# 用户故事模板 - 商品创建功能
story:
  id: STORY-001
  title: 运营人员创建商品
  description: |
    As an 电商运营人员,  
    I want to 在系统中创建新商品并设置基础信息,  
    So that 商品能在前端展示并支持用户购买。  

  # 验收标准（Given-When-Then 格式，可自动化测试）
  acceptance_criteria:
    - Given: 我是已登录的运营人员，进入「商品创建页」  
      When: 填写名称「2025款手机」、价格1999.99元、库存100，上传1张图片  
      Then: 商品创建成功，列表页显示该商品，库存服务中库存为100  
    - Given: 我填写名称为空，点击「保存」  
      When: 无其他操作  
      Then: 弹窗提示「请输入商品名称」，未发起后端请求  

  priority: 高  # 优先级：高/中/低（决定迭代排期）
  estimate: 5  # 故事点估算（相对工作量）
  dependencies: 
    - "商品分类数据已维护（需提前从分类系统导入）"
  notes: |
    - 图片上传支持拖拽功能  
    - 价格输入框需实时格式化（如自动添加千分位：1,999.99）  
```  


### 关键区别总结  
| 模板类型          | 核心关注点                     | 典型用户                  | 核心价值                           |
|-------------------|--------------------------------|--------------------------|------------------------------------|
| `prd-tmpl.yaml`   | **业务需求**（功能、规则）     | 产品经理、测试           | 明确“做什么”，统一需求认知         |
| `architecture.yaml` | **技术方案**（架构、部署）     | 架构师、运维             | 明确“怎么做”，保障技术可行性       |
| `story-tmpl.yaml` | **用户场景**（价值、验收）     | 开发、PO、测试           | 拆分需求，适配敏捷迭代，聚焦用户价值 |  

通过示例对比，可清晰看到：  
- PRD 偏向**“业务规则”**（如价格≥0.01元），  
- 架构文档偏向**“技术实现”**（如微服务拆分、Redis 缓存），  
- 用户故事偏向**“场景化价值”**（如运营人员创建商品的具体流程）。

---

你提到的这些文件名：

```
checklists/ architect-
checklist.md, pm-checklist.md, story-dod-checklist.md, etc.
```

看起来是某种项目管理或工程协作中使用的 **检查清单（Checklist）文档**，它们都以 `.md` 结尾，说明是 **Markdown 格式** 的文本文件。虽然名字相似，但它们的用途和内容差异很大。

下面我们通过 **实际示例 + 用途对比** 来解释这些文档的区别，并告诉你在什么场景下使用哪一个。

---

## 🧩 一、核心概念：什么是“Checklist”？

> **Checklist**（检查清单）是一种结构化文档，用于确保某个流程中的关键步骤不被遗漏。它像“任务核对表”，帮助团队成员按步骤执行工作，提升质量与一致性。

在软件开发、产品管理和架构设计中，常见的 Checklist 类型包括：
- 架构评审清单
- 产品经理交付清单
- 用户故事完成标准（DoD）
- 部署前检查项
- 安全合规检查等

---

## ✅ 二、具体文件解析 + 实际示例

### 1. `architect-checklist.md`  
#### 🔹 用途：**架构师在设计系统时使用的评审清单**
> 确保系统具备可扩展性、安全性、可观测性等非功能性需求。

#### 📌 示例内容：
```markdown
# 架构设计检查清单 (Architect Checklist)

✅ 是否定义了清晰的系统边界？
✅ 是否进行了服务拆分？是否存在单体依赖？
✅ 是否考虑了容错与降级机制？
✅ 是否有监控、日志、链路追踪方案？
✅ 是否评估过数据一致性模型（CAP）？
✅ 是否支持水平扩展？
✅ 是否进行过安全扫描（如OWASP Top 10）？
✅ 是否有灾难恢复预案？
```

#### 💡 使用场景：
当你设计一个微服务系统时，用这个清单来逐项确认是否满足架构要求。比如：你要做电商订单系统 → 拿出 `architect-checklist.md` → 检查是否做了限流、熔断、事务一致性处理。

---

### 2. `pm-checklist.md`  
#### 🔹 用途：**产品经理在发布功能前的核对清单**
> 确保产品从需求到上线的全流程完整，避免漏掉关键环节。

#### 📌 示例内容：
```markdown
# 产品经理交付检查清单 (PM Checklist)

✅ 需求文档是否已评审并签字？
✅ 用户画像和使用场景是否明确？
✅ 是否完成原型设计并通过UX评审？
✅ 是否与技术团队对齐实现方案？
✅ 是否制定MVP范围与优先级？
✅ 是否安排用户测试或AB实验？
✅ 是否准备上线后的数据分析指标？
✅ 是否通知运营/客服团队培训材料？
```

#### 💡 使用场景：
产品经理要上线“新支付方式”功能 → 拿出 `pm-checklist.md` → 检查是否已经完成用户调研、原型评审、数据埋点设计等。

---

### 3. `story-dod-checklist.md`  
#### 🔹 用途：**用户故事完成标准（Definition of Done）**
> 是 Scrum 团队判断一个“用户故事”是否真正完成的标准。

> DOD = Definition of Done（完成标准）

#### 📌 示例内容：
```markdown
# 用户故事完成标准 (Story DoD)

✅ 功能代码已提交并合并到主干
✅ 所有单元测试通过（>=90% 覆盖率）
✅ 集成测试通过（端到端验证）
✅ UI/UX 与设计稿一致
✅ 有完整的文档说明（API文档、用户手册）
✅ 已通过代码审查（Code Review）
✅ 已部署至预发环境并验证
✅ 无严重 Bug（P0/P1）
✅ 相关监控指标已配置
```

#### 💡 使用场景：
开发人员完成“注册页优化”后 → 提交 PR → 团队对照 `story-dod-checklist.md` 逐一打勾 → 决定是否可以关闭该任务。

> ⚠️ 注意：这不是“待办事项”，而是“验收标准”。

---

### 4. 其他常见类型（etc.）
| 文件名 | 用途 | 示例 |
|--------|------|------|
| `deployment-checklist.md` | 上线前检查 | 是否备份数据库？是否灰度发布？ |
| `security-checklist.md` | 安全审计 | 是否开启HTTPS？是否有SQL注入防护？ |
| `onboarding-checklist.md` | 新员工入职 | 是否分配账号？是否培训工具使用？ |
| `release-checklist.md` | 发布流程 | 是否通知客户？是否有回滚方案？ |

---

## 🔄 三、总结对比表

| 文件名 | 角色 | 关注点 | 是否可复用 | 何时使用 |
|--------|------|--------|------------|-----------|
| `architect-checklist.md` | 架构师 | 技术架构、系统稳定性 | ✅ 高 | 设计阶段 |
| `pm-checklist.md` | 产品经理 | 需求完整性、用户体验 | ✅ 中 | 需求评审、发布前 |
| `story-dod-checklist.md` | 开发/测试 | 功能是否真正完成 | ✅ 非常高 | 每个用户故事闭环 |
| `deployment-checklist.md` | 运维/DevOps | 上线流程、风险控制 | ✅ 高 | 每次发布前 |
| `security-checklist.md` | 安全工程师 | 漏洞、合规性 | ✅ 高 | 审计、渗透测试 |

---

## 🎯 四、如何选择使用哪个？

你可以这样想：

> **你是谁？你在做什么？**

- 如果你在画系统图 → 用 `architect-checklist.md`
- 如果你在写需求文档 → 用 `pm-checklist.md`
- 如果你在提交代码 → 用 `story-dod-checklist.md`
- 如果你在准备上线 → 用 `deployment-checklist.md`

---

## 🛠️ 五、最佳实践建议

1. **统一命名规范**：比如 `role-name-checklist.md`，方便查找。
2. **放在共享仓库**：如 GitHub / GitLab 的 `docs/checklists/` 目录下。
3. **定期更新**：随着团队成熟，检查项应迭代优化。
4. **可视化工具辅助**：可以用 Notion、Trello 或 Jira 将 Checklist 变成可勾选的任务。

---

## ✅ 总结一句话：

> **这些 `.md` 文件不是“同一类文档”，而是不同角色在不同阶段用来“防止犯错”的“核对表”。**

就像飞机起飞前飞行员要检查仪表、空乘要检查行李、地勤要检查跑道——每个岗位都有自己的 checklist。

📌 **你的团队越复杂，越需要这些“防呆”清单。**

---

如果你愿意，我可以帮你生成一套完整的 `checklists/` 目录结构模板，包含所有常见场景的 Markdown 文件！

---

## 依赖关系

以下是提取的内容及讲解：

### 一、提取内容
|Agent|Key Commands|Primary Dependencies|
| ---- | ---- | ---- |
|analyst|*create-project-brief, *perform-market-research, *create-competitor-analysis, *brainstorm, *research-prompt|project-brief-tmpl.yaml, market-research-tmpl.yaml, facilitate-brainstorming-session.md|
|pm|*create-prd, *create-brownfield-prd, *create-epic, *shard-prd, *correct-course|prd-tmpl.yaml, brownfield.prd.tmpl.yaml, brownfield-create-epic.md|
|architect|*create-full-stack-architecture, *create-backend-architecture, *create-front-end-architecture, *create-brownfield-architecture|fullstack-architecture-tmpl.yaml, architecture-tmpl.yaml, front-end-architecture-tmpl.yaml|
|sm|*draft, *correct-course, *story-checklist|create-next-story.md, correct-course.md, story-draft-checklist.md|
|po|*execute-checklist-po, *validate-story-draft, *shard-doc, *create-epic, *create-story|po-master-checklist.md, validate-next-story.md, shard-doc.md|
|qa|*review|review-story.md, technical-preferences.md|
|ux-expert|*create-front-end-spec, *generate-ui-prompt|front-end-spec-tmpl.yaml, generate-ai-frontend-prompt.md| 

### 二、讲解
这是一份关于不同角色（Agent）在项目工作中对应的关键指令（Key Commands  ，可理解为主要工作任务操作）和主要依赖项（Primary Dependencies  ，即开展这些工作所需的模板、文档等支撑材料）的清单，用于清晰界定各角色工作内容和所需资源 ：
- **analyst（分析师）**：主要工作围绕项目前期准备与调研分析，像创建项目简报、开展市场调研等，依赖项目简报模板、市场调研模板以及头脑风暴引导文档开展工作。 
- **pm（产品经理）**：聚焦产品需求文档（PRD）相关工作，包括创建不同类型PRD、创建史诗故事（epic，敏捷开发中较大的用户故事）等，依赖各类PRD模板和创建史诗故事的指引文档 。 
- **architect（架构师）**：负责搭建软件不同层面架构，从全栈到前后端等，依赖对应架构设计的模板文件，规范架构设计产出 。 
- **sm（敏捷教练/迭代经理 ，Scrum Master ）**：侧重用户故事相关流程，如起草故事、修正流程、检查故事清单，依赖故事创建、流程修正、清单检查的文档材料 。 
- **po（产品负责人，Product Owner ）**：围绕产品待办事项等工作，执行检查清单、验证故事草稿、分片文档（shard-doc ，可理解为拆分梳理文档 ）、创建史诗和用户故事，依赖产品负责人检查清单、故事验证、文档分片等相关文档 。 
- **qa（质量保证/测试人员，Quality Assurance ）**：主要工作是评审，依赖评审故事的文档和技术偏好说明文档，明确评审依据和技术侧要求 。 
- **ux-expert（用户体验专家）**：专注前端相关规范和界面交互设计准备，创建前端规范、生成UI设计提示，依赖前端规范模板和生成AI前端提示的文档 ，辅助设计出符合体验要求的前端界面 。 

简单来说，就是一个团队不同岗位分工及工作所需“工具包”（依赖项）的说明，让各角色清楚知道自己要做什么，以及需要用哪些模板、文档来开展工作 。 

---

