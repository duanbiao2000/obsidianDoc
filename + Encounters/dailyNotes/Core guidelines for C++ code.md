---
aliases: 
source: Beautiful C++ 30 Core Guidelines for Writing Clean, Safe, and Fast Code (J. Guy Davidson  Kate Gregory) (Z-Library).epub
author: 
createdAt: 
updateAt: 
categories: 
high_priority: false
tags:
---

## SUMMARY
J. Guy Davidson presents 30 core guidelines for writing beautiful, efficient, and maintainable C++ code. The content focuses on best practices, insights, and principles essential for mastering C++ development.

## IDEAS:
- "Beautiful code" is maintainable, efficient, and written with clarity and simplicity.
- ==Prioritize readability over cleverness when writing C++ code.==
- Use const wherever possible to communicate immutability.
在这句话中，“possible”是“尽可能”的意思。整个固定搭配“wherever possible”可以理解为“在可能的情况下”或“尽可能地”。这句话的意思是，在可能的情况下尽可能使用 const 关键字来传达不可变性的意图。
- Prefer [[smart pointers]] over raw pointers for better memory management.
- Write code that is easy to refactor as requirements change.
- Consistently follow a style guide to improve code readability.
- Strive to minimize dependencies between code modules.
- Use RAII (Resource Acquisition Is Initialization) to manage resources efficiently.
- Templates offer powerful tools but should be used judiciously.
- Avoid premature optimization; focus first on correctness and clarity.
- Use exceptions for error handling instead of return codes.
- **Embrace the standard library; it provides robust, tested components.**
- Use modern C++ features like auto and range-based loops to simplify code.
- Encapsulation and abstraction help manage complexity in large codebases.
- Always write unit tests to ensure code correctness.
- Prefer composition over inheritance for better code flexibility.
- Use const-correctness to enforce immutability in your code.
- Leverage C++'s strong typing system to catch errors at compile-time.
- Understand and apply the Rule of Five when managing resource ownership.
- Avoid macros whenever possible; use inline functions and constexpr instead.
- Prefer standard containers over custom data structures for better code interoperability.
- Use std::unique_ptr and std::shared_ptr to manage dynamic memory safely.
<!--SR:!2025-03-21,3,250-->
- Understand the cost of dynamic memory allocation and minimize its use.
- Use type inference (auto) to reduce redundancy and improve code clarity.
- Prefer algorithms over raw loops for better abstraction and expressiveness.
- Use assertions to catch logic errors during development.
- Document your code, but let the code structure speak for itself.
- Keep functions small and focused on a single task.
- Embrace concurrency with caution; it adds complexity.
- Understand the difference between lvalues and rvalues to optimize resource management.

## INSIGHTS:
- Immutability should be explicitly communicated using const for more predictable, safer code.
- Modern C++ features reduce complexity while improving code readability and maintainability.
- RAII and smart pointers are essential for efficient resource management in C++.
- Type safety in C++ is crucial; leverage strong typing to catch errors early.
- Avoid macros and prefer constexpr and inline functions for safer code.
- Focus on writing code that is easy to maintain and refactor, rather than being clever.
- Use the Rule of Five to manage resources and avoid memory leaks.
- Standard containers and algorithms offer reliable, tested components for common tasks.
- Favor composition over inheritance to achieve more flexible and maintainable code.
- C++'s standard library should be the go-to for most tasks to ensure reliability.

## QUOTES:
- "Beautiful code is code that is maintainable, efficient, and written with clarity."
- "Strive for readability over cleverness when writing C++ code."
- "Use const wherever possible to communicate immutability in your code."
- "Smart pointers are your friends; they manage memory safely and effectively."
- "The Rule of Five is crucial for managing resource ownership in C++."
- "RAII is the cornerstone of resource management in modern C++."
- "Embrace the standard library; it provides robust, tested components."
- "Use modern C++ features to simplify your code and reduce boilerplate."
- **"Prefer composition over inheritance to achieve more flexible code."**
- "Avoid premature optimization; focus on clarity and correctness first."
- "Type safety is one of C++'s greatest strengths; use it to your advantage."
- "Avoid macros when possible; inline functions and constexpr are safer alternatives."
- "Document your code, but aim for self-explanatory structure."
- "Small, focused functions lead to more maintainable code."
- "Understand the cost of dynamic memory allocation and minimize its use."
- "Concurrency is powerful but adds complexity; use it with care."

## HABITS:
- Prioritize code readability over complexity and cleverness.
- Use const consistently to enforce immutability in your code.
- Embrace modern C++ features to reduce boilerplate and improve code clarity.
- Favor smart pointers for safer and more efficient memory management.
- Regularly refactor your code to improve maintainability.
- Write small, focused functions to keep code modular and maintainable.
- Leverage the standard library instead of reinventing the wheel.
- Avoid macros and use constexpr or inline functions instead.
- Apply the Rule of Five to manage resources and prevent leaks.
- Use RAII for effective resource management across your codebase.
- Focus on creating self-documenting code structures.
- Test your code thoroughly with unit tests to ensure correctness.
- Use type inference judiciously to avoid unnecessary repetition.
- Minimize dependencies between modules to reduce coupling.
- Embrace concurrency cautiously, understanding its complexity.

