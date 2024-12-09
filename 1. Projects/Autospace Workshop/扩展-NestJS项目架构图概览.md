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
当然，可以用 Markdown 支持的图表语法来绘制一个简单的 NestJS 项目的架构示意图。这里我们将展示一个包含 GraphQL 的 NestJS 项目的架构概览。

以下是 Markdown 支持的 Mermaid 图表语法来表示这个架构：

```mermaid
graph TD
    subgraph Frontend
        FE[Frontend Application]
    end
    
    subgraph Backend
        subgraph Gateway
            GW[NestJS Gateway]
            FE --> GW
        end
        
        subgraph GraphQL Layer
            GL[NestJS GraphQL Layer]
            GW --> GL
        end
        
        subgraph Services Layer
            SL[NestJS Services Layer]
            GL --> SL
        end
        
        subgraph Prisma Layer
            PL[NestJS Prisma Layer]
            SL --> PL
        end
        
        subgraph Database Layer
            DB[PostgreSQL Database]
            PL --> DB
        end
    end
    
    FE -->|HTTP(S)| GW
    GW -->|GraphQL| GL
    GL -->|Resolvers| SL
    SL -->|Business Logic| PL
    PL -->|ORM| DB
```

### 解释

1. **Frontend**：
   - **FE**：前端应用，通过 HTTP(S) 请求与后端交互。

2. **Backend**：
   - **GW**：NestJS Gateway，作为前端请求的入口点，可以处理 WebSocket 连接、请求转发等。
   - **GL**：NestJS GraphQL Layer，处理 GraphQL 请求，通过解析器（resolvers）与服务层交互。
   - **SL**：NestJS Services Layer，负责业务逻辑处理，与 Prisma 层交互。
   - **PL**：NestJS Prisma Layer，使用 Prisma 作为 ORM，与数据库交互。
   - **DB**：PostgreSQL 数据库，存储数据。

### 详细说明

- **前端应用（FE）**：
  - 发起 HTTP(S) 请求到后端应用。
  - 可以发送 GraphQL 查询或变异请求。

- **NestJS Gateway（GW）**：
  - 处理前端请求，并将请求转发到 GraphQL 层。
  - 可以处理身份验证、请求日志记录等。

- **NestJS GraphQL 层（GL）**：
  - 接收 GraphQL 请求，并通过解析器处理请求。
  - 将处理后的数据返回给前端。

- **NestJS 服务层（SL）**：
  - 处理业务逻辑，如数据处理、验证等。
  - 与 Prisma 层交互，获取或修改数据。

- **NestJS Prisma 层（PL）**：
  - 使用 Prisma 作为 ORM，与数据库交互。
  - 提供类型安全的数据访问接口。

- **PostgreSQL 数据库（DB）**：
  - 存储应用数据。
  - 通过 Prisma 层与应用交互。

### 示例代码

为了更好地理解各个层次是如何工作的，这里提供一些示例代码：

#### 1. 定义模块

```typescript
// src/app.module.ts
import { Module } from '@nestjs/common';
import { GraphQLModule } from '@nestjs/graphql';
import { PrismaModule } from './prisma/prisma.module';
import { UserService } from './users/user.service';
import { UserResolver } from './users/user.resolver';

@Module({
  imports: [
    GraphQLModule.forRoot({
      autoSchemaFile: true,
    }),
    PrismaModule,
  ],
  providers: [UserService, UserResolver],
})
export class AppModule {}
```

#### 2. 定义 Prisma 模块

```typescript
// src/prisma/prisma.module.ts
import { Module } from '@nestjs/common';
import { PrismaService } from './prisma.service';

@Module({
  providers: [PrismaService],
  exports: [PrismaService],
})
export class PrismaModule {}
```

#### 3. 定义 Prisma 服务

```typescript
// src/prisma/prisma.service.ts
import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient {}
```

#### 4. 定义解析器

```typescript
// src/users/user.resolver.ts
import { Resolver, Query } from '@nestjs/graphql';
import { UserService } from './user.service';

@Resolver('User')
export class UserResolver {
  constructor(private userService: UserService) {}

  @Query(() => [User])
  async users() {
    return this.userService.findAll();
  }
}
```

#### 5. 定义服务

```typescript
// src/users/user.service.ts
import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';

@Injectable()
export class UserService {
  constructor(private prisma: PrismaService) {}

  async findAll() {
    return await this.prisma.user.findMany();
  }
}
```

通过这样的分层架构，你可以构建一个健壮的 NestJS 应用，其中 GraphQL 层负责处理 API 请求，服务层负责业务逻辑处理，Prisma 层负责数据访问，最终与 PostgreSQL 数据库交互。

