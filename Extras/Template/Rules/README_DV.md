
## `dataview` 查询语法

### 1. 基本查询类型 (LIST, TABLE, TASK, CALENDAR)

*   **LIST**: 显示一个简单的文件链接列表。
    ```datavie
    LIST
    FROM #笔记标签 or "文件夹路径"
    WHERE file.ctime > date(today) - dur(7 days) // 筛选条件：例如最近7天创建的文件
    SORT file.mtime DESC // 排序：例如按修改时间降序
    LIMIT 10 // 限制数量
    ```

*   **TABLE**: 显示一个包含文件元数据的表格。
    ```datavie
    TABLE priority, file.mtime as "修改时间", status
    FROM #项目 or "01-Projects"
    WHERE status = "进行中" AND priority >= 3
    SORT priority DESC, file.mtime ASC // 按优先级降序，然后按修改时间升序
    ```
    *   `AS "列名"`: 可以重命名列标题。

*   **TASK**: 显示来自不同笔记的未完成任务列表。
    ```datavie
    TASK
    FROM #会议 or "02-Areas/Meetings"
    WHERE !completed AND contains(text, "待办") // 筛选：未完成且包含“待办”字样的任务
    GROUP BY file.link // 按文件分组
    SORT file.mtime DESC
    ```
    *   可以使用 `WHERE completed` 查找已完成任务。
    *   `text` 指任务的文本内容。

*   **CALENDAR**: 将具有日期的笔记显示在日历视图中（通常基于 `date` 字段或文件名日期）。
    ```dataview
    CALENDAR file.ctime // 以文件创建时间为依据
    FROM "03-Resources/DailyNotes"
    WHERE file.day // 确保文件名或元数据中有日期信息
    ```

### 2. 数据来源 (FROM)

