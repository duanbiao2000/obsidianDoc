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
使用 Docker 容器化数据库可以极大地简化部署和管理流程，尤其是在多环境（如开发、测试、生产）下，能够保证一致性。下面以 PostgreSQL 为例，展示如何使用 Docker 来容器化数据库，并且配置持久化存储，以便数据不会因为容器重启而丢失。

### 步骤 1: 准备数据卷

为了让数据持久化，我们需要创建一个 Docker 数据卷来存储数据库的数据文件。数据卷是 Docker 容器之间共享或持久化数据的一种方式。

```bash
docker volume create postgres_data
```

### 步骤 2: 启动 PostgreSQL 容器

接下来，使用 [[Docker Compose]] 或者直接使用 `docker run` 命令来启动 PostgreSQL 容器。这里我们使用 `docker run` 命令来演示：

```bash
docker run --name postgres \
           -v postgres_data:/var/lib/postgresql/data \
           -e POSTGRES_PASSWORD=mysecretpassword \
           -p 5432:5432 \
           -d postgres
```

这里解释一下各个选项的意义：

- `--name postgres`：指定容器的名字为 `postgres`。
- `-v postgres_data:/var/lib/postgresql/data`：将本地的数据卷 `postgres_data` 挂载到容器内的 `/var/lib/postgresql/data` 目录，这是 PostgreSQL 存储数据的位置。
- `-e POSTGRES_PASSWORD=mysecretpassword`：设置 PostgreSQL 的管理员密码。
- `-p 5432:5432`：将容器内部的 5432 端口映射到主机的 5432 端口。
- `-d postgres`：使用官方的 PostgreSQL 镜像启动容器，并以后台方式运行。

### 步骤 3: 测试 PostgreSQL 数据库

确保 PostgreSQL 正确启动并运行后，可以使用 `psql` 工具连接数据库进行测试：

```bash
psql -h localhost -U postgres
```

输入密码 `mysecretpassword` 后，你应该能够成功连接到 PostgreSQL 数据库。

### 步骤 4: 使用 Docker Compose 管理多个服务

如果你的应用不仅仅包含一个 PostgreSQL 数据库，还包含其他服务（如 Web 服务等），那么使用 Docker Compose 可以更加方便地管理和启动多个服务。

创建一个 `docker-compose.yml` 文件：

```yaml
version: '3'
services:
  postgres:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: mysecretpassword
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
  web:
    # 这里可以定义你的 Web 服务
    # image: your-web-service-image
    # ports:
    #   - "8080:8080"

volumes:
  postgres_data:
```

然后使用以下命令启动服务：

```bash
docker-compose up -d
```

### 步骤 5: 集成到 NestJS 应用

在你的 NestJS 应用中，你需要配置数据库连接。你可以使用 `nestjs-prisma` 或者直接使用 `typeorm` 等 ORM 来管理数据库连接。

#### 示例：使用 `nestjs-prisma`

安装必要的依赖：

```bash
npm install @nestjs/cli @nestjs/core prisma @prisma/client typescript ts-node nodemon
```

然后在 `prisma/schema.prisma` 文件中配置数据库连接：

```prisma
datasource db {
  provider = "postgresql"
  url      = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"
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

这样你就完成了 PostgreSQL 数据库的容器化，并且成功地将数据库集成到了 NestJS 应用中。通过这种方式，你可以很容易地管理数据库，并且保证不同环境下的数据库配置一致性。


> [!NOTE]
> 在 Windows 系统下使用 Docker Compose 或者 Docker Desktop 运行容器时，需要注意的是 Windows 和 Linux 的文件路径有所不同。Windows 使用盘符加冒号来表示不同的磁盘分区（如 C:\），而 Linux 使用斜杠来表示路径层级（如 /var/lib/postgresql/data）。

如果你是在 Windows 上使用 Docker Desktop，并且希望持久化数据，可以通过以下几种方式来设置数据卷：

### 1. 使用 Windows 路径映射

在 Windows 下，你可以使用 Windows 的本地路径来映射到 Docker 容器中的路径。例如：

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
      - 'C:\\path\\to\\your\\data\\folder:/var/lib/postgresql/data'
    ports:
      - "5432:5432"

```

这里的 `C:\\path\\to\\your\\data\\folder` 是你在 Windows 上希望用来存储数据的实际路径。请注意，路径中的反斜杠需要转义，所以实际写法是两个反斜杠 `\\`。

### 2. 使用 Docker 自带的卷

另一种方法是使用 Docker 自带的卷，这种方式更加推荐，因为它可以跨平台使用，并且 Docker 会自动管理卷。

首先，创建一个卷：

```bash
docker volume create postgres_data
```

然后，在 `docker-compose.yml` 文件中使用这个卷：

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

### 3. 使用 Windows 环境变量

如果你希望使用环境变量来动态设置数据卷的路径，可以在 `docker-compose.yml` 文件中使用 `${VAR_NAME}` 格式来引用环境变量。

例如：

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
      - '${POSTGRES_DATA_PATH}:/var/lib/postgresql/data'
    ports:
      - "5432:5432"

```

然后，在运行 `docker-compose` 命令时设置环境变量：

```bash
POSTGRES_DATA_PATH=C:\path\to\your\data\folder docker-compose up -d
```

### 注意事项

- 如果你在 Windows 上使用的是 WSL2（Windows Subsystem for Linux 2），那么你可以直接使用 Linux 格式的路径来映射，因为 WSL2 使用的是真正的 Linux 内核，支持 Linux 文件路径。
- 在使用 Windows 路径映射时，请确保路径正确并且具有足够的权限来读写数据。

通过上述方法之一，你就可以在 Windows 系统下设置 Docker 数据卷，并且持久化 PostgreSQL 数据库的数据。选择适合你需求的方法来进行设置即可。