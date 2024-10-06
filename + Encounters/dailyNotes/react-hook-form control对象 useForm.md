---
aliases: 
theme: 
high_priority: false
tags:
---
在 React 中，如果你正在使用 `react-hook-form` 与 `@hookform/resolvers/zod` 来处理表单验证，并且你希望将 `control` 对象传递给子组件，以便这些子组件可以注册到表单上下文中，你可以这样做。`control` 对象是 `useForm` 返回的一个重要属性，它允许你管理表单字段的注册、值和状态。

### 示例代码

假设你有一个父组件 `MyForm`，其中使用了 `react-hook-form` 和 `zodResolver`，并且你希望将 `control` 对象传递给一个子组件 `CustomInput`。

#### 父组件 `MyForm`

```jsx
import React from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import CustomInput from './CustomInput';

// 定义 Zod 模式
const schema = z.object({
  username: z.string().min(3, { message: 'Username must be at least 3 characters long' }).max(20, { message: 'Username cannot be longer than 20 characters' }),
  email: z.string().email({ message: 'Invalid email address' }),
});

const MyForm = () => {
  const {
    control,
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
      <CustomInput
        name="username"
        label="Username"
        control={control}
        error={errors.username?.message}
      />
      <CustomInput
        name="email"
        label="Email"
        control={control}
        error={errors.email?.message}
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default MyForm;
```

#### 子组件 `CustomInput`

```jsx
import React from 'react';
import { useController } from 'react-hook-form';

const CustomInput = ({ name, label, control, error }) => {
  // 使用 useController Hook 注册字段
  const {
    field, // 包含 onChange, onBlur, value, ref
    fieldState: { invalid, isTouched, isDirty }, // 验证状态
    formState: { isSubmitted }, // 表单提交状态
  } = useController({
    name,
    control,
    rules: { required: true }, // 可以在这里添加额外的规则
    defaultValue: '', // 默认值
  });

  return (
    <div>
      <label htmlFor={name}>{label}</label>
      <input
        id={name}
        {...field}
        className={`form-control ${invalid && isTouched ? 'is-invalid' : ''}`}
      />
      {error && <p className="text-danger">{error}</p>}
    </div>
  );
};

export default CustomInput;
```

### 解释

1. **父组件 `MyForm`**:
   - 使用 `useForm` 创建表单实例，并传入 `zodResolver`。
   - 将 `control` 对象作为 prop 传递给 `CustomInput` 组件。
   - 传递错误信息 `errors.username?.message` 和 `errors.email?.message` 到 `CustomInput` 组件。

2. **子组件 `CustomInput`**:
   - 使用 `useController` Hook 注册表单字段。`useController` 接受 `name`、`control` 和可选的 `rules` 参数。
   - `field` 对象包含 `onChange`, `onBlur`, `value`, 和 `ref`，这些属性用于绑定到输入元素上。
   - 根据 `invalid` 和 `isTouched` 的状态来动态设置输入框的样式。
   - 显示错误信息（如果有的话）。

通过这种方式，你可以将表单控制逻辑封装在父组件中，同时将具体的输入组件保持为独立的可复用组件。这样可以提高代码的可维护性和可读性。