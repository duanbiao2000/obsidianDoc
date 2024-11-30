---
aliases: 
theme: 
priority: false
tags:
---
`@hookform/resolvers/zod` 是一个库，它允许你将 Zod 验证器与 React Hook Form 集成在一起。Zod 是一个 TypeScript-first 的数据验证库，而 React Hook Form 是一个高性能、灵活且易于使用的表单处理库。通过 `zodResolver`，你可以利用 Zod 的强大验证功能来处理表单数据的验证。

### 安装依赖

首先，你需要安装 `@hookform/resolvers` 和 `zod` 库。如果你还没有安装这些库，可以使用 npm 或 yarn 来安装：

```sh
npm install @hookform/resolvers zod react-hook-form
# 或者
yarn add @hookform/resolvers zod react-hook-form
```

### 使用 `zodResolver`

以下是一个完整的示例，展示了如何在 React Hook Form 中使用 `zodResolver` 来进行表单验证。

1. **定义 Zod 模式**:
   - 首先，定义你的 Zod 模式（schema），描述你的表单数据结构和验证规则。

2. **创建表单组件**:
   - 使用 `react-hook-form` 和 `zodResolver` 来创建表单组件，并应用验证逻辑。

### 示例代码

#### 1. 定义 Zod 模式

```jsx
import { z } from 'zod';

const schema = z.object({
  username: z.string().min(3, { message: 'Username must be at least 3 characters long' }).max(20, { message: 'Username cannot be longer than 20 characters' }),
  email: z.string().email({ message: 'Invalid email address' }),
  password: z.string().min(8, { message: 'Password must be at least 8 characters long' }),
  confirmPassword: z.string().min(8, { message: 'Confirm password must be at least 8 characters long' }),
}).refine((data) => data.password === data.confirmPassword, {
  message: "Passwords don't match",
  path: ['confirmPassword'], // 如果需要指定错误路径
});
```

#### 2. 创建表单组件

```jsx
import React from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

// 引入上面定义的模式
import { schema } from './path-to-schema';

const MyForm = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(schema),
  });

  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label htmlFor="username">Username</label>
        <input id="username" {...register('username')} />
        {errors.username && <p>{errors.username.message}</p>}
      </div>

      <div>
        <label htmlFor="email">Email</label>
        <input id="email" type="email" {...register('email')} />
        {errors.email && <p>{errors.email.message}</p>}
      </div>

      <div>
        <label htmlFor="password">Password</label>
        <input id="password" type="password" {...register('password')} />
        {errors.password && <p>{errors.password.message}</p>}
      </div>

      <div>
        <label htmlFor="confirmPassword">Confirm Password</label>
        <input id="confirmPassword" type="password" {...register('confirmPassword')} />
        {errors.confirmPassword && <p>{errors.confirmPassword.message}</p>}
      </div>

      <button type="submit">Submit</button>
    </form>
  );
};

export default MyForm;
```

### 解释

- **Zod 模式**:
  - 定义了一个对象模式 `schema`，包含 `username`、`email`、`password` 和 `confirmPassword` 字段。
  - 使用 `z.string()` 来定义字符串字段，并添加了最小长度和最大长度的验证。
  - 使用 `z.string().email()` 来验证电子邮件地址。
  - 使用 `refine` 方法来确保 `password` 和 `confirmPassword` 字段匹配。

- **React Hook Form**:
  - 使用 `useForm` Hook 并传递 `resolver` 选项，值为 `zodResolver(schema)`。
  - `register` 用于注册表单字段，以便 React Hook Form 可以跟踪它们的状态。
  - `handleSubmit` 用于处理表单提交。
  - `errors` 对象包含了所有验证失败的字段及其错误信息。

- **表单渲染**:
  - 渲染每个表单字段，并使用 `{...register('fieldName')}` 将其注册到 React Hook Form。
  - 显示每个字段的验证错误信息（如果有）。

通过这种方式，你可以轻松地在 React Hook Form 中集成 Zod 验证，从而实现强大的表单验证功能。