```dataviewjs
let ftMd = dv.pages("").file.sort(t => t.cday)[0]
let total = parseInt([new Date() - ftMd.ctime] / (60*60*24*1000))
let totalDays = "您已使用 ***Obsidian*** "+total+" 天，"
let nofold = '!"misc/templates"'
let allFile = dv.pages(nofold).file
let totalMd = "共创建 "+ allFile.length+" 篇笔记"
let totalTag = allFile.etags.distinct().length+" 个标签"
let totalTask = allFile.tasks.length+"个待办。 "
dv.paragraph(
	totalDays + totalMd + "、" + totalTag + "、" + totalTask
)
```
## 最新10个7日内修改笔记(非archive)
```dataview

// TABLE  file.mtime AS 修改日期, file.mtime AS 修改日期
TABLE date(today)-(file.mday) AS 迄今天数
from -"4. Archives" and -"Extras"
// WHERE (date(today)-(file.mtime)).day<7 
WHERE file.mtime >= date(today) - dur(7 day)
// sort file.mtime DESC
sort file.mtime
LIMIT 10
```

## 项目(全部)
```dataview
TABLE  file.ctime AS 创作日期
FROM "1. Projects"
// WHERE theme = "微信阅读"
sort file.mtime DESC
LIMIT 10
```

## 具体领域(AI)
```dataview
TABLE  file.ctime AS 创作日期
FROM "2. Areas/AI"
// WHERE theme = "微信阅读"
sort file.mtime DESC
LIMIT 10
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

list
FROM #todo 
sort file.mtime desc
// GROUP BY file.folder
limit 10
```

## Todo List2
```dataview

task
//FROM #todo
WHERE !completed
sort file.mtime desc
// GROUP BY file.folder
limit 5
```


## 同月新建的笔记

```dataview

TABLE file.ctime AS 创作日期
from !"Archive"
WHERE file.ctime.month = date(today).month
sort date(today)-(file.ctime)

LIMIT 10
```



## 建檔迄今過了多少時間

```dataview
// striptime(file.ctime)
TABLE file.ctime AS 创作日期, date(today)-(file.mday) AS 迄今时数
// from !"Archive" and !"Extras"
from -"Archive" or -"Extras"
// sort (date(now)-(file.mtime)) DESC
sort (date(now)-(file.mtime)) DESC
LIMIT 10
```

## Archive List
```dataview
LIST
FROM "4. Archives"
sort (date(now)-(file.mtime)) DESC
LIMIT 10
```