
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



好的，没问题。如果想在 `rating` 相同的情况下，让修改时间更早的笔记（即 `file.mtime` 更小）排名更靠前，你需要将 `file.mtime` 作为第二个排序条件，并按升序 (`ASC`) 排列。


```dataview
TABLE rating, file.mtime AS "最近更新时间"
FROM ""
WHERE rating >= 0 AND rating <= 20
SORT rating DESC, file.mtime ASC
LIMIT 10
```
