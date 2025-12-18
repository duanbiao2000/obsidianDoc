### 一、 核心流程：`__new__` 与 `__init__` 的两阶段实例化

Python的类实例化过程被精妙地分解为两个核心阶段，由两个不同的 `magic method` 负责，体现了“创造”与“定义”的分离。

1.  **`__new__` 方法: 对象的创造者 (Creator)**
    - **职责**: 负责**创建**并**返回**一个类的实例。它的核心任务是分配内存，并构建一个“裸”的对象骨架。
    - **调用时机**: 当你执行 `MyClass(...)` 时，`__new__` 是第一个被调用的方法。
    - **关键特性**:
        - 它是一个 `class method`，接收的第一个参数是类本身 (`cls`)。
        - **必须返回一个实例**。通常通过 `super().__new__(cls)` 调用父类的 `__new__` 来完成实际的创建工作。
        - 拥有强大的控制力：可以返回一个已存在的实例（实现 `Singleton` 模式），甚至可以返回一个完全不同类型的对象（实现 `Factory` 模式）。
        - 如果 `__new__` 返回的不是 `cls` 或其子类的实例，那么 `__init__` 将**不会**被调用。
        - 是实现**不可变类型** (`immutable types`) 的关键，因为核心状态可以在对象返回前就被设定好。

2.  **`__init__` 方法: 对象的定义者 (Initializer)**
    - **职责**: 负责**初始化**由 `__new__` 创建好的实例。它的任务是根据传入的参数，为实例设置属性和初始状态。
    - **调用时机**: 在 `__new__` 成功返回一个当前类的实例后，`__init__` 会被**自动**调用。
    - **关键特性**:
        - 它是一个 `instance method`，接收的第一个参数是 `__new__` 返回的实例 (`self`)。
        - **不应该返回任何值** (或只能返回 `None`)。它的工作是“就地”修改 `self`，而不是创造新的东西。
        - 主要用于设置实例的**可变状态** (`mutable state`)。

### 二、 流程总结与设计哲学

**实例化流程**:
`MyClass(...)` → `type.__call__` → `MyClass.__new__` (创建实例) → `MyClass.__init__` (初始化实例) → 返回最终实例

**设计哲学**:
- **`Existence precedes Essence` (存在先于本质)**: 对象必须先被 `__new__` “创造”出来（存在），然后才能被 `__init__` “定义”其属性和状态（本质）。
- **`Separation of Concerns` (责任分离)**:
    - `__new__` 关注**创建** (`creation`)，控制“成为谁”。
    - `__init__` 关注**初始化** (`initialization`)，控制“成为什么样”。
- **灵活性与控制力**: 这种分离为实现 `Singleton`, `Factory` 等高级设计模式，以及创建不可变对象提供了强大的机制。

### 三、 高级应用场景

1.  **实现 `Singleton` 模式**:
    - 在 `__new__` 中检查类级别的 `_instance` 属性。如果实例已存在，直接返回；否则，创建并存储它。
    ```python
    class Singleton:
        _instance = None
        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super().__new__(cls)
            return cls._instance
    ```

2.  **实现不可变对象**:
    - 在 `__new__` 中设置对象的内部属性，并重写 `__setattr__` 以阻止后续修改。
    ```python
    class ImmutablePoint:
        def __new__(cls, x, y):
            instance = super().__new__(cls)
            object.__setattr__(instance, 'x', x)
            object.__setattr__(instance, 'y', y)
            return instance

        def __setattr__(self, key, value):
            raise AttributeError("Cannot modify immutable object")
    ```

3.  **实现 `Factory` 模式**:
    - 在 `__new__` 中根据传入的参数，决定实例化并返回哪个具体的子类。
    ```python
    class Shape:
        def __new__(cls, shape_type, *args, **kwargs):
            if shape_type == 'circle':
                return object.__new__(Circle)
            elif shape_type == 'square':
                return object.__new__(Square)
            # ... and so on
    ```

通过理解 `__new__` 和 `__init__` 的分工与协作，开发者可以更深入地掌握Python的对象模型，并设计出更优雅、更强大的类结构。