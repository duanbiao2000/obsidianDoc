
<details>
<summary>12. 如何创建一个只显示过去7天内修改过的笔记的Base？</summary>
**答案:**
1.  添加一个过滤器，属性选择`file.mtime` (修改时间)。
2.  操作符选择`is after`。
3.  值输入`today() - "7d"`。
</details>

<details>
<summary>13. 如何显示所有图片附件（.png, .jpg）？</summary>
**答案:**
1.  创建一个Base。
2.  添加一个过滤器组（`or`逻辑）。
3.  在组内添加第一个过滤器：`file.ext` is `png`。
4.  在组内添加第二个过滤器：`file.ext` is `jpg`。
</details>

<details>
<summary>14. 如何创建一个显示所有没有设置`status`属性的笔记的Base？</summary>
**答案:**
添加一个过滤器，属性选择`status`，操作符选择`is empty`。
</details>

<details>
<summary>15. 如何导出Base视图为CSV文件？</summary>
**答案:**
点击左上角的视图名称，在下拉菜单中选择“Export to CSV”。
</details>

<details>
<summary>16. 我想建立一个电影清单，笔记中都有一个`rating`（1-5）属性，如何只显示评分大于等于4的电影？</summary>
**答案:**
添加一个过滤器，属性选择`rating`，操作符选择`is greater than or equal to`，值输入`4`。
</details>

<details>
<summary>17. 如何创建一个显示所有包含“会议”一词的笔记的Base？</summary>
**答案:**
添加一个过滤器，属性选择`file.name`，操作符选择`contains`，值输入`会议`。
</details>

<details>
<summary>18. 如何在同一个Base文件中创建第二个视图？</summary>
**答案:**
点击左上角视图名称旁边的“+”号，或者在视图下拉菜单中选择“New view”。
</details>

<details>
<summary>19. 如何将一个表格视图（Table）切换为卡片视图（Cards）？</summary>
**答案:**
1.  点击左上角的视图名称，选择“Configure view”。
2.  在“Layout”选项中，选择“Cards”。
</details>

<details>
<summary>20. 在卡片视图中，如何设置卡片的封面图片？</summary>
**答案:**
在卡片视图的配置中，“Image property”选项选择一个包含图片链接的属性（例如，一个名为`cover`的属性，其值为`[[cover.jpg]]`或一个URL）。
</details>

---

### 第二部分：进阶练习 (21-50)

这部分练习将引导你使用更复杂的过滤、公式和多视图管理。

<details>
<summary>21. 如何创建一个同时满足两个条件的过滤器（AND逻辑）？</summary>
**答案:**
默认情况下，添加多个过滤器就是AND逻辑。例如，同时添加`tags` contains `book`和`status` is `reading`，将只显示正在阅读的书籍。
</details>

<details>
<summary>22. 如何创建一个满足任一条件的过滤器（OR逻辑）？</summary>
**答案:**
在“Filters”面板中，点击“Add filter or group”，选择“New group (any)”。然后在这个组内添加你的多个条件。例如，显示`status` is `urgent` **或** `priority` is `high`的笔记。
</details>

<details>
<summary>23. 如何使用公式（Formula）创建一个新列？</summary>
**答案:**
在“Properties”面板中，点击“Add property”，然后选择“New formula”。例如，给它命名为`price_with_tax`。
</details>

<details>
<summary>24. 假设笔记有`price`属性，如何用公式计算含10%税的价格并显示在新列？</summary>
**答案:**
1.  创建一个名为`price_with_tax`的公式属性。
2.  在公式编辑框中输入`price * 1.1`。
</details>

<details>
<summary>25. 如何用公式将两个文本属性（如`firstName`和`lastName`）合并成一个完整的姓名列？</summary>
**答案:**
创建一个名为`fullName`的公式属性，公式为`firstName + " " + lastName`。
</details>

<details>
<summary>26. 如何创建一个“笔记年龄”的公式列，显示从创建到现在过去了多少天？</summary>
**答案:**
创建一个名为`noteAge`的公式列，输入公式 `(now() - file.ctime).days`。
</details>

