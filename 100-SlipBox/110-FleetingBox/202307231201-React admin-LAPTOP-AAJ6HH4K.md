---
aliases:

---
20230723 1201
links: [React-admin - My First Project Tutorial (marmelab.com)](https://marmelab.com/react-admin/Tutorial.html)
title:
origin:
tags: #flashcards #todo 

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

## Using an API As Data Source
React-admin apps are single-Page-Apps (SPAs) running in the browser, and fetching data from an API. Since there is no standard for data exchanges between computers, react-admin needs an adapter to talk to your API. This adapter is called a _Data Provider_.

For this tutorial, we’ll be using [JSONPlaceholder](https://jsonplaceholder.typicode.com/), a fake REST API designed for testing and prototyping, as the data source for the application. Here is what it looks like:

```plaintext
curl https://jsonplaceholder.typicode.com/users/2
```

```json
{
  "id": 2,
  "name": "Ervin Howell",
  "username": "Antonette",
  "email": "Shanna@melissa.tv",
  "address": {
    "street": "Victor Plains",
    "suite": "Suite 879",
    "city": "Wisokyburgh",
    "zipcode": "90566-7771",
    "geo": {
      "lat": "-43.9509",
      "lng": "-34.4618"
    }
  },
  "phone": "010-692-6593 x09125",
  "website": "anastasia.net",
  "company": {
    "name": "Deckow-Crist",
    "catchPhrase": "Proactive didactic contingency",
    "bs": "synergize scalable supply-chains"
  }
}
```
JSONPlaceholder provides endpoints for users, posts, and comments. The admin we’ll build should allow to Create, Retrieve, Update, and Delete (CRUD) these resources.↳

The `test-admin` project you just created already contains a data provider pre-configured for JSONPlaceholder.

```tsx
// in src/dataProvider.ts
import jsonServerProvider from 'ra-data-json-server';

export const dataProvider = jsonServerProvider(
    import.meta.env.VITE_JSON_SERVER_URL
);
```
 这段代码使用 `ra-data-json-server` 库来创建一个 `dataProvider`。
主要步骤:
1. 从 `ra-data-json-server` 中导入 `jsonServerProvider` 函数。
2. 调用 `jsonServerProvider` 函数,并传入 JSON Server 的 URL。
3. 这里的 URL 使用了 Vite 的环境变量 `VITE_JSON_SERVER_URL`。这允许在不同环境中动态配置 JSON Server 的地址。
4. `jsonServerProvider` 函数会返回一个适用于 `react-admin` 的 `dataProvider`。
5. 这个 `dataProvider` 知道如何调用 JSON Server API 来获取数据。
6. 最后导出这个 `dataProvider` 实例,以供 `App` 组件使用。
总结:
- 使用 `ra-data-json-server` 创建适用于 JSON Server 的 `dataProvider`。
- 利用环境变量动态配置 JSON Server 的地址。
- 将 `dataProvider` 导出供 Admin 组件使用。
所以这段代码允许通过 JSON Server 提供了一个 mock 的 REST API,来动态获取 `react-admin` 所需的数据。

**Tip**: The `import.meta.env.VITE_JSON_SERVER_URL` expression is a [Vite environment variable](https://vitejs.dev/guide/env-and-mode.html). It’s set to `https://jsonplaceholder.typicode.com` in the `.env` file at the root of the project.


```diff
// in src/App.tsx
import { Admin, Resource, ListGuesser, EditGuesser, ShowGuesser } from 'react-admin';
import { dataProvider } from './dataProvider';

export const App = () => (
  <Admin dataProvider={dataProvider}>
+   <Resource name="users" list={ListGuesser} />
  </Admin>
);
```

 在这个更新后的`App`组件中,主要增加了一个`Resource`的配置:
```js
<Resource name="users" list={ListGuesser} />
```
这个`Resource`代表了一个叫做"users"的实体资源,通常对应于后端的一个用户数据表。
`name`属性指定了资源的名称。
`list`属性配置了该资源在列表视图下的组件。这里使用了`ListGuesser`组件,它会根据数据的结构自动生成一个列表视图。
这样,在管理界面中,就会有一个对应的"Users"菜单项。点击进入会看到一个用户列表视图,显示所有用户的数据。
`ListGuesser`组件提供了一个默认的列表布局和功能。我们还可以继续配置:
- `edit` - 编辑视图组件 
- `create` - 创建视图组件
- `show` - 查看视图组件
以及定义每个视图所需的字段,过滤、排序等功能。
总结:
- `Resource`定义了一个实体资源
- `name`指定资源名称
- `list`配置列表视图组件  
- 这里使用`ListGuesser`自动生成一个默认的列表视图
- 可以继续配置其他视图和功能
这让我们可以快速搭建一个拥有基本CRUD功能的管理界面。

 好的,我们可以继续在`Resource`上配置`edit`、`create`和`show`视图:
```jsx
<Resource 
  name="users"
  list={ListGuesser}
  edit={EditGuesser}
  create={CreateGuesser}
  show={ShowGuesser}
/>
```
- `edit`: 配置编辑视图组件,使用`EditGuesser`自动生成编辑表单
- `create`: 配置创建视图组件,使用`CreateGuesser`自动生成创建表单
- `show`: 配置查看视图组件,使用`ShowGuesser`自动生成详细信息页面
这样,我们就拥有了一个完整的CRUD(创建、读取、更新、删除)资源配置:
- `list` - 读取列表数据
- `edit` - 更新编辑数据  
- `create` - 创建新数据
- `show` - 读取单个数据详情
这提供了一个非常快速构建管理界面资源的方式。
当然,实际应用中,我们还可以继续深度定制:
- 使用自定义组件,而不是`XxxGuesser`
- 配置每个视图显示的字段
- 添加过滤、排序、分页等功能
- 添加菜单和子菜单
- 权限管理等等
以完全符合实际业务需求。但当前的配置已经可快速搭建出一个基础的CRUD管理界面。

 好的,我们可以继续深度定制这个Resource的各个视图和功能:
1. 使用自定义组件替换Guesser组件
例如创建一个CustomList组件,实现自定义的列表视图。
```jsx
list={CustomList} 
```
2. 配置各视图显示的字段
通过`field`属性指定每个视图需要展示的字段
```jsx
<Resource
  // ...
  edit={<EditGuesser fields={['id', 'name', 'email']}/>}
/>  
```
3. 添加过滤、排序、分页等功能
可以通过`filter`、`sort`、`pagination`等属性配置
```jsx 
<Resource
  // ...
  list={props => <List {...props} filter={{ status: 'published' }} perPage={50} />}
/>
```
4. 添加菜单和子菜单
通过`<MenuItem>`和`<SubMenu>`配置菜单
```jsx
<Menu>
  <MenuItem /> 
  <SubMenu />
</Menu>
```
5. 权限管理
可以结合类似`react-router`的权限路由,以及配合后端角色权限系统实现
```jsx
<PrivateRoute 
  role="admin"
  path="/users"
  component={UserList} 
/>
```
以上是一些常见的定制方式,可以让我们深入地个性化定制每个资源的界面和功能,完全符合实际业务需求。

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
这个组件包含:
- 自定义列表组件
- 各视图的字段配置 
- 权限路由校验
- 菜单配置
这样可以快速搭建一个功能完备的管理后台系统。
当然,实际应用中要根据具体业务需要继续深化开发,但这提供了一个可快速起步的框架代码。

The `<ListGuesser>` component is not meant to be used in production - it’s just a way to quickly bootstrap an admin. That means you’ll have to replace the `ListGuesser` component in the `users` resource by a custom React component. Fortunately, `ListGuesser` dumps the code of the list it has guessed to the console:

Let’s copy this code, and create a new `UserList` component, in a new file named `users.tsx`:
```tsx
// in src/users.tsx
import { List, Datagrid, TextField, EmailField } from "react-admin";

export const UserList = () => (
    <List>
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <TextField source="name" />
            <TextField source="username" />
            <EmailField source="email" />
            <TextField source="address.street" />
            <TextField source="phone" />
            <TextField source="website" />
            <TextField source="company.name" />
        </Datagrid>
    </List>
);
```
 这是一个使用react-admin的UserList组件的示例代码,主要功能点如下:
1. 默认导出一个名为UserList的React组件。
2. 使用List和Datagrid组件来渲染用户列表。
3. Datagrid组件上的rowClick="edit"属性允许点击表格行时跳转到编辑视图。
4. 使用一系列TextField和EmailField组件来定义每个用户的字段,source属性指定从API数据中取出的字段名称。
5. address和company这样的嵌套字段,可以通过source的点式表示来获取,如address.street。
6. 这样就可以快速构建出一个用户列表视图,显示主要字段并可以点击编辑。
7. 可以继续在List上添加filter、pagination、sort等配置,丰富列表功能。
8. 这个组件可以和App组件结合使用,作为User资源的list属性传入。
总结:
- 使用react-admin的List和Datagrid构建列表视图
- 定义字段显示
- 配置点击行编辑
- 展示嵌套字段
- 可扩展更多列表功能如过滤、分页等
 好的,我们可以通过在UserList组件中添加更多配置,来扩展这个列表视图的功能,例如:
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

React-admin offers a large library of components you can pick from to build the UI that you want using composition. And if this is not enough, it lets you build your own components to get exactly the UI you want.

### Writing A Custom List Component

The react-admin layout is already responsive. Try to resize your browser to see how the sidebar switches to a drawer on smaller screens. Besides, the `<SimpleList>` component is a really good fit for mobile devices.
But on desktop, `<SimpleList>` takes too much space for a low information density. So let’s modify the `<UserList>` component to use the `<Datagrid>` component on desktop, and the `<SimpleList>` component on mobile.

To do so, we’ll use [the `useMediaQuery` hook](https://mui.com/material-ui/react-use-media-query/) from Material UI:

```tsx
// in src/users.tsx
import { useMediaQuery, Theme } from "@mui/material";
import { List, SimpleList, Datagrid, TextField, EmailField } from "react-admin";

export const UserList = () => {
    const isSmall = useMediaQuery<Theme>((theme) => theme.breakpoints.down("sm"));
    return (
        <List>
            {isSmall ? (
                <SimpleList
                    primaryText={(record) => record.name}
                    secondaryText={(record) => record.username}
                    tertiaryText={(record) => record.email}
                />
            ) : (
                <Datagrid rowClick="edit">
                    <TextField source="id" />
                    <TextField source="name" />
                    <TextField source="username" />
                    <EmailField source="email" />
                    <TextField source="address.street" />
                    <TextField source="phone" />
                    <TextField source="website" />
                    <TextField source="company.name" />
                </Datagrid>
            )}
        </List>
    );
};
```
 这段代码实现了根据屏幕大小显示不同的用户列表布局。
主要逻辑:
1. 通过useMediaQuery钩子获取当前屏幕是否小于sm大小。
2. 如果屏幕较小,使用SimpleList组件,只显示主要信息。
3. 如果屏幕较大,使用Datagrid组件,显示完整的列信息。
4. SimpleList组件使用primaryText、secondaryText等属性显示关键字段。
5. Datagrid组件定义各列并可点击编辑。
6. 根据isSmall的值有条件地渲染不同的列表组件。
这样可以实现响应式的用户列表:
- 在手机等小屏幕上只显示主要信息,节省空间
- 在大屏幕上显示完整的用户信息
同时代码也实现了配置中的常见模式:
- 条件渲染组件
- 响应式设计
- 组件复用
通过结合React Admin和React Hooks,可以灵活实现复杂的列表需求。

```ts
useMediaQuery<Theme>((theme) => theme.breakpoints.down("sm"))
```
 这个useMediaQueryhooks用法中的泛型Theme和回调函数的作用是:
1. `useMediaQuery` 本身是一个接受media query条件并返回是否匹配的hooks。
2. 这里使用了[[../../前端开发/TypeScript/typerscript关键知识#泛型|泛型]]`<Theme>`,目的是为了能够在回调函数中获取到MUI的theme。
3. theme中包含了breakpoints等响应式设计所需的信息。
4. 回调函数会接收theme参数,然后我们比较当前屏幕宽度是否小于theme的sm breakpoint。
5. 回调返回的bool值将赋值给isSmall。
6. 所以isSmall就是一个表示“当前屏幕是否为小屏幕”的状态。
总结:
- `<Theme>`泛型是为了在回调中能访问theme 
- 回调函数利用theme的breakpoints来判断当前屏幕尺寸
- 并将匹配结果赋值给isSmall状态
- 这样isSmall可以区分大屏幕和小屏幕场景
这样利用MUI的theme系统实现了优雅的响应式hooks。
 
 在这个useMediaQuery的回调函数中:
```js
theme.breakpoints.down("sm")
```
theme代表当前MUI主题的配置对象,它包含一些响应式设计需要的信息。
theme.breakpoints则是主题中的断点配置,它有一个down方法。
down方法用来比较当前屏幕宽度是否小于给定的断点。
所以:
- theme - 获取当前MUI主题配置 
- breakpoints - 主题中的断点配置
- down - 比较当前屏幕宽度是否小于某个断点
具体用法:
- theme.breakpoints.down("sm") - 当前宽度是否小于sm断点
- theme.breakpoints.down("md") - 当前宽度是否小于md断点
这样通过theme.breakpoints.down和给定断点的字符串,可以判断当前屏幕的响应式状态,实现响应式组件的逻辑。
所以它是一个非常优雅的利用MUI主题系统来实现响应式hooks的方式。
**Tip**: There is much more to Material UI styles than what this tutorial covers. Read the [Material UI documentation](https://mui.com/system/basics/) to learn more about theming, vendor prefixes, responsive utilities, etc.

 React Admin中的Resource组件用于声明和配置一个资源,它是构建管理后台的基础块。
Resource组件的一些关键特性包括:
1. name - 声明资源的名称,会用于生成URL等
2. list - 配置列表视图组件
3. edit - 配置编辑视图组件 
4. create - 配置创建视图组件
5. show - 配置显示视图组件
6. icon - 为菜单项配置图标
7. options - 一些全局配置选项
一个典型的Resource声明:
```jsx
<Resource
  name="posts"
  list={PostList}
  edit={PostEdit}
  create={PostCreate}
  show={PostShow}
  icon={PostIcon}
/>
```
将多个Resource组合起来,就构成了一个数据管理的应用。
Resource允许通过传入组件来定制各视图,也可以使用像ListGuesser这样的自动生成组件快速构建CRUD界面。
总之,Resource是react-admin中核心的资源配置和入口。

要完成帖子列表，请将帖子 `id` 字段放置在第一列，并删除 `body` 字段。从用户体验的角度来看，包含大块文本的字段不应出现在数据网格中，而只能出现在详细视图中。另外，为了使“编辑”操作脱颖而出，我们将 `rowClick` 操作替换为显式操作按钮：
```diff
// in src/posts.tsx
-import { List, Datagrid, TextField, ReferenceField } from "react-admin";
+import { List, Datagrid, TextField, ReferenceField, EditButton } from "react-admin";

export const PostList = () => (
  <List>
-   <Datagrid rowClick="edit">
+   <Datagrid>
+     <TextField source="id" />
      <ReferenceField source="userId" reference="users" />
-     <TextField source="id" />
      <TextField source="title" />
-     <TextField source="body" />
+     <EditButton />
    </Datagrid>
  </List>
);
```

### Adding Editing Capabilities

An admin interface isn’t just about displaying remote data, it should also allow editing records. React-admin provides an `<Edit>` component for that purpose ; let’s use the `<EditGuesser>` to help bootstrap it.

```diff
// in src/App.tsx
-import { Admin, Resource } from "react-admin";
+import { Admin, Resource, EditGuesser } from "react-admin";
import { dataProvider } from './dataProvider';
import { PostList } from "./posts";
import { UserList } from "./users";

export const App = () => (
    <Admin dataProvider={dataProvider}>
-       <Resource name="posts" list={PostList} />
+       <Resource name="posts" list={PostList} edit={EditGuesser} />
        <Resource name="users" list={UserList} recordRepresentation="name" />
    </Admin>
)
```

` <ReferenceInput>`组件在React Admin中用于实现资源之间的引用关联。
其中:
- source属性:指定当前记录所要引用的字段,此例中是userId字段。
- reference属性:指定被引用的资源名称,此例中是users资源。
这样用法表示:
从当前记录(post)的userId字段值,关联引用到users资源的记录。
当渲染post编辑表单时,会显示一个用户选择输入框,允许选择并关联一个user记录。
在post数据中,会保存所选user的id值到userId字段。
`<ReferenceInput>`常用于实现一对多关联,例如:
- 一篇博客文章关联一个用户作者
- 一张订单关联一个客户
等等。
它通过为资源关系提供便利的编辑输入框,可以更容易实现数据模型的关联设计。
 您说得对,我之前的说明中举的例子表示的是一对一的关系,并不准确。让我重新说明一下:
`<ReferenceInput> `组件通常用来实现一对多的关联关系,例如:
- 一篇博客文章(post)可以关联到一个用户(user)作者。这是一对多关系,一篇文章只能有一个作者,但一个作者可以写多篇文章。
- 一张订单(order)可以关联到一个客户(customer)。一张订单只属一个客户,但一个客户可以有多张订单。
也就是说,在一对多的关系中,Resource组件通常在“多”的一方来使用`<ReferenceInput>`:
```jsx
// 在Post资源中
<ReferenceInput source="userId" reference="users" /> 
// 在Order资源中 
<ReferenceInput source="customerId" reference="customers" />
```
这样通过选择用户或客户来关联博客文章或订单数据。
我之前的一对一举例是不恰当的。感谢您的提醒,帮我更正了对React Admin中关联关系使用的错误理解。这有助于我深入学习如何在React Admin中 properly实现一对多的数据关联。

```diff
// in src/posts.tsx
import {
    List,
    Datagrid,
    TextField,
    ReferenceField,
    EditButton,
    Edit,
+   Create,
    SimpleForm,
    ReferenceInput,
    TextInput,
} from "react-admin";

export const PostList = () => (
  { /* ... */ }
);

export const PostEdit = () => (
  { /* ... */ }
);
+export const PostCreate = () => (
+  <Create>
+    <SimpleForm>
+      <ReferenceInput source="userId" reference="users" />
+      <TextInput source="title" />
+      <TextInput source="body" multiline rows={5} />
+    </SimpleForm>
+  </Create>
+);
```


##  Adding Search And Filters To The List

et’s get back to the post list for a minute. It offers sorting and pagination, but one feature is missing: the ability to search content.

React-admin can use Input components to create a multi-criteria search engine in the list view. Pass an array of such Input components to the List `filters` prop to enable filtering:

```tsx
// in src/posts.tsx
const postFilters = [
    <TextInput source="q" label="Search" alwaysOn />,
    <ReferenceInput source="userId" label="User" reference="users" />,
];

export const PostList = () => (
    <List filters={postFilters}>
        // ...
    </List>
);
```

The first filter, ‘q’, takes advantage of a full-text functionality offered by JSONPlaceholder. It is `alwaysOn`, so it always appears on the screen. Users can add the second filter, `userId`, thanks to the “add filter” button, located on the top of the list. As it’s a `<ReferenceInput>`, it’s already populated with possible users.

 这段代码实现了在PostList组件的列表视图中添加过滤功能。
主要逻辑:
1. 定义了一个postFilters数组,包含两个过滤组件:
   - TextInput:基于q字段实现关键词搜索过滤
   - ReferenceInput:基于userId字段过滤关联的User
2. 在PostList组件中,通过`<List>`的filters属性来使用这些过滤器:
```
<List filters={postFilters}>
```
3. 这样就为Post的列表视图添加了两种过滤方式:
   - 根据标题、内容等搜索关键词过滤
   - 根据关联的User过滤
这是React Admin中的一个常见模式,通过配置filters属性,可以轻松添加列表过滤功能。
并且可以混合不同类型的过滤器,如文本、数值、引用等,过滤条件通过与操作组合,为复杂的列表页面提供强大的查询能力。
这种过滤配置也支持响应式,可以根据不同屏幕调整过滤器的顺序或显示。

## Customizing the Menu Icons

The sidebar menu shows the same icon for both posts and users. Customizing the menu icon is just a matter of passing an `icon` attribute to each `<Resource>`:

```tsx
// in src/App.tsx
import PostIcon from "@mui/icons-material/Book";
import UserIcon from "@mui/icons-material/Group";

export const App = () => (
    <Admin dataProvider={dataProvider}>
        <Resource name="posts" list={PostList} edit={PostEdit} create={PostCreate} icon={PostIcon} />
        <Resource name="users" list={UserList} icon={UserIcon} recordRepresentation="name" />
    </Admin>
);
```

### Using a Custom Home Page

By default, react-admin displays the list page of the first `Resource` element as home page. If you want to display a custom component instead, pass it in the `dashboard` prop of the `<Admin>` component.


```tsx
// in src/Dashboard.tsx
import { Card, CardContent, CardHeader } from "@mui/material";

export const Dashboard = () => (
    <Card>
        <CardHeader title="Welcome to the administration" />
        <CardContent>Lorem ipsum sic dolor amet...</CardContent>
    </Card>
);
```

```tsx
// in src/App.tsx
import { Dashboard } from './Dashboard';

export const App = () => (
    <Admin dataProvider={dataProvider} dashboard={Dashboard} >
          // ...
    </Admin>
);
```

### Adding a Login Page

Most admin apps require authentication. React-admin can check user credentials before displaying a page, and redirect to a login form when the REST API returns a 403 error code.↳

_What_ those credentials are, and _how_ to get them, are questions that you, as a developer, must answer. React-admin makes no assumption about your authentication strategy (basic auth, OAuth, custom route, etc.), but gives you the ability to add the auth logic at the right place - using the `authProvider` object.

For this tutorial, since there is no public authentication API, we can use a fake authentication provider that accepts every login request, and stores the `username` in `localStorage`. Each page change will require that `localStorage` contains a `username` item.

The `authProvider` must expose 5 methods, each returning a `Promise`

```tsx
// in src/authProvider.ts
import { AuthProvider } from "react-admin";

export const authProvider: AuthProvider = {
    // called when the user attempts to log in
    login: ({ username }) => {
        localStorage.setItem("username", username);
        // accept all username/password combinations
        return Promise.resolve();
    },
    // called when the user clicks on the logout button
    logout: () => {
        localStorage.removeItem("username");
        return Promise.resolve();
    },
    // called when the API returns an error
    checkError: ({ status }: { status: number }) => {
        if (status === 401 || status === 403) {
            localStorage.removeItem("username");
            return Promise.reject();
        }
        return Promise.resolve();
    },
    // called when the user navigates to a new location, to check for authentication
    checkAuth: () => {
        return localStorage.getItem("username")
            ? Promise.resolve()
            : Promise.reject();
    },
    // called when the user navigates to a new location, to check for permissions / roles
    getPermissions: () => Promise.resolve(),
};
```
 这是一个使用localStorage实现authentication的简单例子:
1. login: 接收用户名,并存入[[../../前端开发/React/React关键技术#localStorage|localstorage]]。直接返回resolved表示登录成功。
2. logout: 从localStorage删除用户名,表示退出登录。
3. checkError: 如果遇到401或403错误,表示登录状态失效,需要删除localStorage中的用户名。
4. checkAuth: 检查localStorage中是否存在用户名,有表示登录态有效,返回resolved;没有表示未登录,返回rejected。
5. getPermissions: 这里直接返回resolved,表示不检查权限。可以扩展权限校验逻辑。
6. 通过这些函数,react-admin可以集成localStorage形式的登录认证。
7. 登录成功后,localStorage中记录用户名;退出登录删除用户名。
8. 接口401/403错误会检查并退出登录状态。 
9. 页面跳转会检查localStorage判断登录状态。
这样通过自定义authProvider,react-admin可以快速集成各种不同的认证方案,如localStorage、JWT、OAuth等。

### Connecting To A Real API

Here is the elephant in the room of this tutorial. In real world projects, the dialect of your API (REST? GraphQL? Something else?) won’t match the JSONPlaceholder dialect. Writing a Data Provider is probably the first thing you’ll have to do to make react-admin work. Depending on your API, this can require a few hours of additional work.

React-admin delegates every data query to a Data Provider object, which acts as an adapter to your API. This makes react-admin capable of mapping any API dialect, using endpoints from several domains, etc.

For instance, let’s imagine you have to use the `my.api.url` REST API, which expects the following parameters:

| Action              | Expected API request                                                                    |
| ------------------- | --------------------------------------------------------------------------------------- |
| Get list            | `GET http://my.api.url/posts?sort=["title","ASC"]&range=[0, 24]&filter={"title":"bar"}` |
| Get one record      | `GET http://my.api.url/posts/123`                                                       |
| Get several records | `GET http://my.api.url/posts?filter={"id":[123,456,789]}`                               |
| Get related records | `GET http://my.api.url/posts?filter={"author_id":345}`                                  |
| Create a record     | `POST http://my.api.url/posts`                                                          |
| Update a record     | `PUT http://my.api.url/posts/123`                                                       |
| Update records      | `PUT http://my.api.url/posts?filter={"id":[123,124,125]}`                               |
| Delete a record     | `DELETE http://my.api.url/posts/123`                                                    |
| Delete records      | `DELETE http://my.api.url/posts?filter={"id":[123,124,125]}`                            |

The code for a Data Provider for the `my.api.url` API is as follows:

 好的,我来对这段数据提供器代码添加一些注释,说明其中的主要逻辑:
```js
// 导入react-admin的DataProvider和fetch工具
import { DataProvider, fetchUtils } from "react-admin"; 
import { stringify } from "query-string";
// 定义APIendpoint
const apiUrl = 'https://my.api.com/'; 
// 使用fetchJson作为http client
const httpClient = fetchUtils.fetchJson;
export const dataProvider: DataProvider = {
  // 获取列表数据
  getList: (resource, params) => {
    // 分页参数
    const { page, perPage } = params.pagination;  
    // 排序参数
    const { field, order } = params.sort;
    
    // 构造查询参数
    const query = {
      sort: JSON.stringify([field, order]),
      range: JSON.stringify([(page - 1) * perPage, page * perPage - 1]),
      filter: JSON.stringify(params.filter),
    };
    
    // 构造请求URL
    const url = `${apiUrl}/${resource}?${stringify(query)}`; 
    
    // 发出请求
    return httpClient(url).then(({ headers, json }) => ({
      data: json,
      // 从响应中解析总数
      total: parseInt(headers.get('content-range').split('/').pop()), 
    }));
  },
  // 其他方法类似,依次实现  
  getOne: () => {},
  getMany: () => {},
  
  // ...
}
```

**Tip**: `fetchUtils.fetchJson()` is just a shortcut for `fetch().then(r => r.json())`, plus a control of the HTTP response code to throw an `HTTPError` in case of 4xx or 5xx response. Feel free to use `fetch()` directly if it doesn’t suit your needs.
 这是一个典型的使用fetch和react-admin dataProvider接口实现对REST API的集成。
主要逻辑:
1. 导入react-admin的DataProvider接口和fetchUtils
2. 定义apiUrl作为REST API的基础URL
3. 使用fetchUtils.fetchJson作为HTTP客户端
4. 实现DataProvider接口的各方法:
- getList:查询列表数据
- getOne:查询单个记录
- getMany:批量查询
- update:更新记录
- create:创建记录
- delete:删除记录
5. 每个方法根据react-admin的参数构造REST API的URL
6. 用fetch发出HTTP请求并处理响应
7. 映射并返回react-admin所需的response格式
这样,通过简单的fetch调用,配合DataProvider接口,就可以轻松将react-admin与任意REST API集成,获得完整的CRUD能力。
并且可以利用react-admin提供的便利功能如分页、排序、过滤等。


```ts
  getList: (resource, params) => {
    // 分页参数
    const { page, perPage } = params.pagination;  
    // 排序参数
    const { field, order } = params.sort;
    }
```
 您问的非常好,我来进一步解释一下getList方法中的参数:
getList是一个函数,它接受两个参数:
1. resource: 表示要查询的资源(数据)名称,如"posts","users"等。这对应着后端的不同数据表或模型。
2. params: 是一个包含查询参数的对象,它包含:
- pagination: 分页信息,如page页码,perPage每页大小
- sort: 排序信息,如field排序字段,order排序顺序
- filter: 过滤条件
react-admin会根据界面操作构造这个params参数对象,传递给getList方法。
然后在getList方法内部,我们可以解构params来获取分页、排序、过滤等信息,以构造后端API的查询请求,最终返回列表数据。
所以resource表示要查询的数据,params包含可定制的查询参数。getList方法负责根据这些参数,调用API获取列表数据,这是实现数据提供器的关键之处。
这样调用getList时传入不同resource,以及通过params动态控制查询,就可以应用在获取后端不同API资源的数据上。

```ts
return httpClient(url).then(({ headers, json }) => ({
      data: json,
      // 从响应中解析总数
      total: parseInt(headers.get('content-range').split('/').pop()), 
    }));
```
 这部分代码是在获取完API响应数据后,对数据做进一步处理,然后返回给react-admin。
主要步骤是:
1. httpClient(url) 发出HTTP请求获取响应
2. .then() 拿到响应数据 响应包含两部分:
   - headers: HTTP头信息
   - json: JSON格式的响应体数据
3. 返回一个对象,这个对象会作为dataProvider的响应结果:
   - data: 将json赋值作为data,这部分会传给界面组件
   - total: 从headers中解析出总记录数,用于分页
4. 具体来说,total是通过解析headers中的content-range头来获取总数的
5. 最后用parseInt转换成数值类型
这样在获取到API响应后,对数据做了适当处理,提取了需要的信息,封装成一个结果对象返回,这是dataProvider的常见用法。
react-admin组件会使用data和total来显示数据和分页。

## Conclusion

React-admin was built with customization in mind. You can replace any react-admin component with a component of your own, for instance to display a custom list layout, or a different edit form for a given resource.

Now that you’ve completed the tutorial, continue your journey with [the Features chapter](https://marmelab.com/react-admin/Features.html), which lists all the features of react-admin.

After that, the best way to learn react-admin is by reading the introduction chapters to each of its major parts:

- [Data Provider and API Calls](https://marmelab.com/react-admin/DataProviderIntroduction.html)
- [Auth Provider and Security](https://marmelab.com/react-admin/Authentication.html)
- [List Page](https://marmelab.com/react-admin/ListTutorial.html)
- [Creation & Edition Pages](https://marmelab.com/react-admin/EditTutorial.html)
- [Show Pages](https://marmelab.com/react-admin/ShowTutorial.html)
- [Fields](https://marmelab.com/react-admin/Fields.html)
- [Inputs](https://marmelab.com/react-admin/Inputs.html)
- [Preferences](https://marmelab.com/react-admin/Store.html)
- [Realtime](https://marmelab.com/react-admin/Realtime.html)

And to help you close the gap between theoretical knowledge and practical experience, take advantage of the react-admin [Demos](https://marmelab.com/react-admin/Demos.html). They are great examples of how to use react-admin in a real world application. They also show the best practices for going beyond simple CRUD apps.


