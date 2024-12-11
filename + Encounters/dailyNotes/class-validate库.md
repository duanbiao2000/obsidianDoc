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
在 NestJS 中，`common.dto.ts` 文件通常包含一些通用的数据传输对象（DTO），用于输入验证。`@IsOptional()` 和 `@IsIn(['asc', 'desc'])` 是验证装饰器，用于确保传入的数据满足一定的条件。这些装饰器来自 `class-validator` 库，这是一个用于验证对象的库，常用于配合 NestJS 进行请求参数的验证。

### 解释

#### `@IsOptional()`

`@IsOptional()` 是一个验证装饰器，用于标记某个属性为可选。这意味着如果该属性没有在请求中提供，验证仍然会通过。具体来说：

- **用途**：标记某个属性为可选，即该属性可以存在也可以不存在。
- **示例**：如果某个请求参数 `sortOrder` 可以不提供，默认情况下可以不进行验证。

#### `@IsIn(['asc', 'desc'])`

`@IsIn(['asc', 'desc'])` 是一个验证装饰器，用于确保一个字符串值必须存在于给定的数组中。具体来说：

- **用途**：验证某个字符串属性的值必须在指定的数组中。
- **示例**：如果 `sortOrder` 必须是 `'asc'` 或 `'desc'` 中的一个，可以使用此装饰器进行验证。

### 示例代码

假设我们有一个 `CommonDto` 类，其中包含一个 `sortOrder` 属性，该属性可以是 `'asc'` 或 `'desc'`，并且是可选的：

```typescript
import { IsOptional, IsIn } from 'class-validator';

export class CommonDto {
  @IsOptional()
  @IsIn(['asc', 'desc'])
  sortOrder?: string;
}
```

### 解释

1. **`sortOrder` 属性**：
   - `sortOrder` 是一个可选属性（通过 `?` 表示），意味着它可以在请求中出现也可以不出现。
   - 使用 `@IsOptional()` 装饰器进一步明确该属性是可选的。

2. **`@IsIn(['asc', 'desc'])` 装饰器**：
   - 该装饰器确保如果 `sortOrder` 属性存在，它的值必须是 `'asc'` 或 `'desc'`。
   - 如果 `sortOrder` 的值不是其中之一，验证会失败，并抛出错误。

### 使用示例

假设你在控制器中使用了这个 DTO 来验证请求参数：

```typescript
import { Controller, Get, Query, UseGuards } from '@nestjs/common';
import { CommonDto } from './common.dto';

@Controller('api')
export class ApiController {
  @Get('items')
  async getItems(@Query() query: CommonDto) {
    // query.sortOrder 可能存在也可能不存在
    // 如果存在，它的值只能是 'asc' 或 'desc'
    const sortOrder = query.sortOrder || 'asc'; // 默认值为 'asc'
    // 根据 sortOrder 进行排序逻辑
  }
}
```

### 总结

`@IsOptional()` 和 `@IsIn(['asc', 'desc'])` 装饰器共同作用于 `CommonDto` 类中的 `sortOrder` 属性，确保该属性是可选的，并且如果存在，其值必须是 `'asc'` 或 `'desc'`。这有助于在处理请求时进行严格的输入验证，提高应用程序的健壮性和安全性。