<details>
<summary>27. 我有一个项目管理Base，笔记属性有`deadline`（日期格式），如何用公式计算距离截止日期还有几天？</summary>
**答案:**
创建一个名为`days_left`的公式属性，公式为`(deadline - now()).days`。
</details>

<details>
<summary>28. 如何使用`if`函数在公式中进行条件判断？</summary>
**答案:**
`if(condition, value_if_true, value_if_false)`。例如，创建一个名为`priority_label`的公式，内容为`if(priority > 3, "高", "普通")`。
</details>

<details>
<summary>29. 如何筛选出文件名以“2025-”开头的笔记？</summary>
**答案:**
添加一个过滤器，使用高级模式（点击过滤器输入框旁边的小代码图标），输入`file.name.startsWith("2025-")`。
</details>

<details>
<summary>30. 如何在卡片视图中，让没有封面的卡片显示特定的颜色？</summary>
**答案:**
在你的笔记中，如果`cover`属性为空，可以设置一个`color`属性，值为十六进制颜色码（如`#ff0000`）。然后在卡片视图配置中，将“Image property”设置为`cover`或`color`。Base会自动渲染颜色。
</details>

<details>
<summary>31. 如何创建一个Base，显示所有链接到当前笔记的笔记（模拟反向链接面板）？</summary>
**答案:**
将Base嵌入到你的笔记中。然后添加一个过滤器，使用高级模式输入 `file.hasLink(this.file)`。这里的`this.file`特指嵌入该Base的当前文件。
</details>

<details>
<summary>32. 如何显示所有`pages`属性大于200，并且`language`属性为“English”的读书笔记？</summary>
**答案:**
添加两个过滤器（AND逻辑）：
1.  `pages` is greater than `200`
2.  `language` is `English`
</details>

<details>
<summary>33. 如何用公式将一个数字格式化为货币字符串，例如将`123`变为`"$123.00"`？</summary>
**答案:**
创建一个公式属性，内容为`"$" + price.toFixed(2)`。
</details>

<details>
<summary>34. 如何创建一个视图，按文件夹分组显示我的所有笔记？</summary>
**答案:**
在视图的配置选项中，找到“Group by”选项，选择`file.folder`。
</details>

<details>
<summary>35. 我有一个会议记录文件夹，如何创建一个Base，显示所有“参与人”（`attendees`，一个列表属性）中包含“张三”的会议？</summary>
**答案:**
添加一个过滤器，属性选择`attendees`，操作符选择`contains`，值输入`张三`。
</details>

<details>
<summary>36. 如何创建一个Base，显示所有出链（outgoing links）数量超过5个的笔记？</summary>
**答案:**
添加一个过滤器，使用高级模式，输入`file.links.length > 5`。
</details>

<details>
<summary>37. 如何用公式检查一个任务是否逾期？（假设有`deadline`和`status`属性）</summary>
</details>

<details>
<summary>38. 如何创建一个“看板”视图的雏形？（按`status`属性分组的卡片视图）</summary>
**答案:**
1.  创建一个卡片视图。
2.  在视图配置中，设置“Group by”为`status`属性。
</details>

<details>
<summary>39. 如何筛选出属性`review_date`（审核日期）是今天的笔记？</summary>
**答案:**
添加一个过滤器，属性`review_date`，操作符`is`，值输入`today()`。
</details>

<details>
<summary>40. 如何在一个Base中创建一个“已归档”视图，显示所有`status`为`archived`或在`Archive`文件夹中的笔记？</summary>
**答案:**
1.  创建一个新视图，命名为“已归档”。
2.  添加一个OR逻辑的过滤器组。
3.  组内添加条件1: `status` is `archived`。
4.  组内添加条件2: `file.folder` is `Archive`。
</details>

<details>
<summary>41. 如何用公式从一个完整的日期时间属性`created_at`中只提取出日期部分？</summary>
**答案:**
创建一个公式属性，输入`created_at.date()`。
</details>

<details>
<summary>42. 如何显示所有YAML属性中`aliases`（别名）不为空的笔记？</summary>
**答案:**
添加一个过滤器，属性选择`aliases`，操作符选择`is not empty`。
</details>

