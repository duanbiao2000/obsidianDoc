---
tags:
  - Type/Reference
  - Domain/Tech/Obsidian
  - dataview-templates
update: 2026-01-26
related:
  - [[Dataviewer]]
  - [[Zoottelkeeper使用指南]]
---

# Dataview 查询模板集

> 本文件收录常用的 Dataview 查询模板,可直接复制到索引文件中使用
>
> 📌 更新时间: 2026-01-26

---

## 📊 1. 统计概览模板

### 基础统计

```dataviewjs
const pages = dv.pages('"目录路径"');
dv.paragraph(`总笔记数: ${pages.length}`);
```

### 分类统计

```dataviewjs
const pages = dv.pages('"目录路径"');
const subdirs = pages
  .groupBy(p => p.file.folder.split('/').pop())
  .filter(p => p.key);
dv.table(["子目录", "笔记数"], subdirs.map(p => [p.key, p.rows.length]));
```

### 标签统计

```dataviewjs
const allTags = dv.pages().file.etags.distinct();
dv.paragraph(`总标签数: ${allTags.length}`);

const domainTags = allTags.filter(t => t.startsWith('#Domain/'));
const statusTags = allTags.filter(t => t.startsWith('#Status/'));
const typeTags = allTags.filter(t => t.startsWith('#Type/'));

dv.table(["标签类型", "数量"], [
  ["Domain 标签", domainTags.length],
  ["Status 标签", statusTags.length],
  ["Type 标签", typeTags.length]
]);
```

---

## 📅 2. 时间相关查询

### 最近更新

```dataview
TABLE
  file.mtime AS "修改时间",
  tags AS "标签"
FROM "目录路径"
WHERE !startswith(file.name, "_Index")
SORT file.mtime DESC
LIMIT 10
```

### 最近创建

```dataview
TABLE
  file.ctime AS "创建时间",
  tags AS "标签"
FROM "目录路径"
WHERE !startswith(file.name, "_Index")
SORT file.ctime DESC
LIMIT 10
```

### N天内修改

```dataview
TABLE
  file.mtime AS "修改时间",
  date(today)-(file.mtime) AS "距今天数"
FROM "目录路径"
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
```

### 本月创建

```dataview
TABLE
  file.ctime AS "创建时间"
FROM "目录路径"
WHERE file.ctime.month = date(today).month
SORT file.ctime DESC
```

---

## 🔗 3. 链接分析

### 查找孤立笔记

```dataviewjs
const orphanNotes = dv.pages()
  .where(p => {
    const links = p.file.inlinks.length + p.file.outlinks.length;
    return links < 2 && !p.file.name.startsWith('_Index');
  });

dv.paragraph(`孤立笔记数: ${orphanNotes.length}`);

dv.table(
  ["文件", "入链", "出链"],
  orphanNotes
    .limit(20)
    .map(p => [p.file.link, p.file.inlinks.length, p.file.outlinks.length])
);
```

### 高链接数笔记

```dataview
TABLE
  file.inlinks.length AS "入链数",
  file.outlinks.length AS "出链数",
  (file.inlinks.length + file.outlinks.length) AS "总链接数"
FROM "目录路径"
WHERE !startswith(file.name, "_Index")
SORT (file.inlinks.length + file.outlinks.length) DESC
LIMIT 10
```

### 反向链接查看

```dataview
TABLE
  tags AS "标签"
FROM ""
WHERE [[当前笔记]]
SORT file.mtime DESC
```

---

## 🏷️ 4. 标签查询

### 按标签筛选

```dataview
TABLE
  file.mtime AS "修改时间"
FROM "目录路径"
WHERE contains(tags, "#特定标签")
SORT file.mtime DESC
```

### 标签使用频率

```dataview
TABLE
  rows.file.link AS "文件"
FROM "目录路径"
FLATTEN file.tags AS tags
WHERE tags != '#Type/Index'
GROUP BY tags
SORT length(rows) DESC
LIMIT 20
```

### 按标签类型分组

```dataview
TABLE
  rows.file.link AS "文件"
FROM ""
FLATTEN file.tags AS tags
WHERE tags.startswith('#Domain/')
GROUP BY tags
SORT length(rows) DESC
```

---

## 📋 5. 任务管理

### 未完成任务

```dataview
TASK
WHERE !completed
FROM "目录路径"
SORT file.mtime DESC
LIMIT 20
```

### 按优先级分组

```dataview
TASK
WHERE !completed
FROM "目录路径"
GROUP BY priority
SORT file.mtime DESC
```

### 即将到期

```dataview
TASK
WHERE !completed
AND due <= date(today) + dur(7 days)
FROM "目录路径"
SORT due ASC
LIMIT 20
```

---

## 📁 6. 目录和文件

### 列出子目录

