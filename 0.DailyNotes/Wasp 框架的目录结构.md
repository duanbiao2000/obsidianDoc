Wasp 框架的目录结构遵循 **“约定优于配置”** 原则，核心目标是简化全栈开发流程——通过固定目录划分前端（UI）、后端（逻辑/数据）和配置，让开发者无需手动维护复杂的工程化配置（如路由、数据库连接、构建脚本）。以下是 Wasp 项目的标准目录结构解析，结合核心文件的作用和使用场景展开说明。


### 一、根目录核心文件（项目配置入口）
根目录仅包含少量关键配置文件，是 Wasp 识别项目结构的“入口”，**不可随意改名或删除**。

| 文件名/目录       | 作用说明                                                                 |
|--------------------|--------------------------------------------------------------------------|
| `main.wasp`        | **项目核心配置文件**，定义全栈项目的“骨架”：<br>- 数据库实体（如 `User` `Task`）<br>- 认证配置（如用户名密码登录）<br>- 后端查询（Queries）/操作（Actions）<br>- 前端页面（Pages）/路由（Routes）<br>- 依赖管理（如添加 NPM 包） |
| `package.json`     | 标准 NPM 配置文件，存储项目名称、版本、脚本（如 `wasp start` 启动命令），Wasp 会自动维护依赖。 |
| `node_modules/`    | NPM 依赖包目录，与普通 JS 项目一致，无需手动修改。                        |
| `.gitignore`       | Git 忽略文件配置，默认包含 `node_modules/`、`.wasp/`（Wasp 编译目录）等。 |
| `.wasp/`           | Wasp 自动生成的编译目录（**无需手动操作**），存储框架处理后的代码、数据库客户端等临时文件，可删除（重启项目会重新生成）。 |


### 二、`src/` 目录：业务代码核心（分前端/后端）
`src/` 是开发者编写业务逻辑的主要目录，内部按 **前端（`client/`）** 和 **后端（`server/`）** 明确划分，逻辑隔离清晰。


#### 1. `src/client/`：前端代码（UI 层）
负责用户交互界面，基于 React（Wasp 默认前端框架），目录结构遵循 React 项目习惯，同时支持 TypeScript（需在 `main.wasp` 中配置）。

| 子目录/文件        | 作用说明                                                                 |
|---------------------|--------------------------------------------------------------------------|
| `src/client/App.jsx` | 前端根组件，类似普通 React 项目的 `App.js`，可定义全局布局（如导航栏、页脚）。 |
| `src/client/pages/`  | **页面组件目录**，与 `main.wasp` 中定义的 `Page` 对应，文件名建议与页面路由匹配（如 `LoginPage.jsx` 对应 `/login` 路由）。<br>例：`src/client/pages/LoginPage.jsx` 会在 `main.wasp` 中配置为 `page LoginPage { component: import('./src/client/pages/LoginPage.jsx') }`，并绑定路由 `route LoginRoute { path: "/login", to: LoginPage }`。 |
| `src/client/components/` | **通用组件目录**，存放可复用的 UI 组件（如按钮、表单、卡片），例：`Button.jsx`、`TaskList.jsx`。 |
| `src/client/hooks/`  | 自定义 React Hooks 目录，封装复用逻辑（如 `useTasks.js` 封装任务数据的获取/更新逻辑）。 |
| `src/client/styles/`  | 样式文件目录，支持 CSS、Sass（需在 `main.wasp` 中添加 `sass` 依赖），可按组件或页面拆分样式（如 `LoginPage.css`）。 |
| `src/client/lib/`    | 前端工具函数目录，存放通用工具（如日期格式化、表单验证函数）。            |


#### 2. `src/server/`：后端代码（逻辑/数据层）
负责业务逻辑处理、数据库操作、身份验证等后端功能，基于 Node.js，Wasp 自动注入 `context`（上下文对象，含数据库客户端、当前用户信息等），无需手动配置数据库连接。

