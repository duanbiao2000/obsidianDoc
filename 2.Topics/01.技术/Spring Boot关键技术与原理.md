### 一、 启动流程 (`SpringApplication.run()`)

`SpringApplication.run()` 是Spring Boot应用的入口，它封装了复杂的初始化过程。

**核心步骤**:
1.  **创建 `SpringApplication` 实例**: 这是启动流程的上下文管理器，在此阶段会加载 `META-INF/spring.factories` 中定义的 `ApplicationContextInitializer` 和 `ApplicationListener`。
2.  **准备 `Environment`**: 创建并配置环境对象，加载所有配置源（如 `application.yml`、环境变量、命令行参数），并根据优先级进行合并。
3.  **创建 `ApplicationContext` (IoC容器)**: 根据应用类型（Web或非Web）选择合适的容器实现，如 `AnnotationConfigServletWebServerApplicationContext`。
4.  **刷新 `ApplicationContext` (`refresh Context`)**: 这是最核心的步骤，包括：
    - **扫描Bean定义**: 查找 `@Component`, `@Configuration` 等注解。
    - **实例化单例Bean**: 创建Bean实例并处理依赖注入 (`Dependency Injection`)。
    - **启动内嵌Web服务器**: 如Tomcat, Jetty等。
5.  **启动后处理**: 调用 `CommandLineRunner` 和 `ApplicationRunner`，并发布 `ApplicationReadyEvent` 事件，标志着应用已准备好处理请求。

---

### 二、 自动配置 (`Auto-Configuration`)

自动配置是Spring Boot的“魔法”核心，它遵循“约定大于配置” (`Convention over Configuration`) 的原则。

**工作原理**:
1.  **`@EnableAutoConfiguration`**: `@SpringBootApplication` 注解中包含了此注解，它是自动配置的总开关。
2.  **`spring.factories`**: Spring Boot在启动时会扫描所有 `starter` 依赖包中的 `META-INF/spring.factories` 文件。
3.  **加载配置类**: `spring.factories` 中列出了大量的 `*AutoConfiguration` 类。
4.  **条件注解 (`Conditional Annotations`)**: 每个自动配置类都使用了条件注解（如 `@ConditionalOnClass`, `@ConditionalOnBean`, `@ConditionalOnProperty`）来判断是否应该生效。例如，只有当类路径下存在 `Tomcat` 类时，`TomcatServletWebServerFactoryAutoConfiguration` 才会生效。

---

### 三、 `Starters`: 依赖管理的“便利贴”

`Starters` 是一组预先配置好的依赖描述符，极大地简化了Maven/Gradle的依赖管理。

- **作用**: 当你引入一个 `starter` (如 `spring-boot-starter-web`)，它会自动传递性地引入构建特定类型应用所需的所有常用依赖（如 `spring-webmvc`, `spring-boot-starter-tomcat`, `spring-boot-starter-json`）。
- **好处**: 避免了手动添加大量依赖和处理版本兼容性问题的麻烦。

---

### 四、 配置管理 (`Configuration Management`)

Spring Boot提供了灵活且强大的配置管理机制。

- **配置源优先级**: Spring Boot会从多个位置加载配置，并按严格的优先级顺序进行覆盖（高优先级覆盖低优先级）。常见顺序如下：
    1.  命令行参数 (`--server.port=9090`)
    2.  操作系统环境变量
    3.  `application-{profile}.yml` (Profile特定配置)
    4.  `application.yml` (应用默认配置)
- **配置绑定 (`Configuration Binding`)**:
    - **`@Value("${property.key}")`**: 注入单个配置值。
    - **`@ConfigurationProperties(prefix = "...")`**: 将一组具有相同前缀的配置项结构化地绑定到一个Java对象上，提供类型安全的配置。

---

### 五、 `Actuator`: 应用的“仪表盘”

`Actuator` 提供了生产级的监控和管理端点 (`endpoints`)，用于洞察应用内部状态。

- **核心端点**:
    - `/health`: 应用健康状况。
    - `/metrics`: 详细的性能指标 (JVM内存、CPU、HTTP请求等)。
    - `/env`: 当前环境中的所有配置属性。
    - `/beans`: 容器中所有Bean的列表。
    - `/configprops`: 所有 `@ConfigurationProperties` Bean的配置信息。
- **集成**: 通常与 `Micrometer` (指标门面) 结合，将指标暴露给 `Prometheus` 等监控系统，再由 `Grafana` 进行可视化。