*   **标签**: `#标签名` (例如 `#笔记`, `#项目/子项目`)
*   **文件夹**: `"文件夹路径"` (例如 `"Inbox"`, `"01-Projects/Active"`)
*   **链接**: `[[笔记链接]]` (查找链接到此笔记的笔记), `outgoing([[笔记链接]])` (查找此笔记链接出去的笔记)
*   **组合**: 使用 `AND`, `OR`, `NOT` (或 `-`) 组合来源。
    *   `FROM #文章 AND "发布"` (来自“发布”文件夹且带有#文章标签)
    *   `FROM #读书笔记 OR #观影笔记`
    *   `FROM "存档" AND NOT #重要` (或 `FROM "存档" WHERE !contains(file.tags, "#重要")`)
*   **省略 FROM**: 默认从整个库查找。

### 3. 筛选条件 (WHERE)

*   **文件属性 (Implicit Fields)**:
    *   `file.name`: 文件名 (字符串)
    *   `file.path`: 文件路径 (字符串)
    *   `file.folder`: 文件所在文件夹 (字符串)
    *   `file.tags`: 文件的标签数组 (例如 `contains(file.tags, "#待办")`)
    *   `file.links`: 文件中的链接数组
    *   `file.inlinks`: 指向此文件的链接数组
    *   `file.outlinks`: 此文件链出的链接数组
    *   `file.ctime`: 文件创建时间 (日期时间)
    *   `file.mtime`: 文件修改时间 (日期时间)
    *   `file.size`: 文件大小 (数字)
    *   `file.day`: 文件名中解析出的日期 (如果文件名符合 `YYYY-MM-DD` 或 `YYYYMMDD` 等格式)
*   **元数据 (Explicit Fields - YAML Frontmatter or Inline Fields)**:
    *   直接使用字段名，如 `priority`, `status`, `rating`, `due_date`。
    *   **Inline Fields**: `Key:: Value`
*   **比较操作符**: ` =`, `!=`, `>`, `<`, ` >=`, `<=`
*   **字符串函数**:
    *   `contains(field, "value")`: 字段包含 "value"
    *   `startswith(field, "prefix")`: 字段以 "prefix" 开头
    *   `endswith(field, "suffix")`: 字段以 "suffix" 结尾
    *   `lower(field)`, `upper(field)`: 转小写/大写
*   **数组/列表函数**:
    *   `contains(list_field, value)`: 列表包含 `value`
    *   `length(list_field)`: 列表长度
*   **日期和时间**:
    *   `date(today)`: 今天
    *   `date(now)`: 当前日期时间
    *   `date("YYYY-MM-DD")`: 指定日期
    *   `dur(X days/weeks/hours)`: 时间段
    *   比较：`due_date < date(today) + dur(3 days)`
*   **逻辑操作符**: `AND`, `OR`, `NOT` (或 `!`)
*   **检查字段是否存在**: `field` (如果字段存在且不为空/false/0) 或 `!field`

### 4. 排序 (SORT)

*   `SORT field ASC` (升序，默认)
*   `SORT field DESC` (降序)
*   可以按多个字段排序：`SORT field1 DESC, field2 ASC`

### 5. 分组 (GROUP BY)

*   `GROUP BY field` 或 `GROUP BY file.folder`
*   通常用于 `TASK` 查询，将任务按来源文件分组。
*   在 `TABLE` 中使用时，该字段的值会成为分组标题，其他列通常需要聚合函数（如 `length(rows)` 统计数量, `sum(rows.field)` 求和等）。

### 6. 限制 (LIMIT)

*   `LIMIT number` (例如 `LIMIT 5`)

---

## `dataviewjs` 查询语法

`dataviewjs` 查询块使用三个反引号加 `dataviewjs` 来包裹。它提供了完整的 JavaScript 环境以及 Dataview 提供的 API (`dv`)，允许更复杂、更灵活的查询和自定义渲染。

```dataviewjs
```

### 1. 核心 API (`dv`)

*   **`dv.pages(source)`**: 获取页面集合。`source` 可以是 `#tag`, `"folder"`, `[[link]]` 等，与 `dataview` 的 `FROM` 类似。省略 `source` 则获取所有页面。
    *   返回一个 `DataArray` 对象，可以使用链式方法。
*   **`dv.current()`**: 获取当前页面的元数据对象。
*   **渲染函数**:
    *   `dv.list(array)`: 渲染一个列表。数组元素通常是链接 `page.file.link`。
    *   `dv.table(headers, data)`: 渲染一个表格。`headers` 是字符串数组，`data` 是二维数组或对象数组。
    *   `dv.taskList(tasks, groupByFile)`: 渲染一个任务列表。`tasks` 是 `page.file.tasks` 的集合，`groupByFile` (布尔值) 指定是否按文件分组。

### 2. 链式方法 (DataArray Methods)

`dv.pages()` 返回的对象可以使用类似 JavaScript 数组的方法进行链式操作：

*   **`.where(predicate)` / `.filter(predicate)`**: 筛选页面。`predicate` 是一个返回布尔值的函数，参数为单个页面对象 `p`。
    ```dataviewjs
    let pages = dv.pages("#项目")
                  .where(p => p.status == "进行中" && p.priority > 3);
    ```
*   **`.sort(comparator)`**: 排序页面。`comparator` 是一个比较函数，接收两个页面对象 `a`, `b`。
    ```dataviewj
    let sortedPages = pages.sort(p => p.file.mtime, 'desc'); // 按修改时间降序
    let sortedByPriority = pages.sort((a, b) => b.priority - a.priority); // 按优先级数字降序
    ```
*   **`.map(mapper)`**: 转换页面集合中的每个元素。`mapper` 是一个函数，接收页面对象 `p`，返回转换后的值。
    ```dataviewjs
    let names = dv.pages().map(p => p.file.name);
    ```
*   **`.limit(number)`**: 限制数量。
*   **`.groupBy(grouper)`**: 分组。`grouper` 是一个函数，接收页面对象 `p`，返回分组的键。

### 3. 访问页面数据

在 `predicate`, `mapper`, `comparator` 等函数中，参数 `p` 代表单个页面对象，可以访问其属性：

*   `p.file.name`, `p.file.path`, `p.file.folder`, `p.file.tags`, `p.file.ctime`, `p.file.mtime`, `p.file.tasks` 等（与 `dataview` 中的 `file.` 类似）。
*   `p.field_name`: 访问 YAML 或 Inline Field (例如 `p.priority`, `p.status`)。
*   `p.file.link`: 获取页面的 Markdown 链接。

### 4. 示例

*   **简单的列表**:
    ```dataviewjs
    dv.list(dv.pages("#笔记").limit(10).map(p => p.file.link));
    ```

*   **自定义表格**:
    ```dataviewj
    let data = dv.pages('"01-Projects"')
                 .where(p => p.status === "待定")
                 .sort(p => p.file.ctime, 'asc')
                 .map(p => [
                     p.file.link,
                     p.priority,
                     dv.date(p.due_date).toFormat("yyyy-MM-dd"), // 使用 Luxon 格式化日期
                     p.file.mtime.toRelative() // 显示相对修改时间
                 ]);

    dv.table(["项目", "优先级", "截止日期", "上次修改"], data);
    ```

*   **按文件分组的任务列表**:
    ```dataviewj
    let tasks = dv.pages('[[项目A]] or #项目A')
                  .file.tasks
                  .where(t => !t.completed && t.text.includes("重要")); // 筛选未完成且包含“重要”的任务

    dv.taskList(tasks, true); // 第二个参数 true 表示按文件分组
    ```

*   **更复杂的逻辑 (例如，计算总数)**:
    ```dataviewjs
    let completedProjects = dv.pages("#项目").where(p => p.status === "已完成");
    let count = completedProjects.length;
    dv.paragraph(`当前已完成的项目总数：**${count}** 个。`);
    dv.list(completedProjects.map(p => p.file.link));
    ```

*   **使用 `dv.current()`**:
    ```dataviewjs
    // 显示链接到当前笔记的相关笔记（假设相关笔记有 'related' 字段指向当前笔记）
    let currentFileLink = dv.current().file.link;
    dv.list(dv.pages().where(p => p.related === currentFileLink).map(p => p.file.link));
    ```

### 5. 注意事项

*   `dataviewjs` 提供了更大的灵活性，但也更复杂，需要 JavaScript 基础。
*   可以使用 `console.log()` 在 Obsidian 的开发者工具 (Ctrl+Shift+I 或 Cmd+Opt+I) 中调试 `dataviewjs` 代码。
*   日期时间处理通常使用 Dataview 内置的 Luxon 库 (`dv.date()`, `dv.duration()`)。
*   性能：非常复杂的 `dataviewjs` 查询可能会影响 Obsidian 的性能，尤其是在页面数量很多的情况下。

---

**选择 `dataview` 还是 `dataviewjs`？**

*   如果你的需求相对简单（筛选、排序、基本表格/列表），`dataview` 通常足够，且语法更简洁。
*   如果你需要复杂的计算、自定义的输出格式、条件逻辑或者 `dataview` 无法实现的查询，选择 `dataviewjs`。

记得查阅 [Dataview 官方文档](https://blacksmithgu.github.io/obsidian-dataview/) 获取最全面和最新的信息。