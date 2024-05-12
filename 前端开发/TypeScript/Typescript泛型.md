2024-02-20 11:22
 在泛型中,常用的类型参数代表如下:
- T - Type的缩写,表示一个泛型类型参数。代表具体的类型如string、number等。
- K - Key的缩写,表示一个泛型类型参数。通常用来表示对象或映射中的键类型。
- V - Value的缩写,表示一个泛型类型参数。通常用来表示对象或映射中的值类型。 
- E - Element的缩写,表示一个泛型类型参数。通常用来表示数组或集合中的元素类型。
- R - Result的缩写,表示一个泛型类型参数。通常用来表示函数返回值类型。
其他还有:
- P - 参数
- O - 对象 
- I - 输入
- U - 泛型约束类型参数
- A - 第一个类型参数
- B - 第二个类型参数
- C - 第三个类型参数
# 泛型
 TypeScript提供了很多有用的类型定义和工具来帮助我们开发更好的代码:

- `Generic<T>`:定义泛型类型,可以在函数、类、接口中使用,让代码更通用和类型安全
## 工具类型
- `Partial<T>`:将类型T中的所有属性变为可选属性
- `Required<T>`:将类型T中的所有属性变为必选属性  
- `Readonly<T>`:将类型T中的所有属性变为只读属性
- `Record<K extends keyof any, T>`:由键值对组成的类型,其中K为字符串或数值字面量类型,T为类型参数
- `Pick<T, K extends keyof T>`:从T中选择部分属性类型组成一个新类型
- `Omit<T, K extends keyof T>`:从T中剔除一些属性类型
- `Exclude<T, U>`: T中排除可以赋值给U的类型
- `Extract<T, U>`:提取 T中可以赋值给U的类型
- `NonNullable<T>`:从T中排除null和undefined
- `Parameters<T extends (...args: any) => any>`:获取函数类型T的参数类型元组
- `ReturnType<T extends (...args: any) => any>`:获取函数类型T的返回值类型
- `InstanceType<T extends new (...args: any) => any>`:获取构造函数类型T的实例类型
### 接口
- `interface`:定义对象的结构类型
### 类型断言
- `as`:用于手动指定一个值的类型
- `<T>`:将一个联合类型断言为一个更具体的类型
所以在开发中合理利用这些类型定义和工具,可以大大提升代码的类型安全性和可维护性。

 TypeScript中最常用的工具类型主要有以下几个:
### Partial
`Partial`用于将类型中的所有属性变为可选的。这经常用在需要对对象进行部分更新的场景。
### Required 
`Required`的作用正好与`Partial`相反,它将类型中的所有属性变为必选的。
### Pick
`Pick`用于从一个类型中选择出部分属性来构成一个新类型。
### Omit
`Omit`与`Pick`相反,它用于从一个类型中剔除某些属性,生成一个新的类型。
### Record
`Record`用于将类型的所有属性值转化为同一个类型,常用于定义映射类型。
### Extract/Exclude
`Extract`用于从联合类型中提取某个类型,`Exclude`用于从联合类型中排除某个类型。
### NonNullable
`NonNullable`用于从一个类型中排除`null`和`undefined`。
### Parameters/ReturnType
`Parameters`和`ReturnType`用于从函数类型中提取参数类型和返回值类型。
### InstanceType
`InstanceType`用于从类类型中提取实例类型。
以上这些类型在日常开发中使用频率最高。其中`Partial`、`Required`、`Pick`、`Omit`、`Record`用得最广泛,解决对象属性转换的需求。`Extract`和`Exclude`也很常见,用于处理联合类型。
所以如果要选择熟悉几个类型,我推荐先了解这些类型。掌握了它们,基本可以解决大多数类型转换和提取的需求。


## CRUD

 ```typescript
// Employee.ts
interface Employee {
  id: number;
  name: string;
}
// EmployeeService.ts
class EmployeeService {
  private employees: Employee[] = [];
  addEmployee(employee: Employee) {
    this.employees.push(employee);
  }
  getEmployees(): Employee[] {
    return this.employees;
  }
  getEmployeeById(id: number): Employee | undefined {
    return this.employees.find(employee => employee.id === id);
  }
}
// index.ts
import { EmployeeService } from './EmployeeService';
const service = new EmployeeService();
const employee1: Employee = {
  id: 1,
  name: 'John'  
};
service.addEmployee(employee1);
const employees = service.getEmployees();
console.log(employees); 
const employee = service.getEmployeeById(1);
console.log(employee);
```
此代码使用TypeScript中的一些最佳实践:
- 定义Employee接口描述对象结构
- EmployeeService类提供CRUD方法
- 使用泛型和类型断言保证类型安全
- 添加注释说明代码结构和用途
- 使用严格的tsconfig.json进行编译
- 注重代码结构和逻辑的清晰性
整体实现了一个简单的增删改查操作,展示了TypeScript在面向对象开发中的一些最佳用法。


