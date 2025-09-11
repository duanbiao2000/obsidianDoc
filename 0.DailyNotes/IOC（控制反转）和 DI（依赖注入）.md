
### [[IOC（控制反-转）和 DI（依赖注入）- 团队最佳实践版]]

这份文档是我们团队关于 **IoC（控制反转）** 和 **DI（依赖注入）** 的官方实践指南。它旨在统一我们的认知，并将其作为代码审查（Code Review）和日常开发的基础。

---

### 🧠 核心概念：什么是 IoC（控制反转）？

**IoC（Inversion of Control）** 是一种核心设计原则，其目的是**降低代码耦合度**。它将对象的创建和依赖关系的管理权从我们的业务代码中“反转”出去，交由一个独立的容器（如 Spring IoC 容器）来负责。

*   **传统方式 (高耦合)**:
    ```java
    // 我们自己控制对象的创建，UserService 强依赖 UserServiceImpl
    UserService userService = new UserServiceImpl();
    ```

*   **IoC 方式 (低耦合)**:
    ```java
    // 我们只声明需要什么，容器会提供给我们
    @Autowired
    private UserService userService;
    ```
    通过 IoC，我们的组件不再关心依赖的具体实现，只关心接口。这直接践行了 **SOLID** 设计原则中的 **D（依赖倒置原则）**。

---

### 💉 核心实现：什么是 DI（依赖注入）？

**DI（Dependency Injection）** 是实现 IoC 的最常见方式。容器在创建对象时，会主动将其所依赖的其他对象“注入”给它。

#### 团队注入方式标准

为了代码的一致性、可维护性和可测试性，我们团队约定了以下注入方式的优先级：

| 注入方式 | 示例 | 团队准则 |
|---|---|---|
| **构造器注入** | `@Autowired public UserService(UserDao dao)` | **🥇 首选推荐**。它能保证依赖在对象创建时就已完备，清晰暴露类的必要依赖，非常利于编写单元测试。 |
| **Setter 注入** | `@Autowired public void setUserDao(UserDao dao)` | **🥈 可选使用**。适用于那些非必需、可变的依赖。 |
| **字段注入** | `@Autowired private UserDao dao;` | **🥉 避免使用**。虽然简洁，但它隐藏了类的依赖关系，且不利于进行单元测试。 |

---

### ✅ 为什么我们坚持使用 IoC/DI？

| 优点 | 在我们团队的意义 |
|---|---|
| **解耦** | 降低模块间的耦合，修改一个模块的实现不会影响到调用方，**减少技术债**。 |
| **易于测试** | 我们可以轻松地将真实依赖替换为 Mock 对象，这是**实现高质量单元测试**和自动化测试的关键。 |
| **提升效率** | 遵循约定，减少了创建和管理对象的样板代码，让开发者更专注于业务逻辑。 |
| **代码更清晰** | 通过构造器，类的依赖关系一目了然，提升了代码的可读性和可维护性。 |

---

### 🚀 提升可测试性：一个实战示例

IoC/DI 最大的优势之一就是让单元测试变得简单。

**1. 使用构造器注入的业务代码：**

```java
@Service
public class UserService {
    private final UserDao userDao;

    @Autowired // Spring 4.3+ 之后，如果只有一个构造函数，此注解可省略
    public UserService(UserDao userDao) {
        this.userDao = userDao;
    }

    public void saveUser() {
        userDao.save();
    }
}
```

**2. 对应的单元测试 (使用 Mockito 框架):**

```java
// 在测试代码中
@Test
void testSaveUser() {
    // 1. 创建一个 Mock 的 UserDao 对象
    UserDao mockDao = Mockito.mock(UserDao.class);

    // 2. 通过构造器将 Mock 对象注入
    UserService userService = new UserService(mockDao);

    // 3. 调用被测试的方法
    userService.saveUser();

    // 4. 验证 Mock 对象的 save() 方法是否被调用了 1 次
    Mockito.verify(mockDao, Mockito.times(1)).save();
}
```
这个例子直观地展示了 DI 如何帮助我们隔离依赖，从而实现快速、可靠的单元测试。

---

### 融入我们的敏捷工作流

为了将这一最佳实践融入日常工作，我们约定：

1.  **代码审查 (Code Review) 检查点**:
    *   是否优先使用了**构造器注入**？
    *   代码中是否存在不必要的 `new` 关键字来创建业务依赖？

2.  **完成的定义 (Definition of Done)**:
    *   一个用户故事或任务的完成，应包含“**新的业务逻辑遵循了 DI 原则，并拥有相应的单元测试覆盖**”这一条。

3.  **回顾会议 (Retrospective) 素材**:
    *   当遇到因代码耦合导致的问题时，我们可以回顾此文档，讨论如何通过更好的 DI 实践来避免未来再次发生。

---

### 📚 学习资源

*   视频教程：[B站：IOC 与 DI 入门讲解](https://www.bilibili.com/video/BV1yGydYEE3H?p=48)
*   图文教程：[博客园：Spring 的 IOC 和 DI 入门](https://www.cnblogs.com/moutory/p/17752747.html)