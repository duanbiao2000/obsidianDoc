---
promptId: quaMacro
aliases: 🖼️ Generate a Macro photo
source: select a text and Macro photo about it will be generated using Dalle-2
author: Prompt Engineering Guide
tags: photo, Agent/dalle,quality
version: 0.0.1
stream: false
disableProvider: true
---

```handlebars
{{#run "getPhoto" "r" "tg_selection"}}
  {{selection}}, Macro
{{/run}}
```

---

---

{{get "r"}}
