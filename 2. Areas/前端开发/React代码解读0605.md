---
date created: 2024-07-14 15:01
date updated: 2024-07-14 15:11
---

**EnrolmentForm.js**

```jsx
import React, { useState } from 'react';
// 创建一个名为"EnrolmentForm"的函数组件
function EnrolmentForm(props) {
  // 在子组件中解构出父组件传递过来的属性值
  const { chosenProgram, setUpdatedSeats, currentSeats } = props;
  // 创建一个名为"enrolment"的对象状态变量，并初始化为空对象
  const [enrolment, setEnrolment] = useState({});
  // 定义一个函数，用于处理表单提交事件
  const handleSubmit = (event) => {
    event.preventDefault(); // 阻止默认表单行为
    // 如果尚未选择课程计划，则直接返回
    if (!chosenProgram) {
      alert("Please choose a program first.");
      return;
    }
    // 如果座位数已满，则提示用户无法报名
    if (currentSeats <= 0) {
      alert("Sorry, there are no seats available for this program.");
      return;
    }
    // 更新当前可用座位数量
    setUpdatedSeats(currentSeats - 1);
    // 创建一个新的报名记录对象，并将其添加到状态变量中
    const newEnrolment = {
      id: Math.random().toString(36).substring(7), // 使用随机数生成一个唯一的ID
      program: chosenProgram,
      date: new Date().toLocaleString(),
    };
    setEnrolment(newEnrolment);
  };
  return (
    <div className="enrolmentForm">
      {/* 表单元素 */}
      <form onSubmit={handleSubmit}>
        <h2>Enrolment Form</h2>
        {/* 输入框：姓名 */}
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          required
          onChange={(event) => setEnrolment({ ...enrolment, name: event.target.value })}
        />
        <br/>
        {/* 输入框：电子邮件地址 */}
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          required
          onChange={(event) => setEnrolment({ ...enrolment, email: event.target.value })}
        />
        <br/>
        {/* 提交按钮 */}
        <button type="submit">Submit</button>
      </form>
      {/* 显示已提交的报名记录 */}
      {enrolment.id && (
        <div className="enrolmentInfo">
          <h3>Thank you for your enrolment!</h3>
          <p>Name: {enrolment.name}</p>
          <p>Email: {enrolment.email}</p>
          <p>Program: {enrolment.program}</p>
          <p>Date: {enrolment.date}</p>
        </div>
      )}
    </div>
  );
}
export default EnrolmentForm;
```

**App.js**

```jsx
import React, { useState } from 'react';
import EnrolmentForm from './EnrolmentForm';
function App() {
  const [program, setProgram] = useState("UG");
  const [seats, setSeats] = useState(100);
  // 定义一个函数，用于在用户更改课程计划时更新"program"状态变量的值
  const handleChange = (event) => {
    setProgram(event.target.value);
  };
  // 定义一个函数，用于更新"seats"状态变量的值
  const setUpdatedSeats = (updatedSeats) => {
    setSeats(updatedSeats);
  };
  return (
    <div className="App">
      <div className="programs">
        {/* 显示当前可用座位的数量 */}
        <label>Remaining Seats - {seats}</label>
        <br/>
        <br/>
        <label>Choose Program:</label>
        {/* 下拉列表，用于让用户选择课程计划 */}
        <select
          className="appDropDowns"
          onChange={handleChange}
          value={program}
        >
          {/* 选项：Undergraduate */}
          <option value="UG">Undergraduate</option>
          {/* 选项：Postgraduate */}
          <option value="PG">Postgraduate</option>
        </select>
      </div>
      {/* 子组件，用于处理用户的注册信息 */}
      <EnrolmentForm
        chosenProgram={program}
        setUpdatedSeats={setUpdatedSeats}
        currentSeats={seats}
      />
    </div>
  );
}
export default App;
```

在这个示例中，我们将`EnrolmentForm`组件拆分到了单独的文件中，并将其导出以便在其他文件中使用。在`App.js`文件中，我们导入了`EnrolmentForm`组件，并将它作为子组件渲染到了父组件中。

## EnrolmentForm.js

3. `const { chosenProgram, setUpdatedSeats, currentSeats } = props;`：解构出父组件传递过来的属性值，用于在子组件中使用。

4. `<form onSubmit={handleSubmit}>...</form>`：渲染一个表单元素，并通过onSubmit事件监听表单的提交。

5. `const handleSubmit = (event) => {...}`：定义一个事件处理函数handleSubmit，用于处理表单提交事件。首先阻止默认表单行为，然后检查是否选择了课程计划和是否有座位可用，最后更新余下座位数量和创建新的报名记录对象。

6. `{enrolment.id && (<div className="enrolmentInfo">...</div>)}"`：通过条件渲染，当"enrolment"的状态值不为空对象时，渲染一个包含已提交的报名记录信息的div元素。

以下是您提供的CSS代码的高亮和逐行注释：

```css
.enrolContainer {
  background-color: #f2f2f2; /* 设置背景颜色为淡灰色 */
}
.enrolForm {
  list-style-type: none; /* 设置列表风格为无序列表 */
}
.ulEnrol li {
  display: block; /* 将列表项设置为块元素 */
  margin-bottom: 10px; /* 下外边距为10像素 */
}
.inputFields {
  width: 100%; /* 设置输入框宽度为100% */
  box-sizing: border-box; /* 设置盒模型为border-box */
}
#btnEnrol {
  background-color: #4caf50; /* 设置提交按钮背景颜色为绿色 */
  border: none; /* 取消边框 */
  cursor: pointer; /* 鼠标移动到按钮上时显示手型 */
}
#btnEnrol:hover {
  background-color: #45a049; /* 鼠标悬停时设置背景颜色为深绿色 */
}
.message {
  color: #4caf50; /* 设置文本颜色为绿色 */
  font-weight: bold; /* 设置文本为粗体 */
}
```

好的，以下是您提供的代码的高亮和逐行注释：

```jsx
useEffect(() => {
  const curItemKey = props.studentDetails.key; // 获取当前学生详情的key
  if (curItemKey){ // 如果当前学生详情的key存在
    items = [...items, props.studentDetails]; // 将当前学生详情加入到列表中
    props.setStudentDetails({}); // 重置学生详情为一个空对象
  }
}, [props]);
```

这行代码是使用ES6的展开语法，将`props.studentDetails`添加到`items`数组中。具体地讲，它首先创建一个新的数组，该数组包含了原来的`items`数组中的所有元素以及新的`props.studentDetails`元素。最后，将新的数组赋值给变量`items`，从而更新了`items`数组。
这种方法比使用`.push()`方法更加安全，因为它不会改变原始数组，而是在其基础上创建一个新的数组。这可以避免一些常见的错误，例如在修改原始数组时不小心引用原始数组的其他部分。

以下是两个类似的示例：
示例1：将数字添加到数组中

```js
const numbers = [1, 2, 3];
const newNumber = 4;
numbers = [...numbers, newNumber];
console.log(numbers); // 输出结果为 [1, 2, 3, 4]
```

值给变量`numbers`。最后，我们输出结果为`[1, 2, 3, 4]`。

示例2：将对象添加到数组中

```js
const people = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 30 }
];
const newPerson = { name: "Charlie", age: 35 };
people = [...people, newPerson];
console.log(people);
```

这里，我们首先定义一个包含两个人员对象的数组`people`，然后将新的人员对象`newPerson`添加到数组中。
