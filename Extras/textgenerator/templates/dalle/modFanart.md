---
<<<<<<< HEAD
promptId: modFanart
aliases: 🖼️ Generate a Fanart photo
summary: This gives the generation a cute young amateur graphic design feel, adding hearts to the image and so on.
author: Prompt Engineering Guide
tags: photo, dalle-2, modifier
=======
promptId: 'modFanart'
name: '🖼️ Generate a Fanart photo'
description: 'This gives the generation a cute young amateur graphic design feel, adding hearts to the image and so on.'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle, Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, Fanart
{{/run}}
```
***
***
{{get "r"}}