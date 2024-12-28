---
aliases: 
categories: 
high_priority: false
tags:
---

## Apollo Client

使用 Apollo Client 与后端 API 交互是一个常见的方式，尤其是在前端应用中使用 GraphQL 作为数据获取协议时。Apollo Client 是一个全面的 JavaScript 客户端工具，支持 GraphQL 的所有功能，并且可以很好地与 React,Angular,Vue 等前端框架集成。

下面是一个使用 Apollo Client 与后端 API 交互的基本示例：

### 步骤 1: 安装 Apollo Client

首先，你需要安装 Apollo Client 的相关包。如果你使用的是 React，可以安装如下依赖：

```bash
npm install @apollo/client graphql
```

如果你使用的是 Vue 或 Angular，可以分别安装相应的 Apollo 客户端库。

### 步骤 2: 配置 Apollo Client

创建一个 Apollo Client 的实例，并配置它与你的后端 API 通信。这里假设你的 GraphQL API 位于 `http://localhost:4000/graphql`。

```javascript
import { ApolloClient, InMemoryCache, gql } from '@apollo/client';

const client = new ApolloClient({
  uri: 'http://localhost:4000/graphql', // 替换为你的 GraphQL 服务器地址
  cache: new InMemoryCache(),
});
```

### 步骤 3: 查询数据

使用 Apollo Client 查询数据非常简单。下面是一个查询用户的示例：

```javascript
const GET_USERS = gql`
  query GetUsers {
    users {
      id
      name
      email
    }
  }
`;

client.query({
  query: GET_USERS,
}).then((result) => {
  console.log(result.data.users);
}).catch((error) => {
  console.error(error);
});
```

### 步骤 4: 修改数据

你可以使用 `mutate` 方法来修改数据，例如创建一个新用户：

```javascript
const ADD_USER = gql`
  mutation AddUser($name: String!, $email: String!) {
    addUser(name: $name, email: $email) {
      id
      name
      email
    }
  }
`;

client.mutate({
  mutation: ADD_USER,
  variables: {
    name: 'John Doe',
    email: 'john.doe@example.com',
  },
}).then((result) => {
  console.log(result.data.addUser);
}).catch((error) => {
  console.error(error);
});
```

### 步骤 5: 使用 React 组件

如果你使用的是 React，Apollo Client 提供了一些高阶组件（HOCs）和 hooks 来简化查询和订阅的使用。例如：

```jsx
import React from 'react';
import { useQuery } from '@apollo/client';
import { GET_USERS } from './queries'; // 导入查询定义

function UsersList() {
  const { loading, error, data } = useQuery(GET_USERS);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return (
    <div>
      {data.users.map((user) => (
        <div key={user.id}>
          {user.name} ({user.email})
        </div>
      ))}
    </div>
  );
}

export default UsersList;
```

### 步骤 6: 使用订阅

Apollo Client 还支持 GraphQL 订阅，这对于实时应用非常有用。例如，监听新用户注册的事件：

```javascript
const NEW_USER_SUBSCRIPTION = gql`
  subscription NewUser {
    newUser {
      id
      name
      email
    }
  }
`;

client.subscribe({
  query: NEW_USER_SUBSCRIPTION,
  onSubscriptionData: ({ subscriptionData }) => {
    console.log(subscriptionData.data.newUser);
  },
});
```

### 总结

通过以上步骤，你可以使用 Apollo Client 来与后端 API 进行交互，无论是查询数据,修改数据还是订阅实时更新。Apollo Client 的强大之处在于它的缓存机制，它可以智能地管理数据的加载和缓存，从而提高应用的性能。

根据你的具体需求和技术栈，你可以进一步定制 Apollo Client 的配置，例如使用不同的缓存策略,集成身份验证等。

你说得对，`gql` 是一个标签模板函数，它接受一个字符串模板作为参数，并返回一个字符串。在 JavaScript 中，标签模板函数允许你在字符串模板前加上一个函数名，然后将字符串的部分作为单独的参数传递给这个函数。

在使用 `gql` 标签模板函数时，实际上 `subscription NewUser { ... }` 是作为字符串模板的一部分传递给 `gql` 函数的。因此，尽管看起来像是直接写成了 `gql` 的参数，但实际上 `gql` 函数并没有显式地以括号形式调用，而是通过标签模板函数的方式传递字符串。

