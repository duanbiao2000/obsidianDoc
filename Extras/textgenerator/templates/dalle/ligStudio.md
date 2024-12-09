---
<<<<<<< HEAD
promptId: ligStudio
aliases: 🖼️ Generate a Studio Lighting photo
summary: Dark/light background is imposed behind the subject, lighting accentuates details of the figure in the foreground.
author: Prompt Engineering Guide
tags: photo, dalle-2,lighting
=======
promptId: 'ligStudio'
name: '🖼️ Generate a Studio Lighting photo'
description: 'Dark/light background is imposed behind the subject, lighting accentuates details of the figure in the foreground.'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle,Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, Studio Lighting
{{/run}}
```
***
***
{{get "r"}}