---
aliases:
date: 2025-12-14 13:43
tags:
  - Status/TODO
source:
  - https://claude.ai/public/artifacts/0a767ddd-3d55-4f7a-9c66-f5023e8457d8
update:
rating:
related:
view-count: 3
---

# Prompt 管理系统（Markdown · Git版）

> **核心理念**：通过 Markdown 文件 + Git 版本控制，实现 Prompt 的质量迭代追踪和跨应用复用。
>
> **无需代码脚本 | 一切开箱即用**

---

## 📁 目录结构设计

```
prompts/
├── 00_META/                          # 元数据和管理文件
│   ├── README.md                     # 总览和快速查询
│   ├── STANDARDS.md                  # 质量标准和评估规范
│   ├── CHANGELOG.md                  # 全局更新日志
│   └── INDEX.md                      # 分类索引
│
├── 01_DOCUMENTATION/                 # 文档质量类 Prompt
│   ├── doc_depth_analyzer/
│   │   ├── v1.0_20250101.md
│   │   ├── v2.0_20251115.md
│   │   └── v2.1_current.md           # 当前版本
│   ├── doc_foresight_check/
│   │   ├── v1.0_20250201.md
│   │   └── v1.5_current.md
│   └── README.md                     # 该分类说明
│
├── 02_CODE_REVIEW/
│   ├── code_quality_check/
│   │   ├── v1.0_20250101.md
│   │   └── v1.2_current.md
│   └── README.md
│
├── 03_DATA_ANALYSIS/
│   ├── data_insight_extraction/
│   │   ├── v1.0_20250101.md
│   │   └── v1.3_current.md
│   └── README.md
│
├── 04_LEARNING_SYNTHESIS/
│   ├── note_summarizer/
│   │   ├── v1.0_20250101.md
│   │   └── v1.2_current.md
│   └── README.md
│
├── 05_CUSTOM/                        # 自定义场景
│   ├── your_domain_1/
│   │   └── prompt_name/
│   │       └── v1.0_current.md
│   └── README.md
│
└── TEMPLATE.md                       # 提示词模板（复制即用）
```

---

## 📋 单个 Prompt 文件格式

每个 Prompt 都遵循这个标准结构（开箱即用的模板）：

```markdown
# [提示词名称]

## 元数据
- **版本**: v2.1
- **创建日期**: 2025-01-15
- **最后更新**: 2025-12-14
- **应用场景**: Claude / GPT-4 / Gemini（支持哪些 AI 应用）
- **标签**: #文档质量 #深度评估 #高频使用

## 效果记录
| 指标 | 数值 | 备注 |
|-----|------|------|
| **成功率** | 92% | 满足预期的比例 |
| **节省时间** | 18 min/次 | 相比手工评估 |
| **使用频率** | 23 次/月 | 最近 30 天 |
| **质量评分** | ⭐⭐⭐⭐⭐ | 满意度 |

## 版本演进

### v2.1 ⭐ 当前推荐
**改进点**：
- 新增"前瞻性"评估维度
- 优化提示词结构，减少歧义
- 增加例子数量（从 2 → 5）

**使用建议**：优先选用此版本

---

### v2.0 (2025-11-20)
**改进点**：
- 添加深度评估的具体指标
- 支持多语言文档

**问题**：前瞻性评估不足

---

### v1.0 (2025-01-15)
**初版**：基础文档质量检查

---

## 正文

### 角色
你是文档质量评估专家，擅长评估技术文档的深度、准确性和前瞻性。

### 目标
对给定文档进行多维度评估，输出具体改进建议。

### 输入格式
```

【文档标题】：[文档名称] 【文档内容】：[粘贴完整内容或关键章节] 【评估维度】：深度 / 前瞻性 / 完整性（可多选）

```

### 输出要求

输出为结构化 Markdown：

1. **深度评估（0-10分）**
   - 原理解释清晰度
   - 示例的代表性
   - 细节覆盖度

2. **前瞻性评估（0-10分）**
   - 是否涵盖最新技术趋势
   - 是否预留扩展空间
   - 是否避免已过时的实践

3. **完整性评估（0-10分）**
   - 结构逻辑性
   - 内容覆盖广度
   - 易用性

4. **具体改进建议**（至少3条，按优先级排序）

### 约束条件
- 必须：基于文档实际内容反馈，不臆测
- 必须：建议具有可执行性
- 禁止：笼统的"很好"或"需改进"
- 禁止：超出文档范畴的建议

### 输出示例
```

## 评估结果

**深度分数**: 7/10

- ✓ 核心概念讲解清晰
- ✗ 缺少源码级别的解释
- ✓ 案例贴近实战

**前瞻性**: 6/10

