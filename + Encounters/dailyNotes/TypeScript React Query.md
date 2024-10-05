---
aliases: 
theme: 
high_priority: false
tags:
---
`trpc/` 文件夹在您的代码库中主要用于定义和管理 tRPC（TypeScript React Query）相关的配置和功能。tRPC 是一个用于构建现代应用程序的 TypeScript 和 React 框架，它提供了一种高效的方式来处理 API 请求和响应。

在这个文件夹中，您可以看到以下几个主要文件和目录：

1. `react.tsx`：这个文件定义了 tRPC 的 React 提供者，它创建了一个 `QueryClient` 实例和一个 `api` 客户端。这个客户端用于与服务器端 API 进行通信。

2. `server.ts`：这个文件定义了 tRPC 的服务器端配置和上下文。它创建了一个 `createTRPCContext` 函数，这个函数用于在处理 tRPC 调用时提供所需的上下文。

3. `query-client.ts`：这个文件定义了一个 `createQueryClient` 函数，这个函数用于创建一个 `QueryClient` 实例。这个实例用于管理 React Query 的状态和缓存。

4. `react.tsx` 文件中的 `RouterInputs` 和 `RouterOutputs` 类型：这些类型用于推断 tRPC 路由的输入和输出类型。

5. `react.tsx` 文件中的 `TRPCReactProvider` 组件：这个组件用于在 React 应用程序中提供 tRPC 的上下文和客户端。

6. `server.ts` 文件中的 `createCaller` 函数：这个函数用于创建一个 tRPC 调用者，这个调用者可以在服务器端组件中使用。

总的来说，`trpc/` 文件夹中的文件和配置用于定义和管理 tRPC 的客户端和服务器端行为，以及 React Query 的状态和缓存。这些配置和功能对于构建高效、可扩展的 React 应用程序至关重要。

`tRPC`（TypeScript Remote Procedure Call）是一个用于构建类型安全 API 的库，它允许你在客户端和服务端之间进行通信，而无需手动处理复杂的类型定义和序列化。下面是 `tRPC` 中各个环节及其处理流程的解释：

### 1. 定义 Procedural APIs

首先，在服务端你需要定义你的远程过程调用（RPC）方法。这些方法被称为“procedures”，它们可以是查询（queries）或变异（mutations）。你使用 `tRPC` 提供的 `createTRPCRouter` 和相关的 `query`、`mutation` 方法来定义这些过程。

```typescript
import { createTRPCRouter, publicProcedure } from './trpc';

export const appRouter = createTRPCRouter({
  greeting: publicProcedure
    .input(z.object({ name: z.string().optional() }))
    .query(({ input }) => {
      return { text: `hello ${input?.name ?? 'world'}` };
    }),
});
```

### 2. 创建 TRPC Server

接下来，你需要创建一个 `tRPC` 服务器实例，并将之前定义的路由器（router）与之关联。这个服务器会处理来自客户端的所有请求，并执行相应的 RPC 方法。

```typescript
import { createHTTPServer } from '@trpc/server/adapters/standalone';
import { appRouter } from './routers/_app';

const server = createHTTPServer({
  router: appRouter,
  createContext: () => ({}), // 你可以在这里提供上下文信息
});

server.listen(3000);
```

### 3. 创建 TRPC Client

在客户端，你需要创建一个 `tRPC` 客户端来与服务端通信。客户端需要知道如何找到服务端以及如何处理数据。

```typescript
import { createTRPCReact } from '@trpc/react';
import { httpBatchLink } from '@trpc/client';
import type { AppRouter } from '../server/routers/_app';

export const trpc = createTRPCReact<AppRouter>();

function MyApp() {
  return (
    <trpc.Provider
      client={trpc.createClient({
        links: [
          httpBatchLink({
            url: 'http://localhost:3000',
          }),
        ],
      })}
    >
      {/* Your application here */}
    </trpc.Provider>
  );
}
```

### 4. 调用 Procedures

一旦客户端和服务端都设置好了，你就可以在 React 组件中调用这些过程了。

```jsx
import { useQuery } from '@trpc/react';
import { trpc } from './trpc';

function Greeting({ name }: { name?: string }) {
  const { data } = trpc.greeting.useQuery({ name });

  return <h1>{data?.text}</h1>;
}
```

### 处理流程

1. **客户端发起请求**：当用户交互触发时，客户端通过 `useQuery` 或 `useMutation` 钩子发起一个请求。
2. **请求发送到服务端**：请求通过 HTTP 发送到 `tRPC` 服务器。
3. **服务端处理请求**：服务器接收到请求后，根据请求路径找到对应的 procedure，并执行相应的逻辑。
4. **返回响应**：服务器将执行结果返回给客户端。
5. **客户端接收响应**：客户端接收到响应，并更新组件状态，从而更新 UI。

整个过程中，`tRPC` 确保了类型的安全性，从客户端到服务端再到数据库，每个环节的数据结构都是严格匹配的，减少了运行时错误的可能性。同时，`tRPC` 的设计使得前后端之间的通信更加简洁高效。