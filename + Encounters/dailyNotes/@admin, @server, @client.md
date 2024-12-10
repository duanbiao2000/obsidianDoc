---
aliases: 
theme: 
high_priority: false
tags:
---
## @Codebase, @admin, @server, @client 的职能和关系

在这个项目中，代码库被分成了三个主要部分：`@admin`，`@server` 和 `@client`。它们分别代表了不同的功能模块，并通过网络请求进行交互。

**1. @server (服务器端):**

* **职能:** 负责处理后端逻辑，包括：
    * 数据库交互 (使用 Mongoose 连接 MongoDB)
    * API 路由定义 (使用 Express.js)
    * 用户认证和授权 (使用 JWT)
    * 数据处理和业务逻辑
    * 发送邮件 (使用 Nodemailer)
* **技术栈:** Node.js, Express.js, MongoDB, Mongoose, JWT, Nodemailer,  bcryptjs, body-parser, cors, dotenv, helmet, [[morgan]].
* **文件示例:** `server/index.js`, `server/routes/index.js`, `server/routes/postRoute.js`, `server/package.json`

**2. @admin (管理后台):**

* **职能:** 提供一个图形界面，让管理员可以管理网站内容，包括：
    * 用户管理
    * 文章管理
    * 数据统计和分析
* **技术栈:** React, Mantine UI, React Router, [[TanStack Query]], Axios, Recharts, [[Firebase]].
* **文件示例:** `admin/src/pages/Content.jsx`, `admin/package.json`, `admin/src/index.js`, `admin/public/index.html`, `admin/src/index.css`

**3. @client (客户端):**

* **职能:**  面向普通用户的网站前端界面，用户可以浏览文章、评论等。
* **技术栈:** React, React Router, Axios, Zustand, React Icons, [[Sonner]],  markdown-to-jsx,  [[Firebase|firebase]], [[react-oauth-google|@react-oauth/google]].
* **文件示例:** `client/src/index.css`, `client/src/components/index.js`, `client/src/App.js`, `client/public/index.html`, `client/package.json`

**关系:**

* `@client` 和 `@admin` 都是前端应用，它们通过 HTTP 请求与 `@server` 进行通信，获取数据和执行操作。
* `@admin` 通常需要更高的权限才能访问 `@server` 的某些 API 接口，例如管理用户和文章的接口。
* `@server` 作为后端，负责处理来自 `@client` 和 `@admin` 的请求，并返回相应的数据或执行相应的操作。

**总结:**

这三个部分共同构成了一个完整的 Web 应用。`@server` 负责后端逻辑和数据存储，`@admin` 提供管理界面，`@client` 提供用户界面。它们通过网络请求进行交互，协同工作，为用户提供完整的服务。