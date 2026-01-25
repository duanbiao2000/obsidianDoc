---
view-count: 4
tags:
  - DocstringStandards
  - CommentBestPractices
  - TechnicalWriting
  - CodeQualityAssessment
  - Type/Reference
  - Domain/Technology
  - DocstringStandards
  - CommentBestPractices
  - TechnicalWriting
  - CodeQualityAssessment
---
# 代码文档化协议：Docstring vs. Comment

## 1. 核心模型
**效能逻辑：$Total\_Clarity = \frac{接口描述 (Docstring) + 意图解释 (Comment)}{代码复杂度}$**

| 维度 | Docstring (文档字符串) | Comment (注释) |
| :--- | :--- | :--- |
| **目标读者** | **代码使用者** (API 调用者) | **代码维护者** (开发者自己/同事) |
| **核心回答** | **“它是什么？怎么用？”** | **“为什么要这么写？”** |
| **可见性** | 运行时可见 (`help()`, IDE 提示) | 仅源码可见 (运行时忽略) |
| **位置** | 类、函数、模块的**第一行** | 代码行内或上方 |
| **约束** | 强规范 (Google/NumPy 风格) | 自由格式 (少即是多) |

## 2. 执行协议 (SOP)

### A. Docstring 编写规范 (User-Facing)
1. **定义行为**：描述函数用途，而非实现步骤。
2. **输入输出**：明确参数含义 (`Args`)、返回类型 (`Returns`) 及可能的报错 (`Raises`)。
3. **示例先行**：提供一个最小可运行示例 (`Example`)，减少用户猜测时间。
4. **准入标准**：所有公共 (Public) 接口必须具备。

### B. 注释编写规范 (Maintainer-Facing)
1. **解释动机**：仅记录非显而易见的逻辑（如：为了兼容旧版本、性能优化的数学原理）。
2. **删除冗余**：禁止用注释解释字面意思（如：`i += 1 # i 加 1`）。
3. **状态标记**：使用规范前缀：
   - `TODO:` 待办事项。
   - `FIXME:` 已知 Bug 需修复。
   - `HACK:` 临时变通方案，需后续重构。

## 3. 质量审计矩阵 (Audit Matrix)

| 场景 | 推荐做法 | 判定标准 |
| :--- | :--- | :--- |
| **复杂算法** | 使用 Comment 解释原理。 | 别人能否在 30 秒内理解逻辑？ |
| **第三方库 Bug** | 使用 Comment + 链接记录 workaround。 | 是否标注了移除该代码的触发条件？ |
| **Public API** | 强制 Docstring。 | 不看源码能否正确调用？ |
| **代码自解释** | 重构变量名，删除多余注释。 | 代码是否像自然语言一样清晰？ |

## 4. 瞬时执行清单 (Checklist)

- [ ] **分工**：Docstring 解释了用法，Comment 解释了动机吗？
- [ ] **去噪**：是否删除了所有“复述代码内容”的废话注释？
- [ ] **规范**：Docstring 是否符合项目统一风格 (如 Google Style)？
- [ ] **时效**：代码修改后，对应的 Docstring/注释 是否同步更新？

---

**关联笔记：** [[代码注释风格]] | [[Python代码注释规范自适应提示词]] | [[道法术器]]