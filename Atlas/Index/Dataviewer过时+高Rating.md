
最早修改
```dataview
TABLE file.mtime AS "修改时间", round((date(today) - file.mtime).days) + " 天前" AS "距离今天的天数"
FROM ""
WHERE !startswith(file.folder, "Extras/") AND !startswith(file.folder, "Templates/")
SORT file.mtime ASC
LIMIT 10
```


最早创建
```dataview
TABLE file.ctime AS "创建时间", round((date(today) - file.ctime).days) + " 天前" AS "距离今天的天数"
FROM ""
WHERE file.ctime = file.mtime
SORT file.ctime ASC
LIMIT 10
```

好的，这里是一个 Dataview 查询，可以列出你的笔记中 rating 最高的（降序排列）前 10 篇：

```dataview
TABLE rating
FROM ""
WHERE rating >= 0 AND rating <= 10
SORT rating DESC
LIMIT 10
```

