https://www.bilibili.com/video/BV1WP411g7Kr/?vd_source=7038f96b6bb3b14743531b102b109c43
![[assets/img/AMIGOSCODE/IMG-AMIGOSCODE-20240714124655405.png]]
#### github项目地址 spring-data-jpa-course
![[assets/img/AMIGOSCODE/IMG-AMIGOSCODE-20240714124657891.png]]
![[assets/img/AMIGOSCODE/IMG-AMIGOSCODE-20240714124701019.png]]
![[assets/img/AMIGOSCODE/IMG-AMIGOSCODE-20240714124702443.png]]
 在Java的持久化框架中，如Hibernate，这些注解用于定义实体类（Entity）及其与数据库表的映射关系。下面是每个注解的作用：

1. `@Entity`：
   - 这个注解用于标识一个类是一个实体类，即它映射到数据库中的一个表。实体类通常包含业务逻辑和数据，并且可以被持久化到数据库中。

2. `@Table`：
   - `@Table` 注解用于指定实体类对应的数据库表的名称。如果没有指定，Hibernate会默认使用实体类的类名（首字母小写）作为表名。例如，如果实体类名为 `User`，没有指定 `@Table`，则默认表名为 `user`。

```java
   @Entity
   @Table(name = "users")
   public class User {
       // ...
   }
   ```

3. `@Id`：
   - `@Id` 注解用于标识实体类中的主键字段。主键是数据库表中唯一标识每条记录的字段。在实体类中，主键字段通常是一个自增的整数或者UUID。

```java
   public class User {
       @Id
       private Long id;
       // ...
   }
   ```

4. `@SequenceGenerator`：
   - `@SequenceGenerator` 注解用于指定实体类中某个字段（通常是主键）的值生成策略。在某些数据库中，如Oracle，主键值是通过序列（Sequence）生成的。这个注解允许你指定序列的名称、初始值、步长等属性。

```java
   public class User {
       @Id
       @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "user_seq")
       @SequenceGenerator(name = "user_seq", sequenceName = "user_sequence", initialValue = 1, allocationSize = 1)
       private Long id;
       // ...
   }
   ```

   在这个例子中，`user_seq` 是 `@SequenceGenerator` 注解的名称，`user_sequence` 是数据库中的序列名称，`initialValue` 是序列的初始值，`allocationSize` 是每次分配的值的数量。

这些注解共同工作，帮助Hibernate理解实体类的结构以及如何将其映射到数据库表。通过这些注解，你可以轻松地实现对象关系映射（ORM），而无需编写复杂的SQL语句。

 在Spring Data JPA中，`StudentRepository` 是一个自定义的接口，它继承自 `JpaRepository`。这个接口定义了一组方法，这些方法允许你对 `Student` 类型的实体进行操作，其中 `Student` 是实体类，`Long` 是该实体的主键类型。
![[assets/img/AMIGOSCODE/IMG-AMIGOSCODE-20240714124702538.png]]
`JpaRepository` 是Spring Data JPA提供的一个核心接口，它提供了许多常用的数据访问操作，如保存（save）、删除（delete）、查询（findAll、findById）等。当你创建一个继承自 `JpaRepository` 的接口时，Spring Data JPA会自动为你实现这个接口，这意味着你不需要编写任何实现代码，就可以使用这些方法。

下面是一个简单的例子，展示了如何使用 `StudentRepository`：

```java
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {
    // 自动实现的方法，如findAll()、findById(Long id)等
    // 如果需要自定义查询，可以在这里添加方法
    // @Query("SELECT s FROM Student s WHERE s.name = :name")
    // List<Student> findByName(String name);
}
```

在这个例子中，`StudentRepository` 接口没有定义任何方法，因为它继承了 `JpaRepository` 提供的所有方法。如果你需要执行特定的查询，你可以在这个接口中添加自定义的方法，并使用 `@Query` 注解来指定查询语句。

当你的Spring Boot应用程序启动时，Spring Data JPA会扫描所有的继承自 `JpaRepository` 的接口，并为它们创建实现。这样，你就可以通过依赖注入（DI）来获取 `StudentRepository` 的实例，并使用它来执行数据库操作。



