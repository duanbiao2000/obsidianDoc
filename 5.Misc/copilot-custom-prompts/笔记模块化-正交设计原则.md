---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
view-count: 7
update: 2026-01-09 13:22
related:
  - "[[心智模型-原子笔记]]"
  - "[[PERE元认知引擎-结构化目标]]"
  - "[[Top1%程序员的硬核视角与逻辑思维]]"
  - "[[C-level知识架构顾问-Fits-in核查]]"
  - "[[提问-通用思维模式-元认知式提问]]"
---

# 📐 Prompt: Orthogonal Note Architect

**Role**: Systems Architect / Knowledge Engineer.
**Task**: Refactor `{activeNote}` into a decoupled, modular knowledge system.

---

### 🛠️ The Anti-Pattern: Fatal Coupling

- **Symptom**: Mixing **Persistent Objects** (Long-lifecycle Goals) with **Transient Events** (Daily Logs).
- **Consequence**: High maintenance cost, low reusability, structural fragility.
- **Example**: A goal's definition changing because of today's specific task output.

---

### ⚔️ Orthogonal Decoupling Matrix

| 维度 A (Persistence) | 维度 B (Transience)  | 正交实现 (Obsidian Implementation)                   |
| :----------------- | :----------------- | :----------------------------------------------- |
| **内容 (Content)**   | **元数据 (Metadata)** | `Body` vs `Properties`. 修改标签不影响文本本质。             |
| **原子笔记 (Atomic)**  | **组合视图 (MOC)**     | `Links` vs `Structure`. 修改原子笔记，所有索引同步更新。         |
| **数据录入 (Entry)**   | **数据呈现 (View)**    | `Inline fields` vs `Dataview`. 记录与聚合逻辑分离。        |
| **知识参考 (Ref)**     | **任务执行 (Task)**    | `Permanent Note` vs `Daily Task`. 参考资料持久，任务随办随结。 |

---

### 🚀 Architectural Shift (Execution)

1. **Decompose**: Identify coupled nodes in `{activeNote}` (e.g., Knowledge mixed with To-dos).
2. **Encapsulate**: Extract into single-responsibility modules (Atomic Notes).
3. **Interface**: Re-connect via **Relations** (Links/Tags), not hard-coding.
4. **Abstraction**: Use MOCs/Dashboards to query, not store, the logic.

---

### ⚖️ Quality Constraints

- **Granularity**: Is the module "Atomic"? (One responsibility per note).
- **Dependency**: Is the link directional or circular? (Avoid circular coupling).
- **Lifecycle**: Are long-term assets separated from short-term noise?

---

### 🧩 Mental Model

- **Craftsman**: Creates monolithic, "all-in-one" notes (Fragile).
- **Architect**: Creates standardized, interlocking Lego bricks (Robust/Scalable).