## 三种泛型

TypeScript中的泛型主要有以下三种:
### 函数泛型
函数泛型可以为函数参数和返回值定义类型参数,使函数变得更通用:
```ts
function identity<T>(arg: T): T {
  return arg;
}
```
### 类泛型
类泛型可以为类定义类型参数,使类中的属性和方法支持不同类型:
```ts 
class GenericNumber<T> {
  zeroValue: T;
  add(x: T, y: T): T {
    return x + y;
  }
}
```
### 接口泛型
接口泛型可以为接口定义类型参数,使接口支持不同类型:
```ts
interface GenericInterface<T> {
  data: T;
}
interface GenericArray<T> {
  list: T[];
}
```
这三种泛型的区别:
- 函数泛型用于定义函数的类型参数
- 类泛型用于定义类的类型参数
- 接口泛型用于定义接口的类型参数
它们都可以为代码元素(函数、类、接口)引入类型参数,从而支持多种类型,提高代码的灵活性和复用性。
通过泛型,我们可以定义出通用的代码结构,这在TypeScript中是一项非常重要的特性。

## 泛型

 TypeScript 中泛型(Generics)的作用是在定义函数、接口或类的时候,不预先指定具体的类型,而在使用的时候再指定类型的一种特性。主要的目的是提高复用性和灵活性。
常见的泛型语法包括:
1. 定义泛型函数或接口:
```ts
function identity<T>(arg: T): T {
  return arg;
}

interface GenericIdentityFn<T> {
  (arg: T): T;
}
```
使用T、U等字母来定义类型参数。
2. 调用泛型函数时传入实际类型:
```ts
let output = identity<string>("myString"); 
```
3. 泛型类型中的类型约束:
```ts
function loggingIdentity<T>(arg: T): T {
    console.log(arg.length); 
    return arg;
}
```
这里由于需要使用arg的length属性,需要对T加上约束`extends { length: number }`。
4. 泛型接口与泛型类:
```ts
interface GenericIdentityFn<T> {
  (arg: T): T;
}
class GenericNumber<T> {
  zeroValue: T;
  add: (x: T, y: T) => T;
}
```
总结来说,泛型可以帮助我们灵活地重用类型逻辑,提高代码复用性,是TypeScript类型系统的重要组成部分。

### 泛型的限制和约束

 TypeScript 中泛型的一些限制和约束包括:
1. 不能直接使用泛型类型实例化,必须传入实际类型:
```ts
let myGeneric: Generic<string> // Error
let myGeneric: Generic<any> // Error 
let myGeneric: Generic<string> = new Generic<string>(); // Ok
```
2. 静态属性不能使用泛型类型:
```ts 
class Generic<T> {
  static prop: T; // Error
}
```
3. 泛型约束必须满足“逆变”或“协变”:
```ts
interface X {
  foo: string;
}
class A {
  x!: X; 
}
class B extends A {
  x!: { foo: string }; 
} 
// Allowed as {foo: string} satisfies constraint
let b: B = new Generic<X>(); 
// Not allowed as X doesn't satisfy constraint
let a: A = new Generic<{foo: string}>(); 
```
4. 泛型不能约束具体内置类型如 string、number等。
5. 对于泛型的类型参数不能部分约束,只能全约束或不约束。
6. 不能同时使用泛型和全局类型声明为同一个类型起多个名字。
总之,正确使用泛型可以提高复用性,但也需要注意泛型的这些限制,避免出现难以定位的错误。


在代码 `import { FC } from 'react'` 中，`FC` 是指 React 的函数组件类型，它是 React TypeScript 类型定义的一部分。
在 React 中，使用函数组件来定义 UI 组件是一种常见的方式。而在 TypeScript 中，为了更好地对组件进行类型检查和推断，可以使用 `FC` 类型来标注函数组件的类型。
`FC` 是一个泛型类型，`FC<Props>` 表示接受一个泛型 `Props`，并返回一个 React 组件的函数类型。通过使用 `FC` 类型，可以为函数组件提供参数类型和返回类型的定义。
例如，一个使用 `FC` 类型的函数组件可以这样定义：
```typescript
import React, { FC } from 'react';
type Props = {
  name: string;
  age: number;
};
const MyComponent: FC<Props> = ({ name, age }) => {
  return (
    <div>
      <p>Name: {name}</p>
      <p>Age: {age}</p>
    </div>
  );
};
export default MyComponent;
```
在上面的示例中，我们使用 `FC<Props>` 将 `Props` 类型作为泛型参数传递给 `FC` 类型，指定了组件接受的属性类型。然后，我们可以在函数组件的参数中解构 `Props` 对象，使用其中的属性来渲染组件的内容。
通过使用 `FC` 类型，可以更好地定义和推断函数组件的类型，提高代码的可读性和可维护性。同时，TypeScript 可以在编译时对函数组件的属性类型进行静态检查，提前发现潜在的类型错误。

