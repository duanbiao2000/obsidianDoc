## Spring注解
![[assets/img/Spring Boot/IMG-Spring Boot-20240714124655322.png]]
 好的，让我们根据您提供的图片，结合 React 前端和 Spring Boot 后端，构建一个完整的全栈应用。

**1. 理解图片架构**

图片展示了一个典型的全栈 Web 应用架构：

- **客户端 (Client):** 使用 React 构建，负责用户界面和交互。
- **API 层 (API Layer):** 后端提供 RESTful API，处理 HTTP 请求 (GET, POST, PUT, DELETE)。
- **服务层 (Service Layer):** 处理业务逻辑，调用数据访问层。
- **数据访问层 (Data Access Layer):** 与数据库交互，执行 CRUD 操作。
- **后端 (Backend):** 使用 Spring Boot 构建，包含 API 层、服务层和数据访问层。
- **数据库:** 用于存储数据。
- **实体 (Student, Class):** 表示应用中的数据模型。

**2. Spring Boot 后端**

- **项目结构:**

```
   src/
   ├── main/
   │   ├── java/
   │   │   └── com/example/
   │   │       ├── controller/
   │   │       │   └── StudentController.java
   │   │       ├── service/
   │   │       │   └── StudentService.java
   │   │       ├── repository/
   │   │       │   └── StudentRepository.java
   │   │       ├── entity/
   │   │       │   ├── Student.java
   │   │       │   └── Class.java
   │   │       └── Application.java
   │   └── resources/
   │       └── application.properties
   └── test/
       └── ...
```

- **实体类 (Student.java, Class.java):**

Java

```java
   // Student.java
   import javax.persistence.*;
   @Entity
   public class Student {
       @Id
       @GeneratedValue(strategy = GenerationType.IDENTITY)
       private Long id;
       private String name;
       private String email;
       private String dob; // Date of birth
       private int age;
       @ManyToOne
       private Class studentClass;
       // Getters and setters...
   }
   // Class.java
   import javax.persistence.*;
   @Entity
   public class Class {
       @Id
       @GeneratedValue(strategy = GenerationType.IDENTITY)
       private Long id;
       private String className;
       // Getters and setters...
   }
```

好的，让我们在 `StudentRepository` 接口的基础上，补充完整的 CRUD 操作，并展示如何在 `StudentService` 中使用这些操作。

**1. `StudentRepository` 接口（完整 CRUD）**

