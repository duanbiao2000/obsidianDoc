---
aliases:
  - <% tp.file.title %>
createdAt: <% tp.file.creation_date() %>
updateAt: <% tp.file.last_modified_date() %>
categories:
  - Mindset
rate: 
tags:
  - Mindset/Reflection
---
# <% tp.file.title %>


## 每日一图
<% tp.web.random_picture("800x600") %>

// Random picture with size and query
<% tp.web.random_picture("800x800", "landscape,water") %>
