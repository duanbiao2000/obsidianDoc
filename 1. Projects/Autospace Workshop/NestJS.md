---
aliases: 
theme: 
high_priority: false
tags:
---
NestJS 是一个用于构建高效、可扩展的服务器端应用程序的框架，它基于 Node.js 和 Express.js，采用了现代的 JavaScript（ES6+）语法。NestJS 设计上强调模块化、可注入性和易于使用的 API，使得开发者可以快速构建健壮的后端服务。

### NestJS 的主要特点

1. **模块化架构**：
   - NestJS 采用了模块化的架构，使得代码组织更为清晰，易于维护和扩展。
   - 每个模块可以包含控制器、服务、提供者等组件，并且模块之间可以相互依赖。

2. **依赖注入（Dependency Injection, DI）**：
   - NestJS 支持[[依赖注入]]，使得组件之间的依赖关系更加明确，提高了代码的可测试性和可重用性。
   - 依赖注入使得组件之间的耦合度降低，提高了代码的可维护性。

3. **装饰器（Decorators）**：
   - NestJS 使用装饰器来标记类、方法和属性，提供元数据用于框架的编排。
   - 装饰器使得开发者可以轻松地定义路由、中间件、拦截器等。

4. **强大的路由系统**：
   - NestJS 提供了强大的路由系统，支持 RESTful API 和 WebSocket。
   - 路由可以轻松定义，并且支持路径参数、查询参数等多种路由方式。

5. **中间件支持**：
   - NestJS 支持 Express.js 的中间件，可以方便地添加身份验证、日志记录等功能。
   - NestJS 还提供了自己的中间件系统，使得中间件的编写更为简洁。

6. **管道（Pipes）**：
   - NestJS 提供了管道机制，可以对请求数据进行转换和验证，确保数据的一致性和安全性。

7. **拦截器（Interceptors）**：
   - 拦截器可以用来在请求处理之前或之后执行某些操作，例如日志记录、响应格式化等。

8. **过滤器（Exception Filters）**：
   - 过滤器可以捕获异常并进行统一处理，提高应用的健壮性。

9. **模板引擎支持**：
   - NestJS 支持多种模板引擎，如 EJS、Handlebars 等，方便生成 HTML 页面。

10. **单元测试支持**：
    - NestJS 内置了单元测试支持，使得编写测试代码变得简单。

### NestJS 的基本概念

1. **模块（Module）**：
   - 模块是 NestJS 应用的核心组成部分，用于组织相关的控制器、服务和其他组件。
   - 模块可以导入其他模块，形成依赖关系。

2. **控制器（Controller）**：
   - 控制器负责处理来自客户端的请求，并返回响应。
   - 控制器通常包含路由定义和相应的处理函数。

3. **服务（Service）**：
   - 服务负责处理业务逻辑，可以被多个控制器共享。
   - 服务通常包含数据访问、计算等操作。

4. **提供者（Provider）**：
   - 提供者可以是服务、工厂或其他可以注入的对象。
   - 提供者可以被依赖注入到其他组件中。

### NestJS 的入门示例

#### 创建一个新的 NestJS 项目

```sh
npm i -g @nestjs/cli
nest new my-nest-app
cd my-nest-app
npm start
```

#### 定义一个简单的模块

```typescript
// src/app.module.ts
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';

@Module({
  imports: [],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

#### 定义一个简单的控制器

```typescript
// src/app.controller.ts
import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }
}
```

#### 定义一个简单的服务

```typescript
// src/app.service.ts
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }
}
```

### 总结

NestJS 是一个强大且灵活的 Node.js 框架，它采用模块化设计和依赖注入机制，使得开发高质量的后端服务变得更为简单。通过 NestJS，你可以快速构建可扩展的 RESTful API 和 WebSocket 应用，并且可以方便地集成多种中间件和模板引擎。无论是构建简单的 API 还是复杂的微服务架构，NestJS 都是一个值得考虑的选择。