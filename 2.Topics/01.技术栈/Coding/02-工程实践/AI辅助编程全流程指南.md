---
date: 2025-05-30 14:38
rating: 2.5
source:
- https://www.youtube.com/watch?v=MBaTuJfICP4
tags:
- structured-documentation
- contextual-encoding
- ai-content-creation-process
- ai-agent-development
- Domain/AI
- Domain/AI/Agent
- Domain/AI/ContentCreation
- Domain/Technology/Programming
- Type/Reference
- Status/Done
view-count: 7
---
# [[AI 辅助编程全流程指南]] | Minimal

---

## 0. 本质 (The Essence)
- **核心逻辑**：AI 编程 = 结构化文档驱动 + 模块化任务闭环。
- **定位**：拒绝“盲目对话”，用文档管理 AI 的上下文，确保生产级代码质量。
- **价值点**：通过 `PLANNING.md` 锁死架构，通过 `TASK.md` 锁死进度。

---

## 1. 核心文档矩阵

| 文档 | 核心目的 | 价值 | 吐槽 |
| :--- | :--- | :--- | :--- |
| **`PLANNING.md`** | 架构、约束、技术栈 | 项目的“灵魂锚点” | 防止 AI 随着对话深入而“降智” |
| **`TASK.md`** | 任务看板、Backlog | 进度的“精确刻度” | 消除“下一步该干什么”的迷茫 |
| **`.cursorrules`**| 全局行为准则 | 强制执行的“紧箍咒” | 相当于给 AI 预装了一个高级工程师的大脑 |

---

## 2. 逻辑骨架 (Workflow Skeleton)

### **A. 规划阶段 (Planning)**
- 在写代码前，先与 AI 磨合出 `PLANNING.md`（高层架构）和 `TASK.md`（首批任务）。

### **B. 全局约束 (Global Rules)**
- 将“文件不过 500 行”、“必须写 Unit Test”、“遵循 PEP8”等规则写入 IDE 的全局规则配置中。

### **C. 初始 Prompt (The Big Bang)**
- **公式**：`引用文档 (@docs) + 参考示例 (Similar Examples) + 明确目标 + 环境约束`。
- **核心**：让 AI 模仿优秀的现有实现。

### **D. 迭代开发 (Modular Prompting)**
- **黄金原则**：一个 Prompt 只处理一个任务。
- **流程**：`修改代码 -> 更新 TASK.md -> 验证效果`。

---

## 3. 避坑指南 (Brutal Truths)

- **文件不过 500 行**：这是 AI 逻辑自洽的红线，过长必产生幻觉。
- **勤开新对话**：上下文污染是 Bug 的温床，任务完成后立即 Reset 会话。
- **环境变量手动配**：严禁把 API Key 喂给 AI，它真的会帮你提交到 GitHub。
- **一次只改一个文件**：跨文件修改极其容易导致逻辑断裂，尽量引导 AI 聚焦。
- **别信 AI 的测试结果**：它说“测试通过”不代表真的通过，必须在本地终端亲自运行。

---

## 4. 任务决策树

1. **项目刚启动？**
    - → 构建 `PLANNING.md`，提供 2-3 个相似项目的代码片段作为参考。
2. **需要新增功能？**
    - → 检查 `TASK.md`，发送单点指令：“根据规划，现在实现功能 X，完成后更新任务列表”。
3. **遇到复杂 Bug？**
    - → 强制 AI 先写 `Pytest`（Mock 外部依赖），复现 Bug 后再修复。
4. **准备部署？**
    - → 引导 AI 编写 Dockerfile。AI 对标准化容器配置的准确率接近 100%。

---

## 5. 执行检查清单 (Final Checklist)

- [ ] **Context**: 每一轮对话开始都让 AI 先读 `PLANNING.md` 吗？
- [ ] **Atomicity**: 这个指令是否包含超过 2 个逻辑改动？（若是，请拆分）
- [ ] **Security**: 代码中是否有硬编码的敏感信息？
- [ ] **Traceability**: 任务完成后，`TASK.md` 和 `README.md` 更新了吗？
- [ ] **Verification**: 每个新功能是否都对应至少一个失败测试用例和一个边缘案例？

---

**原则**：你才是架构师，AI 只是高产的打字员。文档是连接你们唯一可靠的契约。

### AI 交互：一种即时编程模型

- 与 AI 交互是编程，而非提问
- 身份转变：从“提问者”到“程序员”
- 核心原则：上下文即代码
- 交互本质：通过约束工程，收窄无限可能性
- Prompting 类似调用一个文档不全的 API
- 指定角色 = 限定进程权限 (`chroot`)
- 提供上下文 = 为函数传递参数
- 思维链 = 调试时打印中间变量 (`print()`)
- 迭代式提问 = 敏捷开发
* **define** 问题空间与成功标准，如同编写 PRD
* **design** 清晰的逻辑结构与执行步骤
* **write** 具体、无歧义的指令
* **use** 思维链来调试 AI 的逻辑过程
* **iterate** 提示词，而非追求一次性完美
* **focus** 80% 的精力构建上下文
* **apply** 精确约束以引导输出