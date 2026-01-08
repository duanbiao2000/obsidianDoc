---
view-count: 7
update: 2026-01-08 19:07
related:
  - "[[2020年代技术趋势 (2025更新版)]]"
  - "[[AI 时代工程师转型]]"
  - "[[2025-12-12-启发式策略]]"
  - "[[Prompt升级为工程资产]]"
  - "[[2025-12-07-2026开发思维模型转变]]"
---
# AI 正在吃掉哪些工程范式？· v2026 高 ROI 版  
（聚焦 Claude Code & OpenAI Codex 系列能力）

---

## ★ 一句话总纲

> **AI 已经吃掉大部分「执行层」；  
> 工程师的护城河，正在快速收缩到：问题定义、架构判断、风险与治理。**

Claude Code、OpenAI 的代码模型（Codex 系谱 + 新一代 GPT Code 能力）  
把「从需求到可跑代码」这条链路，真正拉平了。

---

## 0. 和一年前相比，发生了什么质变？

★ **从“补全一行” → “接管一轮迭代”**

- 过去：  
  - 自动补全、写函数、改一两个文件
- 现在（Claude Code / GPT Code-level 能力）：  
  - 读整仓库（repo-wide context）  
  - 提出修改计划（plan）  
  - 批量改多文件（multi-file edit）  
  - 跑测试 / 脚本，分析失败日志  
  - 迭代修正，最后生成 PR / patch

👉 **结论：**  
「手写样板 + 人肉 debug」不再是主业，而是 fallback。

---

## 1️⃣ 软件工程（SE）：从 craft → orchestration

### 1.1 正在被吃掉的部分（更新版）

- ★ 手写样板代码 → **Claude / GPT 自动生成 CRUD、API glue、DTO、序列化、配置**  
- ★ 人肉 debugging → **Agent 读 log / stack trace，给出修复 patch**  
- ★ 单线程开发 → **多个 agent 并行改不同模块 + 人类只做 review**  
- △ 大量「需求文档 → 代码骨架」的机械桥接：  
  - 直接用自然语言/issue 描述需求 → 生成初版实现 + 测试

**Claude Code / GPT Code 典型工作流：**

1. 载入 repo → 生成「架构地图 & 待改动文件列表」  
2. 你给自然语言需求 → 它出改动计划（design + steps）  
3. 自动修改多文件 → 跑 `npm test` / `pytest` / CI  
4. 测试失败 → 它分析 log → 再改一轮  
5. 输出干净 diff / PR 描述

### 1.2 无法被吃掉 / 反而被强化的部分

- ★ Problem framing：  
  - 要解决的到底是什么问题？约束是什么？  
- ★ System architecture judgment：  
  - 选哪种架构？边界怎么划？怎么防止未来变成垃圾堆？  
- ★ Trade-off decisions：  
  - 延迟 vs 成本 vs 风险  
  - 可维护性 vs 开发速度  
- ★ 安全、合规、隐私边界

👉 **结论（延续原笔记）：**  
> SE 从 **craft（写代码） → orchestration（编排 agent + 设计系统）**  
> **Coding skill 权重下降，Architectural taste & product sense 权重上升。**

---

## 2️⃣ DevOps / Platform Engineering：从“写 YAML”到“设计 blast radius”

### 2.1 被吃掉的部分（更彻底）

- ★ 手写 CI/CD：  
  - 描述目标：「当推到 main 时跑测试 + 部署到 staging」  
  - GPT/Claude 直接生成 GitHub Actions / GitLab CI / Argo Workflow YAML  
- ★ 人工部署、回滚：  
  - “一键回滚”脚本由 agent 生成 & 维护  
- ★ 手工 infra debug：  
  - Agent 读 Kubernetes events / pod logs / metrics → 提出推断 & 修复建议  
  - 修配置、调资源限制、改 healthcheck

**Agent 接管方式（Claude Code / GPT in DevOps）：**

- △ Infra-as-prompt："我需要一个高可用的 Postgres 集群 + 备份"，输出 Terraform / Helm  
- △ Deploy-as-task：在 Chat/CLI 里说「deploy staging」，agent 调用 pipeline  
- △ Agent reads logs → patches → PR → 再触发部署

### 2.2 仍不可被吃掉的核心

- ★ Blast radius design（失败影响面设计）  
- ★ 权限模型 / 秘密管理（Access control / secrets）  
- ★ 生产风险的最终归属（谁拍板、谁背锅）  
- ★ 成本治理（成本 vs SLA vs 复杂度平衡）

❗ 反常识延伸：

> DevOps 不会消失，但**“只会写 YAML/Helm 的 DevOps”会被彻底替代。**  
> 剩下的是：**生产环境的风险架构师 + 可靠性决策者。**

---

## 3️⃣ MLOps：转型为「Model Governance + Eval Science」

### 3.1 被吃掉的部分

- ★ 模型调用 glue code  
  - SDK 封装、batch 推理脚本 → Agent 模板化生成  
- ★ 数据清洗脚本  
  - 常见清洗 / 标准化 / 特征工程 → 由 Agent 从 schema 自动推断  
