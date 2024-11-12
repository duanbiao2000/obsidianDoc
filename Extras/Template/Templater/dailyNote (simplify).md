---
aliases: 
theme: 
high_priority: false
creation date: <% tp.file.creation_date() %>
modification date: <% tp.file.last_modified_date() %>
tags:
---

<< [[<% tp.date.now("YYYY-MM-DD", -1) %>]] | [[<% tp.date.now("YYYY-MM-DD", 1) %>]] >>

# <% tp.file.title %>


## 晨间思考
- 今天的目标：
- 今天的心情：
- 今天的计划：

## 工作/学习
### 上午
- 第一项任务：
- 第二项任务：
- 其他事项：

### 下午
- 第一项任务：
- 第二项任务：
- 其他事项：

### 晚上
- 第一项任务：
- 第二项任务：
- 其他事项：

## 个人生活
- 家庭/朋友：
- 健康/锻炼：
- 娱乐/休闲：

## 反思与总结
- 今天的成就：(每天画张图表。每天工作结束的时候，问问自己：“今天我学到的最重要的三件事是什么?”)
- 遇到的挑战：
- 明天的计划：

## 随机名言
<% tp.web.daily_quote() %>

## 每日一图
<% tp.web.random_picture("800x600") %>


// Random picture with size and query
<% tp.web.random_picture("800x800", "landscape,water") %>