- ⚠ 未涉及 2024 年的新框架更新
- ✓ 架构设计具有扩展性
- ⚠ 性能优化建议略显保守

**改进建议**:

1. 【高优先级】第 3.2 节新增"并发处理"小节
2. 【中优先级】补充最新框架的 breaking changes
3. 【低优先级】图表美化和代码高亮

```

---

## 使用场景

### 场景 1：文档初稿评估
使用本提示对新编写的技术文档进行第一轮审核。

### 场景 2：迭代优化
结合上一版本的建议，评估改进效果。

### 场景 3：团队审核
用于 Code Review / 文档审核的标准化输入。

---

## 失败案例与改进

### 案例 1 (2025-11-20)
**问题**：模型混淆了"深度"和"完整性"
**原因**：两个维度定义不够清晰
**改进**：v2.0 增加了明确的定义示例

### 案例 2 (2025-12-01)
**问题**：对前瞻性评估时过于保守
**原因**：缺少"趋势参考资源"的指导
**改进**：v2.1 增加了最新技术清单

---

## 后续优化方向

- 考虑与 Code Review Prompt 串联使用
- 针对不同文档类型（API文档 / 架构文档 / 教程）进行专项优化
- 支持与"文档深度提升"Prompt 链式编排

---

## 快速复用

**直接复制上面的"正文"部分到你的 AI 应用中即可使用。**

```

【AI 应用】: Claude / GPT-4 / Gemini / 其他 【粘贴内容】: 从"角色"开始到"约束条件"结束 【输入】: 你要评估的文档内容 【输出】: 获得结构化评估

---

## 其他参考

- 📌 相关 Prompt：`02_CODE_REVIEW/code_quality_check/v1.2_current.md`
- 📌 上级主题：`00_META/STANDARDS.md`（质量评估标准体系）

````

---

## 🔍 快速查询（00_META/INDEX.md）

### 按场景分类

| 场景 | Prompt | 最新版本 | 推荐指数 |
|------|--------|---------|---------|
| 文档深度评估 | `01_DOCUMENTATION/doc_depth_analyzer/v2.1_current.md` | v2.1 | ⭐⭐⭐⭐⭐ |
| 前瞻性检查 | `01_DOCUMENTATION/doc_foresight_check/v1.5_current.md` | v1.5 | ⭐⭐⭐⭐ |
| 代码审查 | `02_CODE_REVIEW/code_quality_check/v1.2_current.md` | v1.2 | ⭐⭐⭐⭐ |
| 数据洞察 | `03_DATA_ANALYSIS/data_insight_extraction/v1.3_current.md` | v1.3 | ⭐⭐⭐⭐⭐ |
| 笔记总结 | `04_LEARNING_SYNTHESIS/note_summarizer/v1.2_current.md` | v1.2 | ⭐⭐⭐⭐ |

### 按应用工具分类

**Claude**:
- `01_DOCUMENTATION/doc_depth_analyzer/v2.1_current.md` ✅
- `02_CODE_REVIEW/code_quality_check/v1.2_current.md` ✅

**GPT-4**:
- 所有 Prompt 都支持（标记为 ✅）

**Gemini**:
- `03_DATA_ANALYSIS/data_insight_extraction/v1.3_current.md` ✅
- `04_LEARNING_SYNTHESIS/note_summarizer/v1.2_current.md` ✅

---

## 📊 效果追踪（00_META/CHANGELOG.md）

### 2025-12 月度统计
- **新增 Prompt**: 2 个
- **版本更新**: 5 次
- **文档质量提升**: +35%（相比 11 月）
- **高频使用排名**: doc_depth_analyzer > code_quality_check > data_insight_extraction

### 版本更新日志

#### 2025-12-14
- ✅ `doc_depth_analyzer` → v2.1（新增前瞻性维度）
- ✅ `code_quality_check` → v1.2（优化输出格式）

#### 2025-11-20
- ✅ `doc_depth_analyzer` → v2.0（扩展支持多语言）
- 📝 `doc_foresight_check` → 创建 v1.0

#### 2025-11-15
- ✅ 建立完整目录结构
- ✅ 迁移现有 Prompt 共 8 个

---

## 🚀 实战工作流

### 第 1 步：初始化（5 分钟）

