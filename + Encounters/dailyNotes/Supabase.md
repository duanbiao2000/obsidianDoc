---
aliases: 
theme: 
high_priority: false
tags:
---
Supabase 是一个开源的 Backend-as-a-Service（BaaS）平台，它提供了一套工具和服务，使开发者能够快速构建和部署全栈 web 应用程序。Supabase 结合了数据库、身份验证、实时订阅、存储等多种功能，为开发者提供了类似于 Firebase 的体验，但完全基于开源技术。

### Supabase 的主要特性

1. **PostgreSQL 数据库**：
   - Supabase 使用 PostgreSQL 作为其核心数据库。PostgreSQL 是一个强大且功能丰富的关系型数据库系统，支持复杂的查询和事务处理。
   - 提供了一个图形化的数据库管理界面，方便管理和操作数据。

2. **身份验证与授权**：
   - 内置的身份验证服务，支持多种登录方式（如邮箱/密码、OAuth 提供商等）。
   - 支持角色和权限管理，可以轻松控制用户对数据的访问。

3. **实时订阅**：
   - 通过 WebSocket 实现实时数据同步，允许客户端订阅特定的数据表或查询，并在数据发生变化时自动接收更新。
   - 适用于需要实时数据更新的应用，如聊天应用、协作工具等。

4. **文件存储**：
   - 提供对象存储服务，支持上传、下载和管理文件。
   - 可以设置文件的访问控制策略，确保文件的安全性。

5. **函数和边缘计算**：
   - 支持自定义函数（使用 JavaScript 或 TypeScript 编写），可以在数据库中执行复杂逻辑。
   - 边缘计算功能允许在靠近用户的边缘节点上运行代码，减少延迟。

6. **API 和 SDK**：
   - 提供 REST API 和 GraphQL API，方便前端应用与后端进行交互。
   - 提供多种语言的 [[SDK]]（如 JavaScript、TypeScript、Python 等），简化开发过程。

### 示例：使用 Supabase 构建简单的应用程序

以下是一个简单的示例，展示如何使用 Supabase 构建一个具有用户注册、登录和数据存储功能的应用程序。

#### 1. 创建 Supabase 项目
首先，你需要在 [Supabase](https://supabase.com/) 上创建一个新项目，并获取项目的 URL 和密钥。

#### 2. 安装 Supabase 客户端库
在你的前端项目中安装 Supabase 客户端库：

```bash
npm install @supabase/supabase-js
```

#### 3. 初始化 Supabase 客户端
在你的项目中初始化 Supabase 客户端：

```javascript
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://your-supabase-url.supabase.co';
const supabaseKey = 'your-supabase-key';

const supabase = createClient(supabaseUrl, supabaseKey);
```

#### 4. 用户注册
实现用户注册功能：

```javascript
async function signUp(email, password) {
  const { user, error } = await supabase.auth.signUp({
    email: email,
    password: password,
  });

  if (error) {
    console.error('Error signing up:', error.message);
  } else {
    console.log('User signed up:', user);
  }
}
```

#### 5. 用户登录
实现用户登录功能：

```javascript
async function signIn(email, password) {
  const { user, error } = await supabase.auth.signInWithPassword({
    email: email,
    password: password,
  });

  if (error) {
    console.error('Error signing in:', error.message);
  } else {
    console.log('User signed in:', user);
  }
}
```

#### 6. 存储数据
将数据存储到 PostgreSQL 数据库中：

```javascript
async function addTodo(title) {
  const { data, error } = await supabase
    .from('todos')
    .insert([{ title: title, is_complete: false }]);

  if (error) {
    console.error('Error adding todo:', error.message);
  } else {
    console.log('Todo added:', data);
  }
}
```

#### 7. 查询数据
从数据库中查询数据：

```javascript
async function getTodos() {
  const { data, error } = await supabase
    .from('todos')
    .select('*');

  if (error) {
    console.error('Error fetching todos:', error.message);
  } else {
    console.log('Todos:', data);
  }
}
```

#### 8. 实时订阅
订阅数据变化并实时更新：

```javascript
const channel = supabase
  .channel('public:todos')
  .on(
    'postgres_changes',
    { event: '*', schema: 'public', table: 'todos' },
    (payload) => {
      console.log('Change received!', payload);
      // 更新 UI
    }
  )
  .subscribe();
```

### 总结

Supabase 提供了一整套工具和服务，使开发者能够快速构建全栈应用程序。它结合了强大的 PostgreSQL 数据库、身份验证、实时订阅、文件存储等功能，非常适合用于构建现代 web 应用程序。通过上述示例，你可以看到如何使用 Supabase 来实现基本的用户认证和数据存储功能。如果你有更具体的需求或问题，可以参考 [Supabase 官方文档](https://supabase.io/docs) 获取更多详细信息。