<details>
<summary>43. 如何创建一个Base，显示所有与当前笔记有相同标签的笔记？</summary>
**答案:**
嵌入Base到笔记中，使用高级过滤器 `file.tags.some(tag => this.file.tags.contains(tag)) and file.path != this.file.path`。
</details>

<details>
<summary>44. 如何用公式将笔记的标签列表转换成一个用逗号分隔的字符串？</summary>
**答案:**
创建一个公式属性，输入`file.tags.join(", ")`。
</details>

<details>
<summary>45. 如何在Base中显示文件的相对路径？</summary>
**答案:**
在“Properties”中，添加`file.path`属性。
</details>

<details>
<summary>46. 如何筛选出YAML区域大于10行的笔记？（一个近似的指标）</summary>
**答案:**
这是一个高级用法，目前Base本身无法直接计算YAML行数。你可以通过外部脚本预处理，在YAML中加入一个`yaml_lines`属性，然后根据这个属性筛选。
</details>

<summary>48. 如何在Base中创建一个“复制Markdown链接”的按钮？</summary>
创建一个公式列，使用`link`函数。公式可以为`link(file.path, "复制")`。但这只会创建一个内部链接，更复杂的操作需要社区插件支持。
</details>

<details>
<summary>49. 如何创建一个显示所有孤立笔记（没有入链也没有出链）的Base？</summary>
**答案:**
添加一个AND过滤器组：
1. `file.inlinks.length == 0`
2. `file.outlinks.length == 0`
</details>

<details>
<summary>50. 如何在不同的Base视图之间快速切换？</summary>
**答案:**
点击Base视图左上角的视图名称，在下拉列表中选择你想要切换到的视图。
</details>

---

### 第三部分：高手练习 & LLM集成 (51-100)

这部分将深入探讨高级公式、复杂视图、自动化工作流，特别是如何利用LLM来生成和维护你的Base内容。你需要安装一个LLM插件，如 `Text Generator`。

