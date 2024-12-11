---
<<<<<<< HEAD
promptId: qua15mm
aliases: 🖼️ Generate a 15mm wide-angle lens photo
summary: Very wide image with lots of information in the image.
author: Prompt Engineering Guide
tags: photo,dalle-2,quality,lens
=======
promptId: 'qua15mm'
name: '🖼️ Generate a 15mm wide-angle lens photo'
description: 'Very wide image with lots of information in the image.'
author: 'Prompt Engineering Guide'
tags: 'Agent/Dalle,Agent/Dalle,Agent/Dalle,Agent/Dalle'
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, 15mm wide-angle lens
{{/run}}
```
***
***
{{get "r"}}