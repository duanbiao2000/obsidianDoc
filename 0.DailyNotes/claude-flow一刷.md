---
aliases:
date: 2025-11-04 21:58
tags:
  - Status/TODO
source:
  - https://github.com/duanbiao2000/claude-flow/commit/e25f21bfa0c16f6ee2224ddbb4ecf9deb20b1ccd
update:
rating: 10
related:
---

> [!NOTE]
> 
> ## Best practices:
>
> [](https://github.com/duanbiao2000/claude-flow/blob/e25f21bfa0c16f6ee2224ddbb4ecf9deb20b1ccd/.claude/agents/architecture/system-design/arch-system-design.md#best-practices)
> 
> - Consider non-functional requirements (performance, security, scalability)
> - Document ADRs (Architecture Decision Records) for major decisions
> - Use standard diagramming notations (C4, UML)
> - Think about future extensibility
> - Consider operational aspects (deployment, monitoring)
> ## Deliverables:
> 1. Architecture diagrams (C4 model preferred)
> 2. Component interaction diagrams
> 3. Data flow diagrams
> 4. Architecture Decision Records
> 5. Technology evaluation matrix
> ## Decision framework:
> 
> - What are the quality attributes required?
> - What are the constraints and assumptions?
> - What are the trade-offs of each option?
> - How does this align with business goals?
> - What are the risks and mitigation strategies?

## ADRs 架构决策记录
ADRs（Architecture Decision Records，架构决策记录）是记录软件架构关键决策的文档化工具，核心目的是**留存决策背景、过程和结果**，解决“为什么这么设计”的问题，避免后期因人员变动、时间推移导致决策逻辑丢失。

其核心价值体现在3个方面：
1. **追溯性**：明确决策的发起原因（如业务需求、技术瓶颈）、评估的方案（含被否决的选项）、最终选择及理由，后续维护或迭代时可快速理解设计初衷；
2. **协作性**：作为团队共识载体，减少新人融入时的“重复提问”，也为跨团队同步架构逻辑提供统一依据；
3. **演进性**：当业务或技术环境变化需调整架构时，ADRs可作为“历史基准”，帮助判断旧决策是否仍适用，避免盲目重构。

一份标准ADR通常包含关键模块（不同团队可能略有差异）：
- **标题**：明确决策主题（如“采用微服务架构拆分用户中心模块”）；
- **背景（Context）**：说明决策的前提（如业务用户量增长、单体架构扩容困难）；
- **选项（Alternatives）**：列出所有考虑过的方案（如“方案1：单体架构优化；方案2：微服务拆分；方案3：Serverless架构”）；
- **决策（Decision）**：明确最终选择的方案；
- **理由（Rationale）**：解释为何选此方案、为何否决其他选项（如“微服务拆分可支持独立扩容，虽增加运维成本，但符合3年内用户增长预期”）；
- **影响（Implications）**：说明决策带来的正面（如弹性扩容）与负面（如分布式事务挑战）影响，及后续应对措施。

ADRs并非“一次性文档”，而是随架构演进动态更新——若后续决策推翻旧方案，需新增一份ADR说明“变更原因”，而非直接修改旧文档，确保架构演进轨迹可完整追溯。

## 图示表示法

以下为你分别用 **C4 模型**和 **UML 图**（以类图、用例图为例）的标准图示说明，可根据业务场景选择适用的 notation：  
  
  
### 一、C4 模型（用于系统架构可视化，分层次描述）  
C4 模型通过 4 个层次（Context、Container、Component、Code）展示系统架构，以下以“数据分析与客户管理系统”为例：  
  
#### 1. 语境图（Context Diagram）  
- **核心元素**：  
- 外部参与者：`客户（Person）`、`销售团队（Person）`、`财务系统（System）`  
- 目标系统：`客户与销售数据分析系统（System）`  
- **关系**：  
- 客户与系统：`提交订单、查看支付状态`  
- 销售团队与系统：`录入订单、管理客户类型`  
- 系统与财务系统：`同步订单支付数据`  
  
  
#### 2. 容器图（Container Diagram）  
- **核心容器**：  
- `Web 应用（Container）`：供客户、销售团队访问的界面，包含“订单管理模块”“客户类型管理模块”  
- `数据存储（Container）`：存储客户、订单、支付数据的数据库  
- `API 服务（Container）`：对接财务系统的支付数据同步接口  
- **关系**：  
- Web 应用 ↔ 数据存储：`读写客户、订单、支付数据`  
- Web 应用 ↔ 销售团队/客户：`HTTP 交互（界面操作）`  
- API 服务 ↔ 数据存储：`读取支付数据`  
- API 服务 ↔ 财务系统：`同步支付状态`  
  
  
#### 3. 组件图（Component Diagram）  
以“Web 应用”容器为例，拆解内部组件：  
- **组件**：  
- `订单管理组件`：处理订单创建、查询  
- `客户类型组件`：维护 Lead/Contact 类型，关联客户信息  
- `支付状态组件`：展示订单支付标记（如表格中“x”）  
- `数据访问组件`：封装与数据库的交互逻辑  
- **关系**：各组件通过内部接口（如函数调用、事件总线）交互，共同支撑 Web 应用功能。  
  
  
### 二、UML 图（以类图、用例图为例）  
#### 1. 用例图（Use Case Diagram）  
- **参与者（Actor）**：`客户（Customer）`、`销售专员（Salesperson）`、`财务系统（External System）`  
- **用例（Use Case）**：  
- 客户：`创建订单`、`查询支付状态`  
- 销售专员：`录入订单`、`修改客户类型（Lead/Contact）`、`统计订单支付情况`  
- 系统间：`财务系统同步支付数据`  
- **关系**：参与者与用例通过“关联（Association）”连接，体现谁执行什么操作。  
  
  
#### 2. 类图（Class Diagram）  
- **核心类**：  
- `Customer`：属性（firstName, customerType）、方法（viewOrder(), checkPayment()）  
- `Order`：属性（salesOrderName, isPaid）、方法（markAsPaid()）  
- `Salesperson`：方法（createOrder(), updateCustomerType()）  
- `PaymentSystem`：方法（syncWithFinance()）  
- **关系**：  
- `Customer` 与 `Order`：`关联（Association）`（一个客户可对应多个订单）  
- `Salesperson` 与 `Order`：`关联（Association）`（销售创建订单）  
- `PaymentSystem` 与 `Order`：`依赖（Dependency）`（支付系统更新订单支付状态）  
  
  
若需更具体的场景（如聚焦“订单支付数据分析”“客户类型转化分析”），可进一步细化上述图示的组件、类或用例。