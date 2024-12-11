---
<<<<<<< HEAD
promptId: modDetailed
aliases: 🖼️ Generate a photo, with more precise details
summary: Adds more precise details to the output, instead of simple art, but can also make the art overwhelming/over the top in small details.
author: Prompt Engineering Guide
tags: photo, dalle-2,modifier
=======
promptId: 'modDetailed'
name: '🖼️ Generate a photo, with more precise details'
description: 'Adds more precise details to the output, instead of simple art, but can also make the art overwhelming/over the top in small details.'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle,Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, Detailed
{{/run}}
```
***
***
{{get "r"}}