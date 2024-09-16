---
aliases: 
theme: 
high_priority: false
tags:
---
使用 Docker Compose 可以更加方便地管理和启动多个服务，特别是当你需要同时启动多个容器（如数据库、Web 服务等）时。下面我将详细介绍如何使用 Docker Compose 来启动 PostgreSQL 数据库，并且展示如何编写 `docker-compose.yml` 文件来配置和启动 PostgreSQL 容器。

### 步骤 1: 创建 `docker-compose.yml` 文件

首先，你需要创建一个 `docker-compose.yml` 文件来定义你的服务和服务间的依赖关系。在这个例子中，我们将仅配置 PostgreSQL 数据库服务。

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:13
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: mysecretpassword
      POSTGRES_DB: autospace
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

### 解释 `docker-compose.yml` 文件

- **version**: 指定 Docker Compose 文件的版本。
- **services**: 定义服务列表。
  - **postgres**: 定义 PostgreSQL 服务。
    - **image**: 指定使用的镜像，这里是官方的 PostgreSQL 13 版本。
    - **restart**: 设置容器重启策略，`always` 表示总是重启。
    - **environment**: 设置环境变量，这里设置了 PostgreSQL 的用户名、密码和默认数据库名。
    - **volumes**: 将本地的数据卷 `postgres_data` 挂载到容器内的 `/var/lib/postgresql/data` 目录，用于存储数据。
    - **ports**: 映射容器的 5432 端口到主机的 5432 端口。
- **volumes**: 定义数据卷，这里定义了一个名为 `postgres_data` 的数据卷。

### 步骤 2: 创建数据卷

如果你还没有创建数据卷，可以先创建一个数据卷来存储数据库的数据。这一步实际上是可选的，因为在 `docker-compose.yml` 文件中已经定义了数据卷，Docker 会在第一次运行时自动创建它。

```bash
docker volume create postgres_data
```

### 步骤 3: 启动服务

使用以下命令启动服务：

```bash
docker-compose up -d
```

这将启动 PostgreSQL 容器，并以后台方式运行。

### 步骤 4: 测试 PostgreSQL 数据库

确保 PostgreSQL 正确启动并运行后，可以使用 `psql` 工具连接数据库进行测试：

```bash
psql -h localhost -U postgres
```

输入密码 `mysecretpassword` 后，你应该能够成功连接到 PostgreSQL 数据库。

### 步骤 5: 停止和删除服务

当你不再需要运行这些服务时，可以使用以下命令停止并删除容器和服务：

```bash
docker-compose down
```

这将停止所有正在运行的服务，并删除相关容器和网络，但保留数据卷中的数据。

### 集成到 NestJS 应用

如果你需要将 PostgreSQL 数据库集成到 NestJS 应用中，可以参考前面提到的步骤来配置 Prisma 或其他 ORM。这里再简单回顾一下如何配置 Prisma：

#### 示例：使用 `nestjs-prisma`

安装必要的依赖：

```bash
npm install @nestjs/cli @nestjs/core prisma @prisma/client typescript ts-node nodemon
```

然后在 `prisma/schema.prisma` 文件中配置数据库连接：

```prisma
datasource db {
  provider = "postgresql"
  url      = "postgresql://postgres:mysecretpassword@localhost:5432/autospace"
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  password  String
}
```

初始化 Prisma：

```bash
npx prisma generate
```

在 `app.module.ts` 中配置 Prisma：

```typescript
import { Module } from '@nestjs/common';
import { PrismaModule } from './prisma/prisma.module';

@Module({
  imports: [PrismaModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
```

创建 Prisma 模块：

```typescript
import { Module } from '@nestjs/common';
import { PrismaService } from './prisma.service';

@Module({
  providers: [PrismaService],
  exports: [PrismaService],
})
export class PrismaModule {}
```

创建 Prisma 服务：

```typescript
import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient {}
```

这样就完成了 PostgreSQL 数据库的容器化，并且成功地将数据库集成到了 NestJS 应用中。通过 Docker Compose 方式管理数据库和其他服务，可以大大简化部署和管理流程，特别是在多环境部署时。