[Spring Boot and Spring Security with JWT including Access and Refresh Tokens_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1N14y157vy/?spm_id_from=333.788.recommend_more_video.17&vd_source=7038f96b6bb3b14743531b102b109c43)
![[assets/img/AMIGOSCODE/IMG-AMIGOSCODE-20240714124703511.png]]
![[assets/img/AMIGOSCODE/IMG-AMIGOSCODE-20240714124703609.png]]
 在Java中，这些注解通常与Spring框架和Hibernate ORM（对象关系映射）一起使用，用于定义实体类和它们之间的关系。下面是每个注解的简要说明：

1. `@Entity`：
   这个注解来自JPA（Java Persistence API），用于标记一个类是实体类，即这个类映射到数据库中的一个表。实体类通常包含业务逻辑和持久化数据。

2. `@Data`：
   这是一个来自Lombok库的注解，它自动为类生成getter、setter、equals、hashCode和toString方法。这有助于减少样板代码，使开发者能够专注于业务逻辑。

3. `@NoArgsConstructor` 和 `@AllArgsConstructor`：
   这两个注解同样来自Lombok库。`@NoArgsConstructor` 生成无参构造函数，而 `@AllArgsConstructor` 生成包含所有字段的构造函数。这使得实体类更容易创建实例。

4. `@ManyToMany`：
   这个注解来自Hibernate，用于表示两个实体类之间的多对多关系。在数据库中，这种关系通常通过一个关联表（也称为连接表或中间表）来实现。在实体类中，使用 `@ManyToMany` 注解的字段应该是一个集合类型，如`Set`、`List`或`Collection`，并且这个集合的元素类型是另一个实体类。

下面是一个使用这些注解的简单示例：

```java
import javax.persistence.Entity;
import javax.persistence.ManyToMany;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import java.util.Set;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String username;
    private String password;

    @ManyToMany
    private Set<Role> roles;
}
```

在这个例子中，`User` 类表示用户实体，它与 `Role` 类之间存在多对多关系。`roles` 字段是一个 `Set<Role>` 类型的集合，表示一个用户可以有多个角色，同样，一个角色可以关联多个用户。在数据库中，这通常需要一个名为 `user_role` 的关联表来存储这种关系。

### Type Inference with Var
 在Java 10及更高版本中，引入了局部变量类型推断（Local Variable Type Inference）的特性，这允许开发者使用 `var` 关键字来声明局部变量，而不必显式指定变量的类型。编译器会根据变量的初始化表达式来推断其类型。这个特性旨在简化代码，减少冗余，并提高代码的可读性。

以下是 `var` 关键字的一些使用场景：

1. **局部变量声明**：
```java
   var list = new ArrayList<String>();
   ```

2. **增强型for循环**：
```java
   List<String> myList = Arrays.asList("a", "b", "c");
   for (var element : myList) {
       // ...
   }
   ```

3. **try-with-resources语句**：
```java
   try (var inputStream = new FileInputStream("file.txt")) {
       // ...
   }
   ```

4. **lambda表达式的参数类型推断**（从Java 11开始）：
```java
   BiFunction<Integer, Integer, Integer> add = (var a, var b) -> a + b;
   ```

需要注意的是，`var` 关键字并不是一个真正的关键字，而是一个保留类型名。这意味着它不能用作类名、接口名或方法名。此外，`var` 只能用于局部变量声明，不能用于成员变量、方法参数或返回类型。

使用 `var` 关键字时，开发者应该谨慎，因为它可能会影响代码的可读性。在某些情况下，显式类型声明可以提供额外的上下文信息，有助于理解代码的意图。因此，是否使用 `var` 应该基于代码的清晰度和团队的编码风格来决定。

## 包装类Wrapper Classes
 在Java中，包装类（Wrapper Classes）是一组特殊的类，它们为Java的基本数据类型（primitive data types）提供了对应的对象封装。这些包装类允许基本数据类型与对象类型之间进行无缝交互，尤其是在需要使用对象作为参数或返回值的场合。Java的基本数据类型及其对应的包装类如下：

1. **byte** - `Byte`
2. **short** - `Short`
3. **int** - `Integer`
4. **long** - `Long`
5. **float** - `Float`
6. **double** - `Double`
7. **char** - `Character`
8. **boolean** - `Boolean`

包装类的主要特点和用途包括：

