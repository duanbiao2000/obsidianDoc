## 7日内新建的笔记(非archive)

要查询过去15日内创建、且最近3日内没有修改的笔记，并按最新创建时间排序，只显示10条，排除"Archive"文件夹，修改后的 Dataview 语法如下：

```dataview
TABLE theme AS 主题,tags AS 标签
FROM !"Archive"
WHERE (date(today) - file.ctime).day < 15 AND file.mtime < (date(today) - dur(3 days))
SORT file.ctime DESC
LIMIT 10
```

