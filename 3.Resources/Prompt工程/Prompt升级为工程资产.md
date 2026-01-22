---
view-count: 3
update: 2026-01-20 22:11
related: null
important: true
tags:
  - workflow-design
  - agent-roles
  - prompt-engineering
  - specification
rating: 10
---

## 一、阶段 0：Prompt（当下主流，但天生不稳）

### Prompt 的真实定位

> Prompt = **Un-typed, Un-tested, Implicit Logic**

### 核心特征

- ★ 自然语言即逻辑

- ★ 人读得懂，机器“猜”

- ❗ 隐含假设多

- ❗ 无边界、无约束

### 适用场景

- △ 探索期

- △ 一次性任务

- △ 个人效率 boost

### 必然问题

- ❗ Prompt Drift（模型变了，结果全变）

- ❗ Prompt Rot（作者走了，没人敢改）

- ❗ Prompt-as-code → 技术债

**一句话：**

> Prompt 是 prototype，不是 production。

---

## 二、阶段 1：Spec（Prompt 的“工程化形态”）

### Spec 是什么？

> Spec = **Explicit, Reviewable, Testable Intent**

不是写得更长的 prompt，而是**结构化意图声明**。

---

### Prompt → Spec 的关键跃迁

#### 1️⃣ 从「说话」→「声明约束」

- ★ Input schema

- ★ Output schema

- ★ Invariants（不能违反的规则）

- ★ Failure modes

```text
Input: user_story
Output: PR + tests
Constraints: no breaking API
```

---

#### 2️⃣ 从「感觉对」→「可评估」

- ★ Acceptance criteria

- ★ Eval metrics

- ★ Golden cases

❗ **没有 eval 的 spec = 祈祷**

---

#### 3️⃣ 从「单一文本」→「模块化」

- △ Research spec

- △ Planning spec

- △ Execution spec

👉 每个 spec 都可以单测。

---

### Spec 的本质变化

- ★ 意图外显

- ★ 逻辑显性

- ★ 人类可 review

- ★ 模型可替换

**这一步，相当于：**

> Prompt → API contract

---

## 三、阶段 2：Executable Workflow（真正的 Agent Engineering）

### Workflow 是什么？

> Workflow = **Spec + State + Control Flow**

也就是：\
**意图 + 状态机 + 可执行路径**

---

### 核心升级点

#### 1️⃣ 控制流外置（Control ≠ LLM）

- ★ If / Else

- ★ Retry / Abort

- ★ Human gate

❗ LLM 不负责 control，只负责 cognition。

---

#### 2️⃣ 状态显性化（State is king）

- ★ 当前阶段

- ★ 中间产物

- ★ 决策记录

→ 避免 agent「失忆 + 幻觉推进」

---

#### 3️⃣ Agent 角色边界

- ★ Research agent

- ★ Planner agent

- ★ Executor agent

- ★ Reviewer agent

👉 单 agent = chaos\
👉 Multi-agent + roles = system

---

### Workflow 的工程属性

- ★ 可 version

- ★ 可 replay

- ★ 可 audit

- ★ 可 fail fast

这一步，本质是：

> Prompt → Program\
> Agent → Runtime

---

## 四、为什么这是**不可逆路径**

### 3 年内的必然演化压力

- ❗ 合规 / audit

- ❗ 规模化并行

- ❗ 人员流动

- ❗ 模型频繁升级

**Prompt 无法承受这些压力。**

---

### 类比历史（很重要）

- Prompt ≈ Shell command

- Spec ≈ API / Interface

- Workflow ≈ Distributed system

你不会用 `bash script` 跑银行核心系统。\
Prompt 的命运一样。

---

## 五、最终形态（Forward-looking）

### 稳定的 Agent Stack 会长这样：

- ★ Prompt = exploration only

- ★ Spec = source of truth

- ★ Workflow = execution fabric

- ★ Human = gatekeeper & judge

- ★ Eval = regression test

**一句狠话：**

> Prompt 不会消失，但它会退回到“草稿纸”的位置。

---

## 六、给你一个判断标准（超实用）

问团队一句话就够了：

> **“如果换模型 / 换人 / 半年后重跑，这套 agent 还能工作吗？”**

- ❌ 不能 → 你在 Prompt 地狱

- ✅ 可以 → 你在 Workflow 时代

---

如果你愿意，下一步我可以直接帮你：

- 🧱 设计一个 **Prompt → Spec → Workflow 的最小可行架构**

- 🧪 给你一套 **Spec / Eval 的模板**

- 🧠 或拆解 **哪些公司已经在偷偷走这条路**

你点哪个？