- **自动装箱（Autoboxing）**：在Java 5及更高版本中，自动装箱允许自动将基本数据类型转换为其对应的包装类对象。例如，`int i = 10;` 会自动装箱为 `Integer i = Integer.valueOf(10);`。
- **自动拆箱（Unboxing）**：与自动装箱相反，自动拆箱允许自动将包装类对象转换回其对应的基本数据类型。例如，`int i = integer;`（假设 `integer` 是 `Integer` 类型的实例）会自动拆箱为 `int i = integer.intValue();`。
- **数值范围**：包装类提供了方法来获取和设置基本数据类型的最小值和最大值，例如 `Integer.MAX_VALUE` 和 `Integer.MIN_VALUE`。
- **数值操作**：包装类提供了一些数值操作的方法，如 `parseInt`、`parseFloat` 等，这些方法在处理字符串和数值转换时非常有用。
- **比较和相等性**：包装类提供了比较方法，如 `compareTo`，以及 `equals` 方法，这些方法在比较对象时考虑了数值相等性，而不是对象引用的相等性。
- **格式化**：包装类提供了格式化方法，如 `Integer.toString(int i)` 和 `Integer.toHexString(int i)`，用于将数值转换为字符串表示。

包装类在Java编程中非常有用，尤其是在需要使用集合（如 `List`、`Map`）时，因为集合只能存储对象，而不能直接存储基本数据类型。通过包装类，你可以将基本数据类型转换为对象，从而满足集合的存储要求。

 在Java 8中，`LocalDate`、`LocalTime`和`LocalDateTime`是处理日期和时间的三个主要类。它们提供了创建特定日期和时间的多种方法。以下是如何使用这些类来创建特定日期和时间的示例：

### LocalDate（日期）

`LocalDate`类用于表示日期，不包含时间信息。

创建当前日期：
```java
LocalDate today = LocalDate.now();
```

创建特定日期（年、月、日）：
```java
LocalDate specificDate = LocalDate.of(2023, Month.MARCH, 15); // 2023年3月15日
```

### LocalTime（时间）

`LocalTime`类用于表示时间，不包含日期信息。

创建当前时间：
```java
LocalTime currentTime = LocalTime.now();
```

创建特定时间（时、分、秒）：
```java
LocalTime specificTime = LocalTime.of(15, 30, 45); // 下午3点30分45秒
```

### LocalDateTime（日期和时间）

`LocalDateTime`类结合了日期和时间，表示一个特定的日期和时间。

创建当前日期和时间：
```java
LocalDateTime now = LocalDateTime.now();
```

创建特定日期和时间：
```java
LocalDateTime dateTime = LocalDateTime.of(2023, Month.MARCH, 15, 15, 30, 45); // 2023年3月15日下午3点30分45秒
```

### 格式化和解析

你可以使用`DateTimeFormatter`类来格式化和解析日期和时间字符串。

格式化日期和时间：
```java
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
String formattedDateTime = dateTime.format(formatter);
```

解析日期和时间字符串：
```java
LocalDateTime parsedDateTime = LocalDateTime.parse("2023-03-15T15:30:45", formatter);
```

### 注意事项

- `LocalDate`、`LocalTime`和`LocalDateTime`都是不可变的，这意味着一旦创建，它们的值就不能被改变。任何修改操作都会返回一个新的对象。
- 默认情况下，这些类使用的是系统默认时区。如果你需要处理特定时区的日期和时间，你可以使用`ZoneId`类来指定时区。
- 在处理日期和时间时，建议使用`DateTimeFormatter`来确保格式的一致性和正确性。

这些类提供了丰富的方法来处理日期和时间，使得在Java 8中处理日期和时间变得更加简单和直观。


## 流式数据处理
 在Java中，流式数据处理（Stream Processing）是一种编程范式，它允许开发者以声明式的方式处理数据流，而不是使用传统的命令式编程。这种范式在Java 8中得到了显著增强，引入了Stream API，它提供了一种高效、简洁的方式来处理集合（如List、Set、Map等）以及数组。

流式数据处理的主要特点包括：

1. **声明式编程**：开发者可以专注于描述“做什么”，而不是“怎么做”。这使得代码更加简洁、易读。

2. **惰性执行**：流操作（中间操作）不会立即执行，只有在调用终止操作（如collect、forEach等）时，流才会被实际处理。

