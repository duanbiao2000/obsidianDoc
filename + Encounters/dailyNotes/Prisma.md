---
aliases: 
categories: 
high_priority: false
tags:
---
Prisma 是一个现代化的数据库工具和对象关系映射（ORM, Object-Relational Mapping）框架，主要用于简化数据库操作和管理。它提供了以下几个核心功能：

1. **数据库迁移（Migration）**：Prisma 允许开发者通过代码定义数据库模式（schema），并自动生成和管理数据库迁移脚本。这些迁移脚本可以用于在不同环境中同步数据库结构，确保开发、测试和生产环境的数据库保持一致。

2. **生成客户端（Client Generation）**：Prisma 根据定义的数据库模式生成一个类型安全的客户端库。这个客户端库可以直接在应用程序中使用，提供了一种类型安全的方式来查询和操作数据库。生成的客户端支持多种数据库（如 PostgreSQL、MySQL、SQLite 等），并且提供了丰富的查询功能，包括复杂的过滤、排序、分页等。

3. **ORM 功能**：Prisma 不仅仅是一个简单的查询生成器，它还提供了 ORM 的功能，允许开发者通过定义模型（Model）来映射数据库表。通过这些模型，开发者可以使用更直观的方式来操作数据库，而不需要直接编写 SQL 语句。

4. **类型安全**：Prisma 生成的客户端是类型安全的，这意味着在编写代码时，IDE 可以提供自动补全和类型检查，减少错误并提高开发效率。

5. **数据库无关性**：Prisma 的设计目标是与具体的数据库实现解耦，因此它支持多种数据库系统。开发者可以在不同的项目中使用不同的数据库，而不需要担心兼容性问题。

`prisma-client-js` 是 Prisma 提供的一个库，允许你以类型安全的方式从 Node.js 应用程序访问数据库。

当你在 `schema.prisma` 文件中写入 `generator client { provider = "prisma-client-js" }` 时，这意味着你在告诉 Prisma 你需要使用 `prisma-client-js` 作为客户端生成器来生成 Prisma Client。这个生成的客户端将基于你在 `schema.prisma` 中定义的数据模型来自动生成相应的 CRUD（创建、读取、更新、删除）操作。

例如，在 `schema.prisma` 文件中可能有如下内容：

```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  name      String?
  posts     Post[]
}

model Post {
  id         Int      @id @default(autoincrement())
  title      String
  content    String?
  published  Boolean  @default(false)
  author     User
}
```

在这个例子中，`generator` 块指定了使用 `prisma-client-js` 来生成客户端代码。一旦你运行了 Prisma 的生成命令（通常是 `npx prisma generate` 或者 `yarn prisma generate`），Prisma 就会根据你的数据模型自动生成 JavaScript/TypeScript 客户端代码，这些代码可以用来执行对数据库的操作，比如查询用户信息或者发布文章等。
- [[+ Encounters/dailyNotes/GraphQL]]
- [[GraphQL Apollo Prisma]]
- [[GraphQL简介]]