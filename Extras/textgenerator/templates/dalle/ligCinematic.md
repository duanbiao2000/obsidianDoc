---
<<<<<<< HEAD
promptId: ligCinematic
aliases: 🖼️ Generate a Cinematic Lighting photo
summary: Movie-like imagery with dramatic shadowing and very strong vibrancy, it also seems to add sun rays whenever it can.
author: Prompt Engineering Guide
tags: photo, dalle-2, lighting
=======
promptId: 'ligCinematic'
name: '🖼️ Generate a Cinematic Lighting photo'
description: 'Movie-like imagery with dramatic shadowing and very strong vibrancy, it also seems to add sun rays whenever it can.'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle, Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, Cinematic Lighting
{{/run}}
```
***
***
{{get "r"}}