---
view-count: 5
tags:
  - advanced-filters
  - llm-automation
  - KnowledgeManagement
  - NoteTaking
  - Type/Reference
  - Domain/Technology
---
以下是 [[Obsidian Base 100练]] 的极简改写版本：

# Obsidian Base 实战进阶路径

### 1. L1：基础过滤与视图管理
- **属性过滤**：按修改时间 (`file.mtime`)、后缀 (`file.ext`)、文件名 (`file.name`) 或特定属性（如 `rating >= 4`）筛选。
- **视图操作**：新建视图 (`+`)、导出 CSV、按文件夹分组 (`file.folder`)、卡片视图布局。

### 2. L2：公式、逻辑与动态计算
- **布尔逻辑**：默认多过滤器为 **AND**；使用过滤器组实现 **OR** 逻辑。
- **数学运算**：创建公式列处理数值，如 `price * 1.1` 或 `toFixed(2)`。
- **时间计算**：
  - 笔记年龄：`(now() - file.ctime).days`。
  - 截止倒计时：`(deadline - now()).days`。
- **条件分支**：使用 `if(condition, true, false)` 生成动态标签。

### 3. L3：高级检索与元数据建模
- **链接分析**：筛选反向链接 `file.hasLink(this.file)` 或出链数量 `file.links.length > 5`。
- **正则匹配**：使用 `test(/regex/, property)` 进行复杂文本筛选（如邮箱校验）。
- **聚合计算**：使用 `map` 和 `sum` 处理嵌套列表，如 `items.map(i => i.price * i.quantity).sum()`。
- **嵌套属性**：通过点符号访问深度数据，如 `person.address.city`。

### 4. L4：LLM 自动化与闭环工作流
- **结构化生成**：利用 LLM 插件（如 `Text Generator`）批量生成带有标准 YAML 的笔记。
- **元数据补全**：自动从正文提取摘要、关键词、会议行动项并回写属性。
- **健康检查**：建立 Base 视图监控“孤立笔记”、“元数据缺失”或“重复文件”。
- **系统闭环**：结合多模态 LLM、GitOps 与数据审计，构建“自我维护”的知识库。

---

### 5. 核心公式/过滤器速查表

| 功能 | 表达式 | |
| --- | --- | --- |
| **过去7天修改** | `file.mtime > today() - "7d"` | |
| **空属性检查** | `status is empty` | |
| **字符串合并** | `firstName + " " + lastName` | |
| **判断逾期** | `if(due_date < today(), "Overdue", "OK")` | |
| **提取日期** | `created_at.date()` | |