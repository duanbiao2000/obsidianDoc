---
aliases:
date: 2025-10-19 14:16
tags:
source:
  - https://github.com/bregman-arie/devops-exercises/blob/master/topics/software_development/README.md
update:
rating:
---

# Kanban vs Scrum： Agile圈的“自由派”与“纪律委员”大PK

咱们先一句话戳中核心：Kanban是“流水不争先”的连续派，Scrum是“冲刺有节奏”的周期派。接下来就顺着你给的几个关键点，掰开揉碎讲清楚，保证既有干货又不无聊～

### 1. 工作节奏：“流水账”VS“冲刺打卡”

- **Kanban**：主打一个“continuous flow（持续流动）”，像奶茶店做奶茶——点单（To Do）、制作（In Progress）、打包（Review）、出餐（Done），任务来了就接，做完一个走一个，全程“流水式”推进，没有固定的“截止日期”。比如运营团队处理日常用户反馈，来了bug就修，有临时活动需求就接，不用等“下一波”。

- **Scrum**：走的是“结构化冲刺”路线，核心是“sprint（冲刺）”——一般1-4周一个周期，比如每2周定一次“冲刺目标”，开始前选好要做的任务（从Product Backlog里挑），到期必须交出一个“能落地的成果”（Potentially Shippable Increment）。就像游戏里打副本，每次冲刺只冲一个BOSS，打完复盘，再打下一个，节奏特别固定。

### 2. 结构化程度：“宽松牛仔裤”VS“定制西装”

- **Kanban**：堪称Agile圈的“松弛感代表”，“less structured（低结构化）”是它的标签。没有强制规则，你甚至可以把它套在现有工作流程上——比如开发团队原来有“需求评审”环节，加个Kanban列就行，不用大改流程，灵活得像穿牛仔裤，怎么舒服怎么来。

- **Scrum**：妥妥的“纪律委员”，规则多且严。从角色（Product Owner、Scrum Master、Dev Team）到会议（Sprint Planning、Daily Scrum），再到文档（Sprint Backlog），每一步都有明确要求，就像穿定制西装，领口、袖口都得按规矩来，不能随便改。

### 3. 可视化：“全透明玻璃房”VS“半透明窗户”

- **Kanban**：把“visualized（可视化）”刻进DNA里！核心工具是“Kanban Board（看板）”，每个任务都像贴了便利贴，在哪一步、卡没卡壳，一眼看穿。更关键的是有“WIP limits（在制品限制）”——比如“In Progress”列最多放3个任务，避免大家手忙脚乱“同时开N个坑”。就像餐厅后厨的出餐屏，哪道菜在炒、哪道菜等传菜，全员看得明明白白。

- **Scrum**：虽然也能用“Scrum Board”跟踪任务，但可视化只是“辅助工具”，不是核心。比如冲刺期间，团队可能用看板列“待做/进行中/已完成”，但没人强制要求加WIP限制，重点是“按时完成冲刺目标”，不是“优化流程流动”。

### 4. 会议与角色：“极简风”VS“全配置”

- **Kanban**：主打“少开会、无套路”——没有强制会议，最多偶尔开个“流程优化会”（比如发现“Review”列总卡壳，大家聊两句怎么改进）；也没有“固定角色”，不用设专门的“看板负责人”，谁有空谁跟进，主打一个“人人都是主人翁”。

- **Scrum**：会议和角色“一个都不能少”——4个强制会议（Sprint Planning定目标、Daily Scrum同步进度、Sprint Review演示成果、Sprint Retrospective复盘问题），3个固定角色（PO管需求优先级、SM保流程合规、Dev Team搞开发），少一个都不算“正经Scrum”。

最后给个“选择小Tips”：如果你的团队常接临时需求、需要灵活响应（比如运营、客服），选Kanban；如果你的项目有明确阶段目标、需要稳定交付（比如开发新功能版本），选Scrum～



# 一文搞懂 Composition：编程界的“乐高大师”玩法

先一句话破防：Composition 就是用“小零件”拼“大物件”，核心思路是 **“组合优于继承”**（Design Principle 里的金句，记不住也没事，看例子就懂）。它的本质，就是把复杂对象拆成一个个“专精单项”的小对象，再像搭乐高一样拼起来——毕竟没人会直接造一整块“乐高城堡”，都是先拼城墙、塔楼，再组装成整体嘛～