## FACTS:
- Modern C++ features can significantly simplify code and reduce boilerplate.
- RAII is the primary method for managing resources in C++.
- The Rule of Five helps manage resource ownership in C++ effectively.
- The standard library is a reliable source of robust, tested components.
- Type safety in C++ catches many errors at compile-time, reducing runtime bugs.
- Smart pointers provide automatic memory management, reducing the risk of leaks.
- Macros in C++ can lead to unsafe code and should be avoided.
- Immutability is a key concept in C++ that improves code predictability.
- Composition is preferred over inheritance for creating flexible code structures.
- C++'s strong typing system is designed to catch errors early.

## REFERENCES:
- Rule of Five
- Resource Acquisition Is Initialization (RAII)
- Smart pointers (std::unique_ptr, std::shared_ptr)
<!--SR:!2025-03-21,3,250-->
- Standard library
- Modern C++ features (auto, range-based loops)
- Const-correctness
- Type inference (auto)
- Standard containers and algorithms

## ONE-SENTENCE TAKEAWAY:
Write maintainable, clear, and efficient C++ code by leveraging modern features and best practices consistently.

## RECOMMENDATIONS:
- Emphasize code readability over complexity and cleverness for long-term maintainability.
- Use const consistently to communicate immutability in your code.
- Apply the Rule of Five to effectively manage resource ownership in C++.
- Utilize smart pointers to safely and efficiently manage dynamic memory.
- Embrace modern C++ features like auto and range-based loops to simplify code.
- Favor composition over inheritance for creating more flexible and maintainable code.
- Leverage the standard library for robust and tested components.
- Write small, focused functions to keep your code modular and maintainable.
- Use RAII for effective and automatic resource management across your codebase.
- Avoid macros in favor of safer alternatives like constexpr and inline functions.
- Strive to create self-documenting code through thoughtful structure and naming conventions.
- Minimize dependencies between code modules to reduce coupling.
- Regularly refactor your code to improve its structure and maintainability.
- Understand and minimize the cost of dynamic memory allocation.
- Be cautious with concurrency; it adds significant complexity to your code.


> [!NOTE] Title
> Use RAII (Resource Acquisition Is Initialization) to manage resources efficiently.

You're absolutely correct. RAII is a fundamental principle in C++ that greatly improves resource management and exception safety. Here's a breakdown of why RAII is so important:

1. Automatic resource management: Resources are acquired during object construction and released during object destruction.

2. Exception safety: Resources are properly released even if exceptions occur.

3. Cleaner code: Reduces the need for explicit resource management code.

4. Predictable lifetimes: Resource lifetimes are tied to object lifetimes, making them more predictable.

Here's a simple example demonstrating RAII:

```cpp
class FileHandler {
private:
    FILE* file;

public:
    FileHandler(const char* filename, const char* mode) {
        file = fopen(filename, mode);
        if (!file) throw std::runtime_error("Failed to open file");
    }

    ~FileHandler() {
        if (file) fclose(file);
    }

    // Use the file...
    void writeData(const char* data) {
        if (file) fputs(data, file);
    }

    // Prevent copying
    FileHandler(const FileHandler&) = delete;
    FileHandler& operator=(const FileHandler&) = delete;
};

// Usage
void processFile() {
    FileHandler fh("example.txt", "w");
    fh.writeData("Hello, RAII!");
    // File is automatically closed when fh goes out of scope
}
```

In this example, the `FileHandler` class uses RAII to manage a file resource:

1. The file is opened in the constructor.
2. If opening fails, an exception is thrown.
3. The file is used via member functions.
4. The destructor automatically closes the file.

This approach ensures that the file is always closed, even if an exception is thrown during `processFile()`.

RAII is not limited to file handling; it's applicable to any resource that needs to be acquired and released, such as:

- Memory allocation
- Network connections
- Database connections
- Mutex locks


> [!NOTE] Title
> "Use modern C++ features to simplify your code and reduce boilerplate."


You're absolutely right. Modern C++ (C++11 and later) introduced many features that simplify code, improve readability, and reduce boilerplate. Here are some key modern C++ features that help achieve these goals:

1. Auto type deduction:
```cpp
auto i = 42;  // int
auto v = std::vector<int>{1, 2, 3};  // std::vector<int>
```

2. Range-based for loops:
```cpp
std::vector<int> numbers = {1, 2, 3, 4, 5};
for (const auto& num : numbers) {
    std::cout << num << " ";
}
```

3. Lambda expressions:
```cpp
auto sum = [](int a, int b) { return a + b; };
std::cout << sum(3, 4);  // Outputs: 7
```

4. nullptr instead of NULL:
```cpp
int* ptr = nullptr;
```

5. Smart pointers:
```cpp
std::unique_ptr<MyClass> ptr = std::make_unique<MyClass>();
```

6. Move semantics and rvalue references:
```cpp
std::vector<int> getVector() {
    return std::vector<int>{1, 2, 3};
}
std::vector<int> v = getVector();  // Efficient move instead of copy
```

7. Uniform initialization syntax:
```cpp
std::vector<int> v{1, 2, 3};
```

8. Delegating constructors:
```cpp
class MyClass {
public:
    MyClass(int x) : MyClass(x, 0) {}
    MyClass(int x, int y) : x_(x), y_(y) {}
private:
    int x_, y_;
};
```

9. constexpr for compile-time computations:
```cpp
constexpr int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}
```

10. Structured bindings (C++17):
```cpp
std::map<std::string, int> myMap = {{"apple", 1}, {"banana", 2}};
for (const auto& [key, value] : myMap) {
    std::cout << key << ": " << value << std::endl;
}
```

These features not only reduce the amount of code you need to write but also make the code more expressive and less error-prone. Would you like me to elaborate on any of these features or provide more examples of how they can be used to simplify C++ code?