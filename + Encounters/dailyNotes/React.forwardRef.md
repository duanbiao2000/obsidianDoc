---
aliases: 
theme: 
high_priority: false
tags:
---
使用 `React.forwardRef` 创建一个带有 `ref` 的 React 组件可以让您在组件内部引用 DOM 元素，这对于需要操作 DOM 或者需要访问底层 DOM 节点的情况非常有用。

下面是一个详细的示例，展示如何创建一个带有 `ref` 的按钮组件，并演示如何在父组件中使用这个带有 `ref` 的子组件。

### 创建带有 `ref` 的按钮组件

1. **定义样式变体**：

   首先，我们需要定义一些样式变体，这将用于生成不同的按钮样式。

   ```typescript
   import { cva, VariantProps } from "class-variance-authority";

   // 定义样式变体
   const buttonVariants = cva("btn", {
     variants: {
       size: {
         sm: "text-sm",
         md: "text-md",
         lg: "text-lg",
       },
       color: {
         primary: "bg-primary text-white",
         secondary: "bg-secondary text-black",
       },
     },
     defaultVariants: {
       size: "md",
       color: "primary",
     },
   });

   // 使用类型来获取所有可能的变体组合
   export type ButtonVariants = VariantProps<typeof buttonVariants>;
   ```

2. **定义按钮组件**：

   使用 `React.forwardRef` 创建一个带有 `ref` 的按钮组件。这个组件可以根据 `asChild` 属性来决定是否使用 `Slot` 组件而非普通的 `button` 元素。

   ```typescript
   import React from "react";
   import { Slot } from "@radix-ui/react-slot";
   import { cn } from "tailwind-merge";
   import { buttonVariants, ButtonVariants } from "./buttonVariants";

   interface ButtonProps extends ButtonVariants {
     className?: string;
     asChild?: boolean;
     children: React.ReactNode;
   }

   const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
     ({ className, variant, size, asChild = false, children, ...props }, ref) => {
       // 根据 asChild 属性决定使用 Slot 组件还是普通的 'button' 元素。
       const Comp = asChild ? Slot : "button";

       // 返回一个 Comp 组件（Slot 或 button），并应用相应的样式。
       // cn 函数用于合并不同的样式，
       // buttonVariants 函数根据 variant、size 和 className 生成样式。
       // ref 和 ...props 确保了 ref 和所有其他属性都被正确地传递给按钮元素。
       return (
         <Comp
           className={cn(buttonVariants({ variant, size, className }))}
           ref={ref}
           {...props}
         >
           {children}
         </Comp>
       );
     }
   );

   export default Button;
   ```

### 使用带有 `ref` 的按钮组件

接下来，我们将在父组件中使用这个带有 `ref` 的按钮组件，并演示如何通过 `ref` 访问底层的 DOM 元素。

1. **父组件**：

   ```typescript
   import React, { useRef, useEffect } from "react";
   import Button from "./Button";

   function App() {
     // 创建一个 ref，用于引用按钮元素
     const buttonRef = useRef<HTMLButtonElement>(null);

     // 使用 useEffect 来演示如何通过 ref 访问 DOM 元素
     useEffect(() => {
       if (buttonRef.current) {
         console.log("按钮的文本内容:", buttonRef.current.innerText);
         // 你可以在这里进行任何 DOM 操作，比如聚焦按钮
         buttonRef.current.focus();
       }
     }, []);

     return (
       <div>
         <Button variant="primary" size="md" ref={buttonRef}>
           点击我
         </Button>
       </div>
     );
   }

   export default App;
   ```

### 解释

1. **创建 `ref`**：
   - 使用 `useRef` 创建一个 `ref`，这个 `ref` 可以引用底层的 DOM 元素。

2. **传递 `ref`**：
   - 在 `Button` 组件中通过 `ref` 属性传递 `ref`。

3. **访问 DOM 元素**：
   - 在 `useEffect` 中，通过 `buttonRef.current` 访问底层的 DOM 元素，并进行一些操作，如打印按钮的文本内容或聚焦按钮。

通过这种方式，您可以创建一个带有 `ref` 的按钮组件，并在父组件中通过 `ref` 访问和操作底层的 DOM 元素。这种方法在需要直接操作 DOM 的情况下非常有用，尤其是在需要聚焦、滚动或执行其他 DOM 相关任务时。