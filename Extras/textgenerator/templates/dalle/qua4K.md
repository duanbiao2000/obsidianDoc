---
<<<<<<< HEAD
promptId: qua4K
aliases: 🖼️ Generate a 4K/8K photo
summary: Images in the dataset with the caption “4K/8K” are of high production value therefore will look more professionally photographed if you add this modifier.
author: Prompt Engineering Guide
tags: photo, dalle-2,quality
=======
promptId: 'qua4K'
name: '🖼️ Generate a 4K/8K photo'
description: 'Images in the dataset with the caption “4K/8K” are of high production value therefore will look more professionally photographed if you add this modifier.'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle,Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, 4K/8K
{{/run}}
```
***
***
{{get "r"}}