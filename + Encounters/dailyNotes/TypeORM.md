---
aliases: 

categories: 
high_priority: false
tags:
---
NestJS 是一个基于 Node.js 的可扩展框架，用于构建高效、可靠和可维护的服务器端应用程序。NestJS 支持多种数据库和 ORM（对象关系映射）工具，其中最常用的 ORM 是 TypeORM 和 Sequelize。这里我们将重点介绍 NestJS 中使用 TypeORM 的情况，因为它是最受欢迎的选择之一。

### NestJS 中的 TypeORM

TypeORM 是一个 ORM 库，支持多种数据库，包括 PostgreSQL、MySQL、SQLite、SQL Server 和 CockroachDB。它允许你在 TypeScript 或 JavaScript 中使用面向对象的方式操作数据库。

#### 安装 TypeORM

要在 NestJS 项目中使用 TypeORM，首先需要安装 TypeORM 以及对应的数据库驱动：

```bash
npm install --save typeorm reflect-metadata @nestjs/typeorm
npm install --save mysql2 # 如果使用 MySQL
```

#### 配置 TypeORM

配置 TypeORM 包括设置数据库连接信息以及实体类的路径。可以在 `app.module.ts` 中配置 TypeORM：

```typescript
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'mysql',
      host: 'localhost',
      port: 3306,
      username: 'root',
      password: 'password',
      database: 'test',
      entities: [__dirname + '/dist/**/*.entity{.ts,.js}'],
      synchronize: true, // 生产环境下应设为 false
      logging: true,
    }),
  ],
})
export class AppModule {}
```

这里的配置项包括数据库类型、主机地址、端口、用户名、密码、数据库名称等。`entities` 项指定了实体类的路径，`synchronize` 设置为 `true` 表示 TypeORM 会自动同步实体类到数据库表，但生产环境下建议手动同步以避免意外数据丢失。

#### 定义实体类

实体类代表数据库中的表。在 NestJS 中，实体类通常定义在 `entities` 目录下，并继承自 `BaseEntity`：

```typescript
import { Entity, Column, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;

  @Column()
  email: string;
}
```

#### 使用实体类

在 NestJS 的服务中，可以通过注入 [[Repository]] 来使用实体类：

```typescript
import { Injectable } from '@nestjs/common';
import { Repository } from 'typeorm';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from './entities/user.entity';

@Injectable()
export class UserService {
  constructor(
    @InjectRepository(User)
    private userRepository: Repository<User>,
  ) {}

  async findAll(): Promise<User[]> {
    return await this.userRepository.find();
  }

  async findOne(id: number): Promise<User> {
    return await this.userRepository.findOneBy({ id });
  }

  async create(user: User): Promise<User> {
    return await this.userRepository.save(user);
  }

  async delete(id: number): Promise<void> {
    await this.userRepository.delete(id);
  }
}
```

#### 使用模块路由

在控制器中，可以使用服务来处理来自客户端的请求：

```typescript
import { Controller, Get, Post, Body, Delete, Param } from '@nestjs/common';
import { UserService } from './user.service';

@Controller('users')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Get()
  findAll() {
    return this.userService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.userService.findOne(+id);
  }

  @Post()
  create(@Body() user: any) {
    return this.userService.create(user);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.userService.delete(+id);
  }
}
```

### 总结

在 NestJS 中使用 TypeORM 可以让你以面向对象的方式处理数据库操作，从而简化开发过程。通过配置 TypeORM 并定义实体类，你可以轻松地与数据库进行交互，执行 CRUD 操作。此外，NestJS 提供了模块化的结构，使得服务、控制器和实体类的组织变得更加清晰。

TypeORM 的强大之处在于它不仅提供了数据库操作的功能，还支持事务管理、查询构建等功能，使得数据库操作更加灵活和强大。在实际开发中，根据项目的具体需求选择合适的 ORM 工具是非常重要的。