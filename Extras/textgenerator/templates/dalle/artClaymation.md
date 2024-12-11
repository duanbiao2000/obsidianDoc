---
promptId: artClaymation
aliases: 🖼️ Generate a claymation art photo
summary: select a text and photo with the style of claymation art will be generated using Dalle-2
author: Prompt Engineering Guide
tags: []
version: 0.0.1
stream: false
disableProvider: true
---
```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
 {{selection}}, claymation art/clay art
{{/run}}
```
***
***
{{get "r"}}