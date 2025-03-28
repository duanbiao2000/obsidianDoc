---
aliases: null
categories: null
high_priority: false
updateAt: 2025-03-28 00:24
---

在 MyBatis 中，`Mapper` 接口和 `XML` 映射文件通常是配合使用的，而不是二选一的关系。虽然理论上你可以只使用其中一种方式来定义 SQL 映射，但实际上，结合使用 `Mapper` 接口和 `XML` 映射文件可以提供更多的灵活性和可维护性。

### 为什么通常结合使用

1. **SQL 复杂度**：
   - 当 SQL 语句变得复杂时，使用 XML 文件来编写 SQL 语句更加直观，尤其是在需要动态 SQL（如 `<if>`、`<choose>`、`<foreach>` 等标签）的情况下。

2. **结果映射**：
   - 复杂的结果映射（如嵌套查询、延迟加载等）在 XML 文件中定义更为方便。

3. **可读性和可维护性**：
   - 将 SQL 语句与 Java 代码分离，使得 SQL 语句更加清晰易读，也方便维护和管理。

4. **版本控制**：
   - 将 SQL 语句存储在外部 XML 文件中，可以方便地进行版本控制，特别是在多人协作的环境中。

### 如何结合使用

在实际开发中，通常是这样结合使用的：

1. **定义 Mapper 接口**：
   - 在 Java 代码中定义一个 `Mapper` 接口，声明需要执行的方法及其返回类型。

2. **编写 XML 映射文件**：
   - 在 XML 文件中定义具体的 SQL 语句及其映射规则。

### 示例

#### 1. Mapper 接口

```java
package com.example.mapper;

import com.example.entity.User;
import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface UserMapper {

    @SelectProvider(type = SqlProvider.class, method = "findByUserId")
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

#### 2. XML 映射文件

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

### 动态 SQL 的例子

在 XML 文件中定义动态 SQL 语句，可以使用 `<if>`、`<choose>`、`<when>`、`<otherwise>`、`<foreach>` 等标签来构造动态 SQL：

```xml
<select id="findUsersByName" parameterType="java.lang.String" resultType="com.example.entity.User">
    SELECT * FROM users WHERE 1=1
    <if test="name != null and name.trim() != ''">
        AND name LIKE concat('%', #{name}, '%')
    </if>
</select>
```

### 总结

虽然你可以选择只使用 `Mapper` 接口或者只使用 `XML` 映射文件来定义 SQL 映射，**但结合使用这两种方式通常会更加灵活和强大。** 这样可以让你的代码更加清晰、易于维护，并且能够处理更复杂的查询和映射逻辑。**在大多数情况下，结合使用 `Mapper` 接口和 `XML` 映射文件是最佳实践。** 如果你的应用只需要简单的 CRUD 操作，并且 SQL 语句非常简单，那么也可以考虑仅使用 `Mapper` 接口来定义 SQL 语句。
