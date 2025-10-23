在 Java 中，**动态代理**是一种强大的机制，允许你在运行时创建代理对象，并在调用方法时动态地插入逻辑。它在 **RPC 框架** 中尤为重要，因为它能让你“像调用本地方法一样调用远程服务”。下面我们来深入理解它的原理和在 RPC 中的应用 👇

---

## 🧠 什么是 JDK 动态代理？

JDK 动态代理基于接口，它通过 `Proxy` 类和 `InvocationHandler` 接口实现：

```java
// 接口
public interface HelloService {
    void sayHello(String name);
}

// 实现 InvocationHandler
public class HelloHandler implements InvocationHandler {
    private final Object target;

    public HelloHandler(Object target) {
        this.target = target;
    }

    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("Before call...");
        Object result = method.invoke(target, args);
        System.out.println("After call...");
        return result;
    }
}

// 创建代理对象
HelloService proxy = (HelloService) Proxy.newProxyInstance(
    HelloService.class.getClassLoader(),
    new Class[]{HelloService.class},
    new HelloHandler(new HelloServiceImpl())
);
```

---

## 🚀 在 RPC 框架中的作用

在 RPC 中，客户端调用的是一个**接口**，但实际实现是在远程服务器上。动态代理的作用是：

> **拦截接口方法调用 → 封装为网络请求 → 发送到远程服务 → 接收响应 → 返回结果**

### 🧩 示例流程（以 JDK 动态代理为例）

```java
public class RpcInvocationHandler implements InvocationHandler {
    private final Class<?> serviceInterface;

    public RpcInvocationHandler(Class<?> serviceInterface) {
        this.serviceInterface = serviceInterface;
    }

    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        // 1. 封装请求
        RpcRequest request = new RpcRequest(serviceInterface.getName(), method.getName(), args);

        // 2. 网络传输（如 Netty、HTTP）
        RpcResponse response = RpcClient.send(request);

        // 3. 返回结果
        return response.getResult();
    }
}
```

客户端只需：

```java
HelloService proxy = (HelloService) Proxy.newProxyInstance(
    HelloService.class.getClassLoader(),
    new Class[]{HelloService.class},
    new RpcInvocationHandler(HelloService.class)
);
proxy.sayHello("Book"); // 实际是远程调用
```

---

## 🧪 动态代理技术对比（在 RPC 中的选择）

| 技术        | 是否基于接口 | 性能  | 应用场景               |
| --------- | ------ | --- | ------------------ |
| JDK Proxy | ✅ 是    | 中等  | 接口驱动的 RPC 框架       |
| CGLIB     | ❌ 否    | 较高  | 类代理（无接口）           |
| Javassist | ❌ 否    | 很高  | 字节码级别控制            |
| ByteBuddy | ❌ 否    | 高   | Spring AOP、Mocking |

> 例如：Dubbo 使用 Javassist，Motan 使用 JDK Proxy。

---

## 📦 总结

- JDK 动态代理适合**接口驱动的 RPC 框架**
- 它让你“像调用本地方法一样”调用远程服务
- 动态代理是实现 **服务透明化、解耦调用逻辑** 的关键技术

---

如果你想，我可以帮你写一个完整的“模拟 RPC 框架”的小项目，展示如何用动态代理封装远程调用逻辑。要不要来点实战练练手？😄