在 React TypeScript 中，`interface` 和 `type` 是用来定义类型的两种方式。它们有一些区别和联系，如下所示：
区别：
1. 语法：`interface` 使用 `interface` 关键字来定义，而 `type` 使用 `type` 关键字来定义。
2. 合并能力：当定义同名的 `interface` 时，可以自动合并多个同名的 `interface`，而 `type` 是不会自动合并的。
3. 继承能力：`interface` 可以通过 `extends` 关键字来继承其他接口，而 `type` 可以使用交叉类型（`&`）来组合其他类型。
联系：
1. 目的：`interface` 和 `type` 都用于描述和定义对象的结构和类型。
2. 兼容性：在大多数情况下，`interface` 和 `type` 是可以互换使用的，可以用来定义对象、函数、联合类型、交叉类型等。
3. 扩展：`interface` 和 `type` 都支持扩展，可以添加新的属性或重新定义已有的属性。
4. 可读性：`interface` 更常用于描述对象的结构，因为它有更好的可读性和可维护性。而 `type` 更常用于定义复杂的类型别名，或者对已有类型进行重命名。
总的来说，`interface` 和 `type` 在功能和使用方式上有一些差异，但在大多数情况下可以互换使用。选择使用哪个取决于具体的需求和个人偏好，以及与团队的约定和代码风格的一致性。

这段代码定义了一个名为 `NewDocButtonProps` 的接口，并通过 `extends` 关键字继承了 `React.HTMLAttributes<HTMLButtonElement>` 接口。它是一个用于描述 `NewDocButton` 组件属性的类型声明。
具体来说，`NewDocButtonProps` 继承了 `React.HTMLAttributes<HTMLButtonElement>`，这意味着它包含了 `HTMLButtonElement` 元素的所有标准属性和事件回调。通过继承这个接口，`NewDocButtonProps` 可以接受所有适用于 `<button>` 元素的属性，并且保持了与原生按钮元素一致的类型定义。
使用这个接口可以使 `NewDocButton` 组件能够接受 `<button>` 元素的属性，例如 `className`、`onClick`、`disabled` 等，并且能够通过类型检查来确保传递的属性与按钮元素的属性一致。
例如，可以将 `NewDocButtonProps` 用作 `NewDocButton` 组件的属性类型声明：
```typescript
import React from 'react';
interface NewDocButtonProps extends React.HTMLAttributes<HTMLButtonElement> {}
const NewDocButton: React.FC<NewDocButtonProps> = (props) => {
  return <button {...props}>New Document</button>;
};
export default NewDocButton;
```

在上面的示例中，`NewDocButton` 组件接受 `NewDocButtonProps` 作为属性类型声明，并将传递给组件的所有属性应用到 `<button>` 元素上。通过 `...props`，可以将所有属性传递给按钮元素，使得可以在使用 `NewDocButton` 组件时传递任意有效的按钮属性，并保持类型检查的一致性。
---
aliases:

---
20230806 1004
links: https://www.bilibili.com/video/BV1HF41197bN/?vd_source=7038f96b6bb3b14743531b102b109c43
title:
origin:
tags: #flashcards #todo 

![[Pasted image 20230806100402.png]]
![[Pasted image 20230806101838.png]]
![[Pasted image 20230806103611.png]]
![[Pasted image 20230806105323.png]]
![[Pasted image 20230806105344.png]]


### TypeScript和Flow代码示例

下面是TypeScript和Flow的代码示例和注释：

