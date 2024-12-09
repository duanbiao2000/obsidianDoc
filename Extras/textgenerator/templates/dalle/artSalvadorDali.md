---
<<<<<<< HEAD
promptId: artSalvadorDali
aliases: 🖼️ photo by Salvador Dali
summary: select a text and photo with the style of Salvador Dali will be generated using Dalle-2
author: Prompt Engineering Guide
tags: photo, dalle-2, art
=======
promptId: 'artSalvadorDali'
name: '🖼️ photo by Salvador Dali'
description: 'select a text and photo with the style of Salvador Dali will be generated using Dalle-2'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle, Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, by Salvador Dali
{{/run}}
```
***
***
{{get "r"}}