---
aliases: 
theme: 
important: false
date: 2024-12-14 12:33
update: 
tags:
---

```js
{

"compilerOptions": {
	"target": "es5",
	"lib": ["dom", "dom.iterable", "esnext"],
	"allowJs": true,
	"skipLibCheck": true,
	"esModuleInterop": true,
	"allowSyntheticDefaultImports": true,
	"strict": false,
	"forceConsistentCasingInFileNames": true,
	"noFallthroughCasesInSwitch": true,
	"module": "esnext",
	"moduleResolution": "node",
	"resolveJsonModule": true,
	"isolatedModules": true,
	"noEmit": true,
	"jsx": "react-jsx",
	"baseUrl": ".",
	"paths": {
	"@/*": ["src/*"]
	}
},
"include": ["src"]
}
```

这是一个 TypeScript 配置文件 `tsconfig.json`，用于配置 TypeScript 编译器的选项。下面是各个配置项的解释：

- `compilerOptions`: 编译选项，用于配置 TypeScript 编译器的行为。
  - `target`: 指定 ECMAScript 目标版本，这里设置为 ES5。
  - `lib`: 指定要包含在编译中的库文件，这里包括 DOM、DOM 可迭代对象和 ESNext。
  - `allowJs`: 允许编译 JavaScript 文件。
  - `skipLibCheck`: 跳过库文件的类型检查。
  - `esModuleInterop`: 启用 ES 模块互操作性。
  - `allowSyntheticDefaultImports`: 允许从没有默认导出的模块中默认导入。
  - `strict`: 关闭所有严格类型检查选项。
  - `forceConsistentCasingInFileNames`: 强制文件名的大小写一致。
  - `noFallthroughCasesInSwitch`: 报告 switch 语句中的错误：没有 `break`、`return` 或 `throw` 的 case。
  - `module`: 指定模块系统，这里设置为 ESNext。
  - `moduleResolution`: 指定模块解析策略，这里设置为 Node。
  - `resolveJsonModule`: 允许导入 JSON 模块。
  - `isolatedModules`: 启用隔离模块，确保每个文件都可以单独编译。
  - `noEmit`: 不生成输出文件。
  - `jsx`: 指定 JSX 代码的转换方式，这里设置为 `react-jsx`。
  - `baseUrl`: 设置基础目录用于解析非相对模块名称。
  - `paths`: 设置模块名称到基准 URL 的映射，这里将 `@/*` 映射到 `src/*`。

- `include`: 指定要包含在编译中的文件或文件夹，这里包括 `src` 文件夹。

这个配置文件主要用于 TypeScript 项目，特别是使用 React 的项目。它允许开发者使用最新的 JavaScript 特性，同时保持与旧版浏览器的兼容性。通过配置 `paths`，开发者可以使用简短的别名来引用模块，提高代码的可读性和可维护性。
