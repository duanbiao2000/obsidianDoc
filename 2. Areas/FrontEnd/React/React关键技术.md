---
aliases: 
categories: 
tags:
---

- [[API数据请求]]
- [[API网关]]
- [[API设计模式]]
- [[Findlay - React - The Road To Enterprise.pdf]]
- [[Flask开发部署]]
- [[GitHub Actions]]
- [[Github Gist JavaScript 的精彩代码片段]]
- [[Lodash]]
- [[Material-UI]]
- [[需求分析]]
- [[React admin]]
- [[React Bootstrap]]
- [[React Hooks]]
- [[React Quickly pdf]]
- [[react-bootstrap]]
- [[react后台管理系统]]
- [[ReactRouter]]
- [[React代码解读0608]]
- [[Redux]]
- [[React关键技术]]
- [[React官方文档]]
- [[React实现无线滚动加载]]
- [[React实现轮播图]]
- [[React插件教程]]
- [[React测试]]
- [[React状态管理Redux]]
- [[React生命周期方法]]
- [[React组件间通信代码示例]]
- [[React表单验证]]
- [[React设计模式与最佳实践]]
- [[React软件架构]]
- [[React进阶]]
- [[Typesciprt扩展]]
- [[两类Web应用]]
- [[学习Redux]]
- [[新手React项目]]

### useEffect

```js
// 定义一个名为App的函数组件
function App(){
  // 定义一个常量，用于存储本地存储的键名
  LOCAL_STORAGE_KEY="contacts";
  // 使用useState钩子函数，初始化一个空数组，用于存储联系人信息
  const {contacts, setContacts} = useState([]);

  // 定义一个函数，用于添加联系人信息
  addContactHandler =(contact)=>{
    // 将新联系人信息添加到联系人数组中
    setContacts([...contacts, contact]);
  }

  // 使用useEffect钩子函数，在组件加载时，从本地存储中获取联系人信息，并将其添加到联系人数组中
  useEffect(()=>{
    const retrieveContacts = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY));  
    if (retrieveContacts) setContacts(retrieveContacts);
  }, [contacts])
  
  // 使用useEffect钩子函数，在联系人数组发生变化时，将联系人信息保存到本地存储中
  useEffect(()=>{
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.strigify(contacts));  
  }, [contacts]);

  // 返回一个包含Header、AddContact和ContactList组件的div元素
  return (
    <div className="ui container">
      <Header />
        <AddContact addContactHandler={addContactHandler} />
        <ContactList contacts={contacts} />
    </div>
  );
}
// 导出App组件
export default App;
```

