---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
view-count: 8

tags: ["Domain/AI/PromptEngineering", "Type/Reference"]

---
### 核心逻辑：心智模型优先
**原则**：理解“为什么” > 追踪“怎么做”；运行代码 > 静态阅读；鸟瞰全景 > 放大细节。

---

### 🛠️ 三层递进理解法 (The 3-Layer Ladder)

| 层次 | 重点 | 核心行动 (Action) | 关键产出 |
| :--- | :--- | :--- | :--- |
| **L1: 目标/设计** | **本质** | 阅读 README + 扫描文件树 + 锁定入口点 (Entry) | 一句话定义项目 + 核心数据流 |
| **L2: 抽象/逻辑** | **模式** | 识别 Top 5 核心类/函数 + 设计模式 + 依赖拓扑 | 关键调用链路 + 80% 业务逻辑 |
| **L3: 验证/细节** | **深度** | Debugger 单步追踪 + 阅读测试用例 + Git Blame | 边界处理 + 设计权衡 (Trade-offs) |

---

### 🎯 实战场景校验 (Scenario Matrix)

- **Code Review**: 解决什么问题？改动是否符合架构约定？测试是否覆盖边界？
- **Onboarding**: 如何本地运行？某个功能在哪个文件改？谁是该模块的专家？
- **开源库学习**: 设计哲学是什么？主要 API 模式？内部如何处理高性能/高并发？

---

### ⚠️ 陷阱与应对 (The Anti-Traps)

- **细节黑洞**: 严禁在未建立 L1 模型时逐行读代码。
- **静态错觉**: 代码不等于文档。**立即运行**，通过 Debug 观察变量变化，速度快 10 倍。
- **假设偏见**: 永远通过测试用例验证你的“想当然”。

---

### 🚀 极简行动指南

1. **5min 扫盲**: 文件夹组织逻辑 + 顶层配置 (`package.json`/`requirements.txt`)。
2. **10min 追踪**: 找一个核心请求，从入口点追踪到数据库操作。
3. **15min 实验**: 修改一行代码，运行测试，看报错是否符合预期。
4. **归档**: 用 3-5 个关键概念描述整个系统的“骨架”。

---

### 关联笔记
- [[认知负荷管理]]：通过分层降低理解代码时的瞬间认知压力。
- [[第一性原理思维]]：透过语法糖直击系统的底层设计目标。