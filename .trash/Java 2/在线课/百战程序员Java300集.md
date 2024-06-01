![[Pasted image 20240222181614.png]]
2024-02-22 18:16
 `try-with-resources` 是 Java 7 引入的一项新特性，它简化了资源管理，特别是在使用需要关闭的资源（如文件流、数据库连接等）时。这个特性的主要目的是确保在 `try` 块执行完毕后，即使在 `try` 块中发生了异常，资源也能被正确地关闭。

在 Java 9 中，`try-with-resources` 语句得到了进一步的改进，允许开发者在 `try` 块中使用已经声明为 `final` 或等效于 `final` 的变量。这意味着你可以在 `try-with-resources` 语句外部声明资源，然后在 `try` 块中直接使用这些资源，而不需要在 `try-with-resources` 语句内部再次声明它们。

以下是 Java 9 中 `try-with-resources` 的一个示例：

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class TryWithResourcesExample {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("example.txt"));
        try (br) {
            // 使用 br 进行操作
            String line = br.readLine();
            System.out.println(line);
        } // br 在这里自动关闭
    }
}
```

在这个例子中，`BufferedReader` 对象 `br` 在 `try` 块外部被创建，然后在 `try-with-resources` 语句中使用。当 `try` 块执行完毕时，无论是否发生异常，`br` 都会自动关闭。

这种改进使得代码更加简洁，减少了资源管理的复杂性，并且提高了代码的可读性。开发者不再需要在 `finally` 块中手动关闭资源，也不用担心资源关闭时可能抛出的异常会掩盖原始异常。如果资源关闭时确实发生了异常，这个异常会被添加到 `try` 块中抛出的异常的 `suppressed` 异常列表中，这样开发者可以通过异常链来追踪所有相关的异常。
 抱歉，让我更清晰地解释一下 `try-with-resources` 语句的结构和用法。

在 Java 7 及以后的版本中，`try-with-resources` 语句允许你在 `try` 块中声明资源，这些资源会在 `try` 块执行完毕后自动关闭。这个特性特别适用于那些实现了 `AutoCloseable` 或 `Closeable` 接口的对象，因为这些接口提供了 `close()` 方法来关闭资源。

`try-with-resources` 语句的基本结构如下：

```java
try (ResourceType resource1 = new ResourceType(); ResourceType resource2 = new ResourceType()) {
    // 使用 resource1 和 resource2 的代码
    // 当这个块执行完毕时，无论是否发生异常，resource1 和 resource2 都会自动关闭
} catch (Exception e) {
    // 处理可能发生的异常
}
```

在这个结构中，`ResourceType` 是资源的类型，`resource1` 和 `resource2` 是资源的实例。你可以在 `try` 块中声明多个资源，它们都会在 `try` 块执行完毕后自动关闭。这种自动关闭机制是通过在 `try` 块的末尾添加一个隐式的 `finally` 块来实现的，这个 `finally` 块包含了对所有资源的 `close()` 方法调用。

例如，如果你有一个文件读取操作，你可以这样使用 `try-with-resources`：

```java
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt")) {
    // 读取文件内容
    String line = reader.readLine();
    System.out.println(line);
} catch (IOException e) {
    e.printStackTrace();
}
```

在这个例子中，`BufferedReader` 是一个资源，它实现了 `AutoCloseable` 接口。当 `try` 块执行完毕时，`reader` 对象会自动关闭，无论是否发生异常。这样就不需要显式地在 `finally` 块中关闭资源，也不用担心忘记关闭资源导致的资源泄露问题。
![[Pasted image 20240222182116.png]]
![[Pasted image 20240222182532.png]]
![[Pasted image 20240222183919.png]]
