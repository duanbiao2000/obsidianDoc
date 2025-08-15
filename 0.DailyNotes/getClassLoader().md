

```java
InputStream in = this.getClass().getClassLoader().getResourceAsStream("user.txt");
```

其实是对 Java 原生文件读取方式的一种**简化和封装**，它主要简化了以下两方面：

---

## 🧱 简化了的原生方式

### ✅ 原生方式一：使用绝对路径读取文件

```java
File file = new File("src/main/resources/user.txt");
InputStream in = new FileInputStream(file);
```

- 缺点：
  - 依赖文件系统路径，**不适用于 JAR 包运行环境**
  - 不具备跨平台性和可移植性

---

### ✅ 原生方式二：使用 `Class.getResourceAsStream()`

```java
InputStream in = this.getClass().getResourceAsStream("/user.txt");
```

- `/` 表示从 classpath 根目录开始查找
- 支持 JAR 包内资源读取
- 但路径规则稍复杂（相对路径 vs 绝对路径）

---

## 🔍 `getClassLoader().getResourceAsStream()` 的优势

```java
InputStream in = this.getClass().getClassLoader().getResourceAsStream("user.txt");
```

- **路径统一**：始终从 classpath 根目录查找（不支持 `/` 开头）
- **适配 JAR 包**：可直接读取打包进 JAR 的资源
- **跨平台**：不依赖操作系统文件路径
- **简洁安全**：避免硬编码路径和文件不存在异常

---

## 🧠 总结对比

| 方式 | 是否支持 JAR 包 | 是否依赖文件系统 | 路径规则 | 推荐程度 |
|------|------------------|------------------|-----------|-----------|
| `new FileInputStream()` | ❌ 否 | ✅ 是 | 操作系统路径 | ❌ 不推荐 |
| `getClass().getResourceAsStream()` | ✅ 是 | ❌ 否 | 支持 `/` 表示 classpath 根 | ✅ 推荐 |
| `getClass().getClassLoader().getResourceAsStream()` | ✅ 是 | ❌ 否 | 相对 classpath 根目录，不支持 `/` | ✅✅ 强烈推荐 |

---

## 📚 延伸阅读

- [CSDN：Java资源加载详解](https://blog.csdn.net/2201_75813105/article/details/146285486)
- [腾讯云：一文理解 getClassLoader().getResourceAsStream()](https://cloud.tencent.com/developer/article/2038066)

---

如果你正在开发 Spring Boot 或 Jakarta EE 项目，这种方式非常适合加载配置文件、模板、静态资源等。想不想我帮你封装一个资源加载工具类，支持读取文本、图片、JSON 等格式？