<details>
<summary>51. [LLM] 我想创建一个书籍库，如何让LLM帮我生成10本关于“科幻小说”的书籍笔记，并包含标准化的YAML属性？</summary>
**答案:**
1.  安装并配置好`Text Generator`插件。
2.  创建一个新的笔记，打开`Text Generator`。
3.  使用类似以下的提示词 (Prompt):
    > “请为我生成10个独立的Markdown笔记内容，每个笔记代表一本经典的科幻小说。每个笔记都必须包含以下YAML frontmatter格式：
    > ```yaml
    > ---
    > title: "书籍标题"
    > author: "作者"
    > year: 出版年份
    > rating: 0
    > status: "toread"
    > tags: [book, scifi]
    > cover_url: "一个有效的封面图片URL"
    > ---
    > 
    > # [书籍标题]
    > 
    > [书籍的一段简短介绍]
    > ”
4.  执行生成，然后将返回的内容分割成10个独立的`.md`文件。你的书籍Base现在就会自动填充这些新笔记。
</details>

<details>
<summary>52. [LLM] 如何使用LLM为一个已存在的笔记（例如一篇粘贴的文章）自动生成摘要和关键词，并填充到YAML属性中？</summary>
**答案:**
1.  在`Text Generator`中创建一个模板。
2.  模板内容可以设置为：
    > ```yaml
    > ---
    > summary: "{{摘要}}"
    > keywords: [{{关键词列表}}]
    > ---
    > 
    > {{笔记原文}}
    > ```
3.  配置一个使用此模板的命令，其中包含两个LLM请求：一个用于生成`摘要`（“请为以下文章生成一个50字的摘要：{{笔记原文}}”），另一个用于生成`关键词列表`（“请为以下文章提取5个关键词，并用逗号分隔：{{笔记原文}}”）。
4.  对你的文章笔记执行此命令，它会自动更新YAML区域。
</details>

<details>
<summary>53. 如何创建一个“项目仪表盘”，其中包含三个视图：“进行中的项目”、“已完成的项目”和“所有项目的卡片视图”？</summary>
**答案:**
1.  在一个`.base`文件中创建三个视图。
2.  **视图1 “进行中”**: 表格布局。过滤器设置为 `type` is `project` AND `status` is `inprogress`。
3.  **视图2 “已完成”**: 表格布局。过滤器设置为 `type` is `project` AND `status` is `completed`。
4.  **视图3 “所有项目卡片”**: 卡片布局。过滤器设置为 `type` is `project`。设置封面图片和需要显示的属性。
</details>

<details>
<summary>54. 我有一个习惯打卡的Base，笔记属性有`habit`和`date`，如何用公式计算出每个习惯的“连续打卡天数”？</summary>
**答案:**
这是一个非常高级的挑战，因为Base的公式目前无法直接跨笔记进行连续性计算。实现这个功能的最佳方法是：
1.  **方法一（简化）**: 创建一个“最近打卡”视图，按`habit`分组，按`date`降序排序，让你能直观地看到每个习惯的最近打卡日期。
2.  **方法二（外部脚本）**: 使用Python或DataviewJS等工具定期扫描笔记，计算连续天数，并将结果写回每个习惯主笔记的YAML属性（如`streak_days`）中。然后Base就可以直接显示这个属性了。
</details>

<details>
<summary>55. [LLM] 我有很多会议录音的文字稿，如何利用LLM自动提取会议日期、参与者、以及行动项，并创建带有这些属性的会议记录笔记？</summary>
**答案:**
使用`Text Generator`插件，设计一个复杂的提示词：
> “你是一个会议纪要分析助手。请从以下会议文字稿中提取信息，并以YAML frontmatter的格式输出。你需要提取：
> - `meeting_date`: 会议日期 (格式 YYYY-MM-DD)
> - `participants`: 参与者列表 (YAML list格式)
> - `action_items`: 行动项列表，每个项目前要标记负责人 (YAML list格式)
> 
> 文字稿如下：
> ```
> {{selection}}
> ```
> ”
>
> 将这段提示词配置为命令，选中文字稿后执行，即可生成带有结构化数据的笔记。
</details>

<details>
<summary>56. 如何创建一个Base，用于管理CRM客户信息，并根据`last_contact_date`属性，将超过90天未联系的客户高亮显示？</summary>
**答案:**
1.  创建一个客户信息Base。
2.  添加一个名为`follow_up_status`的公式列。
3.  公式为：`if((now() - last_contact_date).days > 90, "🔴 需要跟进", "🟢 正常")`。
4.  你可以根据这个新列进行排序，优先处理需要跟进的客户。
</details>


<details>
<summary>59. [LLM] 如何使用LLM批量为一系列产品笔记生成统一格式的优缺点列表？</summary>
**答案:**
1.  创建一个`Text Generator`模板，用于调用LLM。
2.  提示词示例：
    > "根据以下产品描述，生成一个Markdown格式的优缺点列表。
    >
    > ### 优点
    > - [优点1]
    > - [优点2]
    >
    > ### 缺点
    > - [缺点1]
    >
    > 产品描述：
    > {{note_content}}
    > "
3.  可以使用`Text Generator`的批量处理功能，对一个文件夹下的所有产品笔记执行此模板。
</details>

<details>
<summary>60. 如何创建一个动态的“学习路线图”Base，根据前置课程（`prerequisites`属性）是否完成（`status: "completed"`）来决定当前课程的状态？</summary>
**答案:**
这同样超出了Base内置公式的能力范围，因为它需要查询其他笔记的状态。推荐的实现方式是：
1.  使用Dataview插件的行内查询（inline query）来动态显示每个课程的状态。
2.  或者，使用更强大的DataviewJS脚本来生成一个动态的Markdown表格，模拟Base的功能，但在其中加入跨笔记查询的逻辑。
</details>

<details>
<summary>61. 如何在Base中处理多对多关系？例如，管理作者和书籍，一个作者可以写多本书，一本书也可以有多个作者。</summary>
**答案:**
1.  创建两类笔记：“作者笔记”和“书籍笔记”。
2.  在“书籍笔记”的YAML中，使用列表属性`authors`链接到对应的作者笔记，如 `authors: ["[[作者A]]", "[[作者B]]"]`。
3.  在“作者笔记”的YAML中，也可以创建一个`books`列表。
4.  创建一个“书籍”Base，可以按`authors`属性进行筛选。
5.  创建一个“作者”Base，可以按`books`属性进行筛选。
</details>

<details>
<summary>62. [LLM] 如何让LLM扮演一个项目经理，为一个新的项目构想（一句话描述）生成一个包含任务拆解、预计工时和优先级的笔记，并自动添加`type: task`等属性？</summary>
**答案:**
配置一个`Text Generator`命令，提示词如下：
> “你是一个经验丰富的项目经理。请将以下项目构想拆解成一个详细的任务列表，并为每个任务估算工时（小时）和设置优先级（高/中/低）。请以一个完整的Markdown笔记形式输出，包含一个`tasks`属性，其值为一个对象列表的YAML。
>
> 项目构想: `{{selection}}`
>
> 输出格式示例:
> ```yaml
> ---
> project_name: "{{selection}}"
> status: "planning"
> tags: [project]
> tasks:
>   - task: "任务一"
>     hours: 8
>     priority: "高"
>   - task: "任务二"
>     hours: 16
>     priority: "中"
> ---
>
> # 项目：{{selection}}
>
> ## 任务分解
>
> ### 任务一
> ...
> ”
</details>