### 示例代码

让我们来看一个完整的示例代码，展示如何使用 `gql` 标签模板函数来定义 GraphQL 查询和订阅：

```javascript
import { ApolloClient, InMemoryCache, gql } from '@apollo/client';

// 创建 Apollo Client 实例
const client = new ApolloClient({
  uri: 'http://localhost:4000/graphql', // 替换为你的 GraphQL 服务器地址
  cache: new InMemoryCache(),
});

// 定义 GraphQL 订阅
const NEW_USER_SUBSCRIPTION = gql`
  subscription NewUser {
    newUser {
      id
      name
      email
    }
  }
`;

// 订阅数据
client.subscribe({
  query: NEW_USER_SUBSCRIPTION,
  onSubscriptionData: ({ subscriptionData }) => {
    if (!subscriptionData.data) {
      return;
    }
    console.log('New User:', subscriptionData.data.newUser);
  },
});

// 示例：定义 GraphQL 查询
const GET_USERS_QUERY = gql`
  query GetUsers {
    users {
      id
      name
      email
    }
  }
`;

// 执行查询
client.query({
  query: GET_USERS_QUERY,
}).then((result) => {
  console.log(result.data.users);
}).catch((error) => {
  console.error(error);
});
```

### 解释

1. **导入 `gql`**：

   ```javascript
   import { ApolloClient, InMemoryCache, gql } from '@apollo/client';
   ```

   这里导入了 `ApolloClient`,`InMemoryCache` 和 `gql` 标签模板函数。

2. **创建 Apollo Client 实例**：

   ```javascript
   const client = new ApolloClient({
     uri: 'http://localhost:4000/graphql', // 替换为你的 GraphQL 服务器地址
     cache: new InMemoryCache(),
   });
   ```

   创建一个 `ApolloClient` 实例，并指定 GraphQL 服务器的 URL 和缓存。

3. **定义 GraphQL 订阅**：

   ```javascript
   const NEW_USER_SUBSCRIPTION = gql`
     subscription NewUser {
       newUser {
         id
         name
         email
       }
     }
   `;
   ```

   使用 `gql` 标签模板函数定义一个名为 `NewUser` 的订阅，该订阅将接收新用户的数据。

4. **订阅数据**：

   ```javascript
   client.subscribe({
     query: NEW_USER_SUBSCRIPTION,
     onSubscriptionData: ({ subscriptionData }) => {
       if (!subscriptionData.data) {
         return;
       }
       console.log('New User:', subscriptionData.data.newUser);
     },
   });
   ```

   使用 `client.subscribe()` 方法订阅数据，并提供一个回调函数来处理接收到的数据。

5. **定义 GraphQL 查询**：

   ```javascript
   const GET_USERS_QUERY = gql`
     query GetUsers {
       users {
         id
         name
         email
       }
     }
   `;
   ```

   使用 `gql` 标签模板函数定义一个名为 `GetUsers` 的查询，该查询将获取所有用户的数据。

6. **执行查询**：

   ```javascript
   client.query({
     query: GET_USERS_QUERY,
   }).then((result) => {
     console.log(result.data.users);
   }).catch((error) => {
     console.error(error);
   });
   ```

   使用 `client.query()` 方法执行查询，并处理结果或错误。

### 标签模板函数的工作原理

在 JavaScript 中，标签模板函数的工作原理如下：

```javascript
const template = gql`template string here`;
```

实际上相当于：

```javascript
const template = gql("template string here");
```

但是 `gql` 函数接收的是多个参数，第一个参数是字符串模板的部分，后续参数是字符串模板中的变量值。在 `gql` 标签模板函数中，Apollo Client 会处理字符串中的换行和缩进，并返回一个合适的字符串。

因此，`gql` 标签模板函数的使用方式是：

```javascript
const NEW_USER_SUBSCRIPTION = gql`
  subscription NewUser {
    newUser {
      id
      name
      email
    }
  }
`;
```

而不是：

```javascript
const NEW_USER_SUBSCRIPTION = gql("subscription NewUser { ... }");
```

这种语法糖使得 GraphQL 字符串更加清晰和易于阅读。
