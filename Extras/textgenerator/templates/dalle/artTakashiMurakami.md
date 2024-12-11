---
<<<<<<< HEAD
promptId: artTakashiMurakami
aliases: 🖼️ Generate a photo by  Takashi Murakami
summary: select a text and photo with the style of  Takashi Murakami will be generated using Dalle-2
author: Prompt Engineering Guide
tags: photo, dalle-2, art
=======
promptId: 'artTakashiMurakami'
name: '🖼️ Generate a photo by  Takashi Murakami'
description: 'select a text and photo with the style of  Takashi Murakami will be generated using Dalle-2'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle, Agent/Dalle, Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, by Takashi Murakami
{{/run}}
```
***
***
{{get "r"}}