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

## useFormContext
`useFormContext` 是 `react-hook-form` 库中的一个 Hook，它允许你在组件树的任何地方访问表单上下文。这对于在深层嵌套的组件中使用表单状态和方法非常有用，而不需要手动将这些 props 逐层传递下去。

### 基本用法

`useFormContext` 返回一个包含所有表单状态和方法的对象，类似于 `useForm` 的返回值。你可以使用这个 Hook 来访问表单的 `control`、`register`、`handleSubmit` 等属性。

### 示例代码

假设你有一个表单，并且你想在一个深层嵌套的子组件中访问表单上下文。

#### 父组件 `MyForm`

```jsx
import React from 'react';
import { useForm, FormProvider } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import CustomInput from './CustomInput';

// 定义 Zod 模式
const schema = z.object({
  username: z.string().min(3, { message: 'Username must be at least 3 characters long' }).max(20, { message: 'Username cannot be longer than 20 characters' }),
  email: z.string().email({ message: 'Invalid email address' }),
});

type FormData = z.infer<typeof schema>; // 推断出表单数据的类型

const MyForm = () => {
  const methods = useForm<FormData>({
    resolver: zodResolver(schema),
  });

  const onSubmit = (data: FormData) => {
    console.log(data);
  };

  return (
    <FormProvider {...methods}>
      <form onSubmit={methods.handleSubmit(onSubmit)}>
        <CustomInput name="username" label="Username" />
        <CustomInput name="email" label="Email" />
        <button type="submit">Submit</button>
      </form>
    </FormProvider>
  );
};

export default MyForm;
```

#### 子组件 `CustomInput`

```jsx
import React from 'react';
import { useController, useFormContext } from 'react-hook-form';

type CustomInputProps = {
  name: string;
  label: string;
};

const CustomInput = ({ name, label }: CustomInputProps) => {
  const { control, formState: { errors } } = useFormContext();

  const {
    field, // 包含 onChange, onBlur, value, ref
    fieldState: { invalid, isTouched }, // 验证状态
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
      {errors[name] && <p className="text-danger">{errors[name].message}</p>}
    </div>
  );
};

export default CustomInput;
```

### 解释

1. **父组件 `MyForm`**:
   - 使用 `useForm` 创建表单实例，并传入 `zodResolver`。
   - 使用 `FormProvider` 将表单上下文提供给子组件。`FormProvider` 接受 `useForm` 返回的方法对象作为 prop。
   - 在 `FormProvider` 内部，你可以直接使用 `methods.handleSubmit` 和其他表单方法。

2. **子组件 `CustomInput`**:
   - 使用 `useFormContext` 获取表单上下文。这会返回一个包含 `control`、`formState` 等属性的对象。
   - 使用 `useController` 注册表单字段。`useController` 接受 `name`、`control` 和可选的 `rules` 参数。
   - `field` 对象包含 `onChange`, `onBlur`, `value`, 和 `ref`，这些属性用于绑定到输入元素上。
   - 根据 `invalid` 和 `isTouched` 的状态来动态设置输入框的样式。
   - 显示错误信息（如果有的话）。

通过这种方式，你可以在深层嵌套的组件中轻松访问表单上下文，而不需要手动传递 `control` 或其他表单相关的 props。这样可以提高代码的可维护性和可读性。

## useForm钩子
在 `react-hook-form` 中，`useForm` 钩子返回一个对象，该对象包含多个属性和方法，用于管理和处理表单。以下是一些常用的属性和方法的详细解释：

### `useForm` 返回的对象

```typescript
const {
  control,
  register,
  handleSubmit,
  formState,
  watch,
  setValue,
  getValues,
  reset,
  setError,
  clearErrors,
  trigger,
  unregister,
} = useForm({
  // 配置选项
});
```

#### 1. `control`
- **类型**: `Control<TFieldValues, TContext>`
- **用途**: 用于与 `useController` 和 `useWatch` 等钩子一起使用，以更细粒度地控制表单字段。
- **示例**:
  ```jsx
  import { useController } from 'react-hook-form';

  const { field } = useController({
    name: 'username',
    control,
    rules: { required: true },
    defaultValue: '',
  });
  ```

