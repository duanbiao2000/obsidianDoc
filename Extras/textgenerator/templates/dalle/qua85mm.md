---
<<<<<<< HEAD
promptId: qua85mm
aliases: 🖼️ Generate a 85mm lens photo
summary: Quite zoomed in photo, a lot of background blur and detail on subject
author: Prompt Engineering Guide
tags: photo, dalle-2,quality, lens
=======
promptId: 'qua85mm'
name: '🖼️ Generate a 85mm lens photo'
description: 'Quite zoomed in photo, a lot of background blur and detail on subject'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle,Agent/Dalle, Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, 85mm lens
{{/run}}
```
***
***
{{get "r"}}