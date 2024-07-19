---
aliases: 
tags: 
theme: 
original: 
url: 
author: 
created_date: 2023-07-23 17:02
date updated: 2024-07-14 17:02
type: 
high priority: false
---


```tsx
// in src/index.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { App } from './App';

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
```

```tsx
// in src/App.tsx
import { Admin, Resource, ListGuesser, EditGuesser, ShowGuesser } from 'react-admin';
import { dataProvider } from './dataProvider';

export const App = () => (
    <Admin dataProvider={dataProvider}>
    </Admin>
);
```
在给定的代码中，我们可以看到以下内容：
1. `react-admin` 库被导入，其中包含了一些用于构建管理界面的组件和工具。
2. `dataProvider` 被导入，它是一个用于与后端数据交互的数据提供程序。
3. `App` 组件被定义，它是一个函数式组件。
4. 在 `App` 组件中，我们使用 `Admin` 组件作为根组件。`Admin` 组件是 `react-admin` 的核心组件，用于创建管理界面。
5. `dataProvider` 被传递给 `Admin` 组件，以提供数据交互功能。
6. 在 `Admin` 组件中，我们可以添加多个资源（Resource）。每个资源代表了管理界面中的一个实体（Entity），如用户、文章等。资源可以用于展示、编辑、查看等操作。
7. 在给定的代码中，还没有添加具体的资源配置。`ListGuesser`、`EditGuesser` 和 `ShowGuesser` 是一些辅助组件，用于根据数据结构自动猜测资源的展示、编辑和查看界面。你可以根据需要替换这些组件，并根据实际情况配置资源的展示和交互功能。
总结：给定的代码是
使用 `react-admin` 构建管理界面的示例，使用 `Admin` 组件作为根组件，并通过 `dataProvider` 提供数据交互功能。资源可以通过配置来定义，并使用辅助组件自动猜测资源的展示、编辑和查看界面。你可以根据实际需求进行进一步的配置和定制。



## 整合代码

 好的,把之前讨论的代码整合起来,可以是这样一个更完整的`App`组件:
```jsx
// App.js
import { Admin, Resource, List, Edit, Create, Show } from 'react-admin';
import { Menu, MenuItem, SubMenu } from 'react-admin';
import { PrivateRoute } from 'react-router';
import { dataProvider } from './dataProvider'; 
import { CustomList } from './components/CustomList';

const CustomeList=props=>(
  <List
    {...props}
    filter={{status:'published'}}
    perPage={50}
  />
)


export const App = () => (
  <Admin dataProvider={dataProvider} menu={Menu}>
    <PrivateRoute 
      role="admin"
      path="/users"
      component={UserList} 
    />
    <Resource
      name="users"
      list={CustomList}
      
      edit={<Edit fields={['id', 'name', 'email']} />}
      create={<Create fields={['name', 'email']}/>}
      show={<Show fields={['id', 'name', 'email']}/>}  
    />
    <MenuItem />
    <SubMenu />
  </Admin>
);
```


- 使用react-admin的List和Datagrid构建列表视图
- 定义字段显示
- 配置点击行编辑
- 展示嵌套字段
- 可扩展更多列表功能如过滤、分页等
 可以通过在UserList组件中添加更多配置,来扩展这个列表视图的功能,例如:
1. 添加过滤
```jsx
<List filters={[
  <TextInput source="q" label="Search" alwaysOn />
]}>
```
2. 添加分页
```jsx 
<List pagination={<Pagination perPage={10} />}> 
```
3. 添加排序
```jsx
<List sort={{ field: 'name', order: 'ASC' }}>
```
4. 自定义操作按钮
```jsx
<List actions={<Button>自定义操作</Button>}>  
```
5. 自定义列表头
```jsx
<List bulkActionButtons={false}> 
  <Datagrid>
   <CustomHeader />
  </Datagrid>
</List>
```
我们可以灵活组合使用这些配置,例如:
```jsx
export const UserList = () => (
  <List 
    filters={...}
    pagination={...} 
    actions={...}
  >
    <Datagrid>
      ...
    </Datagrid>
  </List>
)
```
这样可以得到一个功能更丰富的列表页面,提供过滤、排序、自定义操作等功能。
```diff
// in src/App.tsx
-import { Admin, Resource, ListGuesser, EditGuesser, ShowGuesser } from 'react-admin';
+import { Admin, Resource } from "react-admin";
import { dataProvider } from './dataProvider';
+import { UserList } from "./users";

export const App = () => (
  <Admin dataProvider={dataProvider}>
-   <Resource name="users" list={ListGuesser} />
+   <Resource name="users" list={UserList} />
  </Admin>
);
```