3. **并行处理**：Stream API支持并行流（Parallel Stream），可以利用多核处理器的优势，提高数据处理效率。

4. **函数式接口**：Stream API大量使用了函数式接口（如Predicate、Function、Consumer等），这些接口通过Lambda表达式实现，使得代码更加灵活。

5. **链式调用**：流操作可以链式调用，形成数据处理的管道，这使得复杂的数据处理逻辑可以以一种流式的方式表达。

6. **不可变**：流是不可变的，这意味着在流操作过程中，原始数据不会被修改。

流式数据处理的基本步骤通常包括：

- **创建流**：从数据源（如集合、数组）创建流。
- **中间操作**：对流进行一系列操作，如过滤（filter）、映射（map）、排序（sorted）等。
- **终止操作**：执行终止操作，如收集（collect）、计数（count）、找到第一个元素（findFirst）等，这会触发流的执行并产生结果。

以下是一个简单的流式数据处理示例：

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class StreamExample {
    public static void main(String[] args) {
        List<String> words = Arrays.asList("apple", "banana", "cherry", "date");

        // 创建流
        List<String> filteredWords = words.stream()
                // 中间操作：过滤长度大于4的单词
                .filter(word -> word.length() > 4)
                // 中间操作：转换为大写
                .map(String::toUpperCase)
                // 终止操作：收集结果为列表
                .collect(Collectors.toList());

        System.out.println(filteredWords); // 输出: [BANANA, CHERRY, DATE]
    }
}
```

在这个例子中，我们首先从列表创建了一个流，然后通过链式调用进行了过滤和映射操作，最后通过`collect`方法收集结果。这种流式处理方式使得代码更加简洁和易于理解。

## Spring框架代码组织
[Java Master Class | Amigoscode](https://www.amigoscode.com/courses/java-master-class)
![[assets/img/AMIGOSCODE/IMG-AMIGOSCODE-20240714124704203.png]]

 在软件开发中，组织代码以提高可维护性、可扩展性和可重用性是非常重要的。N层架构（N-tier Architecture）是一种常见的设计模式，它将应用程序分为多个逻辑层，每一层负责特定的功能。这种架构通常包括以下几层：

1. **表示层（Presentation Layer）**：
   - 负责与用户交互，展示数据和接收用户输入。
   - 通常包括前端框架（如Angular, React, Vue.js）和后端控制器（如Spring MVC的Controller）。

2. **业务逻辑层（Business Logic Layer）**：
   - 包含服务类（Service Classes），处理业务规则和业务流程。
   - 服务类通常调用数据访问对象（DAO）来获取或更新数据。

3. **数据访问层（Data Access Layer）**：
   - 数据访问对象（DAO）负责与数据库交互，执行CRUD（创建、读取、更新、删除）操作。
   - DAO通常使用ORM框架（如Hibernate, JPA）来简化数据库操作。

4. **数据持久层（Data Persistence Layer）**：
   - 包含数据库和实体类（Models），实体类映射数据库表，表示数据模型。
   - 数据库可以是关系型（如MySQL, PostgreSQL）或非关系型（如MongoDB）。

5. **基础设施层（Infrastructure Layer）**：
   - 提供通用功能，如日志记录、安全性、配置管理等。
   - 通常包括工具类（Utility Classes）和框架提供的组件。

在N层架构中，连接DAO和Service层的关键在于定义清晰的接口和契约。以下是一些建议：

- **接口定义**：为DAO定义接口，Service层通过这些接口与DAO交互。这有助于解耦，使得Service层不直接依赖于DAO的具体实现。

- **依赖注入**：使用依赖注入（如Spring的@Autowired）来管理Service层对DAO的依赖。这样可以在不修改Service层代码的情况下，更换DAO的实现。

- **数据传输对象（DTO）**：在Service层和DAO层之间传递数据时，使用DTO来封装数据。这有助于保持数据的一致性和封装性。

- **异常处理**：在Service层处理DAO层抛出的异常，并将其转换为业务相关的异常，以便在表示层进行适当的处理。

- **事务管理**：确保在执行数据库操作时，事务得到正确管理。可以使用Spring的@Transactional注解来声明事务。

以下是一个简化的示例，展示了如何在Spring框架中实现这些概念：

```java
// DAO接口
public interface UserRepository {
    User findById(int id);
    // 其他DAO方法
}