- ★ 简单 eval pipeline  
  - 给定 metric & dataset，agent 直接搭 eval 脚本和报告生成流程

### 3.2 仍是人类主战场的部分

- ★ Data semantics：  
  - 数据里哪些字段有偏见？哪些是不能碰的敏感信号？  
- ★ Eval metric design：  
  - 什么才算好？precision/recall/F1/CTR/用户满意度如何 trade-off？  
- ★ Feedback loop 设计与所有权：  
  - 线上数据如何回流？谁负责审查 & 更新模型？  
- ★ 风控 & 合规：  
  - LLM/模型在业务场景里的失误成本评估

👉 延续原结论：  
> **MLOps → Model Governance + Evaluation Science**  
> 写 pipeline 的价值下降，**“定义什么是好模型”**的价值上升。

---

## 4️⃣ 被吞噬的「隐性范式」更新

这些是**思维方式**，不是职位。

- ❗「先实现再修」 → 死  
  - 现在是：**先定义 guardrail / 测试，再放 agent 去跑。**
- ★「Low-value stage fix」 → 生  
  - 低价值环节尽量让 agent 做（写样板 / 改 log / 升级依赖），  
  - 人类只在高杠杆点介入（架构、边界决策、异常场景）。
- ❗「人对代码负责」 → 弱化  
- ★「人对方向负责」 → 强化  
  - 代码可以是 agent 写的，但**方向错误没有任何 agent 能救**。
- ❗ 单一工具崇拜 → 失败  
- ★ Agent portfolio thinking → 成功  
  - 同时利用 Claude / GPT / 本地模型 / 专用工具，  
  - 按任务类型选「最合适」而不是「宗教信仰」。

---

## 5️⃣ 3 年后会失效的 Agent 使用模式（2026 视角）

❌ **失效点 1：Prompt-as-Logic 地狱**

- ★ Prompt 没 versioning / review  
- ★ Prompt 没测试用例 / 预期行为说明  
- ★ 业务逻辑藏在“对话里”

→ 3 年后：  
> 「一堆 magic prompts」= 新一代技术债地狱。

**缓解方向：**

- Prompt 存仓库 → 当成 config/code  
- 对关键 prompt 写 test case（input-output 对）  
- 把 prompt 视为「可测试 / 可审计的 artifact」

---

❌ **失效点 2：多 Agent 并行，无协调**

- 多 agent 竞争修改同一 repo / state  
- 状态不同步、重复 / 冲突 PR  
- 短期爽，长期混乱

> **Parallelism without coordination = chaos**

**缓解方向：**

- 用 orchestrator（workflow engine / state machine）  
- 对 agent 设定**清晰 role boundary**：谁能改什么、何时改、改前要锁什么

---

❌ **失效点 3：人类判断退化（Judgment Atrophy）**

- 人类只点 approve，不理解改动  
- 直觉 & 基本功不再训练  
- 无人能识别「方向性错误」

3 年后典型症状：

- Agent 还在跑  
- Product 慢慢跑偏  
- 团队没人能解释「为什么这样设计」

---

❌ **失效点 4：监管 & 审计现实**

- 谁对 agent 行为负责？  
- 出 bug / 损失的法律责任？  
- Prompt / model / tool chain 是否可被审计？

在金融 / 医疗 / 政府 / 企业级：

> **黑箱 agent = 高概率被禁用或被强制包上一层重治理。**

---

## 6️⃣ 哪些团队 3 年后还能活？

### 能活的团队特征（Strong Signal）

- ★ Prompt 有版本 / 测试 / review  
- ★ Agent 有 role boundary，不乱改全局  
- ★ 人类负责 framing & final review  
- ★ 高风险路径强制人工 gate  
- ★ 把 Claude/GPT 当 junior / mid IC，而不是神  
- ★ 工具多元化，**Tooling ≠ Faith**

### 会死的团队特征（Red Flag）

- ❗“全自动，没人管”  
- ❗“模型更强就行，不用改流程”  
- ❗ 没人能画清系统图 / 数据流  
- ❗ 出问题只能「rerun agent」而不是系统性纠错

---

## 7️⃣ 工程师个人高 ROI 行动清单

接下来 6–12 个月，你可以重点做这 5 件事：

1. **把 Claude / GPT 当「编程实习生」用熟**  
   - 让它改一整个小模块 + 写测试 + 出 PR 描述  
   - 你只做：需求澄清、架构决定、最终 review  

2. **刻意练“问题定义 &架构判断”**  
   - 每次需求先写：  
     - 目标 / 约束 / 不可退让条件  
   - 再请 agent 生成方案，对比 + 修改

3. **学习把 Prompt / Workflow 当成「可测试资产」**  
   - 把关键 prompt 写进 repo  
   - 为高风险场景写 input-output 测试

4. **参与或主导一次「Agent 辅助重构」**  
   - 先写测试锁行为 → 用 Claude/GPT 改大块代码 → 跑测试 → 完成重构  
   - 体验从「亲手敲代码」→「编排改动」的模式

