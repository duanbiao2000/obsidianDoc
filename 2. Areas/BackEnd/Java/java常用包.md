 在Java中，`java.lang`和`java.util`是两个非常重要的基础包，它们包含了许多核心API，这些API在几乎所有Java项目中都会用到。以下是这两个包中一些关键的API及其用法：

### java.lang包

1. **Object类**：
   - `equals(Object obj)`：用于比较两个对象是否相等。
   - `hashCode()`：返回对象的哈希码。
   - `toString()`：返回对象的字符串表示。

2. **String类**：
   - `String.concat(String str)`：连接两个字符串。
   - `String.format(String format, Object... args)`：格式化字符串。
   - `String.substring(int beginIndex, int endIndex)`：获取子字符串。

3. **Math类**：
   - `Math.sqrt(double a)`：计算平方根。
   - `Math.random()`：生成一个随机数。

4. **System类**：
   - `System.out`：标准输出流。
   - `System.in`：标准输入流。
   - `System.exit(int status)`：退出程序。

5. **Throwable类**：
   - `Throwable.getMessage()`：获取异常信息。
   - `Throwable.printStackTrace()`：打印异常堆栈跟踪。

### java.util包

1. **List接口**：
   - `ArrayList`：动态数组实现，支持快速随机访问。
   - `LinkedList`：双向链表实现，支持快速插入和删除。

2. **Set接口**：
   - `HashSet`：基于哈希表的集合，不允许重复元素。
   - `TreeSet`：基于红黑树的集合，元素自动排序。

3. **Map接口**：
   - `HashMap`：基于哈希表的键值对集合。
   - `TreeMap`：基于红黑树的键值对集合，键自动排序。
   - `LinkedHashMap`：维护插入顺序的HashMap。

4. **Date和Calendar类**：
   - `Date`：日期和时间的表示。
   - `Calendar`：日期和时间的日历功能。

5. **Random类**：
   - `Random.nextInt(int bound)`：生成一个指定范围内的随机整数。

6. **Iterator接口**：
   - 提供遍历集合元素的方法，如`hasNext()`和`next()`。

7. **Comparator接口**：
   - `Comparator.compare(Object o1, Object o2)`：比较两个对象。

8. **Arrays类**：
   - `Arrays.sort(Object[] a)`：对数组进行排序。
   - `Arrays.asList(Object... a)`：将数组转换为列表。

9. **Collections类**：
   - 提供了一系列静态方法来操作集合，如`sort()`、`reverse()`、`shuffle()`等。

10. **UUID类**：
    - `UUID.randomUUID()`：生成一个随机的UUID。

这些API是Java编程的基础，无论是在简单的脚本还是在复杂的企业级应用中，都会频繁使用。掌握这些API的用法对于Java开发者来说是非常重要的。
 在Java中，除了`java.lang`和`java.util`这两个基础包之外，还有许多其他常用的包，它们提供了丰富的功能，适用于不同的开发场景。以下是一些常用的包及其关键API：

### java.io包
- **File类**：
  - `File(String pathname)`：创建一个新`File`对象，表示一个文件或目录。
  - `boolean exists()`：检查文件或目录是否存在。
  - `boolean mkdir()`：创建新目录。

- **InputStream和OutputStream类**：
  - `InputStream`和`OutputStream`是所有输入流和输出流的超类，用于处理字节流。

- **BufferedReader和BufferedWriter类**：
  - 提供缓冲区，提高读写效率。

- **FileReader和FileWriter类**：
  - `FileReader`和`FileWriter`是处理字符流的类，用于读写文本文件。

### java.net包
- **URL类**：
  - `URL(String spec)`：创建一个URL对象，表示一个统一资源定位符（URL）。

- **HttpURLConnection类**：
  - `HttpURLConnection`是用于发送HTTP请求的类。

### java.sql包
- **Connection接口**：
  - 提供了与数据库建立连接的方法。

- **Statement接口**：
  - 用于执行SQL语句。

- **ResultSet接口**：
  - 表示数据库查询结果集。

### java.time包（Java 8引入）
- **LocalDate、LocalTime、LocalDateTime类**：
  - 提供了日期和时间的现代API。

- **ZonedDateTime类**：
  - 表示带有时区的日期和时间。