```dataviewjs
const dirs = dv.pages('"目录路径"')
  .groupBy(p => p.file.folder)
  .filter(p => p.key !== "目录路径");

dv.table(["目录", "文件数"], dirs.map(p => [p.key, p.rows.length]));
```

### 文件大小排序

```dataview
TABLE
  file.size AS "大小(字节)",
  (file.size / 1024).toFixed(1) + " KB" AS "大小"
FROM "目录路径"
WHERE !startswith(file.name, "_Index")
SORT file.size DESC
LIMIT 10
```

### 随机笔记

```dataviewjs
const pages = dv.pages('"目录路径"').array();
const randomPages = pages.sort(() => 0.5 - Math.random()).slice(0, 5);

dv.table(["随机笔记"], randomPages.map(p => [p.file.link]));
```

---

## 📈 7. 高级查询

### 条件组合查询

```dataview
TABLE
  file.mtime AS "修改时间",
  tags AS "标签"
FROM "目录路径"
WHERE contains(tags, "#标签1")
OR contains(tags, "#标签2")
AND !contains(file.name, "模板")
SORT file.mtime DESC
```

### 聚合统计

```dataviewjs
const pages = dv.pages('"目录路径"');

const totalLinks = pages
  .reduce((sum, p) => sum + p.file.inlinks.length + p.file.outlinks.length, 0);

const avgLinks = (totalLinks / pages.length).toFixed(1);

dv.table(["指标", "数值"], [
  ["总笔记数", pages.length],
  ["总链接数", totalLinks],
  ["平均链接数", avgLinks]
]);
```

### 按时间范围分组

```dataview
TABLE
  rows.file.link AS "文件"
FROM "目录路径"
WHERE file.ctime.year = 2026
GROUP BY file.ctime.month
SORT file.ctime.month DESC
```

---

## 🎨 8. 索引专用模板

### 索引文件统计(完整版)

```dataviewjs
const pages = dv.pages('"当前目录"');

// 基础统计
dv.paragraph(`**总笔记数**: ${pages.length}`);

// 子目录统计
const subdirs = pages
  .groupBy(p => p.file.folder.split('/').pop())
  .filter(p => p.key);

dv.table(["子目录", "笔记数"], subdirs.map(p => [p.key, p.rows.length]));

// 最近更新
dv.table(["最近更新"], pages
  .sort(p => p.file.mtime, 'desc')
  .limit(5)
  .map(p => [p.file.link])
);
```

### 简化索引统计

```dataviewjs
const count = dv.pages('"当前目录"').length;
dv.paragraph(`📊 **${count}** 篇笔记`);
```

---

## 🔍 9. 搜索与过滤

### 按文件名搜索

```dataview
TABLE
  file.link AS "文件"
FROM "目录路径"
WHERE contains(file.name, "关键词")
```

### 按内容搜索

```dataview
TABLE
  file.link AS "文件"
FROM "目录路径"
WHERE contains(file.content, "关键词")
```

### 正则表达式匹配

```dataview
TABLE
  file.link AS "文件"
FROM "目录路径"
WHERE file.name =~ "^模式"
```

---

## 💡 使用技巧

### 1. 复制模板后修改路径

将 `"目录路径"` 替换为实际路径,例如:
- `"2.Topics"`
- `"0.DailyNotes"`
- `"Atlas/Index"`

### 2. 组合多个查询

可以在一个文件中添加多个 Dataview 代码块,每个代码块执行不同的查询

### 3. 与 Zoottelkeeper 结合

在 Zoottelkeeper 标记之前添加 Dataview 查询:

```markdown
%% Zoottelkeeper: Beginning %%
(自动生成的文件列表)
%% Zoottelkeeper: End %%

## 📊 统计
(Dataview 查询代码块)
```

### 4. 性能优化

- 使用 `FROM "具体路径"` 代替 `FROM ""` 限制查询范围
- 使用 `LIMIT` 限制结果数量
- 复杂查询优先使用 `dataviewjs` 而不是 `dataview`

---

## 📚 相关资源

### 官方文档
- [Dataview 插件文档](https://blacksmithgu.github.io/obsidian-dataview/)
- [Dataview 查询语法](https://blacksmithgu.github.io/obsidian-dataview/query/queries/)

### 社区资源
- [Obsidian Hub - Dataview](https://obsidian.md hub.json#Dataview)
- [Dataview 示例合集](https://github.com/obsidian-community/obsidian-hub)

### 相关笔记
- [[Dataviewer]] - 本知识库的查询示例
- [[索引健康报告]] - 索引监控查询
- [[仓库标签管理系统]] - 标签查询示例

---

## 🔄 更新日志

| 日期 | 更新内容 |
|------|---------|
| 2026-01-26 | 创建查询模板集 |
| 2026-01-26 | 添加索引专用模板 |
| 2026-01-26 | 完善使用技巧说明 |
