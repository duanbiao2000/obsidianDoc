---
<<<<<<< HEAD
promptId: qua35mm
aliases: 🖼️ Generate a 35mm lens photo
summary: Reasonable amount of background blur, reasonable zoom level.
author: Prompt Engineering Guide
tags: photo, dalle-2,quality,lens
=======
promptId: 'qua35mm'
name: '🖼️ Generate a 35mm lens photo'
description: 'Reasonable amount of background blur, reasonable zoom level.'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle,Agent/Dalle,Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, 35mm lens
{{/run}}
```
***
***
{{get "r"}}