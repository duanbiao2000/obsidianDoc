---
aliases: 
theme: 
high_priority: false
tags:
---
[prisma-examples/typescript/rest-nextjs-api-routes/src/components at latest · prisma/prisma-examples · GitHub](https://github.com/prisma/prisma-examples/tree/latest/typescript/rest-nextjs-api-routes/src/components)

GraphQL 是一种用于 API 的查询语言，也是一个运行时用于执行那些查询的服务器端运行环境。它提供了一种更高效、强大和灵活的方式来请求数据，相比于传统的 RESTful API，GraphQL 允许客户端精确地指定需要的数据，从而减少网络传输的数据量，并提高应用性能。

### 主要特性

1. **强类型系统**：GraphQL 使用模式（Schema）来定义数据的结构。模式描述了可用的查询和变更（Mutation），以及它们如何关联到应用程序中的数据。

2. **声明式数据获取**：客户端可以声明性地指定需要哪些字段，这使得客户端能够准确地获取所需的数据，而不需要处理多余的信息。

3. **单个端点**：通常情况下，GraphQL 服务只有一个 HTTP 端点，所有的查询和变更都通过这个端点发送。

4. **内省能力**：GraphQL 提供了内省的能力，这意味着你可以查询 GraphQL 服务以了解其支持的所有操作，包括查询、变更和订阅。

5. **实时数据**：通过订阅（Subscriptions），GraphQL 支持实时更新，允许客户端在数据发生变化时接收通知。

### 基本概念

- **Query**：用于读取数据。
- **Mutation**：用于写入或修改数据。
- **Subscription**：用于实时数据流，当数据发生变化时，客户端会收到更新。
- **Schema**：定义了所有可能的查询和变更，以及它们返回的数据类型。
- **Resolver**：在服务器上运行的函数，负责解析每个字段的实际值。

### 示例

假设你有一个简单的博客应用，这里是如何使用 GraphQL 来查询文章列表：

#### Schema
```graphql
type Query {
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  content: String!
}
```

#### 查询
```graphql
query {
  posts {
    id
    title
    content
  }
}
```

#### 变更
```graphql
mutation CreatePost($title: String!, $content: String!) {
  createPost(title: $title, content: $content) {
    id
    title
    content
  }
}
```

#### 订阅
```graphql
subscription OnNewPost {
  newPost {
    id
    title
    content
  }
}
```

### 工具和生态系统

- **Apollo**：一套完整的工具集，包括客户端库、服务端库和服务层。
- **GraphiQL**：一个交互式的图形化界面，用来测试和调试 GraphQL 查询。
- **Relay**：Facebook 开发的 JavaScript 框架，专为与 GraphQL 一起工作设计。
- **Prisma**：数据库访问层，简化了数据库模式与 GraphQL 模式之间的映射。

### 在 VS Code 中使用 GraphQL

VS Code 有许多插件可以帮助你编写和调试 GraphQL 查询，例如：
- **GraphQL for VSCode**：提供了语法高亮、自动完成、错误检测等功能。
- **Apollo GraphQL**：专门为 Apollo 客户端和服务器开发的扩展，支持更多的功能，如代码生成。

安装这些插件后，你可以在 `.graphql` 或 `.gql` 文件中编写 GraphQL 查询，并且享受到更好的开发体验。如果你正在使用特定的框架或库（如 Apollo 或 Relay），还可以查找相应的官方文档和插件来进一步增强你的开发流程。

是的，GraphQL、Apollo 和 Prisma 可以很好地一起使用，并且这种组合在现代 web 应用开发中非常流行。它们各自扮演不同的角色，但可以协同工作来构建高效和可维护的应用程序。下面是这三者如何协作的概述：

### GraphQL
- **角色**：定义数据查询语言和运行时环境。
- **功能**：允许客户端精确地请求所需的数据，并减少网络传输的数据量。

### Apollo
- **角色**：提供了一整套工具和库，用于在客户端和服务器端处理 GraphQL。
- **功能**：
  - **Apollo Client**：一个强大的 GraphQL 客户端，用于与 GraphQL 服务通信。它支持缓存、错误处理、订阅等功能。
  - **Apollo Server**：一个社区驱动的、无偏见的 GraphQL 服务器，可以在任何 Node.js HTTP 服务器上运行。
  - **Apollo Federation**：一种架构模式，允许多个 GraphQL 服务组成一个单一的图（graph）。
  - **代码生成**：根据你的 GraphQL 模式自动生成类型安全的客户端和服务端代码。

### Prisma
- **角色**：是一个 ORM（对象关系映射）和数据库访问层，简化了数据库操作。
- **功能**：
  - **Prisma Schema**：定义数据库模型，包括表结构和关系。
  - **Prisma Client**：一个类型安全的 ORM，基于 Prisma Schema 生成，提供了丰富的 API 来操作数据库。
  - **数据库迁移**：管理数据库模式变更，确保数据库结构与 Prisma Schema 保持同步。
  - **集成**：可以直接与 Apollo Server 集成，作为数据获取层。

### 如何混用

1. **定义 GraphQL 模式**：
   - 使用 GraphQL SDL（Schema Definition Language）定义你的 GraphQL 模式。

2. **设置 Prisma**：
   - 创建 `prisma/schema.prisma` 文件，定义数据库模型。
   - 使用 Prisma CLI 生成 Prisma Client 并进行数据库迁移。

3. **创建 Apollo Server**：
   - 使用 Apollo Server 创建一个 GraphQL 服务器。
   - 在解析器（resolvers）中使用 Prisma Client 来查询和修改数据库。

4. **编写解析器**：
   - 解析器是实现 GraphQL 查询和变更逻辑的地方。在这里，你可以调用 Prisma Client 来执行数据库操作。

5. **设置 Apollo Client**：
   - 在前端应用中设置 Apollo Client，连接到你的 GraphQL 服务器。
   - 使用 Apollo Client 的查询和变更功能来获取和修改数据。

### 示例

假设你有一个简单的博客应用，下面是如何将这三个工具结合在一起的示例：

#### Prisma Schema
```prisma
// prisma/schema.prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String
  published Boolean  @default(false)
}
```

#### Apollo Server
```javascript
// server.js
const { ApolloServer, gql } = require('apollo-server');
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();

const typeDefs = gql`
  type Query {
    posts: [Post!]!
  }

  type Mutation {
    createPost(title: String!, content: String!): Post!
  }

  type Post {
    id: ID!
    title: String!
    content: String!
    published: Boolean!
  }
`;

const resolvers = {
  Query: {
    posts: () => prisma.post.findMany(),
  },
  Mutation: {
    createPost: (parent, args) => prisma.post.create({ data: args }),
  },
};

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`🚀  Server ready at ${url}`);
});
```

#### Apollo Client
```javascript
// client.js
import { ApolloClient, InMemoryCache, gql } from '@apollo/client';

const client = new ApolloClient({
  uri: 'http://localhost:4000',
  cache: new InMemoryCache()
});

client.query({
  query: gql`
    query GetPosts {
      posts {
        id
        title
        content
        published
      }
    }
  `
}).then(result => console.log(result));
```

通过这种方式，你可以利用 GraphQL 提供的强大查询能力，Apollo 提供的完整工具链，以及 Prisma 提供的高效数据库访问层，来构建现代化、高性能的 web 应用。