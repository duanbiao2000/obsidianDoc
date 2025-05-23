

```dataview
TABLE file.mtime AS "修改时间", round((date(today) - file.mtime).days) + " 天前" AS "距离今天的天数"
FROM ""
WHERE !startswith(file.folder, "Extras/") AND !startswith(file.folder, "Templates/")
SORT file.mtime ASC
LIMIT 10
```



```dataview
TABLE file.ctime AS "创建时间", round((date(today) - file.ctime).days) + " 天前" AS "距离今天的天数"
FROM ""
WHERE file.ctime = file.mtime
SORT file.ctime ASC
LIMIT 10
```

