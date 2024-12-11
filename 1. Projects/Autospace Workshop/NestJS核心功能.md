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
NestJS 是一个基于 Node.js 的可扩展框架，用于构建高效、可靠和可伸缩的服务器端应用程序。它利用了 TypeScript 的特性，但也支持 JavaScript 和 JSX。NestJS 提供了许多内置功能，其中包括守卫（Guards）、管道（Pipes）、拦截器（Interceptors）以及异常过滤器（Exception Filters），这些都是用来增强应用的功能性和灵活性的重要组件。

### 守卫（Guards）

守卫是用来保护路由处理器免受未授权请求影响的类。它们在路由处理器执行之前被触发，并且允许开发者根据某些条件来决定是否应该允许请求继续。

#### 如何使用守卫

守卫通过装饰器（如 `@UseGuards()`）添加到控制器方法或类上。常见的守卫包括：

- **认证守卫（AuthGuard）**：通常用来确保用户已通过某种形式的身份验证。如果用户没有通过身份验证，则请求会被阻止。
- **自定义守卫**：开发者可以创建自己的守卫类来实现特定的逻辑，例如检查特定的请求头或查询参数。

### 管道（Pipes）

管道是在请求进入路由处理器之前处理请求体、查询字符串或 URL 参数的对象。它们可以用于转换请求数据或者验证数据。

#### 如何使用管道

管道通过 `@UsePipes()` 装饰器添加到控制器方法或类上。例如，你可以创建一个管道来验证传入的数据是否符合特定模式，或者对数据进行预处理。

### 拦截器（Interceptors）

拦截器是在请求到达路由处理器之前和之后执行的一段逻辑。它们可以用来修改请求或响应，例如添加响应头、日志记录、修改请求体等。

#### 如何使用拦截器

拦截器同样通过装饰器 `@UseInterceptors()` 添加到控制器方法或类上。例如，你可以创建一个日志记录拦截器，在请求到达前记录请求信息，在响应发送后记录响应信息。

### 异常过滤器（Exception Filters）

异常过滤器用来处理由应用程序抛出的错误。当发生错误时，异常过滤器会捕获异常并根据需要处理它，例如发送一个友好的错误消息给客户端而不是原始的堆栈跟踪。

#### 如何使用异常过滤器

异常过滤器通过全局异常处理机制或者通过 `@UseFilters()` 装饰器添加到控制器上。你可以创建自定义的异常过滤器来处理特定类型的异常，或者设置全局异常过滤器来捕获所有未处理的异常。

### 示例

下面是一个简单的例子来演示如何在一个 NestJS 应用中使用这些特性：

#### 创建一个认证守卫

```typescript
import { CanActivate, ExecutionContext, Injectable } from '@nestjs/common';

@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    // 在这里检查请求上下文中的认证信息
    const request = context.switchToHttp().getRequest();
    return request.isAuthenticated(); // 假设这是一个检查用户是否已认证的方法
  }
}
```

#### 创建一个验证管道

```typescript
import { PipeTransform, Injectable, ArgumentMetadata, BadRequestException } from '@nestjs/common';

@Injectable()
export class ValidationPipe implements PipeTransform<any> {
  transform(value: any, metadata: ArgumentMetadata) {
    // 在这里验证 value 是否符合预期
    if (!value.isValid()) {
      throw new BadRequestException('Validation failed');
    }
    return value;
  }
}
```

#### 创建一个日志记录拦截器

```typescript
import { CallHandler, ExecutionContext, Injectable, NestInterceptor } from '@nestjs/common';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    console.log('Before...');

    const now = Date.now();

    return next.handle().pipe(
      tap(() => console.log(`After... ${Date.now() - now}ms`)),
    );
  }
}
```

#### 创建一个全局异常过滤器

```typescript
import { ExceptionFilter, ArgumentsHost, HttpException, HttpStatus } from '@nestjs/common';

export class AllExceptionsFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost) {
    const ctx = host.switchToHttp();
    const response = ctx.getResponse();
    const request = ctx.getRequest();

    const status =
      exception instanceof HttpException
        ? exception.getStatus()
        : HttpStatus.INTERNAL_SERVER_ERROR;

    response.status(status).json({
      statusCode: status,
      timestamp: new Date().toISOString(),
      path: request.url,
    });
  }
}
```

以上就是 NestJS 中几个核心功能的基本介绍及其使用方式。这些功能可以帮助开发者构建更加健壮的应用程序，并提供了灵活的方式来处理请求和响应。