<details>
<summary>63. 如何创建一个Base视图，显示所有重复的笔记（文件名相同，但路径不同）？</summary>
**答案:**
这需要分组和计数的聚合功能，目前Base还不支持。但你可以通过DataviewJS查询实现：
```dataviewjs
const pages = dv.pages()
    .groupBy(p => p.file.name)
    .filter(g => g.rows.length > 1)
    .sort(g => g.key);
dv.table(["重复文件名", "文件路径"], pages.map(p => [p.key, p.rows.map(row => row.file.link).join(", ")]));
```
</details>

<details>
<summary>64. 我能否在Base的公式中使用正则表达式？</summary>
**答案:**
是的，可以使用`test()`函数。例如，要筛选出`email`属性符合标准邮箱格式的笔记，可以在高级过滤器中使用 `test(/^[^\s@]+@[^\s@]+\.[^\s@]+$/, email)`。
</details>

<details>
<summary>65. [LLM] 如何使用LLM将非结构化的文本（如剪藏的网页）转换为结构化的笔记，自动提取标题、作者、发布日期等信息填入YAML？</summary>
**答案:**
与问题55类似，创建一个`Text Generator`模板，让LLM从文本中提取关键信息。
> "从以下文章内容中提取`title`, `author`, `publication_date`，并以YAML格式返回。如果找不到某个信息，请将其值留空。
>
> 文章内容:
> {{clipboard}}
>"
</details>

<details>
<summary>66. 如何创建一个“每周回顾”的Base，自动筛选出上周创建的所有笔记，并按文件夹分组？</summary>
**答案:**
1.  创建一个新Base或新视图。
2.  添加一个AND过滤器组：
    -   `file.ctime` is after `today() - "7d" - (weekday(today()) - 1) + "d"` (上周一)
    -   `file.ctime` is before `today() - (weekday(today()) - 1) + "d"` (本周一)
3.  在视图配置中，设置“Group by”为`file.folder`。
</details>

<details>
<summary>67. 如何在Base中管理食谱，并添加一个“总热量”的公式列，该列的值是`ingredients`（一个对象列表）中每个成分热量的总和？</summary>
**答案:**
假设`ingredients`的YAML结构是：
```yaml
ingredients:
  - name: "鸡蛋"
    calories: 155
  - name: "面粉"
    calories: 364
```
可以使用`map`和`sum`函数来计算总和。创建一个公式列，输入：
`ingredients.map(i => i.calories).sum()`
</details>

<details>
<summary>68. [LLM] 如何使用LLM为我的旅行照片笔记批量生成描述性的文字和相关的`tags`？</summary>
**答案:**
这需要一个能够处理图片的多模态LLM插件。如果你的LLM插件支持（例如通过API连接到GPT-4V），你可以这样设计提示词：
> "这是一张旅行照片。请为其生成一段50字的生动描述，并提取5个相关的标签（如`#beach`, `#sunset`）。
>
> 图片: `{{image_path}}`"
>
> 然后批量处理你的照片笔记。
</details>

