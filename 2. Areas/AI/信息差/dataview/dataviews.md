## 最新10个7日内修改笔记(非archive)
```dataview

TABLE  file.mtime AS 修改日期, file.ctime AS 创建日期
from !"Archive"
WHERE (date(today)-(file.ctime)).day<7 

sort file.mtime DESC

LIMIT 10
```

## 主题为微信阅读
```dataview
TABLE  file.ctime AS 创作日期
WHERE theme = "微信阅读"
```

## 15日内新建的笔记(非archive)

```dataview
TABLE theme AS 主题,tags AS 标签
FROM !"Archive"
WHERE (date(today)-(file.ctime)).day<15
SORT file.ctime DESC
```

## Todo List
```dataview

task
from #todo

```

## 同月新建的笔记

```dataview
TABLE file.ctime AS 创作日期
WHERE file.ctime.month = date(today).month
sort date(today)-(file.ctime)
```



## 建檔迄今過了多少時間

```dataview
TABLE file.ctime AS 创作日期, date(now)-(file.ctime) AS 迄今时数
sort date(today)-(file.ctime)
```
## Archive List
```dataview
LIST
FROM "Archive"
```
