```js
import React from 'react';
import { PromiseState } from 'react-refetch';

// 定义一个函数来发起数据请求
const fetchData = () => fetch('https://api.example.com/data')
  .then(response => response.json());

// DataComponent 组件
function DataComponent() {
  // 使用 React.useMemo 来缓存 fetchData 函数的结果，
  // 这样每次渲染 DataComponent 时都不需要重新创建 fetchData 函数
  const dataPromise = React.useMemo(fetchData, []);

  return (
    // 使用 PromiseState 组件来包裹 dataPromise，
    // 它会根据 dataPromise 的状态显示不同的内容
    <PromiseState promise={dataPromise}>
      {({ 
        // 这个对象包含 dataPromise 的状态信息
        fulfilled, pending, rejected, value, reason 
      }) => {
        // 如果 dataPromise 仍在等待响应，显示 "Loading..."
        if (pending) {
          return <div>Loading...</div>;
        } 
        // 如果 dataPromise  rejected，显示错误信息
        else if (rejected) {
          return <div>Error: {reason}</div>;
        } 
        // 如果 dataPromise  fulfilled，显示数据
        else if (fulfilled) {
          const data = value;
          return (
            <div>
              <h1>Data Component</h1>
              <ul>
                {data.map(item => (
                  // 渲染每个数据项，使用 item.id 作为 key
                  <li key={item.id}>{item.name}</li>
                ))}
              </ul>
            </div>
          );
        } 
        // 如果 dataPromise 的状态是其他值，返回 null
        else {
          return null;
        }
      }}
    </PromiseState>
  );
}

// 导出 DataComponent 组件
export default DataComponent;
```