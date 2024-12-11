---
<<<<<<< HEAD
promptId: ligGoldenHour
aliases: 🖼️ Generate a Golden Hour Sunlight photo
summary: The hour just after sunrise or just before sunset when the natural light is soft and warm. Increases the temperature of generations.
author: Prompt Engineering Guide
tags: photo, dalle-2,lighting
=======
promptId: 'ligGoldenHour'
name: '🖼️ Generate a Golden Hour Sunlight photo'
description: 'The hour just after sunrise or just before sunset when the natural light is soft and warm. Increases the temperature of generations.'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle,Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, Golden Hour Sunlight
{{/run}}
```
***
***
{{get "r"}}