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