- **Duration和Period类**：
  - 分别表示时间持续时间和日期持续时间。

### java.nio包
- **ByteBuffer类**：
  - 提供了对字节缓冲区的高效操作。

- **Files类**：
  - 提供了一系列静态方法，用于文件操作，如复制、删除、移动文件等。

### java.security包
- **KeyPairGenerator类**：
  - 生成公钥和私钥对。

- **MessageDigest类**：
  - 提供消息摘要算法，如MD5、SHA-1等。

### java.text包
- **SimpleDateFormat类**：
  - 用于格式化和解析日期。

- **NumberFormat类**：
  - 提供了格式化和解析数字的方法。

### java.awt包（图形用户界面）
- **Graphics类**：
  - 提供了绘制图形的方法。

- **Frame类**：
  - 创建一个窗口。

### javax.swing包（Swing图形用户界面）
- **JFrame类**：
  - 创建一个窗口框架。

- **JButton类**：
  - 创建一个按钮。

这些包和API是Java开发者在进行日常开发时经常使用的，它们涵盖了文件操作、网络通信、数据库操作、日期时间处理、安全、并发编程等多个方面。掌握这些API对于提高开发效率和编写高效、健壮的Java应用程序至关重要。
 当然，以下是一些常用Java包及其API的示例代码，包括注释说明以帮助理解它们的用法：

### java.io包 - 文件操作

```java
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class FileExample {
    public static void main(String[] args) {
        // 创建File对象
        File file = new File("example.txt");
        
        // 创建文件（如果文件不存在）
        if (!file.exists()) {
            try {
                file.createNewFile();
                System.out.println("File created successfully.");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        
        // 写入文件内容
        try (FileWriter writer = new FileWriter(file)) {
            writer.write("Hello, World!");
            System.out.println("Content written to file.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
// 输出: File created successfully.
//       Content written to file.
```

### java.net包 - 网络通信

```java
import java.net.HttpURLConnection;
import java.net.URL;

public class NetworkExample {
    public static void main(String[] args) {
        try {
            // 创建URL对象
            URL url = new URL("http://www.example.com");
            
            // 打开连接
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            
            // 发送GET请求
            connection.setRequestMethod("GET");
            
            // 获取响应码
            int responseCode = connection.getResponseCode();
            System.out.println("Response Code : " + responseCode);
            
            // 关闭连接
            connection.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
// 输出: Response Code : 200 (假设网站正常响应)
```

