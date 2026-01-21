---
view-count: 2
---
## 极简版（brutally minimal）

你现在的问题不是“笔记质量”，是**集成失败**：  
- RSA（学习法）= 有 `main()` 但回调全是 TODO  
- Prompt Patterns = 有 `std::think` 标准库但从不被调用  
目标：把两者装配成可运行的 **Personal Cognitive OS**。

---

# 0. 系统定义（形式化）

- **MLA（Master Learning Algorithm）**：顶层学习循环（有状态）
- **RSA 九招**：MLA 的抽象接口 / 回调
- **Prompt Pattern**：`std::think` 子程序库（确定性、可复用、输入→结构化输出）
- **学习技能**：实例化一个进程  
  `MLA.execute({ skill, target_level })`

---

# 1. 核心改动（把“招数”变“系统调用”）

RSA Move → `std::think` Call → 目的

- 元学习 → First-Principles Breakdown → 初始化路径/拆技能
- 专注 → Action Strategy Conversion → 把目标变最小动作
- 直接性 → Future Consequences → 选最短有效路径
- 钻研 → Concept Deep-Dive → 深挖关键概念
- 检索 → Feynman Technique → 强制提取+重编码
- 反馈 → Devil’s Advocate / Socratic → 压测理解（找 bug）
- 保留 → Mental Model Extractor → 压缩成可复用模型
- 直觉 → Cross-Pollination → 跨域连接，形成高层抽象
- 实验 → Post-Mortem → 实战复盘，迭代策略

结论：RSA 负责**控制流**；Pattern 负责**实现**。

---

# 2. 部署方案（Obsidian：OS v1.0）

## Phase 1：建库（`std::think`）
1) 建目录：`_templates/`（或 `_patterns/`）  
2) 每个 Pattern 一文件：  
   - `_templates/Concept Deep-Dive.md`  
   - `_templates/Feynman Technique.md`  
3) 每个模板参数化：用占位符（`{{concept}}`, `{{goal}}`）

## Phase 2：实例化进程（每个技能一个“主控面板”）
新建：`Learning_<Skill>.md`

```markdown
---
skill: Go
status: in-progress
start_date: 2025-05-20
target_level: Build a simple web service
---

# Learning: Go

## 1 Meta-Learning
Call: First-Principles Breakdown
![[ _templates/First-Principles Breakdown.md ]]

## 2 Drill
Call: Concept Deep-Dive + Feynman
- [[Go_Goroutines]]
- [[Go_Channels]]
- [[Go_Interfaces]]

## 3 Feedback
Call: Devil's Advocate / Socratic
![[ _templates/Devils Advocate.md ]]

## 4 Experiment
Call: Post-Mortem
- Project: Simple CLI
- Post-Mortem: [[PM_Go_CLI]]

## 5 Retention
Call: Mental Model Extractor
- [[Go_Core_Mental_Model]]
```

## Phase 3：日常执行（你不“学习”，你“跑进程”）
- 每天只打开 `Learning_<Skill>`  
- 按 Phase 调模板、填空、产出笔记/代码/复盘  
- 完成一个 Phase 就更新状态并推进

---

# 3. 最终动作（下一步就做）
1) 建 `_templates/`  
2) 把 10 个 Pattern 拆成独立模板文件  
3) 为当前技能建 `Learning_<Skill>`  
4) 先跑一次：`First-Principles Breakdown`
