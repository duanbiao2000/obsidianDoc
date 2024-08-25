
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

### 2. 字面量类型（Literal Types）：

字面量类型允许你使用特定的值作为类型，而不仅仅是数据值。这有助于缩小变量的范围，使代码更加清晰和具有更严格的类型检查。示例：

```typescript
// 字面量类型
let dayOfWeek: "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" = "Monday";

// 使用字面量类型
function getDay(day: "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday"): string {
  return `Today is ${day}`;
}

console.log(getDay("Wednesday")); // 输出: Today is Wednesday

// 使用常量和变量
const weekend: "Saturday" | "Sunday" = "Saturday";
let today: "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" = "Friday";
```