```typescript
// TypeScript示例
interface Person {
  name: string;
  age: number;
}
function greet(person: Person): string {
  return `Hello, ${person.name}! You are ${person.age} years old.`;
}
const alice: Person = { name: 'Alice', age: 20 };
console.log(greet(alice));
// Flow示例
type Person = {
  name: string,
  age: number,
};
function greet(person: Person): string {
  return `Hello, ${person.name}! You are ${person.age} years old.`;
}
const alice: Person = { name: 'Alice', age: 20 };
console.log(greet(alice));
```
TypeScript和Flow都是用于静态类型检查的工具，它们可以在JavaScript代码中添加类型注释，并在编译或运行之前进行类型检查。以上示例中，我们定义了一个Person接口（TypeScript）或类型（Flow），并使用它来指定参数和变量的类型。在函数中，我们使用模板字符串来拼接字符串，并返回相应的问候语。最后，我们创建了一个名为alice的Person对象，并将其传递给greet函数进行打印。

TypeScript和Flow都是用于在JavaScript中添加静态类型检查的工具，它们的目标是提供更可靠和健壮的代码。以下是TypeScript和Flow之间的几个主要区别：

1. 语言类型：TypeScript是一种完整的编程语言，它在JavaScript的基础上添加了类型注解和其他语言特性，以创建类型安全的代码。Flow是一个静态类型检查工具，使用了类型推断和类型注释来分析代码中的类型信息，但它本身不是一种独立的编程语言。
2. 发展历史：TypeScript由微软开发并于2012年发布，它在JavaScript社区中得到了广泛的应用和支持。Flow由Facebook开发，并于2014年发布，主要用于Facebook内部的JavaScript代码。
3. 类型注解：在TypeScript中，类型注解是必需的，用于指定变量、函数参数、函数返回值等的类型。在Flow中，类型注解是可选的，可以根据需要选择性地添加类型注解。
4. 类型系统：TypeScript的类型系统相对更严格和复杂，支持接口、类、枚举等高级类型。Flow的类型系统相对较简单，但仍可以满足大多数需求。
5. 生态系统和工具支持：TypeScript拥有更大的生态系统和更广泛的工具支持，包括编辑器插件（如VS Code）、构建工具（如Webpack）和第三方库。Flow的生态系统相对较小，但在一些大型项目和Facebook内部仍有广泛应用。
  总体而言，TypeScript更成熟、更广泛地应用于生产环境，并且拥有更丰富的工具和社区支持。Flow则更轻量、更简单，并适合于小型项目或对类型系统需求不太严格的场景。选择使用哪个工具取决于个人偏好、项目需求和团队情况。

#### TypeScript高级类型

TypeScript提供了许多高级类型特性，可以帮助开发人员更好地管理和操作类型。以下是一些常见的高级类型示例和使用场景：

1. 泛型（Generics）：允许在函数、类和接口中使用类型参数，以提供灵活的类型定义。
```typescript
function identity<T>(arg: T): T {
  return arg;
}
const result = identity<string>('Hello');
```
使用场景：当需要编写可重用的函数或类，但不确定要使用的具体类型时，可以使用泛型。
2. 联合类型（Union Types）和交叉类型（Intersection Types）：联合类型允许一个值具有多个可能的类型，交叉类型将多个类型合并为一个新的类型。
```typescript
type NumberOrString = number | string;
function printId(id: NumberOrString): void {
  console.log(id);
}
type User = {
  name: string;
};
type Admin = {
  role: string;
};
type AdminUser = User & Admin;
```
使用场景：联合类型可用于处理多种类型的参数或变量，交叉类型可用于合并多个类型的属性和方法。
3. 类型别名（Type Aliases）和字面量类型（Literal Types）：类型别名允许为现有类型创建一个新名称，字面量类型允许指定具体的值作为类型。
```typescript
type Color = 'Red' | 'Blue' | 'Green';
type Point = {
  x: number;
  y: number;
};
type Rectangle = {
  topLeft: Point;
  bottomRight: Point;
};
```
使用场景：类型别名可用于简化复杂类型的使用，字面量类型可用于限制变量或参数的取值范围。
4. 映射类型（Mapped Types）：允许以一种简洁的方式转换和操作现有类型的属性。
```typescript
type Person = {
  name: string;
  age: number;
};
type ReadonlyPerson = Readonly<Person>;
type PartialPerson = Partial<Person>;
```
使用场景：映射类型可用于根据现有类型创建新类型，例如将所有属性设为只读或可选。
5. 条件类型（Conditional Types）：根据类型的条件判断来选择不同的类型。
```typescript
type IsArray<T> = T extends Array<any> ? true : false;
type Result = IsArray<number[]>;
```
使用场景：条件类型可用于根据类型的条件判断执行不同的类型逻辑。
这些高级类型示例展示了TypeScript的一些强大功能，可以帮助开发人员更好地管理和操作类型。根据不同的需求和场景，可以灵活使用这些特性来提高代码的可读性和健壮性。

[[CSS预处理]]

[[React关键技术]]