---
tags:
  - file-sorting
  - timestamp-organization
  - table
  - dataview
  - Type/Index
  - Domain/Cognitive
---

## 🔗 相关链接

- **主索引**: [[Atlas/Index/Whole Vault任务管理.md | 任务管理]]
- **Dataview文档**: [[Atlas/Index/Dataviewer.md | Dataview使用指南]]

---

## 📅 最早修改的文件

查看知识库中长期未修改的文件，有助于识别需要更新或归档的内容。

```dataview
TABLE file.mtime AS "修改时间", round((date(today) - file.mtime).days) + " 天前" AS "距离今天的天数"
FROM ""
WHERE !startswith(file.folder, "Extras/") AND !startswith(file.folder, "Templates/") AND !startswith(file.folder, ".sisyphus/")
SORT file.mtime ASC
LIMIT 10
```

## 📝 最早创建的文件

显示知识库中最早创建的文档，帮助了解知识库的发展历程。

```dataview
TABLE file.ctime AS "创建时间", round((date(today) - file.ctime).days) + " 天前" AS "距离今天的天数"
FROM ""
WHERE file.ctime = file.mtime AND !startswith(file.folder, ".sisyphus/")
SORT file.ctime ASC
LIMIT 10
```

## ⭐ 高Rating笔记

按评分排序显示高质量笔记，相同评分时优先显示修改时间较早的内容。

```dataview
TABLE rating, file.mtime AS "最近更新时间", round((date(today) - file.mtime).days) + " 天前" AS "距离今天天数"
FROM ""
WHERE rating >= 0 AND rating <= 20 AND !startswith(file.folder, ".sisyphus/")
SORT rating DESC, file.mtime ASC
LIMIT 15
```

## 📊 使用说明

- **最早修改**: 帮助识别需要更新的内容
- **最早创建**: 了解知识库发展历史
- **高Rating**: 快速访问重要内容，按评分和时间双重排序
- 所有查询都排除了系统目录(.sisyphus/)和模板目录