#### 2. `register`
- **类型**: `(name: FieldPath<TFieldValues>, options?: RegisterOptions) => UseFormRegisterReturn`
- **用途**: 用于注册表单字段，以便 `react-hook-form` 可以跟踪其状态。
- **示例**:
  ```jsx
  <input {...register('username', { required: true })} />
  ```

#### 3. `handleSubmit`
- **类型**: `(onValid: (data: TFieldValues, e?: Event) => void, onInvalid?: (errors: FieldErrors<TFieldValues>, e?: Event) => void) => (e: React.BaseSyntheticEvent) => Promise<void>`
- **用途**: 用于处理表单提交。它会在提交时自动验证表单，并在验证通过后调用提供的回调函数。
- **示例**:
  ```jsx
  const onSubmit = (data) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('username', { required: true })} />
      <button type="submit">Submit</button>
    </form>
  );
  ```

#### 4. `formState`
- **类型**: `UseFormStateReturn<TFieldValues>`
- **用途**: 包含表单的状态信息，如 `isSubmitting`、`isValid`、`dirtyFields`、`errors` 等。
- **示例**:
  ```jsx
  const { isSubmitting, errors } = formState;

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('username', { required: true })} />
      {errors.username && <p>{errors.username.message}</p>}
      <button type="submit" disabled={isSubmitting}>Submit</button>
    </form>
  );
  ```

#### 5. `watch`
- **类型**: `<TName extends FieldPath<TFieldValues> | FieldArrayPath<TFieldValues>>(name: TName, defaultValue?: unknown) => TFieldValues[TName]`
- **用途**: 用于监听表单字段的变化，并返回当前值。
- **示例**:
  ```jsx
  const username = watch('username');

  useEffect(() => {
    console.log('Username changed:', username);
  }, [username]);
  ```

#### 6. `setValue`
- **类型**: `<TName extends FieldPath<TFieldValues>>(name: TName, value: TFieldValues[TName], shouldValidate?: boolean) => Promise<void>`
- **用途**: 用于设置表单字段的值。
- **示例**:
  ```jsx
  setValue('username', 'newUsername', { shouldValidate: true });
  ```

#### 7. `getValues`
- **类型**: `<TName extends FieldPath<TFieldValues>>(name: TName) => TFieldValues[TName]`
- **用途**: 用于获取表单字段的当前值。
- **示例**:
  ```jsx
  const values = getValues();
  console.log(values);
  ```

#### 8. `reset`
- **类型**: `(values?: Partial<TFieldValues>, omitResetState?: OmitResetState) => void`
- **用途**: 用于重置表单字段到初始值或指定的值。
- **示例**:
  ```jsx
  const handleReset = () => {
    reset({ username: '', email: '' });
  };
  ```

#### 9. `setError`
- **类型**: `<TName extends FieldPath<TFieldValues>>(name: TName, error: ValidateError<TFieldValues>) => void`
- **用途**: 用于手动设置表单字段的错误。
- **示例**:
  ```jsx
  setError('username', { type: 'manual', message: 'This is a manual error' });
  ```

#### 10. `clearErrors`
- **类型**: `<TName extends FieldPath<TFieldValues>>(name: TName) => void`
- **用途**: 用于清除表单字段的错误。
- **示例**:
  ```jsx
  clearErrors('username');
  ```

#### 11. `trigger`
- **类型**: `<TName extends FieldPath<TFieldValues>>(name: TName, shouldFocus?: boolean) => Promise<boolean>`
- **用途**: 用于手动触发表单字段的验证。
- **示例**:
  ```jsx
  const isValid = await trigger('username');
  if (isValid) {
    console.log('Username is valid');
  }
  ```

#### 12. `unregister`
- **类型**: `<TName extends FieldPath<TFieldValues>>(name: TName) => void`
- **用途**: 用于取消注册表单字段。
- **示例**:
  ```jsx
  unregister('username');
  ```

这些属性和方法提供了强大的功能，可以帮助你轻松地管理和处理表单数据。通过结合使用这些工具，你可以创建高效且易于维护的表单。