---
tags:
  - Timeframe/daily
created: 2025-05-03 07:07
cssclasses:
  - hide-properties_editing
  - hide-properties_reading
source: https://github.com/NonakaVal/MyObsidianSetup/blob/main/Calendar/DAILY/2025-05-03.md
---

> [!quote] If you're walking down the right path and you're willing to keep walking, eventually you'll make progress.
> — Barack Obama

# How am'I feeling Today ?

# Tasks 

```dataview
TASK
FROM "1.Projects"
WHERE !completed AND !checked
GROUP BY file.name

```


# Log



# now doing

```dataview
table area_category as "Area Category", created as "Date Created" from "Efforts/AREAS"
WHERE type = "area_family"
```

```dataview
table created AS "Created", summary AS "goal"
from "Efforts/PROJECTS"
where file.name != "collectors-tutorials"
sort created DESC
```



## Areas Tasks
```dataview
TASK
FROM "Efforts/AREAS"
WHERE !completed AND !checked
GROUP BY file.name

```

---

# How Was My Day ?


