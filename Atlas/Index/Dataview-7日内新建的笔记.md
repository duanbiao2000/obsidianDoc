---
view-count: 4
tags:
  - note-filtering
  - date-sorting
  - dataview
  - table
  - Type/Index
  - Domain/Cognitive
  - note-filtering
  - date-sorting
  - dataview
  - table
---

## 🔗 相关链接

- **主索引**: [[Atlas/Index/Whole Vault任务管理.md | 任务管理]]
- **Dataview文档**: [[Atlas/Index/Dataviewer.md | Dataview使用指南]]

---

## 7日内新建的笔记(非archive)

要查询过去15日内创建、且最近3日内没有修改的笔记，并按最新创建时间排序，只显示10条，排除"Archive"文件夹，修改后的 Dataview 语法如下：

```dataview
TABLE tags AS 标签
FROM !"Archive"
WHERE (date(today) - file.ctime).day < 15 AND file.mtime < (date(today) - dur(7 days))
SORT file.ctime DESC
LIMIT 10
```

