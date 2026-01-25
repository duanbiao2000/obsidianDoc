---
view-count: 2
tags:
  - tdd-driven-design
  - interface-design
  - software-engineering
  - system-design
  - Domain/Technology/Go
  - Type/Reference
  - tdd-driven-design
  - interface-design
  - software-engineering
  - system-design
---
## TDD 驱动的设计演进**

TDD 的魔力在于，**为了让代码变得可测试，你被迫进行优秀的设计**。

##### **第一步：编写测试，驱动出接口与领域模型**

我们先为 `CreateUser` 编写测试。但问题来了：如何不依赖数据库来测试它？答案是：**抽象**。

```go
// good_design/user_service_test.go
package userservice_test

// 1. 定义 Mock，这会“驱动”我们去定义一个接口
type mockUserRepository struct {
    // ...
}

func (m *mockUserRepository) Create(user good_design.User) error { /* ... */ }
func (m *mockUserRepository) GetByEmail(email string) (good_design.User, error) { /* ... */ }

func TestUserService_CreateUser_Success(t *testing.T) {
    // Arrange: 准备 Mock 和 Service
    repo := &mockUserRepository{ /* ... */ }
    // 依赖注入：Service 通过构造函数接收依赖
    service := good_design.NewUserService(repo) 
    
    // Act
    err := service.CreateUser("Alice", "alice@example.com")
    
    // Assert
    // ... 验证 repo.Create 是否被正确调用
}
```

**设计决策的产生:**
*   **接口抽象 (`UserRepository`)**: 为了使用 `mockUserRepository`，我们必须定义一个 `UserRepository` 接口，`UserService` 只能依赖这个接口。**耦合被解除了**。
*   **领域模型 (`User`)**: 为了在接口中传递数据，我们定义了一个强类型的 `User` 结构体，取代了不安全的 `map`。**内聚性提高了**。
*   **依赖注入 (`NewUserService`)**: 为了在测试中传入 Mock，我们必须通过构造函数注入依赖。**控制反转实现了**。

##### **第二步：根据测试完善设计**

测试驱动我们分离了业务逻辑和数据访问，最终的设计如下：

```go
// good_design/user.go (领域模型层)
package userservice

// User 模型: 承载业务数据和验证逻辑，高内聚
type User struct { /* ID, Name, Email */ }
func (u *User) Validate() error { /* ... */ }

// UserRepository 接口: 定义数据访问契约，低耦合
type UserRepository interface {
    Create(user User) error
    GetByEmail(email string) (User, error)
}
```

```go
// good_design/user_service.go (业务逻辑层)
package userservice

// UserService: 只关心业务流程，不关心数据如何存储
type UserService struct {
    repo UserRepository // 依赖接口，而非具体实现
}

func NewUserService(repo UserRepository) *UserService { /* ... */ }

func (s *UserService) CreateUser(name, email string) error {
    user := User{Name: name, Email: email}
    if err := user.Validate(); err != nil {
        return err // 业务验证
    }
    // ... 检查邮箱是否重复等业务逻辑 ...
    return s.repo.Create(user) // 调用仓储层
}
```

```go
// good_design/mysql_repository.go (数据访问层)
package userservice

// MySQLUserRepository: UserRepository 接口的具体实现
type MySQLUserRepository struct {
    db *sql.DB
}

func (r *MySQLUserRepository) Create(user User) error {
    // ... 执行 SQL ...
}
```

---

#### **3. 设计改进总结：从架构图看演进**

**无 TDD 的设计：**
```
UserService
└── *sql.DB (具体实现)
```
*   **特点**: 耦合、僵化、难以测试。

**TDD 驱动的设计：**
```
UserService (业务层)
└── UserRepository (接口)
    └── MySQLUserRepository (实现层)

User (领域模型)
```
*   **特点**: **分层清晰、依赖倒置、职责单一**。`UserService` 现在可以独立测试，并且 `UserRepository` 可以轻松地替换为其他实现（如内存、Redis），系统灵活性和可维护性大大增强。

---
