---
tags:
  - Domain/知识管理
  - Status/Done
  - Type/教程
created: 2026-01-25
update: 2026-01-25
rating: 5
view-count: 0
related:
  - [[Atlas/BASE/快速入门指南.md]]
  - [[Atlas/Index/Dataviewer.md]]
---

## 🔗 相关链接

**上级索引**:
- [[Atlas/BASE/_Index_of_BASE.md|BASE]]
- [[Atlas/BASE/插件使用指南/|插件使用指南]]

---

# 📊 Dataview 插件使用指南

> **Dataview 是 Obsidian 最强大的插件之一**，它让你像使用数据库一样查询和展示你的笔记。

---

## 🎯 什么是 Dataview？

Dataview 可以将你的 Markdown 笔记视为数据表，进行查询、过滤、排序和展示。

### 核心能力

- 📊 **数据查询**：像 SQL 一样查询笔记
- 📈 **数据展示**：以表格、列表、任务列表等形式展示
- 🔍 **元数据读取**：读取 YAML frontmatter 中的数据
- ⚡ **实时更新**：数据变化时自动更新查询结果

---

## 📦 安装和配置

### 安装步骤

1. 打开 Obsidian 设置
2. 进入 **"社区插件"**
3. 搜索 **"Dataview"**
4. 点击安装并启用

### 基本配置

```yaml
# 在笔记中启用 Dataview
```dataview
TABLE file.link AS "笔记", tags AS "标签"
FROM "2.Topics"
```
```

---

## 🚀 核心语法

### 1️⃣ TABLE 查询（表格形式）

展示笔记数据的表格：

```dataview
TABLE file.link AS "笔记标题", tags AS "标签", created AS "创建日期"
FROM "2.Topics"
WHERE created
SORT created DESC
LIMIT 10
```

**说明**：
- `TABLE`: 定义表格列
- `FROM`: 指定查询范围
- `WHERE`: 过滤条件
- `SORT`: 排序
- `LIMIT`: 限制结果数量

### 2️⃣ LIST 查询（列表形式）

以列表形式展示笔记：

```dataview
LIST
FROM "3.Resources"
WHERE contains(tags, "Domain")
SORT file.name ASC
```

### 3️⃣ TASK 查询（任务列表）

展示所有任务：

```dataview
TASK
WHERE !completed
GROUP BY file.folder
```

---

## 💡 常用查询示例

### 📁 **查询指定目录的笔记**

```dataview
TABLE file.link, tags
FROM "1.Projects"
```

### 🏷️ **按标签查询**

```dataview
TABLE file.link AS "笔记", rating AS "评分"
FROM "2.Topics"
WHERE contains(tags, "Domain/AI")
```

### ⭐ **查询高评分笔记**

```dataview
TABLE file.link AS "笔记", rating AS "评分", view-count AS "访问次数"
FROM "1.Projects" OR "2.Topics" OR "3.Resources"
WHERE rating AND rating >= 4.0
SORT rating DESC, view-count DESC
```

### 📅 **查询最近创建的笔记**

```dataview
TABLE file.link AS "笔记", dateformat(created, "yyyy-MM-dd") AS "创建日期"
FROM "1.Projects" OR "2.Topics" OR "3.Resources"
WHERE created
SORT created DESC
LIMIT 20
```

### ❌ **查询未完成的任务**

```dataview
TASK
WHERE !completed
GROUP BY file.link
```

### 🔄 **查询最近更新的笔记**

```dataview
TABLE file.link AS "笔记", dateformat(update, "yyyy-MM-dd") AS "更新日期"
FROM "1.Projects" OR "2.Topics" OR "3.Resources"
WHERE update
SORT update DESC
LIMIT 10
```

---

## 🔧 高级用法

### 📊 **分组统计**

```dataview
TABLE rows.file.link AS "笔记", length(rows) AS "数量"
FROM "2.Topics"
GROUP BY file.folder
```

### 🎯 **复杂条件查询**

```dataview
TABLE file.link, rating, tags
FROM "1.Projects" OR "2.Topics"
WHERE (rating AND rating >= 3.0) OR (contains(tags, "Status/InProgress"))
SORT rating DESC
```

### 📈 **聚合计算**

```dataview
TABLE
  round(average(rating), 2) AS "平均评分",
  length(rows) AS "笔记数量",
  length(rows[rating >= 4]) AS "优秀笔记数"
FROM "2.Topics"
WHERE rating
GROUP BY file.folder
```

---

## 🎨 格式化输出

### 📅 **日期格式化**

```dataview
TABLE file.link, dateformat(created, "yyyy年MM月dd日") AS "创建日期"
FROM "2.Topics"
```

### 🔢 **数字格式化**