<details>
<summary>69. 我可以自定义Base视图的CSS样式吗？</summary>
**答案:**
可以。通过Obsidian的CSS片段（CSS Snippets）功能，你可以针对Base的特定CSS类（如`.base-table-view`, `.base-card-view`）编写自定义样式，来改变字体、颜色、间距等。
</details>

<details>
<summary>70. 如何创建一个“今日待办”的Base，显示所有`type: task`、`status: incomplete`且`due_date`为今天或之前的笔记？</summary>
**答案:**
创建一个AND过滤器组：
1. `type` is `task`
2. `status` is `incomplete`
3. `due_date` is on or before `today()`
</details>

<details>
<summary>71. [LLM] 我正在学习一门外语，如何用LLM为我的单词本笔记自动生成例句，并存入`examples`属性？</summary>
**答案:**
为`Text Generator`配置一个命令：
> “为单词`{{title}}`（在笔记标题中）生成三个英语例句，并以YAML列表的格式返回。
>
> 单词：`{{title}}`
>
> 格式:
> ```yaml
> examples:
>   - "例句1"
>   - "例句2"
>   - "例句3"
> ```
</details>

<details>
<summary>72. 如何在Base中创建一个“甘特图”的近似视图？</summary>
**答案:**
目前Base没有原生的甘特图视图。但你可以：
1.  创建一个任务Base，包含`start_date`和`end_date`属性。
2.  创建一个公式列，名为`timeline`，用文本字符（如`■`）来模拟时间条的长度和位置，但这非常复杂。
3.  更现实的方法是，使用Mermaid图表语法，并借助DataviewJS从Base查询的数据动态生成Mermaid代码。
</details>

<details>
<summary>73. 如何处理Base中的嵌套属性？例如`person.address.city`。</summary>
**答案:**
你可以在过滤器和公式中直接使用点符号来访问嵌套属性。例如，筛选城市为“北京”的笔记：`person.address.city` is `北京`。
</details>

<details>
<summary>74. [LLM] 我想写一部小说，如何用LLM帮我生成角色卡片笔记，包含姓名、年龄、背景故事和性格特点等YAML属性？</summary>
**答案:**
提示词示例：
> “为我的赛博朋克小说创建一个新的角色。请随机生成角色的姓名、年龄、职业，并撰写一段200字的背景故事和5个核心性格特点。请将这些信息以YAML frontmatter的格式输出。”
</details>

<details>
<summary>75. 如何在Base中实现一个简单的发票管理系统，自动计算每张发票的“总金额”（`items`列表中`price * quantity`的总和）？</summary>
**答案:**
类似于问题67，假设`items`结构为`{name, price, quantity}`。
创建一个名为`total_amount`的公式列，输入：
`items.map(i => i.price * i.quantity).sum()`
</details>

**剩余的25个练习将进一步挑战极限，并融合多种高级技巧。**

