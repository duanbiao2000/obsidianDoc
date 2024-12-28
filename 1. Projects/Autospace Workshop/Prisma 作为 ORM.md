在 NestJS 项目中，**Prisma Layer** 是负责与数据库交互的核心部分。为了扩展 Prisma Layer 的功能，可以采取以下几种方式：

---

### 1. **自定义 Prisma 服务**
   你可以在 `PrismaService` 中添加自定义方法，封装常用的数据库操作，以便在服务层中更方便地调用。

#### 示例：
```typescript
// src/prisma/prisma.service.ts
import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient {
  // 自定义方法：根据条件查询用户
  async findUserByEmail(email: string) {
    return this.user.findUnique({ where: { email } });
  }

  // 自定义方法：批量删除用户
  async deleteUsersByIds(ids: number[]) {
    return this.user.deleteMany({ where: { id: { in: ids } } });
  }
}
```

在服务层中调用：
```typescript
// src/users/user.service.ts
import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';

@Injectable()
export class UserService {
  constructor(private prisma: PrismaService) {}

  async findByEmail(email: string) {
    return this.prisma.findUserByEmail(email);
  }

  async deleteUsers(ids: number[]) {
    return this.prisma.deleteUsersByIds(ids);
  }
}
```

---

### 2. **实现 Repository 模式**
   虽然 Prisma 已经提供了高度抽象的 API，但在某些场景下，你可能希望进一步封装数据库操作，以实现更清晰的业务逻辑分离。这时可以实现 **Repository 模式**。

#### 示例：
```typescript
// src/users/user.repository.ts
import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';

@Injectable()
export class UserRepository {
  constructor(private prisma: PrismaService) {}

  async findAll() {
    return this.prisma.user.findMany();
  }

  async create(data: { name: string; email: string }) {
    return this.prisma.user.create({ data });
  }

  async update(id: number, data: { name?: string; email?: string }) {
    return this.prisma.user.update({ where: { id }, data });
  }

  async delete(id: number) {
    return this.prisma.user.delete({ where: { id } });
  }
}
```

在服务层中使用：
```typescript
// src/users/user.service.ts
import { Injectable } from '@nestjs/common';
import { UserRepository } from './user.repository';

@Injectable()
export class UserService {
  constructor(private userRepository: UserRepository) {}

  async getUsers() {
    return this.userRepository.findAll();
  }

  async createUser(data: { name: string; email: string }) {
    return this.userRepository.create(data);
  }
}
```

---

### 3. **扩展 Prisma 模型**
   Prisma 允许你通过 `schema.prisma` 文件定义数据模型。你可以扩展这些模型，添加新的字段、关系或索引，以满足业务需求。

#### 示例：
```prisma
// prisma/schema.prisma
model User {
  id        Int      @id @default(autoincrement())
  name      String
  email     String   @unique
  posts     Post[]   // 扩展关系
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  authorId  Int
  author    User     @relation(fields: [authorId], references: [id])
}
```

运行 `npx prisma generate` 更新 Prisma Client。

---

### 4. **添加中间件**
   Prisma 支持中间件（Middleware），可以在执行查询前后添加自定义逻辑。例如，记录日志、验证数据或修改查询结果。

#### 示例：
```typescript
// src/prisma/prisma.service.ts
import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient {
  constructor() {
    super();
    this.$use(async (params, next) => {
      // 记录日志
      console.log('Query:', params.model, params.action, params.args);

      // 执行查询
      const result = await next(params);

      // 修改结果
      if (params.model === 'User' && params.action === 'findMany') {
        return result.map((user) => ({ ...user, email: user.email.toUpperCase() }));
      }

      return result;
    });
  }
}
```

---

### 5. **集成数据验证**
   在 Prisma Layer 中，可以集成数据验证逻辑，确保输入数据符合业务规则。可以使用类验证器（如 `class-validator`）或自定义验证逻辑。

#### 示例：
```typescript
// src/users/user.service.ts
import { Injectable, BadRequestException } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';

@Injectable()
export class UserService {
  constructor(private prisma: PrismaService) {}

  async createUser(data: { name: string; email: string }) {
    // 验证邮箱格式
    if (!this.validateEmail(data.email)) {
      throw new BadRequestException('Invalid email format');
    }

    return this.prisma.user.create({ data });
  }

  private validateEmail(email: string): boolean {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  }
}
```

---

### 6. **支持多数据库**
   如果你的项目需要支持多个数据库，可以在 Prisma Layer 中配置多个 `PrismaClient` 实例，并根据需要切换。

#### 示例：
```typescript
// src/prisma/prisma.service.ts
import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService {
  public readonly db1: PrismaClient;
  public readonly db2: PrismaClient;

  constructor() {
    this.db1 = new PrismaClient({ datasources: { db: { url: process.env.DB1_URL } } });
    this.db2 = new PrismaClient({ datasources: { db: { url: process.env.DB2_URL } } });
  }
}
```

在服务层中使用：
```typescript
// src/users/user.service.ts
import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';

@Injectable()
export class UserService {
  constructor(private prisma: PrismaService) {}

  async getUsersFromDb1() {
    return this.prisma.db1.user.findMany();
  }

  async getUsersFromDb2() {
    return this.prisma.db2.user.findMany();
  }
}
```

---

### 7. **性能优化**
   - **批量操作**：使用 Prisma 的批量操作功能（如 `createMany`、`updateMany`）来提高性能。
   - **查询优化**：使用 `select` 和 `include` 来减少不必要的数据加载。
   - **连接池**：配置 Prisma 的连接池，以支持高并发场景。

#### 示例：
```typescript
// src/prisma/prisma.service.ts
import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient {
  constructor() {
    super({
      datasources: {
        db: {
          url: process.env.DATABASE_URL,
        },
      },
      log: ['query', 'info', 'warn', 'error'],
    });
  }
}
```

---

### 总结
通过以上方式，你可以扩展 **Prisma Layer** 的功能，使其更符合业务需求。无论是自定义方法、实现 Repository 模式、添加中间件，还是支持多数据库，Prisma 都提供了灵活的扩展能力。根据项目的复杂度和需求，选择合适的方式来优化和扩展 Prisma Layer。

如果你有更多具体需求或问题，欢迎继续提问！