```dataview
TABLE file.link, round(rating * 10) / 10 AS "评分（一位小数）"
FROM "2.Topics"
WHERE rating
```

### 🔗 **链接格式化**

```dataview
TABLE link(file.link, "查看") AS "操作", file.link AS "笔记"
FROM "2.Topics"
LIMIT 5
```

---

## ⚡ 性能优化

### 🎯 **优化查询范围**

❌ **不好的做法**：查询整个仓库
```dataview
TABLE *
FROM ""
```

✅ **好的做法**：限定查询范围
```dataview
TABLE file.link
FROM "2.Topics"
```

### 📊 **使用索引文件**

优先查询 `_Index_of_*.md` 文件，而不是扫描整个目录。

### 🔢 **限制结果数量**

```dataview
TABLE file.link
FROM "2.Topics"
LIMIT 50
```

---

## 🐛 常见问题

### Q1: 为什么查询结果为空？

**可能原因**：
1. 查询路径不正确（检查 `FROM` 子句）
2. 元数据字段不存在（使用 `WHERE field` 前确认字段存在）
3. 过滤条件过于严格（放宽 `WHERE` 条件）

### Q2: 如何调试查询？

**方法**：
1. 从简单查询开始，逐步添加条件
2. 使用 `TABLE *` 查看所有可用字段
3. 检查 YAML frontmatter 是否正确

### Q3: Dataview 查询很慢怎么办？

**优化方法**：
1. 限制查询范围（使用 `FROM` 指定目录）
2. 限制结果数量（使用 `LIMIT`）
3. 避免在大型仓库中使用通配符查询

### Q4: 如何查询嵌套字段？

```dataview
TABLE metadata.field1, metadata.field2
FROM "2.Topics"
WHERE metadata
```

---

## 📚 实用代码片段

### 📋 **所有待办事项**

```dataview
TASK
WHERE !completed
GROUP BY file.folder
```

### 📊 **本月创建的笔记**

```dataview
TABLE file.link, dateformat(created, "MM-dd") AS "日期"
FROM "1.Projects" OR "2.Topics" OR "3.Resources"
WHERE dateformat(created, "yyyy-MM") = dateformat(date(now), "yyyy-MM")
SORT created DESC
```

### 🔥 **高优先级未完成任务**

```dataview
TASK
WHERE !completed AND (priority = "high" OR priority = "medium")
GROUP BY file.link
```

### 📈 **质量评分分布**

```dataview
TABLE
  length(rows[rating >= 4.5]) AS "优秀",
  length(rows[rating >= 4.0 AND rating < 4.5]) AS "良好",
  length(rows[rating >= 3.0 AND rating < 4.0]) AS "合格",
  length(rows[rating < 3.0]) AS "需改进"
FROM "1.Projects" OR "2.Topics" OR "3.Resources"
WHERE rating
GROUP BY file.folder
```

---

## 🎓 进阶学习

### 📖 **推荐阅读**

- Dataview 官方文档: [https://blacksmithgu.github.io/obsidian-dataview/](https://blacksmithgu.github.io/obsidian-dataview/)
- Dataview 查询语法: [https://blacksmithgu.github.io/obsidian-dataview/query/](https://blacksmithgu.github.io/obsidian-dataview/query/)
- Dataview 函数参考: [https://blacksmithgu.github.io/obsidian-dataview/data-commands/](https://blacksmithgu.github.io/obsidian-dataview/data-commands/)

### 🔗 **相关文档**

- [[Atlas/Index/Dataviewer.md]] - 本库的 Dataview 查询示例
- [[Atlas/BASE/内容质量看板.md]] - 使用 Dataview 的质量看板
- [[5.Misc/Template/]] - 使用 Dataview 的模板

---

## 💡 最佳实践

### ✅ **好的做法**

1. **限定查询范围**：使用 `FROM` 指定目录
2. **使用索引文件**：优先查询索引
3. **限制结果数量**：使用 `LIMIT` 避免过多结果
4. **添加注释**：在查询前用 `%%` 注释说明用途

### ❌ **避免的做法**

1. ❌ 查询整个仓库（`FROM ""`）
2. ❌ 没有条件限制的查询
3. ❌ 过于复杂的嵌套查询
4. ❌ 忘记使用 `SORT` 排序结果

---

## 🚀 下一步

1. **实践**：复制上面的查询示例，修改后运行
2. **探索**：查看 [[Atlas/Index/Dataviewer.md]] 了解更多示例
3. **优化**：根据需要调整查询条件
4. **创建看板**：使用 Dataview 创建个人看板

---

**更新日志**:
- **2026-01-25**: 创建 Dataview 使用指南

**预计学习时间**: 30-45 分钟
**难度等级**: ⭐⭐⭐☆☆ (中级)
**适合人群**: 已完成快速入门指南的用户
