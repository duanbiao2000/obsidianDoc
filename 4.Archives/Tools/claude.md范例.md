---
aliases:
date: 2025-09-11 21:41
tags: ["Domain/Cognitive/Tools", "Type/Reference"]
source:
  - https://github.com/grahama1970/claude-code-mcp-enhanced/blob/main/
update:
rating:
view-count: 6
---

## 🔗 相关链接

**上级索引**:
- [[4.Archives\Tools\_Index_of_Tools.md|Tools]]
- [[4.Archives\_Index_of_4.Archives.md|4.Archives]]

---

## 🧠 一句话总纲（Executive Summary）

> **这是一个“防 Agent 失控、防假验证、防工程腐烂”的强约束开发规范。**  
> 核心目标不是「写得优雅」，而是：  
> **任何代码，在任何时间点，都能被验证、被接管、被延续。**

---

## 🔴 第一性原则（最重要的 6 条）

### 1️⃣ 真实性 > 一切（Reality over Ritual）

- **只允许真实数据**
    
- **禁止 Mock 核心逻辑**
    
- **禁止 MagicMock**
    
- **禁止“看起来通过”的测试**
    

👉 你不是在“证明代码正确”，  
你是在**证明它在现实世界能跑**。

---

### 2️⃣ 验证先于一切（Verification First）

执行顺序被强制定义为：

```
能跑
→ 验证结果对不对
→ 再考虑测试
→ 再考虑 lint / 风格
```

反直觉但正确：

> **测试是未来保障，不是当前正确性的来源。**

---

### 3️⃣ 失败必须被完整记录（Failure Accounting）

- 不允许“遇到第一个错误就停”
    
- **必须统计：**
    
    - 总测试数
        
    - 失败数
        
    - 每一条失败的具体原因
        
- 成功信息 **必须是条件触发**
    

👉 这是工程化思维，不是学生作业。

---

### 4️⃣ Agent = 严格执行者，不是自由创作者

- **所有 Agent 指令具有最高优先级**
    
- 本文档 > 任何历史 prompt / 个人习惯
    
- 不符合标准 = 不允许交付
    

👉 本质：  
**你在训练一个可控的软件工程代理，而不是聊天机器人。**

---

### 5️⃣ 可接管性（Continuity）是硬指标

通过以下机制保证：

- 单文件 ≤ 500 行
    
- 强文档头（目的 / 输入 / 输出 / 依赖）
    
- mirror 目录结构（src / tests / examples）
    
- uv + pyproject.toml（锁死依赖）
    

👉 一个陌生工程师 **明天就能接手**，这是成功标准。

---

### 6️⃣ 约束 async / import / CLI 是为了避免“隐式复杂度”

- ❌ 函数里 `asyncio.run`
    
- ❌ try/except import 核心依赖
    
- ✅ 所有 CLI 必须 typer
    
- ✅ 所有日志必须 loguru
    

不是教条，是为了：

> **把隐式失败点，全部拉到显式层。**

---

## 🧩 模块级最小合规模型（Mental Checklist）

**每个 `.py` 文件，本质上都是一个“自证正确的单元”**

它必须回答 5 个问题：

1. **我存在是为了什么？**（文档头）
    
2. **我依赖什么？**（明确 import + 文档链接）
    
3. **我处理什么真实输入？**
    
4. **我在 main 里能不能被直接跑？**
    
5. **如果我错了，错误能不能被完整看到？**
    

不能回答其中任何一个 → 不合规。

---

## 🧪 Validation 的真正含义（很多人会误解）

这套规范里的「Validation」≠ 单元测试  
而是：

> **可重复、可审计、可失败的最小真实运行证明**

所以才会有这些“看似偏执”的规则：

- 禁止 unconditional success message
    
- 禁止只测 happy path
    
- 禁止提前 exit
    
- 必须 exit code 区分成功 / 失败
    

这不是为 CI  
这是为 **工程信任链**

---

## 📦 包管理与依赖哲学（隐藏但关键）

- uv + lock file
    
- research first
    
- 95% 用原生能力，5% 定制
    
- 文档链接必须写进代码
    

👉 含义很简单：  
**你不是在“用库”，你是在“背书库”。**

---

## 🚦 隐含的工程成熟度判断

如果一个开发者/Agent：

- 抱怨“不能 mock 很麻烦”
    
- 觉得“先 lint 再说”
    
- 想跳过 main validation 直接写 tests
    
- 想 try/except import 来兜底
    

结论很直接：  
👉 **工程成熟度不足，不应放权给 Agent。**

---

## 🧠 最终压缩成一句话

> **这不是 Coding Standard，  
> 这是一套“防止 AI + 人类 联手自欺”的工程约束系统。**

冷酷一点说：  
它假设你、我、Agent **都会犯错**，  
所以它不相信任何“我觉得没问题”。
