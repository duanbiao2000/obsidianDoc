---
title: Slidev 中文文档
source: https://cn.sli.dev/features/shiki-magic-move
author:
  - "[[Anthony Fu]]"
published:
created: 2026-01-12
description: 控制代码变化时的细粒度过渡，类似于 Keynote 中的 Magic Move 效果。
tags: ["clippings", "Domain/Cognitive/Tools", "Type/Reference"]
  - clippings
view-count: 3
---
[Skip to content](https://cn.sli.dev/features/#VPContent)

## Shiki Magic Move

[Shiki Magic Move](https://github.com/shikijs/shiki-magic-move) 让你能够控制代码变化时的细粒度过渡，类似于 Keynote 中的 Magic Move 效果。在 [此处](https://shiki-magic-move.netlify.app/) 查看它是如何工作的。

<video src="https://github.com/slidevjs/slidev/assets/11247099/79927794-27ba-4342-9911-9996cec889d6" controls=""></video>

在 Slidev 中，我们将 Magic Move 绑定到 [点击事件](https://cn.sli.dev/guide/animations#click-animation) 中。它的语法是用 ` ````md magic-move ` 包裹代表每个步骤的代码块（注意是 **四个反引号** ）。这将被转换为一个根据动画步骤变化的代码快。