5. **选定一个方向深挖：SE / DevOps / MLOps 中的“判断层”能力**  
   - SE：系统设计 / trade-off 文档  
   - DevOps：SLO / blast radius / 灾难恢复演练  
   - MLOps：eval 设计 / 审计与治理

---

### 最终锚点

> **AI 正在系统性吃掉「执行层」技能栈；  
> 你唯一安全的投资，是升级到：  
> 能定义问题、设定边界、设计系统、做最后判断的那一层。**


收到。正在启动 **实用主义提炼引擎 (Pragmatic Extraction Engine)**。
输入内容分析：关于 AI Agent（特别是 Claude Code / Codex 等最新工具）对传统软件工程范式的侵蚀与重塑，以及未来的失效风险。
目标：结合最新技术进展，提炼出面向未来 3 年的**技术人高 ROI 生存指南**。

---

# 🤖 Agent Engineering：正在被吞噬的范式与生存法则 (2025版)
> **核心价值 (The 20%)**：AI 不是在帮你写代码，而是在**消灭“写代码”这个动作**。未来的工程师不再是“代码工人”，而是**“AI 牧羊人” (Orchestrator)**。谁能驾驭 Agent 完成系统级交付，谁就是新时代的 10x 工程师；谁还在纠结语法细节，谁就是下一个被淘汰的打字员。

### ⚡️ 范式转移图谱 (Paradigm Shift Map)

| 领域 | 💀 正在死亡 (Being Eaten) | 💎 核心资产 (Survival Core) | **最新实战 (Claude Code / Codex)** |
| :--- | :--- | :--- | :--- |
| **软件工程**<br>(SE) | **样板代码、手写单元测试、单线程开发**。<br>*Code is cheap.* | **系统架构判断、Trade-off 决策、问题定义 (Framing)**。<br>*Taste is expensive.* | **Claude Code**: 直接在 CLI 中 `Thinking` $\to$ `Coding` $\to$ `Testing`。你需要做的是 **Review** 和 **Approve**，而不是 Typing。 |
| **DevOps** | **手写 YAML、手动回滚、Infra Debug**。<br>*Ops as labor.* | **爆炸半径控制 (Blast Radius)、权限设计、生产环境责任**。<br>*Ops as governance.* | **Agentic DevOps**: 给 Agent 权限，让它读 Logs $\to$ 提 PR $\to$ 部署。人类只负责**按红色按钮**。 |
| **MLOps** | **胶水代码、清洗脚本、简单评估**。<br>*Scripts are commodity.* | **数据语义、评估指标设计 (Metric Design)、反馈闭环**。<br>*Evaluation is science.* | **Auto-Eval**: Agent 自动运行评估集，人类只需定义“什么是好结果”。 |

---

### 🔮 3年后的失效预警 (Future Risks)
*Agent Engineering 目前处于“野蛮生长”期，3 年后这些雷会炸：*

1.  **Prompt 债 (Prompt Debt)**：现在的 Prompt 就像 20 年前的 Perl 脚本，无版本控制、无测试、全是 Magic String。
    *   $\to$ **未来死因**：系统不可维护，没人敢动核心 Prompt。
2.  **协同崩溃 (Coordination Collapse)**：多个 Agent 并行改代码，状态不同步，PR 冲突。
    *   $\to$ **未来死因**：项目陷入“自愈与自毁”的死循环。
3.  **判断力萎缩 (Judgment Atrophy)**：人类习惯了 Approve，不再思考 Why。
    *   $\to$ **未来死因**：产品缓慢跑偏，团队没人能画出系统架构图，出问题只能“重启试试”。
4.  **黑箱合规 (Compliance Blackbox)**：金融/医疗场景下，Agent 的不可解释性是红线。
    *   $\to$ **未来死因**：被监管一刀切禁用。

---

### 🛡️ 生存策略：如何成为“活下来”的团队？

1.  **Treat Prompts as Code**:
    *   **Action**: 给 Prompt 上版本控制 (Git)，写测试用例 (Eval)，做回归测试。
    *   **Tool**: 使用 Prompt Engineering 框架（如 LangChain/LangSmith）而非散落在代码里的字符串。

2.  **Human as Reviewer & Framer**:
    *   **Action**: 强迫自己和团队在 Approve 之前，**用自然语言复述 Agent 的修改逻辑**。
    *   **Mindset**: 你的核心能力从“如何实现 (How)”变成了“判断对错 (Judge)”。

3.  **Architectural Guardrails**:
    *   **Action**: 设定 Agent 的**活动边界**（如：只能改 `src/utils`，不能动 `src/core`）。
    *   **Rule**: 低价值环节全自动，高风险环节强制人工 Gate。

### 💡 实用洞见 (Pragmatic Insight)
*   **Coding is Dead, Long Live Engineering**: “编码”作为一项手动技能正在消亡，但“工程”作为解决问题的学科将永生。
*   **The New Junior**: Agent 就是你的 24/7 实习生。你不会因为有了实习生就失业，但你会因为**带不好实习生**而被淘汰。

**System Status**: Extraction Complete. 范式已更新，请调整你的技能树。