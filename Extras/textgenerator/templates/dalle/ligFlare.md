---
<<<<<<< HEAD
promptId: ligFlare
aliases: 🖼️ Generate a Lens Flare photo
summary: Adds a streak of light onto an image generation, creating the appearance of a bright light source being just outside of the frame.
author: Prompt Engineering Guide
tags: photo, dalle-2,lighting
=======
promptId: 'ligFlare'
name: '🖼️ Generate a Lens Flare photo'
description: 'Adds a streak of light onto an image generation, creating the appearance of a bright light source being just outside of the frame.'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle,Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, Lens Flare
{{/run}}
```
***
***
{{get "r"}}