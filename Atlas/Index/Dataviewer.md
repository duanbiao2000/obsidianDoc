

```dataviewjs
let ftMd = dv.pages("").file.sort(t => t.ctime)[0]
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

好的，这是查询 "尚硅谷" 路径下最后更改的 5 条笔记的 Dataview 命令：

```dataview
LIST
FROM "2.Sphere"
SORT file.mtime ASC
WHERE !startswith(file.name, "_Index_of")
LIMIT 5
```

```dataview
LIST
FROM "1.Projects"
SORT file.mtime ASC
WHERE !startswith(file.name, "_Index_of")
LIMIT 5
```

```dataview
LIST
FROM "0.DailyNotes"
SORT file.mtime ASC
WHERE !startswith(file.name, "_Index_of")
LIMIT 5
```


## 待实践动作：

```dataview
TASK
// FROM -"Atlas/kanban"
FROM "1.Projects"
WHERE !completed
SORT file.mtime DESC
LIMIT 20
GROUP BY file.folder
```


## Dataview 插件示例

最近编辑

任务管理

每月新建文档数

即将到期

## 大小排列

```dataviewjs
const pages = dv.pages("")
  .sort(p => p.file.size, 'desc');

if (pages.length < 7) {
  dv.paragraph("Vault 中文件数量少于 7 个，无法执行查询。");
} else {
  const slicedPages = pages.slice(2, 7);

  dv.table(
    ["File", "Size (Bytes)"],
    slicedPages.map(p => [p.file.link, p.file.size])
  );
}
```

## 随机10条笔记table
```dataviewjs
const pages = dv.pages().array();
const shuffledPages = pages.sort(() => 0.5 - Math.random());
const randomPages = shuffledPages.slice(0, 5);

const tableData = randomPages.map(page => [
  page.file.link,
  page.file.tags ? page.file.tags.join(", ") : "无标签"
]);

dv.table(["文件", "标签"], tableData);
```

## 高优先级
```dataview
TABLE  high_priority, file.ctime AS 创作日期
from -"4. Archives" or -"Extras" or #todo
WHERE  high_priority = false
sort file.mtime DESC
LIMIT 10
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

[[Dataview-7日内新建的笔记]]

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