在 Spring Data JPA 中，`JpaRepository` 已经提供了大部分常用的 CRUD 操作，因此我们不需要在 `StudentRepository` 中添加额外的方法。但为了演示，我们可以添加一些自定义的查询方法。 [[#通过方法命名约定自动生成查询]]

Java

```java
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {

    // 自定义查询方法 (示例)
    Student findByEmail(String email);
    List<Student> findByNameContaining(String name);
}
```

**2. `StudentService` 类（使用 CRUD 操作）**

Java

```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class StudentService {

    @Autowired
    private StudentRepository studentRepository;

    // 创建学生
    public Student createStudent(Student student) {
        return studentRepository.save(student);
    }

    // 获取所有学生
    public List<Student> getAllStudents() {
        return studentRepository.findAll();
    }

    // 根据 ID 获取学生
    public Student getStudentById(Long id) {
        return studentRepository.findById(id).orElse(null);
    }

    // 更新学生信息
    public Student updateStudent(Long id, Student updatedStudent) {
        Student student = studentRepository.findById(id).orElse(null);
        if (student != null) {
            student.setName(updatedStudent.getName());
            student.setEmail(updatedStudent.getEmail());
            student.setDob(updatedStudent.getDob());
            student.setAge(updatedStudent.getAge());
            student.setStudentClass(updatedStudent.getStudentClass());
            return studentRepository.save(student);
        }
        return null; // 或者抛出异常
    }

    // 删除学生
    public void deleteStudent(Long id) {
        studentRepository.deleteById(id);
    }

    // 自定义查询方法的使用 (示例)
    public Student getStudentByEmail(String email) {
        return studentRepository.findByEmail(email);
    }

    public List<Student> getStudentsByNameContaining(String name) {
        return studentRepository.findByNameContaining(name);
    }
}
```

**3. `StudentController` 类（使用 Service 层）**

Java

```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/students")
public class StudentController {

    @Autowired
    private StudentService studentService;

    // 创建学生
    @PostMapping
    public Student createStudent(@RequestBody Student student) {
        return studentService.createStudent(student);
    }

    // 获取所有学生
    @GetMapping
    public List<Student> getAllStudents() {
        return studentService.getAllStudents();
    }

    // 根据 ID 获取学生
    @GetMapping("/{id}")
    public Student getStudent(@PathVariable Long id) {
        return studentService.getStudentById(id);
    }

    // 更新学生信息
    @PutMapping("/{id}")
    public Student updateStudent(@PathVariable Long id, @RequestBody Student updatedStudent) {
        return studentService.updateStudent(id, updatedStudent);
    }

    // 删除学生
    @DeleteMapping("/{id}")
    public void deleteStudent(@PathVariable Long id) {
        studentService.deleteStudent(id);
    }

    // 自定义查询方法的使用 (示例)
    @GetMapping("/email/{email}")
    public Student getStudentByEmail(@PathVariable String email) {
        return studentService.getStudentByEmail(email);
    }

    @GetMapping("/name/contains/{name}")
    public List<Student> getStudentsByNameContaining(@PathVariable String name) {
        return studentService.getStudentsByNameContaining(name);
    }
}
```

**关键点：**

- **`JpaRepository` 提供的 CRUD 方法：**
    - `save()`：保存或更新实体。
    - `findAll()`：获取所有实体。
    - `findById()`：根据 ID 获取实体。
    - `deleteById()`：根据 ID 删除实体。
- **自定义查询方法：**
    - 可以在 `StudentRepository` 中定义自定义查询方法，Spring Data JPA 会根据方法名自动生成 SQL 查询。
- **Service 层：**
    - Service 层负责调用 Repository 层的方法，并处理业务逻辑。
- **Controller 层：**
    - Controller 层负责处理 HTTP 请求，调用 Service 层的方法，并将结果返回给客户端。

通过这些补充，我们实现了完整的 CRUD 操作，并展示了如何在 Spring Boot 后端中使用它们。

- **application.properties:**

```
   spring.datasource.url=jdbc:h2:mem:testdb
   spring.datasource.driverClassName=org.h2.Driver
   spring.jpa.hibernate.ddl-auto=create-drop
```

**3. React 前端**

- **组件:**

JavaScript

```
   // StudentList.jsx
   import React, { useState, useEffect } from 'react';
   import axios from 'axios';
   function StudentList() {
       const [students, setStudents] = useState([]);
       useEffect(() => {
           axios.get('/api/students')
               .then(response => setStudents(response.data));
       }, []);
       return (
           <div>
               {students.map(student => (
                   <div key={student.id}>
                       {student.name} - {student.email}
                   </div>
               ))}
           </div>
       );
   }
   export default StudentList;
```

- **App.js:**

JavaScript

```
   import React from 'react';
   import StudentList from './StudentList';
   function App() {
       return (
           <div>
               <StudentList />
           </div>
       );
   }
   export default App;
```

- **package.json (添加 axios):**

JSON

```
   "dependencies": {
       "axios": "^0.21.1",
       // ...
   }
```

**4. 前后端交互**

- **CORS 配置:**
    - 在 Spring Boot 中，添加 `@CrossOrigin` 注解或配置 CORS。
- **Axios 请求:**
    - React 前端使用 `axios` 发送 HTTP 请求到 Spring Boot 后端。

**总结**

这个示例提供了一个基于图片架构的全栈应用，实现了学生信息的简单 CRUD 操作。您可以根据需要扩展这个示例，添加更多的功能和 UI 组件。

[[Spring Data JPA]]
[[Spring Core与Spring MVC]]


## 通过方法命名约定自动生成查询
这句话的核心在于解释 Spring Data JPA 如何通过方法命名约定自动生成查询，以及何时需要自定义查询方法。

**理解 Spring Data JPA 的方法命名约定**

Spring Data JPA 提供了一种强大的机制，允许开发者通过定义符合特定命名规则的接口方法，自动生成对应的 SQL 查询。这种机制称为“方法命名约定”或“查询方法派生”。

**JpaRepository 的自动实现**

`JpaRepository` 接口继承自 `CrudRepository` 和 `PagingAndSortingRepository` 接口，这些接口已经提供了基本的 CRUD 操作方法，如 `save()`、`findById()`、`findAll()`、`deleteById()` 等。

除此之外，Spring Data JPA 还支持通过方法名自动生成查询，例如：

- `findBy<PropertyName>(...)`：根据属性值查询。
- `findBy<PropertyName>Containing(...)`：根据属性值包含某个字符串查询。
- `findBy<PropertyName>And<OtherPropertyName>(...)`：根据多个属性值组合查询。

**findByEmail 的自动实现**

当我们定义 `StudentRepository` 接口并继承 `JpaRepository<Student, Long>` 时，Spring Data JPA 会自动解析方法名，并尝试根据方法名生成查询。

- 如果方法名符合命名约定（如 `findByEmail`），Spring Data JPA 会自动生成相应的 SQL 查询，例如 `SELECT s FROM Student s WHERE s.email = ?1`。
- 因此，即使我们不在 `StudentRepository` 接口中显式实现 `findByEmail` 方法，Spring Data JPA 也能根据方法名自动生成查询。

**何时需要自定义查询方法**

虽然 Spring Data JPA 的方法命名约定很强大，但有些情况下，我们需要自定义查询方法：

- **复杂的查询逻辑：** 当查询逻辑非常复杂，无法通过方法命名约定表达时，我们需要使用 `@Query` 注解编写自定义的 JPQL 或原生 SQL 查询。[[#复杂示例]]
- **需要优化的查询：** 有时，自动生成的查询可能不是最优的，我们需要手动编写查询以提高性能。
- **需要使用特定的数据库函数：** 有些数据库提供了特定的函数，我们需要在查询中使用这些函数。

**findByEmail 的使用场景**

在 `StudentRepository` 接口中添加 `findByEmail` 方法，是为了演示如何使用自定义查询方法。即使不添加这个方法，我们也可以通过其他方式查询学生信息，例如：

- `findAll()`：获取所有学生，然后在 Service 层或 Controller 层筛选出符合条件的学生。
- 使用 `@Query` 注解编写自定义查询。

但是添加 `findByEmail` 方法，可以使代码更简洁、更易读，并提高查询效率。

**总结**

Spring Data JPA 的方法命名约定可以自动生成大部分常用的查询，但对于复杂的查询逻辑或需要优化的情况，我们需要自定义查询方法。

## 复杂示例
好的，让我们深入探讨一下在 Spring Data JPA 中使用 `@Query` 注解编写自定义 JPQL 或原生 SQL 查询的场景和方法。

**何时使用 `@Query` 注解？**

1. **复杂的查询逻辑：**
    - 当查询涉及多个实体、复杂的条件组合、聚合函数、子查询等，无法通过方法命名约定表达时。
    - 例如，查询某个班级中年龄大于平均年龄的学生。
2. **需要优化的查询：**
    - 当自动生成的查询效率不高，需要手动编写查询以提高性能时。
    - 例如，使用 `JOIN FETCH` 预先加载关联实体，减少数据库查询次数。
3. **需要使用特定的数据库函数：**
    - 当需要使用特定数据库（如 MySQL、PostgreSQL）提供的函数或特性时。
    - 例如，使用 MySQL 的 `DATE_FORMAT` 函数格式化日期。
4. **需要执行更新或删除操作：**
    - 当需要执行批量更新或删除操作时，使用 `@Modifying` 注解配合 `@Query` 注解。
5. **需要执行原生 SQL 查询：**
    - 当需要直接使用原生 SQL 查询时，例如访问数据库特定的表或视图。

**如何使用 `@Query` 注解？**

1. **JPQL 查询：**
    
    - JPQL（Java Persistence Query Language）是一种面向对象的查询语言，类似于 SQL，但操作的是实体对象和属性。
    - 使用 `@Query` 注解，并将 JPQL 查询语句作为参数传递。
    - 例如：
    
    Java
    
    ```java
    @Query("SELECT s FROM Student s WHERE s.studentClass.className = :className AND s.age > :age")
    List<Student> findStudentsByClassAndAgeGreaterThan(@Param("className") String className, @Param("age") int age);
    ```
    - 使用 `:参数名` 绑定参数，并使用 `@Param` 注解指定参数值。
2. **原生 SQL 查询：**
    
    - 使用 `@Query` 注解，并将 `nativeQuery` 属性设置为 `true`。
    - 例如：
    
    Java
    
    ```
    @Query(value = "SELECT * FROM student WHERE class_id = ?1 AND age > ?2", nativeQuery = true)
    List<Student> findStudentsByClassAndAgeGreaterThanNative(Long classId, int age);
    ```
    - 使用 `?序号` 绑定参数，序号从 1 开始。
3. **更新或删除操作：**
    
    - 使用 `@Modifying` 注解，表示这是一个更新或删除操作。
    - 使用 `@Transactional` 注解，保证事务一致性。
    - 例如：
    
    Java
    
    ```
    @Modifying
    @Transactional
    @Query("DELETE FROM Student s WHERE s.studentClass.id = :classId")
    void deleteStudentsByClassId(@Param("classId") Long classId);
    ```
    

**示例：复杂的查询逻辑**

假设我们需要查询某个班级中年龄大于平均年龄的学生，可以使用以下 JPQL 查询：

Java

```
@Query("SELECT s FROM Student s WHERE s.studentClass.id = :classId AND s.age > (SELECT AVG(s2.age) FROM Student s2 WHERE s2.studentClass.id = :classId)")
List<Student> findStudentsByClassAndAgeGreaterThanAverage(@Param("classId") Long classId);
```

**总结**

`@Query` 注解提供了强大的自定义查询能力，可以满足各种复杂的查询需求。在实际开发中，应根据具体情况选择使用方法命名约定或 `@Query` 注解。