| 子目录/文件                   | 作用说明                                                                                                                                                                                                                                                                         |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src/server/queries/`    | **查询函数目录**，处理“读取数据”的后端逻辑（如获取用户的任务列表），需在 `main.wasp` 中定义为 `query` 才能被前端调用。<br>例：`src/server/queries/getTasks.js` 定义 `getTasks` 函数，在 `main.wasp` 中配置 `query getTasks { fn: import('./src/server/queries/getTasks.js') }`，前端可通过 `useQuery(getTasks)`（Wasp 提供的 React Hook）调用该接口。 |
| `src/server/actions/`    | **操作函数目录**，处理“修改数据”的后端逻辑（如创建/删除任务、用户注册），需在 `main.wasp` 中定义为 `action` 才能被前端调用。<br>例：`src/server/actions/createTask.js` 定义 `createTask` 函数，在 `main.wasp` 中配置 `action createTask { fn: import('./src/server/actions/createTask.js') }`，前端可通过 `useAction(createTask)` 调用。        |
| `src/server/entities/`   | **数据库实体扩展目录**（可选），默认数据库实体（如 `User` `Task`）在 `main.wasp` 中定义，若需扩展实体的方法（如自定义验证逻辑），可在此目录编写（需与 `main.wasp` 中的实体名对应）。                                                                                                                                                             |
| `src/server/lib/`        | 后端工具函数目录，存放通用逻辑（如密码加密、第三方 API 调用、自定义错误处理）。                                                                                                                                                                                                                                   |
| `src/server/migrations/` | **数据库迁移文件目录**（Wasp 自动生成），当修改 `main.wasp` 中的数据库实体（如新增字段、修改关联）后，执行 `wasp db migrate-dev` 会生成迁移文件，记录数据库结构变更，**不可手动修改**（如需回滚，通过 Wasp 命令操作）。                                                                                                                                      |


### 三、其他可选目录（根据项目需求添加）
根据项目复杂度，可在 `src/` 或根目录添加以下可选目录，Wasp 对这些目录无强制约束，按团队习惯维护即可：

| 目录名              | 适用场景                                                                 |
|---------------------|--------------------------------------------------------------------------|
| `src/shared/`       | 前后端共享代码目录（如 TypeScript 类型定义、通用常量），例：`src/shared/types/Task.ts` 定义 `Task` 类型，供前端组件和后端查询/操作复用。 |
| `public/`           | 静态资源目录（如图片、图标、favicon），Wasp 会自动将该目录下的文件暴露到根路由（如 `public/logo.png` 可通过 `/logo.png` 访问）。 |
| `tests/`            | 测试文件目录（如单元测试、E2E 测试），可按 `tests/client/` 和 `tests/server/` 划分前后端测试，支持 Jest、Cypress 等测试工具（需在 `main.wasp` 中添加对应依赖）。 |


### 四、核心目录关系总结（可视化）
```
your-wasp-project/          # 根目录
├── .wasp/                  # Wasp 自动编译目录（临时）
├── node_modules/           # NPM 依赖
├── public/                 # 静态资源（可选）
├── src/                    # 业务代码核心
│   ├── client/             # 前端代码（React）
│   │   ├── components/     # 通用 UI 组件
│   │   ├── hooks/          # 自定义 React Hooks
│   │   ├── pages/          # 页面组件（与路由绑定）
│   │   ├── styles/         # 样式文件
│   │   ├── lib/            # 前端工具函数
│   │   └── App.jsx         # 前端根组件
│   └── server/             # 后端代码（Node.js）
│       ├── queries/        # 数据查询函数（读操作）
│       ├── actions/        # 数据操作函数（写操作）
│       ├── lib/            # 后端工具函数
│       └── migrations/     # 数据库迁移文件（自动生成）
├── main.wasp               # 项目核心配置文件（必选）
├── package.json            # NPM 配置文件
└── .gitignore              # Git 忽略配置
```


### 五、关键注意事项
1. **`main.wasp` 是“配置中枢”**：所有核心资源（实体、查询、页面、路由）必须在 `main.wasp` 中定义，Wasp 才会识别并生成对应的前后端代码（如接口、路由映射）。  
2. **目录约定不可随意改**：`src/client/`、`src/server/queries/` 等核心目录的名称和位置是固定的，修改后 Wasp 无法识别（可选目录如 `src/shared/` 除外）。  
3. **迁移文件不可手动改**：`src/server/migrations/` 下的文件由 `wasp db migrate-dev` 自动生成，手动修改可能导致数据库结构不一致，如需调整，应修改 `main.wasp` 中的实体后重新生成迁移。

通过这种结构，Wasp 实现了“前后端代码分离但配置统一”，开发者只需专注于业务逻辑，无需关心工程化细节（如跨域、接口路由、数据库连接）。