
### 1. 枚举（Enum）：

枚举是 TypeScript 中的一种数据类型，用于定义一组命名的常量值。它为一组相关的数值提供了友好的名字，增加了代码的可读性和可维护性。示例：

```typescript
// 枚举类型
enum Direction {
  Up,
  Down,
  Left,
  Right,
}

// 使用枚举
let userDirection: Direction = Direction.Up;
console.log(userDirection); // 输出: 0 (Up)

// 可以显式指定枚举值
enum Status {
  Active = "ACTIVE",
  Inactive = "INACTIVE",
}

let userStatus: Status = Status.Active;
console.log(userStatus); // 输出: ACTIVE
```


