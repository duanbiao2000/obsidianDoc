---
promptId: qua35mm
aliases: 🖼️ Generate a 35mm lens photo
summary: Reasonable amount of background blur, reasonable zoom level.
author: Prompt Engineering Guide
tags: photo, dalle-2,quality,lens
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