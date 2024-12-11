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
好的，我可以帮助你配置 MySQL 和你的后端应用。以下是一些步骤：

**1. 安装 MySQL 驱动:**

首先，你需要安装 `mysql2` 驱动，它允许 TypeORM 与 MySQL 数据库交互。

```bash
npm install mysql2
```

**2. 创建 `ormconfig.json` 文件:**

在你的项目根目录下创建一个名为 `ormconfig.json` 的文件，并添加以下配置：

```json:ormconfig.json
{
  "type": "mysql",
  "host": "localhost", // 你的 MySQL 主机地址
  "port": 3306, // 你的 MySQL 端口号
  "username": "your_username", // 你的 MySQL 用户名
  "password": "your_password", // 你的 MySQL 密码
  "database": "your_database_name", // 你的数据库名称
  "entities": [
    "src/entity/**/*.ts"
  ],
  "migrations": [
    "src/migration/**/*.ts"
  ],
  "cli": {
    "migrationsDir": "src/migration"
  }
}
```

**3. 更新你的代码:**

在你的 `src/index.ts` 文件中，确保 `createConnection()` 函数没有传递任何参数，因为它会自动读取 `ormconfig.json` 文件中的配置。

```typescript:server/src/index.ts
createConnection()
    .then(async () => {
        // ... 你的代码 ...
    })
    .catch((error) => console.log(error));
```

**4. 运行迁移:**

使用以下命令运行迁移，这将根据你的实体定义创建数据库表：

```bash
npm run migration
```

**5. 启动你的后端应用:**

使用以下命令启动你的后端应用：

```bash
npm run start
```

**注意:**

* 确保你的 MySQL 服务器正在运行。
* 将 `ormconfig.json` 文件中的占位符替换为你自己的数据库凭据。
* 你可以使用 `.gitignore` 文件忽略 `ormconfig.json` 文件，以防止将敏感信息提交到版本控制系统。


希望这些步骤能帮助你配置 MySQL 和你的后端应用。如果你有任何其他问题，请随时问我。