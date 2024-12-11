---
aliases: 
<<<<<<< HEAD
theme: 
priority: false
=======
categories: 
high_priority: false
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
tags:
---
# libs 文件夹分析

libs 文件夹包含了 Autospace Workshop 项目的所有可复用库，这些库被不同的应用程序使用，以实现代码共享和模块化。

**库列表:**

- **3d:** 3D 模型库，使用 Three.js 和 React Three Fiber 构建，用于渲染停车场和车辆的 3D 模型。
    - **主要组件:** CarScene, Spawner, Square, Car, Building, BuildingSet
    - **依赖:** @react-three/drei, @react-three/fiber, three
- **forms:** 表单库，包含各种表单组件和逻辑，用于创建和管理停车场、停车位等。
    - **主要组件:** FormProviderCreateGarage, useFormCreateGarage
    - **依赖:** @hookform/resolvers, react-hook-form, zod
- **network:** 网络请求库，使用 Apollo Client 与后端 API 交互，处理 GraphQL 查询和突变。
    - **主要文件:** generated.tsx (GraphQL 代码生成文件)
    - **依赖:** @apollo/client, jsonwebtoken, @graphql-codegen/*
- **sample-lib:** 示例库，用于演示如何创建和使用库。
- **ui:** UI 组件库，包含各种 UI 组件，例如按钮、表单、地图等。
    - **主要组件:** Button, Form, Map, GarageCard, ListGarages, AuthLayout
    - **依赖:** @autospace/forms, @autospace/util, @emotion/react, @emotion/styled, @headlessui/react, @mapbox/polyline, @mui/material, @stripe/stripe-js, mapbox-gl, next, react, react-dom, react-map-gl, react-toastify
- **util:** 工具库，包含各种工具函数和常量，例如日期格式化、分页等。
    - **主要文件:** constants.ts, types.ts
    - **依赖:** date-fns, pluralize

**特点:**

- 每个库都有自己的 `package.json` 文件，用于管理依赖项和构建脚本。
- 每个库都有自己的 `tsconfig.json` 文件，用于配置 TypeScript 编译器选项。
- 库之间可以相互依赖，例如 ui 库依赖于 forms 和 util 库。

**总结:**

libs 文件夹的结构清晰，每个库都有明确的职责和依赖关系，方便开发者查找和使用。这种模块化的设计提高了代码的可重用性和可维护性，使得 Autospace Workshop 项目更加易于开发和扩展。

## libs 文件夹疑难要点摘要注释

**1. 3D 库:**

- **坐标系:** Three.js 使用右手坐标系，其中 X 轴指向右，Y 轴指向上，Z 轴指向屏幕外。
- **单位:** Three.js 使用的单位是任意单位，通常可以将其视为米或厘米。
- **渲染循环:** Three.js 使用渲染循环来更新场景并将其渲染到屏幕上。渲染循环通常使用 `requestAnimationFrame` 函数来实现。
- **组件:** 3D 库中的组件（例如 Car, Building）都是 React 组件，可以使用 JSX 语法进行渲染。

**2. forms 库:**

- **表单验证:** forms 库使用 Zod 进行表单验证，可以定义表单字段的类型和验证规则。
- **表单提交:** forms 库使用 React Hook Form 来处理表单提交，可以轻松地获取表单数据并将其发送到后端。

**3. network 库:**

- **GraphQL 代码生成:** network 库使用 GraphQL Code Generator 来生成 TypeScript 类型和操作，可以提高代码的类型安全性和可读性。
- **Apollo Client:** network 库使用 Apollo Client 来与后端 API 交互，可以轻松地发送 GraphQL 查询和突变。

**4. ui 库:**

- **Next.js:** ui 库使用 Next.js 框架构建，可以实现服务器端渲染和静态站点生成。
- **Tailwind CSS:** ui 库使用 Tailwind CSS 框架进行样式设计，可以快速构建美观的用户界面。
- **Mapbox GL JS:** ui 库使用 Mapbox GL JS 库来渲染地图，可以显示停车场的位置和其他地理信息。

**5. util 库:**

- **日期格式化:** util 库使用 date-fns 库来格式化日期，可以将日期转换为不同的格式。
- **分页:** util 库提供分页相关的工具函数，可以方便地实现分页功能。


**总结:**

libs 文件夹中的库涵盖了 Autospace Workshop 项目的各个方面，从 3D 渲染到表单验证再到网络请求，都提供了相应的工具和组件。理解这些库的功能和使用方法对于开发 Autospace Workshop 项目至关重要。


## hooks 文件夹分析讲解

hooks 文件夹包含了 Autospace Workshop 项目中使用的自定义 React Hooks，这些 Hooks 封装了一些常用的逻辑，例如防抖、分页等，可以提高代码的可重用性和可维护性。

**Hooks 列表:**

- **useDebounce:** 防抖 Hook，用于延迟函数的执行，例如在用户输入时延迟搜索请求的发送。
- **usePagination:** 分页 Hook，用于管理分页状态和逻辑，例如获取当前页码、每页显示数量等。
- **useCloudinaryUpload:** 云存储上传 Hook，用于将文件上传到 Cloudinary 云存储服务。

**useDebounce Hook:**

```typescript:libs/util/hooks/async.ts
import { useEffect, useState } from 'react'

export const useDebounce = <T>(
  value: T,
  delay = 1000,
): [T, { debouncing: boolean }] => {
  const [debouncedValue, setDebouncedValue] = useState<T>(value)
  const [debouncing, setDebouncing] = useState<boolean>(false)

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value)
      setDebouncing(false)
    }, delay)

    setDebouncing(true)

    return () => {
      clearTimeout(handler)
    }
  }, [value, delay])

  return [debouncedValue, { debouncing }]
}
```

**功能:**

- 接收一个值和一个延迟时间作为参数。
- 返回一个防抖后的值和一个指示是否正在防抖的状态。
- 当值发生变化时，会启动一个定时器，延迟 `delay` 毫秒后更新防抖后的值。
- 如果在延迟时间内值再次发生变化，则会取消之前的定时器，重新启动一个新的定时器。

**使用方法:**

```typescript
const [searchTerm, { debouncing }] = useDebounce(input, 500)

// 使用 debouncedValue 进行搜索
```

**usePagination Hook:**

```typescript:libs/util/hooks/pagination.ts
import { useState } from 'react'

export const useTakeSkip = () => {
  const [skip, setSkip] = useState(0)
  const [take, setTake] = useState(10)

  return { skip, take, setSkip, setTake }
}
```

**功能:**

- 管理分页状态，包括当前页码 (`skip`) 和每页显示数量 (`take`)。
- 提供更新分页状态的方法 (`setSkip` 和 `setTake`)。

**使用方法:**

```typescript
const { skip, take, setSkip, setTake } = usePagination()

// 使用 skip 和 take 获取分页数据
```

**useCloudinaryUpload Hook:**

```typescript:libs/util/hooks/cloudinary.ts
import { useState } from 'react'

export const useCloudinaryUpload = () => {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [url, setUrl] = useState<string | null>(null)

  const upload = async (file: File) => {
    setLoading(true)
    setError(null)

    try {
      const formData = new FormData()
      formData.append('file', file)
      formData.append('upload_preset', 'autospace')

      const response = await fetch(
        `https://api.cloudinary.com/v1_1/${process.env.NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME}/image/upload`,
        {
          method: 'POST',
          body: formData,
        },
      )

      const data = await response.json()

      if (data.secure_url) {
        setUrl(data.secure_url)
      } else {
        setError('Upload failed')
      }
    } catch (error) {
      setError('Upload failed')
    } finally {
      setLoading(false)
    }
  }

  return { loading, error, url, upload }
}
```

**功能:**

- 将文件上传到 Cloudinary 云存储服务。
- 提供上传状态 (`loading`)、错误信息 (`error`) 和上传后的 URL (`url`)。
- 提供上传方法 (`upload`)。

**使用方法:**

```typescript
const { loading, error, url, upload } = useCloudinaryUpload()

// 调用 upload 方法上传文件
```

**总结:**

hooks 文件夹中的 Hooks 提供了一些常用的逻辑，可以提高代码的可重用性和可维护性。理解这些 Hooks 的功能和使用方法对于开发 Autospace Workshop 项目至关重要。