// DAO实现
@Repository
public class UserRepositoryImpl implements UserRepository {
    // 使用JPA或JDBC实现数据库操作
}

// Service类
@Service
public class UserService {
    @Autowired
    private UserRepository userRepository;

    public User getUser(int id) {
        return userRepository.findById(id);
    }
    // 其他业务逻辑方法
}

// 控制器
@RestController
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping("/users/{id}")
    public ResponseEntity<User> getUser(@PathVariable int id) {
        User user = userService.getUser(id);
        if (user == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(user);
    }
    // 其他控制器方法
}
```

在这个例子中，`UserService`依赖于`UserRepository`，但通过接口进行交互。这样，如果需要更换DAO的实现，只需在Spring配置中注入新的实现即可。同时，`UserController`通过`UserService`与数据库交互，实现了业务逻辑与表示层的分离。
### 依赖注入 Dependency Injection
 Dependency Injection (DI) 是一种设计模式，它允许你将组件之间的依赖关系通过外部注入的方式进行管理，而不是在组件内部创建依赖。这样做的好处包括提高代码的可测试性、可维护性和可扩展性。以下是关于DI的一些关键概念和实践：
![[assets/img/AMIGOSCODE/IMG-AMIGOSCODE-20240714124704974.png]]


1. **Don't Do This (避免这样做)**：
   - 避免在组件内部直接创建依赖对象。例如，不要在类中直接实例化其他类，这会导致紧耦合。

2. **Dependency Injection (依赖注入)**：
   - DI的核心思想是将依赖对象的创建和管理交给容器（如Spring框架的ApplicationContext）来处理。容器在组件需要时提供所需的依赖。

3. **Dependency Injection In Action (依赖注入实践)**：
   - 在Spring框架中，你可以使用`@Autowired`或`@Inject`注解来实现依赖注入。这些注解告诉Spring容器在组件初始化时注入所需的依赖。

4. **Singletons and @Inject/@Autowire (单例和注入注解)**：
   - `@Singleton`注解（在CDI如Guice中）或Spring的`@Scope("singleton")`注解用于确保一个类只有一个实例。`@Autowired`和`@Inject`注解用于在组件中注入依赖。

5. **CLI Project Exercise (CLI项目练习)**：
   - 创建一个简单的CLI项目，使用DI来管理组件之间的依赖关系。例如，你可以创建一个命令行工具，用于处理文本文件，其中包含一个解析器组件和一个报告生成器组件。解析器负责解析文件内容，报告生成器负责生成报告。这两个组件应该通过DI进行注入，而不是在代码中直接创建。

以下是一个简化的Spring CLI项目示例，展示了如何使用依赖注入：

```java
// Service类，依赖于Parser和Reporter
@Service
public class TextProcessorService {
    @Autowired
    private Parser parser;
    @Autowired
    private Reporter reporter;

    public void processFile(String filePath) {
        Data data = parser.parse(filePath);
        reporter.generateReport(data);
    }
}

// Parser类，负责解析文件
@Component
public class Parser {
    public Data parse(String filePath) {
        // 解析文件并返回Data对象
        return new Data();
    }
}

// Reporter类，负责生成报告
@Component
public class Reporter {
    public void generateReport(Data data) {
        // 生成报告
    }
}

// 主类，包含main方法
public class TextProcessorApp {
    public static void main(String[] args) {
        ApplicationContext context = new AnnotationConfigApplicationContext(TextProcessorApp.class);
        TextProcessorService service = context.getBean(TextProcessorService.class);
        service.processFile("path/to/file.txt");
    }
}
```

在这个例子中，`TextProcessorService`依赖于`Parser`和`Reporter`。Spring容器负责创建这些依赖并注入到`TextProcessorService`中。这样，`TextProcessorService`的实现不需要关心如何创建这些依赖，只需要关注业务逻辑。

通过这个练习，你可以更好地理解DI的概念，并学会如何在实际项目中应用它。

继续更新
[Java Master Class | Amigoscode](https://www.amigoscode.com/courses/java-master-class)
![[assets/img/AMIGOSCODE/IMG-AMIGOSCODE-20240714124705538.png]]


![[后续要跟的课程]]

