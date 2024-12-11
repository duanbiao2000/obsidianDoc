---
<<<<<<< HEAD
promptId: modAwardWinning
aliases: 🖼️ Generate a Award-Winning Art photo
summary: Images in the dataset with captions like “Award-Winning Art” are usually extremely creative and original, so using this modifier can greatly improve the quality and inventiveness of your generations.
author: Prompt Engineering Guide
tags: photo, dalle-2, modifier
=======
promptId: 'modAwardWinning'
name: '🖼️ Generate a Award-Winning Art photo'
description: 'Images in the dataset with captions like “Award-Winning Art” are usually extremely creative and original, so using this modifier can greatly improve the quality and inventiveness of your generations.'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle, Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, Award-Winning Art
{{/run}}
```
***
***
{{get "r"}}