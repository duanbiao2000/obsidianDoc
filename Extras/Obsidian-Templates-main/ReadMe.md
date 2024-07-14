# 自己的 Obsidian 模板

![last-commit](https://img.shields.io/github/last-commit/dmscode/Obsidian-Templates?style=for-the-badge) ![version](https://img.shields.io/static/v1?label=Version&message=0.0.83&color=40AEF0&style=for-the-badge)

## 简介

自用的一些 Obsidian 模板、脚本、片段等。需要搭配对应插件使用。

## 使用说明

可以 clone 整个仓库，本仓库尽量按照不影响用户原本保险库（Vault）的原则进行组织的，不过为了便于查看，这些文件夹都放在根目录了，也许你 clone 到保险库下的某个文件夹更为合理。

当然也可以只选用你需要的某个功能，复制对应文件，不过这样更新会稍显麻烦。

## 关于收费

[A cup of coffee.](https://afdian.net/a/daomishu)

毕竟，咖啡就是生产力。

## Table of Content

- [简介](#%E7%AE%80%E4%BB%8B)
- [使用说明](#%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E)
- [关于收费](#%E5%85%B3%E4%BA%8E%E6%94%B6%E8%B4%B9)
- [Table of Content](#Table-of-Content)
- [目录说明](#%E7%9B%AE%E5%BD%95%E8%AF%B4%E6%98%8E)
- [模板列表](#%E6%A8%A1%E6%9D%BF%E5%88%97%E8%A1%A8)
    - [书签缩略图列表](#%E4%B9%A6%E7%AD%BE%E7%BC%A9%E7%95%A5%E5%9B%BE%E5%88%97%E8%A1%A8)
    - [一日时间段标注](#%E4%B8%80%E6%97%A5%E6%97%B6%E9%97%B4%E6%AE%B5%E6%A0%87%E6%B3%A8)
    - [笔记热力图（Heatmap）](#%E7%AC%94%E8%AE%B0%E7%83%AD%E5%8A%9B%E5%9B%BEHeatmap)
    - [任务完成度](#%E4%BB%BB%E5%8A%A1%E5%AE%8C%E6%88%90%E5%BA%A6)
    - [习惯打卡](#%E4%B9%A0%E6%83%AF%E6%89%93%E5%8D%A1)
    - [月历视图](#%E6%9C%88%E5%8E%86%E8%A7%86%E5%9B%BE)
    - [年历视图](#%E5%B9%B4%E5%8E%86%E8%A7%86%E5%9B%BE)
    - [笔记分布视图](#%E7%AC%94%E8%AE%B0%E5%88%86%E5%B8%83%E8%A7%86%E5%9B%BE)
    - [列表卡片（票据）](#%E5%88%97%E8%A1%A8%E5%8D%A1%E7%89%87%E7%A5%A8%E6%8D%AE)
    - [自动打开入口笔记](#%E8%87%AA%E5%8A%A8%E6%89%93%E5%BC%80%E5%85%A5%E5%8F%A3%E7%AC%94%E8%AE%B0)
    - [侧边栏图标排序](#%E4%BE%A7%E8%BE%B9%E6%A0%8F%E5%9B%BE%E6%A0%87%E6%8E%92%E5%BA%8F)
    - [笔记内容分栏](#%E7%AC%94%E8%AE%B0%E5%86%85%E5%AE%B9%E5%88%86%E6%A0%8F)
    - [禁止通行分割条](#%E7%A6%81%E6%AD%A2%E9%80%9A%E8%A1%8C%E5%88%86%E5%89%B2%E6%9D%A1)
    - [索引标签样式卡片](#%E7%B4%A2%E5%BC%95%E6%A0%87%E7%AD%BE%E6%A0%B7%E5%BC%8F%E5%8D%A1%E7%89%87)
    - [让加粗显著加粗](#%E8%AE%A9%E5%8A%A0%E7%B2%97%E6%98%BE%E8%91%97%E5%8A%A0%E7%B2%97)
    - [生成文字卡片](#%E7%94%9F%E6%88%90%E6%96%87%E5%AD%97%E5%8D%A1%E7%89%87)
    - [获取随机诗词](#%E8%8E%B7%E5%8F%96%E9%9A%8F%E6%9C%BA%E8%AF%97%E8%AF%8D)
    - [生成渐变背景笔记头图](#%E7%94%9F%E6%88%90%E6%B8%90%E5%8F%98%E8%83%8C%E6%99%AF%E7%AC%94%E8%AE%B0%E5%A4%B4%E5%9B%BE)
    - [获取一言](#%E8%8E%B7%E5%8F%96%E4%B8%80%E8%A8%80)
    - [获取今日日期](#%E8%8E%B7%E5%8F%96%E4%BB%8A%E6%97%A5%E6%97%A5%E6%9C%9F)
    - [获取历史上的今天](#%E8%8E%B7%E5%8F%96%E5%8E%86%E5%8F%B2%E4%B8%8A%E7%9A%84%E4%BB%8A%E5%A4%A9)
    - [获取天气](#%E8%8E%B7%E5%8F%96%E5%A4%A9%E6%B0%94)
    - [获取年进度](#%E8%8E%B7%E5%8F%96%E5%B9%B4%E8%BF%9B%E5%BA%A6)
    - [对选中行排序](#%E5%AF%B9%E9%80%89%E4%B8%AD%E8%A1%8C%E6%8E%92%E5%BA%8F)
    - [转换为大字符](#%E8%BD%AC%E6%8D%A2%E4%B8%BA%E5%A4%A7%E5%AD%97%E7%AC%A6)
    - [更新时间和日期](#%E6%9B%B4%E6%96%B0%E6%97%B6%E9%97%B4%E5%92%8C%E6%97%A5%E6%9C%9F)
    - [选中内容另存为新笔记](#%E9%80%89%E4%B8%AD%E5%86%85%E5%AE%B9%E5%8F%A6%E5%AD%98%E4%B8%BA%E6%96%B0%E7%AC%94%E8%AE%B0)
- [技巧分享](#%E6%8A%80%E5%B7%A7%E5%88%86%E4%BA%AB)
- [计划](#%E8%AE%A1%E5%88%92)
    - [Next](#Next)
    - [Plan](#Plan)

## 目录说明

- `/Dataview`：Dataview 的自定义视图，每个文件夹对应一个功能，需要 [Dataview](https://github.com/blacksmithgu/obsidian-dataview) 插件的支持
- `/Docs`：本仓库中模板的说明文档
- `/QuickAdd`：QuickAdd 的脚本，每个脚本对应一个功能，需要 [QuickAdd](https://github.com/chhoumann/quickadd) 插件的支持
- `/snippets`：Obsidian 的 CSS 片段，对应 `.obsidian/snippets` 文件夹（为了方便直接复制过去，所以这个文件夹没有大写），需在 `设置——外观——CSS 片段` 中启用对应的样式
- `/Templater`：Templater 的模板文件夹，每个模板对应一个功能，需要 [Templater](https://github.com/SilentVoid13/Templater) 插件的支持，**并将 Templater 的模板文件夹设置为此文件夹**
- `/Templater-Script`：Templater 的脚本文件夹，每个脚本对应一个功能，需要 [Templater](https://github.com/SilentVoid13/Templater) 插件的支持，**并将 Templater 的脚本文件夹设置为此文件夹**。脚本需要对应的调用方法，会在文档中写出

## 模板列表

不同于提交时间，这里列出的是每个文件的最后编辑时间，可以视为文件的版本号，用来对照你使用的模板是否有更新版本。

有一些功能可以用多种方式实现，各有优缺点，所以这里按功能划分，而不按照依赖插件划分，

### 书签缩略图列表

- 使用说明：[书签缩略图列表](./Docs/Dataview/Bookmarks.md)（涉及内容较多，暂缓整理）
- 相关文件：
    - [/Dataview/Bookmarks/view.css](assets/img/ReadMe/IMG-ReadMe-20240714124636325.css)<sup>2022-11-23 10:11:20</sup>
    - [/Dataview/Bookmarks/view.js](assets/img/ReadMe/IMG-ReadMe-20240714124637900.js)<sup>2022-10-26 13:26:55</sup>

### 一日时间段标注

- 使用说明：[一日时间段标注](Docs/Dataview/Day-Line.md)
- 相关文件：
    - [/Dataview/Day-Line/view.css](Docs/Dataview/assets/img/Day-Line/IMG-Day-Line-20240714124636479.css)<sup>2022-11-23 15:55:12</sup>
    - [/Dataview/Day-Line/view.js](Docs/Dataview/assets/img/Day-Line/IMG-Day-Line-20240714124638076.js)<sup>2022-11-23 15:55:23</sup>

### 笔记热力图（Heatmap）

- 使用说明：[笔记热力图（Heatmap）](Docs/Dataview/Heatmap.md)
- 相关文件：
    - [/Dataview/Heatmap/view.js](Docs/Dataview/assets/img/Heatmap/IMG-Heatmap-20240714124636480.js)<sup>2022-11-23 15:57:29</sup>

### 任务完成度

- 使用说明：[任务完成度](./Docs/Dataview/Task-Progress.md)
- 相关文件：
    - [/Dataview/Task-Progress/view.css](assets/img/ReadMe/IMG-ReadMe-20240714124623916.css)<sup>2022-11-23 16:00:20</sup>
    - [/Dataview/Task-Progress/view.js](assets/img/ReadMe/IMG-ReadMe-20240714124624225.js)<sup>2022-11-23 16:00:29</sup>

### 习惯打卡

- 使用说明：[习惯打卡](Docs/Dataview/Habits.md)
- 相关文件：
    - [/Dataview/Habits/view.css](Docs/Dataview/assets/img/Habits/IMG-Habits-20240714124636482.css)<sup>2022-12-19 17:14:53</sup>
    - [/Dataview/Habits/view.js](Docs/Dataview/assets/img/Habits/IMG-Habits-20240714124638635.js)<sup>2022-12-19 17:14:53</sup>

### 月历视图

- 使用说明：[月历视图](Docs/Dataview/Month-View.md)
- 相关文件：
    - [/Dataview/Month-View/view.css](Docs/Dataview/assets/img/Month-View/IMG-Month-View-20240714124636484.css)<sup>2022-12-23 10:26:44</sup>
    - [/Dataview/Month-View/view.js](Docs/Dataview/assets/img/Month-View/IMG-Month-View-20240714124638760.js)<sup>2022-12-27 09:20:05</sup>

### 年历视图

- 使用说明：[年历视图](Docs/Dataview/Year-View.md)
- 相关文件：
    - [/Dataview/Year-View/view.css](Docs/Dataview/assets/img/Year-View/IMG-Year-View-20240714124636488.css)<sup>2023-01-12 19:39:52</sup>
    - [/Dataview/Year-View/view.js](Docs/Dataview/assets/img/Year-View/IMG-Year-View-20240714124639003.js)<sup>2023-01-12 19:40:06</sup>

### 笔记分布视图

- 使用说明：[笔记分布视图](Docs/Dataview/Notes-Count-View.md)
- 相关文件：
    - [/Dataview/Notes-Count-View/view.css](Docs/Dataview/assets/img/Notes-Count-View/IMG-Notes-Count-View-20240714124636481.css)<sup>2022-12-28 15:58:49</sup>
    - [/Dataview/Notes-Count-View/view.js](Docs/Dataview/assets/img/Notes-Count-View/IMG-Notes-Count-View-20240714124638392.js)<sup>2022-12-28 15:29:21</sup>

### 列表卡片（票据）

- 使用说明：[列表卡片（票据）](Docs/Dataview/Ticket-Card.md)
- 相关文件：
    - [/Dataview/Ticket-Card/view.css](./Dataview/Ticket-Card/view.css)<sup>{{/Dataview/Ticket-Card/view.css}}</sup>

### 自动打开入口笔记

- 使用说明：[自动打开入口笔记](Docs/QuickAdd/Open-Home-Page.md)
- 相关文件：
    - [/QuickAdd/Open-Home-Page.js](Docs/QuickAdd/assets/img/Open-Home-Page/IMG-Open-Home-Page-20240714124636337.js)<sup>2022-11-23 16:11:50</sup>

### 侧边栏图标排序

- 使用说明：[侧边栏图标排序](./Docs/Snippets/Side-Dock-Icon-Order.md)
- 相关文件：
    - [/snippets/Side-Dock-Icon-Order.css](assets/img/ReadMe/IMG-ReadMe-20240714124624372.css)<sup>2022-11-23 20:32:32</sup>

### 笔记内容分栏

- 使用说明：[笔记内容分栏](Docs/Snippets/Split-Page-Callout.md)
- 相关文件：
    - [/snippets/Split-Page-Callout.css](Docs/Snippets/assets/img/Split-Page-Callout/IMG-Split-Page-Callout-20240714124636521.css)<sup>2022-11-25 08:35:56</sup>

### 禁止通行分割条

- 使用说明：[禁止通行分割条](Docs/Snippets/Stop-Callout.md)
- 相关文件：
    - [/snippets/Stop-Callout.css](Docs/Snippets/assets/img/Stop-Callout/IMG-Stop-Callout-20240714124636524.css)<sup>2022-11-23 20:35:24</sup>

### 索引标签样式卡片

- 使用说明：[索引标签样式卡片](Docs/Snippets/Paper-Index-Callout.md)
- 相关文件：
    - [/snippets/Paper-Index-Callout.css](Docs/Snippets/assets/img/Paper-Index-Callout/IMG-Paper-Index-Callout-20240714124636523.css)<sup>2022-11-23 20:37:59</sup>

### 让加粗显著加粗

- 使用说明：[让加粗显著加粗](Docs/Snippets/Strong-Strong.md)
- 相关文件：
    - [/snippets/Strong-Strong.css](Docs/Snippets/assets/img/Strong-Strong/IMG-Strong-Strong-20240714124636525.css)<sup>2022-12-02 14:57:50</sup>

### 生成文字卡片

- 使用说明：[生成文字卡片](Docs/Templater/Generate-Tweet-Card.md)
- 相关文件：
    - [/Templater-Scripts/Generate_Tweet_Card.js](Docs/Templater/assets/img/Generate-Tweet-Card/IMG-Generate-Tweet-Card-20240714124636496.js)<sup>2022-11-26 08:47:44</sup>

### 获取随机诗词

- 使用说明：[获取随机诗词](Docs/Templater/Get-Poems.md)
- 相关文件：
    - [/Templater-Scripts/Get_Poems.js](Docs/Templater/assets/img/Get-Poems/IMG-Get-Poems-20240714124636338.js)<sup>2022-11-26 08:47:50</sup>

### 生成渐变背景笔记头图

- 使用说明：[生成渐变背景笔记头图](Docs/Templater/Add-Gradient-Header.md)
- 相关文件：
    - [/Templater-Scripts/Get_Random_Gradient.js](Docs/Templater/assets/img/Add-Gradient-Header/IMG-Add-Gradient-Header-20240714124636498.js)<sup>2022-11-26 08:47:58</sup>
    - [/Templater/Add-Gradient-Header.md](../Template/Templater/Add-Gradient-Header.md)

### 获取一言

- 使用说明：[获取一言](Docs/Templater/Get-Sentence.md)
- 相关文件：
    - [/Templater-Scripts/Get_Sentence.js](Docs/Templater/assets/img/Get-Sentence/IMG-Get-Sentence-20240714124636342.js)<sup>2022-11-26 08:48:05</sup>

### 获取今日日期

- 使用说明：[获取今日日期](Docs/Templater/Get-Today-Date.md)
- 相关文件：
    - [/Templater-Scripts/Get_Today_Date.js](Docs/Templater/assets/img/Get-Today-Date/IMG-Get-Today-Date-20240714124636343.js)<sup>2022-11-26 08:48:12</sup>

### 获取历史上的今天

- 使用说明：[获取历史上的今天](Docs/Templater/Get-Today-History.md)
- 相关文件：
    - [/Templater-Scripts/Get_Today_History.js](Docs/Templater/assets/img/Get-Today-History/IMG-Get-Today-History-20240714124636345.js)<sup>2022-11-26 08:48:21</sup>

### 获取天气

- 使用说明：[获取天气](Docs/Templater/Get-Weather.md)
- 相关文件：
    - [/Templater-Scripts/Get_Weather.js](Docs/Templater/assets/img/Get-Weather/IMG-Get-Weather-20240714124636346.js)<sup>2022-11-26 08:48:27</sup>

### 获取年进度

- 使用说明：[获取年进度](Docs/Templater/Get-Year-Progress.md)
- 相关文件：
    - [/Templater-Scripts/Get_Year_Progress.js](Docs/Templater/assets/img/Get-Year-Progress/IMG-Get-Year-Progress-20240714124636347.js)<sup>2022-11-26 08:48:36</sup>

### 对选中行排序

- 使用说明：[对选中行排序](Docs/Templater/Sort-Tasks-Lines.md)
- 相关文件：
    - [/Templater-Scripts/Sort_Tasks_Lines.js](Docs/Templater/assets/img/Sort-Tasks-Lines/IMG-Sort-Tasks-Lines-20240714124636353.js)<sup>2022-11-26 08:48:47</sup>

### 转换为大字符

- 使用说明：[转换为大字符](./Docs/Templater/To-Big-Chars.md)
- 相关文件：
    - [/Templater-Scripts/To_Big_Chars.js](assets/img/ReadMe/IMG-ReadMe-20240714124624533.js)<sup>2022-11-26 08:48:55</sup>
    - [/Templater/Add-Big-Chars.md](../../Templater/Add-Big-Chars.md)
    - [/Templater/Add-Big-Chars-Date.md](../../Templater/Add-Big-Chars-Date.md)
    - [/Templater/Add-Big-Chars-Time.md](../../Templater/Add-Big-Chars-Time.md)

### 更新时间和日期

- 使用说明：[更新时间和日期](./Docs/Templater/Update-Date-and-Time.md)
- 相关文件：
    - [/Templater/Update-Date-and-Time.md](../../Templater/Update-Date-and-Time.md)

### 选中内容另存为新笔记

- 使用说明：[选中内容另存为新笔记](Docs/Templater/Save-selection-content.md)
- 相关文件：
    - [/Templater/Save-selection-content.md](../Template/Templater/Save-selection-content.md)

## 技巧分享

- [动态插入代码](Docs/Usages/Dynamic-Insert-Code.md)
- [Dataview 自定义视图的使用方法](Docs/Usages/Dataview-Custom-View.md)
- [CSS Snippets 的安装方法](Docs/Usages/Install-CSS-Snippets.md)
- [Callout 样式的使用方法](./Docs/Usages/How-to-Use-Callout.md)
- [Templater 脚本的使用方法](Docs/Usages/How-to-Use-Templater-Script.md)

## 计划

### Next

### Plan