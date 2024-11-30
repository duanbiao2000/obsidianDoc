---
aliases: 
theme: 
priority: false
tags:
---
当然，这些术语是 Redux 生态系统中的关键概念。下面我会逐一解释这些名词，并展示它们如何在 Redux 中协同工作。

### 1. Reducer

**Reducer** 是一个纯函数，它接收当前的状态（state）和一个动作（action），并返回新的状态。Reducer 必须是纯函数，这意味着它不能修改传入的状态，而是返回一个新的状态对象。Reducer 的主要职责是根据接收到的动作来更新应用程序的状态。

```javascript
const counterReducer = (state = { count: 0 }, action) => {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + 1 };
    case 'decrement':
      return { ...state, count: state.count - 1 };
    default:
      return state;
  }
};
```

### 2. Actions

**Actions** 是描述发生了什么的对象。它们通常包含一个 `type` 字段，用于标识动作的类型，以及可选的 `payload` 字段，用于传递数据。Action Creator 是生成这些动作对象的函数。

```javascript
const increment = () => ({ type: 'increment' });
const decrement = () => ({ type: 'decrement' });

// 带有 payload 的 action
const add = (amount) => ({ type: 'add', payload: amount });
```

### 3. PayloadAction

**PayloadAction** 是来自 `@reduxjs/toolkit` 库的一个辅助类型，用于定义带有效载荷的动作。它简化了创建带有 payload 的 action creator 和 reducer 的过程。

```javascript
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    incremented: state => {
      // 不需要返回新状态，因为 Immer 会自动处理不可变性
      state.value += 1;
    },
    decremented: state => {
      state.value -= 1;
    },
    addedBy: (state, action: PayloadAction<number>) => {
      state.value += action.payload;
    }
  }
});

export const { incremented, decremented, addedBy } = counterSlice.actions;
export default counterSlice.reducer;
```

在这个例子中，`addedBy` 是一个带有效载荷的 action，它的 `payload` 是一个数字，表示要加到 `value` 上的值。

### 4. Slice

**Slice** 是 Redux Toolkit 提供的一个概念，它是一个自包含的模块，包含了特定功能相关的 reducer 和 actions。使用 `createSlice` 函数可以非常方便地创建这样的模块。

```javascript
import { createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    incremented: state => {
      state.value += 1;
    },
    decremented: state => {
      state.value -= 1;
    },
    incrementedByAmount: (state, action) => {
      state.value += action.payload;
    }
  }
});

export const { incremented, decremented, incrementedByAmount } = counterSlice.actions;
export default counterSlice.reducer;
```

在这个例子中，`counterSlice` 包含了三个 actions (`incremented`, `decremented`, `incrementedByAmount`) 和一个 reducer。这个 slice 可以被导入到 Redux store 中，并且其 actions 可以在整个应用中使用。

通过这些概念，Redux 提供了一种管理应用程序状态的方式，使得状态的变化更加可预测和易于调试。

```js
/**

 * 导入createSlice和PayloadAction函数

 * 这些函数来自'@reduxjs/toolkit'库

 * createSlice用于生成 Redux slice，包括reducer和actions

 * PayloadAction用于定义带有效载荷的action类型

 */

import { createSlice, PayloadAction } from '@reduxjs/toolkit'

  

interface DarkModeState {

  isEnabled: boolean

}

  

const initialState: DarkModeState = {

  isEnabled: false,

}

  

// 创建一个名为styleSlice的slice，用于管理应用的主题状态

export const styleSlice = createSlice({

  name: 'darkMode', // slice的名称为'darkMode'

  initialState, // 初始状态，通常由initialState常量提供

  reducers: { // 定义reducer函数

    // 设置或切换暗黑模式的状态

    setDarkMode: (state, action: PayloadAction<boolean | null>) => {

	// 更新 state 的 isEnabled 属性
	// 如果 action.payload 是布尔值，则直接使用该值
	// 如果 action.payload 是 null，则取反当前的 isEnabled 值

      state.isEnabled = action.payload !== null ? action.payload : !state.isEnabled

  

      // 当document对象存在时，即在浏览器环境中

      if (typeof document !== 'undefined') {

        // 根据darkMode状态，为body元素的class列表添加或移除'dark-scrollbars'类

        document.body.classList[state.isEnabled ? 'add' : 'remove']('dark-scrollbars')

  

        // 同样操作，为html元素的class列表添加或移除'dark'和'dark-scrollbars-compat'类

        document.documentElement.classList[state.isEnabled ? 'add' : 'remove'](

          'dark',

          'dark-scrollbars-compat'

        )

      }

    }

  }

});

  

      // You can persist dark mode setting

      // if (typeof localStorage !== 'undefined') {

      //   localStorage.setItem('darkMode', state.darkMode ? '1' : '0')

      // }

    },

  },

})

  

// Action creators are generated for each case reducer function

export const { setDarkMode } = styleSlice.actions

  

export default styleSlice.reducer
```