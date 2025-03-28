### 闭包回调装饰器:

请解释闭包,回调,装饰器等编程概念之前的区别与练习, 并分别给出各自的应用实例(分别用 JS, Java, Python 三种语言) , 并对关键代码段给出注解.

闭包、回调和装饰器是三种不同的编程概念。下面分别对它们进行解释，并给出使用JavaScript、Java和Python的应用实例。

1. 闭包（Closure）：
闭包是一个函数，它可以捕获其所在作用域中的变量。在外部函数执行后，内部的匿名函数仍然可以访问外部函数的局部变量。

JavaScript 示例:
```javascript
function outer() {
    let count = 0; // 定义一个局部变量count

    // 返回一个匿名函数，这个匿名函数可以访问外部函数outer的局部变量count
    return function () {
        count++; // 每次调用时递增count
        console.log(count);
    }
}

const closureExample = outer(); // 调用outer函数，返回的是一个匿名函数
closureExample(); // 输出1，count变为1
closureExample(); // 输出2，count变为2
```

Java 示例（Java 8 及以上版本）：
```java
import java.util.function.*;

public class ClosureExample {
    public static void main(String[] args) {
        IntSupplier closureExample = outer();
        System.out.println(closureExample.getAsInt()); // 输出1
        System.out.println(closureExample.getAsInt()); // 输出2
    }

    private static IntSupplier outer() {
        int count = 0;
        return new IntSupplier() {
            private int innerCount = count;
            @Override
            public int getAsInt() {
                return ++innerCount;
            }
        };
    }
}
```

Python 示例：
```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    return inner

closure_example = outer()
closure_example()  # 输出1
closure_example()  # 输出2
```

2. 回调（Callback）：
回调是将一个函数作为参数传递给另一个函数，并在合适的时机由另一个函数执行该函数。通常用于异步操作，但也可以用于同步操作。

JavaScript 示例：
```javascript
function callbackExample(name, callback) {
    console.log("Hello, " + name);
    callback(); // 调用传入的回调函数
}

callbackExample("World", function () {
    console.log("This is a callback function.");
});
```

Java 示例：
```java
public class CallbackExample {
    public static void main(String[] args) {
        callbackExample("World", () -> System.out.println("This is a callback function."));
    }

    private static void callbackExample(String name, Runnable callback) {
        System.out.println("Hello, " + name);
        callback.run(); // 调用传入的回调函数
    }
}
```

Python 示例：
```python
def callback_example(name, callback):
    print(f"Hello, {name}")
    callback()

callback_example("World", lambda: print("This is a callback function."))
```

3. 装饰器（Decorator）：
装饰器是一种特殊类型的高阶函数，它接收一个函数作为输入，并返回一个新的函数。装饰器可以修改或扩展原始函数的行为而不改变其源代码。

JavaScript 示例：
```javascript
function decoratorExample(fn) {
    return function () {
        console.log("Decorator: Before calling the original function");
        fn(); // 调用原始函数
        console.log("Decorator: After calling the original function");
    }
}

function hello() {
    console.log("Hello, World!");
}

const decoratedHello = decoratorExample(hello);
decoratedHello(); // 输出装饰器添加的信息和原始函数的输出
```

Java 示例（使用Java注解实现）：
```java
@Retention(RetentionPolicy.RUNTIME)
@interface DecoratorExample {
}

class DecoratedClass {
    @DecoratorExample
    public void hello() {
        System.out.println("Hello, World!");
    }
}

public class Main {
    public static void main(String[] args) throws NoSuchMethodException {
        DecoratedClass obj = new DecoratedClass();
        Method method = obj.getClass().getMethod("hello");

        if (method.isAnnotationPresent(DecoratorExample.class)) {
            System.out.println("Decorator: Before calling the original function");
            obj.hello();
            System.out.println("Decorator: After calling the original function");
        } else {
            obj.hello();
        }
    }
}
```

Python 示例：
```python
def decorator_example(fn):
    def wrapper():
        print("Decorator: Before calling the original function")
        fn()  # 调用原始函数
        print("Decorator: After calling the original function")

    return wrapper

@decorator_example
def hello():
    print("Hello, World!")

hello()  # 输出装饰器添加的信息和原始函数的输出
```

以上代码展示了闭包、回调和装饰器在JavaScript、Java和Python中的应用及区别。

[[Nodejs关键技术]]


### React Router
[[../前端开发/React/ReactRouter#面试提问]]