76.  **[LLM] 知识图谱扩展**：使用LLM分析一篇笔记，识别出其中的关键概念，并自动创建新的笔记链接到这些概念，同时在Base中跟踪这些新生成的“概念笔记”。
77.  **动态MOC**：创建一个Base，它能根据当前文件夹（`this.file.folder`）动态筛选和显示该文件夹下的所有笔记，作为一个可嵌入的、自动更新的目录。
78.  **财务追踪**：创建一个支出记录Base，用公式计算每个月的总支出，并通过视图分组功能按类别（`category`属性）查看支出分布。
79.  **A/B测试笔记**：创建两个版本的笔记模板（A和B），用一个`template_version`属性标记。然后用Base分析这两个版本的笔记在“完成率”（`status: "completed"`）上是否有差异。
80.  **[LLM] 自动链接建议**：使用LLM读取一个新笔记的内容，然后在你的知识库中找到3个最相关的旧笔记，并将它们的链接添加到一个名为`related_links`的YAML属性中。
81.  **高级时间计算**：在任务Base中，创建一个公式列`working_days_left`，只计算剩余的工作日（排除周末）。这需要更复杂的日期函数组合。
82.  **内容依赖过滤**：筛选出所有在笔记正文（`file.content`）中提到了`[[项目X]]`，但在YAML的`project`属性中却没有标记`项目X`的笔记，用于数据清洗。
83.  **[LLM] 风格转换器**：用LLM将一篇技术性的笔记改写成通俗易懂的语言，并将改写后的内容保存在一个新的笔记中，通过`original_note`属性链接回原文。
84.  **Base作为导航**：创建一个“仪表盘”笔记，嵌入多个Base视图，分别显示“今日待办”、“最近文档”、“高优项目”，作为你进入Obsidian的启动页面。
85.  **习惯养成可视化**：在习惯打卡Base中，使用公式列，根据连续打卡天数（假设已通过外部脚本计算）显示不同的emoji（如🔥, 👍, 😊），实现游戏化。
86.  **[LLM] 生成测试题**：让LLM根据你的学习笔记内容，生成选择题或填空题，并创建为带有`question`, `options`, `answer`属性的新笔记，方便后续用Base制作成复习卡片。
87.  **元数据健康检查**：创建一个Base，专门用来查找元数据不完整的笔记，例如`title`为空，或`review_date`格式不正确的笔记。
88.  **嵌套Base**：在一个描述项目的笔记中，嵌入一个只显示该项目相关任务的Base。这个Base的过滤器会引用父笔记的项目名称：`project` is `this.file.name`。
89.  **[LLM] 市场研究**：使用LLM插件和网页抓取功能，自动收集关于某个主题的最新新闻，并将每条新闻保存为一个带有来源、日期和摘要属性的笔记，在Base中进行跟踪。
90.  **复杂评分系统**：为书籍创建一个“综合评分”公式列，该评分由你的个人评分（`my_rating`）和社区评分（`goodreads_rating`）加权平均得出。
91.  **动态项目报告**：在一个项目周报模板中嵌入一个Base，该Base自动筛选出本周内所有状态变为“完成”的任务。
92.  **[LLM] 角色扮演对话**：创建一个`Text Generator`命令，让你能与你的一个“角色”笔记（问题74创建的）进行对话。LLM会基于角色的背景和性格特点来回答你的问题。
93.  **版本控制模拟**：管理文档时，为每次重大修改创建一个副本，并添加`version`和`change_log`属性。用Base来查看一个文档的所有历史版本和修改记录。
94.  **跨库查询（高级）**：虽然Base本身不支持，但可以通过将其他库的笔记数据导出为JSON，然后在一个库中使用DataviewJS读取这个JSON文件来模拟跨库Base。
95.  **[LLM] 情感分析**：对你的日记笔记（文件夹），使用LLM进行情感分析（正面/中性/负面），并将结果写入`sentiment`属性，然后在Base中可视化你一段时间内的情绪波动。
96.  **查找信息孤岛**：创建一个Base，筛选出那些只有一个入链（通常是来自某个MOC或索引），但没有任何出链的笔记，这些可能是知识网络中的“断头路”。
97.  **“下一步行动”生成器**：创建一个Base，显示所有`status`为`waiting_for`的任务。并创建一个公式按钮，点击后可以用LLM生成一封催办邮件的草稿。
98.  **[LLM] 思维链（CoT）提示**：创建一个复杂的`Text Generator`命令，让LLM在处理一个复杂问题时，先输出它的思考过程，再给出最终答案，并将整个过程记录在一个笔记中，用于知识溯源。
99.  **Base驱动的写作流程**：创建一个写作项目Base，管理你的章节。其中一个视图是“大纲”，只显示章节标题和简介。另一个是“写作中”，只显示`status: "writing"`的章节。还有一个是“字数统计”，用公式（`file.content.length`）来跟踪每章的进度。
100. **终极挑战：自我维护的知识库**：结合以上所有技巧，设计一个工作流。当你创建一个新笔记时，一个自动化工具（如Templater + Text Generator）会触发LLM进行分析，自动添加标签、摘要和相关链接。然后，一个“数据健康”Base会定期检查所有笔记的元数据完整性，并标记出需要你手动整理的条目，形成一个几乎全自动的知识管理闭环。
