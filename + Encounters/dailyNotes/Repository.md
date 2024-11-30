---
aliases: 
theme: 
priority: false
tags:
---
在软件开发中，特别是使用面向对象编程语言构建应用程序时，`Repository` 模式是一种常用的设计模式，用于抽象数据访问层。`Repository` 的主要作用是封装数据访问逻辑，并为业务逻辑层提供统一的接口来访问存储在数据库中的数据。

#### NestJS 中使用 TypeORM 和 Repository 模式

在 NestJS 中使用 TypeORM 时，通常会创建一个 `Repository` 来处理特定实体的数据访问逻辑。以下是一个简单的示例：

1. **定义实体类**：

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

2. **创建 Repository**：

```typescript
import { Injectable } from '@nestjs/common';
import { Repository } from 'typeorm';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from './entities/user.entity';

@Injectable()
export class UserRepository {
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

3. **在服务中使用 Repository**：

```typescript
import { Injectable } from '@nestjs/common';
import { UserRepository } from './user.repository';

@Injectable()
export class UserService {
  constructor(private userRepository: UserRepository) {}

  async findAll(): Promise<User[]> {
    return this.userRepository.findAll();
  }

  async findOne(id: number): Promise<User> {
    return this.userRepository.findOne(id);
  }

  async create(user: User): Promise<User> {
    return this.userRepository.create(user);
  }

  async delete(id: number): Promise<void> {
    return this.userRepository.delete(id);
  }
}
```

### 总结

`Repository` 模式在软件开发中起到了很重要的作用，它不仅提供了数据访问的抽象，还增强了代码的可维护性和可测试性。通过将数据访问逻辑封装在 `Repository` 中，可以有效地分离业务逻辑与数据访问逻辑，使得代码更加清晰、模块化。在使用如 NestJS 这样的现代框架时，结合 ORM 工具如 TypeORM，可以充分利用 `Repository` 模式的优势，提高开发效率和代码质量。