```bash
# 创建本地目录结构（复制上面的目录树）
# 将现有的分散 Prompt 按分类放入各目录

# 例如：
prompts/
└── 01_DOCUMENTATION/
    └── doc_depth_analyzer/
        └── v1.0_20251214.md    # 你现有的 Prompt
````

### 第 2 步：规范化（每个 Prompt 10 分钟）

用上面提供的**单个 Prompt 文件格式**重新整理每个 Prompt，添加：

- 元数据（版本、日期、应用场景）
- 效果记录表
- 版本演进历史

### 第 3 步：建立索引（一次性 10 分钟）

创建 `00_META/INDEX.md`，填入你的所有 Prompt：

```markdown
| 场景 | 文件路径 | 版本 | 推荐 |
|------|---------|------|------|
| 你的第一个 Prompt | `01_DOCUMENTATION/xxx/v1.0_current.md` | v1.0 | ⭐⭐ |
| 你的第二个 Prompt | `02_CODE_REVIEW/xxx/v1.2_current.md` | v1.2 | ⭐⭐⭐⭐ |
```

### 第 4 步：使用与迭代（持续）

**使用时**：

```
打开 prompts/00_META/INDEX.md 
  ↓
找到对应场景 
  ↓
打开 xxx/v_current.md 
  ↓
复制到 AI 应用使用
```

**迭代时**（使用效果不满意）：

```
复制 v1.2_current.md → v1.3_20251215.md
修改提示词内容
在版本演进区添加"改进点"说明
运行对比测试
满意后重命名为 v1.3_current.md（旧版本保留历史记录）
```

---

## 💡 关键设计原则

### 1. **「_current」 命名约定**

- 每个场景始终有一个 `v_current.md` 版本
- 这是你日常使用的版本
- 历史版本永久保存（便于回溯）

```
doc_depth_analyzer/
├── v1.0_20250115.md      ← 历史版本
├── v2.0_20251120.md      ← 历史版本
├── v2.1_20251214.md      ← 历史版本
└── v2.1_current.md       ← 总是指向最新推荐版本
```

### 2. **Git 天然的版本控制**

```bash
# 不需要任何脚本，Git 自动追踪
git log --oneline prompts/01_DOCUMENTATION/doc_depth_analyzer/

# 输出：
# a3f2c1b ✅ doc_depth_analyzer v2.1：新增前瞻性维度
# 7d4e2f8 🔄 doc_depth_analyzer v2.0：支持多语言
# 2b5a1c3 ✨ doc_depth_analyzer v1.0：初版
```

### 3. **极简信息追踪**

只记录这些关键指标（不过度复杂化）：

- **成功率**：满足预期的频率
- **节省时间**：相比手工
- **使用频率**：最近 30 天
- **质量评分**：简单 5 星制

### 4. **链式提示编排**

复杂任务可以串联多个 Prompt：

```markdown
# 【高级场景】完整文档质量体系

## 执行流程

1. **第一步**：用 `doc_depth_analyzer` 评估深度
   文件：`01_DOCUMENTATION/doc_depth_analyzer/v2.1_current.md`

2. **第二步**：用 `doc_foresight_check` 检查前瞻性
   文件：`01_DOCUMENTATION/doc_foresight_check/v1.5_current.md`

3. **第三步**：用 `code_quality_check` 检查代码示例
   文件：`02_CODE_REVIEW/code_quality_check/v1.2_current.md`

4. **第四步**：汇总所有反馈，生成改进清单

## 记录改进历史
在主文档的 CHANGELOG 中记录：
- 日期
- 应用了哪个 Prompt
- 改进了什么
- 效果如何
```

---

## 🎯 迭代演进的 3 层模型

### 第 1 层：单个 Prompt 的迭代

```
v1.0（初版）
  ↓ 使用中发现问题
v1.1（小修复）
  ↓ 效果明显改善
v1.2（推荐版本）
  ↓ 遇到新场景
v2.0（大升级）
```

**记录方式**：

```markdown
## 版本演进

### v2.0 (2025-12-10)
**改进点**：
- 问题 1 解决了
- 问题 2 解决了

**仍存在**：
- 问题 3（待后续版本）
```

### 第 2 层：Prompt 之间的关联迭代

```
doc_depth_analyzer 优化了
  ↓ 从中发现：前瞻性评估很重要
  ↓ 创建新 Prompt
doc_foresight_check
  ↓ 两个 Prompt 合并
code_quality_unified_checker
```

**记录方式**：在 `00_META/CHANGELOG.md` 中：

```markdown
### 跨 Prompt 优化（2025-12）
- `doc_depth_analyzer` v2.1 的改进启发了 `doc_foresight_check`
- 决策：不合并，保持独立（各有专注）
```

### 第 3 层：整体策略的迭代

```
初期：零散的 Prompt 堆积
  ↓ 1 个月后
分类清晰：按场景组织
  ↓ 2 个月后
跨应用复用：同一 Prompt 用于 Claude / GPT-4 / Gemini
  ↓ 3 个月后
团队级沉淀：优秀 Prompt 开源或内部分享
```

**记录方式**：`00_META/STANDARDS.md`

```markdown
## 演进历史

### Phase 1（2025-11）：建立分类体系
- 完成 Prompt 从零散到分类的过渡
- 质量评分体系确立