### java.sql包 - 数据库操作

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class DatabaseExample {
    public static void main(String[] args) {
        // 数据库连接URL
        String url = "jdbc:mysql://localhost:3306/testdb";
        // 数据库用户名和密码
        String user = "user";
        String password = "password";
        
        try {
            // 加载数据库驱动
            Class.forName("com.mysql.jdbc.Driver");
            
            // 建立连接
            Connection conn = DriverManager.getConnection(url, user, password);
            
            // 创建Statement对象
            Statement stmt = conn.createStatement();
            
            // 执行查询
            ResultSet rs = stmt.executeQuery("SELECT * FROM users");
            
            // 处理结果集
            while (rs.next()) {
                // 获取列值
                String name = rs.getString("name");
                int age = rs.getInt("age");
                System.out.println("Name: " + name + ", Age: " + age);
            }
            
            // 关闭资源
            rs.close();
            stmt.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
// 输出: Name: John Doe, Age: 30
//       Name: Jane Smith, Age: 25
//       ... (假设数据库中有这些数据)
```

### java.time包 - 日期时间处理（Java 8及以上）

```java
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DateTimeExample {
    public static void main(String[] args) {
        // 创建LocalDate对象
        LocalDate today = LocalDate.now();
        System.out.println("Today's date: " + today);
        
        // 创建LocalDateTime对象
        LocalDateTime dateTime = LocalDateTime.now();
        System.out.println("Current date and time: " + dateTime);
        
        // 格式化日期时间
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String formattedDateTime = dateTime.format(formatter);
        System.out.println("Formatted date and time: " + formattedDateTime);
    }
}
// 输出: Today's date: 2024-02-21
//       Current date and time: 2024-02-21T12:34:56.789
//       Formatted date and time: 2024-02-21 12:34:56
```

这些示例展示了如何在Java中使用这些包进行基本的文件操作、网络请求、数据库连接和日期时间处理。在实际应用中，你可能需要根据具体需求进行更复杂的操作。
 当然，让我们继续看看其他几个常用的Java包及其API的示例代码。

### java.util包 - 集合操作

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class CollectionExample {
    public static void main(String[] args) {
        // 使用ArrayList
        List<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        System.out.println("ArrayList: " + list); // 输出: [Apple, Banana]

        // 使用HashMap
        Map<String, Integer> map = new HashMap<>();
        map.put("Alice", 25);
        map.put("Bob", 30);
        System.out.println("HashMap: " + map); // 输出: {Alice=25, Bob=30}

        // 使用HashSet
        Set<String> set = new HashSet<>();
        set.add("Alice");
        set.add("Bob");
        System.out.println("HashSet: " + set); // 输出: [Alice, Bob]

        // 使用LinkedHashSet保持插入顺序
        Set<String> linkedSet = new LinkedHashSet<>();
        linkedSet.add("Alice");
        linkedSet.add("Bob");
        System.out.println("LinkedHashSet: " + linkedSet); // 输出: [Alice, Bob]
    }
}
```

### java.util.regex包 - 正则表达式

```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexExample {
    public static void main(String[] args) {
        // 创建正则表达式模式
        Pattern pattern = Pattern.compile("\\d{3}-\\d{3}-\\d{4}");
        
        // 使用Matcher进行匹配
        String input = "123-456-7890";
        Matcher matcher = pattern.matcher(input);
        
        // 检查是否匹配
        if (matcher.matches()) {
            System.out.println("Input matches the pattern.");
        } else {
            System.out.println("Input does not match the pattern.");
        }
        // 输出: Input matches the pattern.
    }
}
```

### java.util.concurrent包 - 并发编程

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class ConcurrencyExample {
    public static void main(String[] args) {
        // 创建线程池
        ExecutorService service = Executors.newFixedThreadPool(2);
        
        // 提交任务
        service.submit(() -> System.out.println("Task 1 executed."));
        service.submit(() -> System.out.println("Task 2 executed."));
        
        // 关闭线程池
        service.shutdown();
        try {
            service.awaitTermination(1, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
// 输出: Task 1 executed.
//       Task 2 executed.
```

### java.util.zip包 - 数据压缩

```java
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class ZipExample {
    public static void main(String[] args) {
        try (FileOutputStream fos = new FileOutputStream("example.txt.gz");
             GZIPOutputStream gzos = new GZIPOutputStream(fos);
             FileOutputStream fosInput = new FileOutputStream("example.txt");
             GZIPInputStream gzis = new GZIPInputStream(new FileInputStream("example.txt.gz"))) {
            
            // 压缩文件
            String content = "Hello, World!";
            fosInput.write(content.getBytes());
            gzos.write(content.getBytes());
            
            // 解压缩文件
            byte[] buffer = new byte[1024];
            int len;
            while ((len = gzis.read(buffer)) > 0) {
                fosInput.write(buffer, 0, len);
            }
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
// 这个示例展示了如何压缩和解压缩文件，输出不会直接显示，但文件会被创建和修改。
```

这些示例展示了如何在Java中使用集合、正则表达式、并发编程和数据压缩等高级功能。在实际开发中，这些包提供了强大的工具来处理复杂的任务。
 当然，Java生态系统中还有许多其他常用的包，这里再介绍几个：

### java.nio包 - 新型I/O（NIO）

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class NIOExample {
    public static void main(String[] args) {
        try {
            // 使用NIO创建新文件并写入内容
            Files.write(Paths.get("example.txt"), "Hello, NIO!".getBytes(), StandardOpenOption.CREATE);

            // 使用NIO读取文件内容
            String content = new String(Files.readAllBytes(Paths.get("example.txt")));
            System.out.println("Content of the file: " + content);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
// 输出: Content of the file: Hello, NIO!
```

### java.security包 - 安全和加密

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class SecurityExample {
    public static void main(String[] args) {
        try {
            // 创建MD5摘要
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest("Hello, World!".getBytes());
            System.out.println("MD5 Hash: " + bytesToHex(messageDigest));
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }

    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}
// 输出: MD5 Hash: 86f7e437faa5a5a7fce15d1ddcb9eaeaea377
```

