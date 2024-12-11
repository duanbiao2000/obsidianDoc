---
<<<<<<< HEAD
promptId: artChildrenDrawing
aliases: 🖼️ Generate a children’s drawing
summary: select a text and photo with the style of children’s drawing will be generated using Dalle-2
author: Prompt Engineering Guide
tags: photo, dalle-2, art
=======
promptId: 'artChildrenDrawing'
name: '🖼️ Generate a children’s drawing'
description: 'select a text and photo with the style of children’s drawing will be generated using Dalle-2'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle, Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 A children’s drawing of {{selection}}
{{/run}}
```
***
***
{{get "r"}}