### Phase 2（2025-12）：多应用适配
- Prompt 开始支持 Claude / GPT-4 / Gemini
- 单个 Prompt 使用频率 ↑ 40%

### Phase 3（2026-01，规划）：团队协作
- 建立审核机制
- 高价值 Prompt 内部分享
```

---

## ⚡ 快速启动（今天就开始）

### Step 1：创建目录（2 分钟）

在你的本地或 GitHub 创建这个结构：

```
prompts/
├── 00_META/
│   ├── README.md
│   ├── INDEX.md
│   └── CHANGELOG.md
├── 01_DOCUMENTATION/
├── 02_CODE_REVIEW/
├── 03_DATA_ANALYSIS/
├── 04_LEARNING_SYNTHESIS/
├── 05_CUSTOM/
└── TEMPLATE.md
```

### Step 2：迁移现有 Prompt（15 分钟）

找出你现在在用的所有 Prompt（可能散落在 Notes、Email、ChatGPT 历史中）：

```
当前状态：
- "文档评估 Prompt" → 保存在 Notion
- "代码审查 Prompt" → 保存在 Word
- "数据分析 Prompt" → 写在 ChatGPT 对话中

↓ 迁移后：

prompts/01_DOCUMENTATION/doc_depth_analyzer/v1.0_current.md
prompts/02_CODE_REVIEW/code_quality_check/v1.0_current.md
prompts/03_DATA_ANALYSIS/data_insight_extraction/v1.0_current.md
```

### Step 3：规范化格式（5 分钟/个）

用上面的**单个 Prompt 文件格式模板**重写每个 Prompt，添加元数据。

### Step 4：建立索引（5 分钟）

编辑 `00_META/INDEX.md`，列出所有 Prompt。

### Step 5：提交到 Git（5 分钟）

```bash
git init prompts/
git add .
git commit -m "初始化 Prompt 管理系统"
```

**总耗时：~40 分钟完成完整搭建**

---

## 🔑 核心优势

| 需求          | 解决方案                          | 优势                 |
| ----------- | ----------------------------- | ------------------ |
| Prompt 分散各地 | Markdown 目录 + Git             | 集中管理 + 版本历史永久保存    |
| 难以追踪质量演进    | 每个 Prompt 标记版本号 + 效果记录表       | 清晰看到每次改进的效果        |
| 跨应用复用困难     | 标明适用的 AI 工具 + 标准化格式           | 一个 Prompt 即插即用多个平台 |
| 文档太长难维护     | 纯 Markdown，无需数据库或代码           | 极简但不失功能            |
| 需要团队协作      | Git workflow 天然支持 PR / review | 无缝升级为团队版           |

---

## 📌 常见问题

### Q1：Markdown 文件如何跨 AI 应用使用？

**A**：非常简单，就是复制粘贴。打开 `v_current.md` 文件，复制从"角色"到"约束条件"的内容，粘贴到任何 AI 应用（Claude、GPT-4、Gemini）都能用。

### Q2：如何处理失败的 Prompt 版本？

**A**：不删除，保留历史记录。失败的版本能告诉你"什么不行"，和成功版本对比能学到更多。

### Q3：Git 怎么用？需要懂很深吗？

**A**：不需要。你只需要 5 条命令：

```bash
git init          # 初始化一次
git add .         # 添加所有文件
git commit -m ""  # 每次更新提交
git log           # 查看历史
git diff          # 对比两个版本
```

### Q4：能和团队协作吗？

**A**：可以。建立一个 GitHub 或 GitLab repo，允许团队成员提交改进建议（Pull Request）。每个 Prompt 的改进历史完全可追踪。

### Q5：这个系统能扩展吗？

**A**：可以。如果以后需要：

- 添加更多 Prompt：在 `05_CUSTOM/` 中新建文件夹
- 自动化索引：写个简单脚本自动生成 INDEX.md
- 效果数据化：添加更详细的指标记录
- 团队共享：提交到公司 GitLab 即可

---

## 🎓 学习资源

- **Markdown 语法**：<https://www.markdownguide.org/>
- **Git 快速入门**：<https://git-scm.com/book/zh/v2/（中文版）>
- **GitHub 协作**：<https://docs.github.com/zh/pull-requests>

---

## 最后的话

**这个系统的核心理念**：

- ✅ **极简**：无需代码、无需数据库、无需学习曲线
- ✅ **可追踪**：Git 自动记录所有历史
- ✅ **可迭代**：清晰看到质量、深度、前瞻性如何演进
- ✅ **可复用**：同一 Prompt 跨越多个 AI 应用

从保存第一个 Prompt 开始，6 个月后你会拥有一座**结构化的、有版本历史的、质量可追踪的个人 AI 知识库**。

**现在就开始吧！** 🚀
