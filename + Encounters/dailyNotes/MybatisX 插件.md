---
aliases: 
categories: 
high_priority: false
tags:
  - Effective/VibeCode
  - Effective/Tools
---
#  MybatisX 插件生成对应的实体类、Mapper 接口及 XML 映射文件

## 步骤  #Mindset/FCPM/PK 
### 准备工作

确保你已经安装了 IntelliJ IDEA，并且安装了 MybatisX 插件。另外，确保你的数据库连接已经配置好，并且设计好了相应的数据库表。

### 生成代码

#### 1. 生成实体类（Entity）

假设你的数据库表名为 `users`，并且你想要生成对应的实体类 `User`。

1. **打开数据库连接**：
   - 在 IntelliJ IDEA 中，通过 `Database` 视图打开数据库连接。
   - 导航到 `users` 表。

2. **右键选择生成**：
   - 右键点击 `users` 表，选择 `Generate...`，然后选择 `Mapper & Entity` 或 `Entity`。

3. **配置生成选项**：
   - 在弹出的对话框中，选择生成的实体类的存放位置。
   - 设置命名规则（例如，表名转换为类名时是否使用首字母大写等）。

#### 2. 生成 Mapper 接口

1. **右键选择生成**：
   - 再次右键点击 `users` 表，选择 `Generate...`，然后选择 `Mapper` 或 `Mapper & Entity`（如果之前没有一起生成）。

2. **配置生成选项**：
   - 在弹出的对话框中，选择 Mapper 接口的存放位置。
   - 设置命名规则（例如，接口名是否使用表名加上 `Mapper` 后缀）。

#### 3. 生成 XML 映射文件

1. **右键选择生成**：
   - 再次右键点击 `users` 表，选择 `Generate...`，然后选择 `Mapper XML`。

2. **配置生成选项**：
   - 在弹出的对话框中，选择 XML 映射文件的存放位置。
   - 设置命名规则（例如，XML 文件名是否使用表名加上 `.xml` 后缀）。

### 示例代码

#### 实体类（Entity）

假设生成的 `User` 实体类如下所示：

```java
package com.example.entity;

import lombok.Data;

@Data
public class User {
    private Long id;
    private String username;
    private String password;
    private String email;
    // ... 其他字段
}
```

#### Mapper 接口

假设生成的 `UserMapper` 接口如下所示：

```java
package com.example.mapper;

import com.example.entity.User;
import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface UserMapper {

    @Select("SELECT * FROM users WHERE id = #{id}")
    User findById(Long id);

    @Insert("INSERT INTO users(username, password, email) VALUES(#{username}, #{password}, #{email})")
    @Options(useGeneratedKeys = true, keyProperty = "id")
    void insert(User user);

    @Update("UPDATE users SET username=#{username}, password=#{password}, email=#{email} WHERE id=#{id}")
    void update(User user);

    @Delete("DELETE FROM users WHERE id=#{id}")
    void deleteById(Long id);

    @Select("SELECT * FROM users")
    List<User> findAll();
}
```

#### XML 映射文件

假设生成的 `UserMapper.xml` 文件如下所示：

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="com.example.mapper.UserMapper">

    <resultMap id="UserResultMap" type="com.example.entity.User">
        <id property="id" column="id"/>
        <result property="username" column="username"/>
        <result property="password" column="password"/>
        <result property="email" column="email"/>
        <!-- ... 其他字段 -->
    </resultMap>

    <select id="findById" resultMap="UserResultMap">
        SELECT * FROM users WHERE id = #{id}
    </select>

    <insert id="insert" useGeneratedKeys="true" keyProperty="id">
        INSERT INTO users(username, password, email)
        VALUES(#{username}, #{password}, #{email})
    </insert>

    <update id="update">
        UPDATE users
        SET username=#{username}, password=#{password}, email=#{email}
        WHERE id=#{id}
    </update>

    <delete id="deleteById">
        DELETE FROM users WHERE id=#{id}
    </delete>

    <select id="findAll" resultMap="UserResultMap">
        SELECT * FROM users
    </select>

</mapper>
```

### 配置 Spring Boot 应用

为了确保这些生成的代码可以正常工作，还需要在 Spring Boot 应用中进行相应的配置。

#### Spring Boot 配置

在 `pom.xml` 文件中添加 MyBatis 和 Spring Boot Starter 相关依赖：

```xml
<dependencies>
    <dependency>
        <groupId>org.mybatis.spring.boot</groupId>
        <artifactId>mybatis-spring-boot-starter</artifactId>
        <version>2.1.4</version>
    </dependency>
    <!-- MySQL 数据库驱动 -->
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <scope>runtime</scope>
    </dependency>
    <!-- Spring Boot Starter JDBC -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-jdbc</artifactId>
    </dependency>
    <!-- Spring Boot Starter Web -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

在 `application.properties` 或 `application.yml` 文件中配置数据库连接：

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/yourdb
spring.datasource.username=root
spring.datasource.password=yourpassword
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
```

在 `application.properties` 或 `application.yml` 文件中配置 MyBatis：

```properties
mybatis.mapper-locations=classpath:mapper/*.xml
mybatis.type-aliases-package=com.example.entity
```

通过上述步骤，你可以使用 IntelliJ IDEA 的 MybatisX 插件自动生成 MyBatis 相关的实体类、Mapper 接口和 XML 映射文件，并在 Spring Boot 应用中进行配置。如果你有任何其他问题或需要进一步的帮助，请随时告知。