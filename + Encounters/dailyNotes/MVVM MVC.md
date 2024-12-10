---
aliases: 

categories: 
high_priority: false
---
### 模型、仓库、视图模型、数据访问对象（DAO）和数据库之间的层级与引用关系

在现代软件开发中，特别是使用MVC（Model-View-Controller）或MVVM（Model-View-ViewModel）等架构模式时，模型、仓库、视图模型、数据访问对象（DAO）和数据库这几个概念经常被提及。它们之间存在着清晰的层级和引用关系，共同构成了应用程序的数据管理和展示逻辑。

### 层级关系

从上到下，我们可以将这些概念分为以下几个层次：

1. **视图层（View）：** 负责用户界面的展示，通常由视图模型提供数据。
2. **视图模型层（ViewModel）：** 作为视图和模型之间的桥梁，负责处理用户交互，将模型数据转换为视图可展示的格式。
3. **业务逻辑层（Service）：** 包含应用程序的核心业务逻辑，通常会调用仓库层来操作数据。
4. **仓库层（Repository）：** 提供对数据的访问接口，封装了对数据源（如数据库）的操作。
5. **数据访问层（DAO）：** 负责与数据库进行直接交互，执行SQL语句等操作。
6. **数据库层（Database）：** 作为数据存储的底层，负责数据的持久化。

### 引用关系

- **视图层引用视图模型：** 视图从视图模型获取数据，并根据数据更新界面。
- **视图模型引用业务逻辑层：** 视图模型调用业务逻辑层的方法来获取数据或执行业务操作。
- **业务逻辑层引用仓库层：** 业务逻辑层通过调用仓库层的方法来操作数据。
- **仓库层引用数据访问层：** 仓库层通过调用数据访问层的方法来执行数据库操作。
- **数据访问层引用数据库：** 数据访问层直接与数据库进行交互。

### 各层职责

- **模型（Model）：** 代表应用程序中的数据和业务对象，通常与数据库中的表对应。
- **仓库（Repository）：** 提供对模型的CRUD（创建、读取、更新、删除）操作，隐藏了底层数据访问的细节。
- **视图模型（ViewModel）：** 将模型数据转换为视图可展示的格式，同时处理用户输入，并通知视图更新。
- **数据访问对象（DAO）：** 负责与数据库进行交互，执行SQL查询和更新操作。
- **数据库：** 存储应用程序的数据。

### UML图示例

### 总结

通过这种分层结构，可以将应用程序的各个方面进行解耦，提高代码的可维护性、可测试性和可扩展性。

- **视图层**关注用户界面。
- **视图模型层**负责数据转换和用户交互。
- **业务逻辑层**包含核心业务逻辑。
- **仓库层**提供对数据的访问。
- **数据访问层**负责与数据库交互。



### 层级和引用关系

#### 1. Model

- **定义**: 数据模型类，通常是数据实体。
- **示例**:
  ```java
  public class User {
      @PrimaryKey(autoGenerate = true)
      private int id;
      private String name;
      private String email;

      // Getters and Setters
  }
  ```

#### 2. DAO

- **定义**: 定义对数据库的操作方法。
- **示例**:
  ```java
  @Dao
  public interface UserDao {
      @Insert
      void insert(User user);

      @Query("SELECT * FROM user")
      LiveData<List<User>> getAllUsers();

      @Update
      void update(User user);

      @Delete
      void delete(User user);
  }
  ```

#### 3. Database

- **定义**: 管理数据库表，并提供对 `DAO` 的访问。
- **示例**:
  ```java
  @Database(entities = {User.class}, version = 1)
  public abstract class AppDatabase extends RoomDatabase {
      public abstract UserDao userDao();
  }
  ```

#### 4. Repository

- **定义**: 封装数据访问逻辑，管理多个数据源。
- **示例**:
  ```java
  public class UserRepository {
      private final UserDao userDao;
      private final LiveData<List<User>> allUsers;

      public UserRepository(AppDatabase db) {
          userDao = db.userDao();
          allUsers = userDao.getAllUsers();
      }

      public LiveData<List<User>> getAllUsers() {
          return allUsers;
      }

      public void insert(User user) {
          new InsertAsyncTask(userDao).execute(user);
      }

      public void update(User user) {
          new UpdateAsyncTask(userDao).execute(user);
      }

      public void delete(User user) {
          new DeleteAsyncTask(userDao).execute(user);
      }

      // 异步任务类
      private static class InsertAsyncTask extends AsyncTask<User, Void, Void> {
          private UserDao asyncTaskDao;

          InsertAsyncTask(UserDao dao) {
              asyncTaskDao = dao;
          }

          @Override
          protected Void doInBackground(final User... params) {
              asyncTaskDao.insert(params[0]);
              return null;
          }
      }

      // 其他异步任务类类似
  }
  ```

#### 5. ViewModel

- **定义**: 为 UI 提供数据，处理业务逻辑，并与 `Repository` 交互。
- **示例**:
  ```java
  public class UserViewModel extends AndroidViewModel {
      private UserRepository repository;
      private LiveData<List<User>> allUsers;

      public UserViewModel(@NonNull Application application) {
          super(application);
          AppDatabase database = AppDatabase.getInstance(application);
          repository = new UserRepository(database);
          allUsers = repository.getAllUsers();
      }

      public LiveData<List<User>> getAllUsers() {
          return allUsers;
      }

      public void insert(User user) {
          repository.insert(user);
      }

      public void update(User user) {
          repository.update(user);
      }

      public void delete(User user) {
          repository.delete(user);
      }
  }
  ```