### 核心逻辑：“Has-A” 关系，不是“Is-A”

首先得区分个关键：Composition 搞的是 **“Has-A”（有一个）**，不是继承里的“Is-A”（是一个）。

比如你写一个 `Phone` 类：

- 用继承的话，可能会搞出 `Phone Is-A Camera` 这种离谱关系（手机是相机？不对啊，手机只是“有”相机）；

- 用 Composition 就对了：`Phone Has-A Camera` + `Phone Has-A Battery` + `Phone Has-A Screen`——每个零件都是独立的“小专家”，相机管拍照，电池管供电，屏幕管显示，分工明确还不打架。

### 代码实例：用 Composition 拼一本“书”

拿最常见的 `Book` 举例，一本完整的书得有作者、章节、出版社吧？咱不用把所有功能塞在 `Book` 里，而是拆成小类再组合：

```python

# 先造“小零件”：每个类只干一件事

class Author: # 作者类：专精“作者信息”

def __init__(self, name, genre):

self.name = name # 名字

self.genre = genre # 擅长类型（比如科幻、言情）

class Chapter: # 章节类：专精“章节内容”

def __init__(self, title, word_count):

self.title = title # 章节名

self.word_count = word_count # 字数（方便统计全书字数）

class Publisher: # 出版社类：专精“出版信息”

def __init__(self, name, publish_date):

self.name = name # 出版社名

self.publish_date = publish_date # 出版日期

# 再拼“大物件”：Book 类用 Composition 把零件装起来

class Book:

def __init__(self, book_title, author, chapters, publisher):

self.book_title = book_title # 书名

self.author = author # Book Has-A Author（有一个作者）

self.chapters = chapters # Book Has-A Chapters（有一堆章节）

self.publisher = publisher # Book Has-A Publisher（有一个出版社）

# 利用零件的能力实现复杂功能：统计全书总字数

def total_word_count(self):

return sum(chapter.word_count for chapter in self.chapters)

# 第一步：先造好所有小零件

my_author = Author("刘慈欣", "硬科幻") # 大刘yyds！

my_chapters = [

Chapter("带上她的眼睛", 8000),

Chapter("地球大炮", 12000)

]

my_publisher = Publisher("科幻世界杂志社", "2000-01")

# 第二步：像搭乐高一样组装成 Book

my_book = Book("带上她的眼睛", my_author, my_chapters, my_publisher)

# 调用组合后的功能：算总字数

print(f"全书总字数：{my_book.total_word_count()} 字") # 输出：20000 字

```

你看，`Book` 自己不用管“作者是谁”“章节有多少字”，全靠调用小零件的能力——这就叫“专业的事交给专业的对象”，比把所有代码堆在一个类里清爽多了，后期改起来也不头疼（比如想加个“章节修改时间”，只改 `Chapter` 类就行，不用动 `Book`）。

### 为什么 Composition 比“堆代码”香？

1. **灵活性拉满**：零件能随便换，比如想给 `Book` 换个出版社，直接传个新的 `Publisher` 对象就行，不用重构整个 `Book` 类——就像乐高换个零件，城堡还是那个城堡，但细节能升级；

2. **复用性爆炸**：比如 `Author` 类，不光能给 `Book` 用，还能给 `Magazine`（杂志）、`Article`（文章）用，不用重复写“作者信息”的代码（DRY 原则：Don’t Repeat Yourself，懂的都懂）；

3. **debug 更轻松**：如果全书字数算错了，直接查 `Chapter` 类的 `word_count` 就行，不用在 `Book` 的几百行代码里找 bug——定位问题像“拆乐高找坏零件”，精准又高效。

### 最后补个冷知识

很多人初学容易把 Composition 和“聚合（Aggregation）”搞混，简单说：

- Composition 是“生死与共”：比如 `Book` 没了，它里面的 `Chapter` 也没啥意义了（总不能单独说“我有个章节，但不属于任何书”）；

- 聚合是“各玩各的”：比如 `Team`（团队）和 `Member`（成员），团队散了，成员还能去别的团队——但咱日常编程里，Composition 用得最多，毕竟“强绑定”的场景更常见～

总结一下：Composition 就是编程界的“模块化思维”，把复杂问题拆小，再组合解决——毕竟再牛的项目，也不是“一口吃成胖子”，而是“一个零件一个零件拼出来的”～


