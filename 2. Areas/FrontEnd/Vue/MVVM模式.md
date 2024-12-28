---
aliases: null
theme: null
priority: false
date_created: 2024-12-15 05:25
date_update: null
tags: null
---

### 省三: 在 Vue.js 中应用 MVVM 模式和数据代理的示例

在MVVM模式中，ViewModel作为桥梁沟通View和Model，它将业务逻辑从视图中抽象出来，并提供与视图对接的方法。通过数据代理，在处理创建一个独立的页面或组件，将数据绑定到相关用户界面上时，可以提高开发效率，简化代码结构并允许更好的跨团队协作。

​	在 Vue.js 中，MVVM 模式和数据代理是核心概念，通过建立ViewModel层，并进行数据绑定的方式，将这些技术用于创建 Web 应用程序可带来很多优点。除了提高开发效率、简化代码和跨团队协作外，Vue.js 还支持组件化编程范式，可以更好地管理代码库和促进复用和读写性。

​	让我们来看一个购物车的例子：

- Model: 在购物车例子中，数据Model 是商店里售卖的商品、价格、库存等信息。这些信息一般会在数据库或者服务器端进行存储和管理。

- View: 视图就是用户在前端浏览器（Web、APP）中看到的页面和UI界面。比如，显示所有商品的列表，每个商品都拥有图片、名称、描述、价格、数量和“加入购物车”的按钮等元素。

- ViewModel: ViewModel 的任务就是负责将 Model 中的数据转化为可用于视图的数据格式，并且将视图中的操作事件也转化为对Model方法的调用，以便进行数据修改和更新。在购物车的例子中，ViewModel 层会负责将商品列表封装成购物车对象，并计算选购的商品总价和总量，在其中还可能包括促销活动的计算等。

- 数据代理: 数据代理技术负责数据双向绑定，能够在 Model 层发生变化时及时更新 View 和 ViewModel 层中相关的数据。在购物车例子中，当用户点击 “加入购物车” 按钮时，View 组件会立即调用 ViewModel 层的加入购物车方法。ViewModel 层则会通过 数据代理将数据改变通知到其他组件或广播出消息供其他组件监听并接收处理。

下面是一个简单的Vue实现的购物车示例代码：

```html
<!-- View 表现层 -->
<div id="app">
  <h2>购物车清单</h2>
  <ul>
    <li v-for="item in cartItems">
      <img :src="item.imgUrl" alt="">
      <div>{{ item.name }}</div>
      <div>{{ item.price | formatPrice }}</div>
      <div>
        数量: 
        <button @click="decreaseQty(item)">-</button>
        {{ item.qty }}
        <button @click="increaseQty(item)">+</button>
      </div>
    </li>
  </ul>
  <p>Total: {{ total | formatPrice }}</p>
</div>

<!-- ViewModel 视图模型 -->
<script>
 var vm=new Vue({
   el:'#app',
   data:{
      cartItems:[
        {
          id: 1,
          name: '商品名称1',
          price: 19.9,
          imgUrl: '商品图片地址1',
          qty: 1
        },
        {
          id: 2,
          name: '商品名称2',
          price: 199,
          imgUrl: '商品图片地址2',
          qty: 1
        }
      ]
   },
   computed:{
     //计算总价格和总数量
      total: function () {
        return this.cartItems.reduce((total, item) => {
          return total + (item.price * item.qty);
        }, 0);
      }
   },
   methods:{
     //加入/移除商品到购物车中
      addToCart:function(item){
         let found=this.cartItems.find(el=>el.id == item.id);
         if(found){
           found.qty++;
         }else{
           this.cartItems.push(Vue.set({...item},"qty",1));
         }
      },
      decreaseQty:function(item){
        if(item.qty <= 1)
          return;
        item.qty--;
      },
      increaseQty:function(item){
        item.qty++;
      }
   },
    filters: {
      formatPrice: function (value) {
        let result = Number(value).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
        return result;
      }
    }
 })
 </script>
```

这个购物车示例中，我们可以看到 ViewModel 层用 Vue 实现并绑定到了 View 上，实现了组件之间的数据双向绑定和响应式操作，并通过 computed 计算属性和 methods 来控制数据的变化。ShoppingCart（购物车）作为一个封装了整个页面中商品信息、购买数量等一系列业务逻辑的对象，在此处起到承载 Model 的作用。

总的来说，这就是一个基于 Vue 实现的 MVVM 模式购物车例子，也展示了数据代理在应用程序开发中的核心地位和作用。

当然，再来看一个简单的登录注册表单的例子，结合MVVM模式和数据代理。

- Model: 在登录注册表单的例子中，数据 Model 是用户账户信息和相关认证信息。这些信息一般会在数据库或者服务器端进行存储和管理。

- View: 在前端浏览器中，视图就是用户看到的登录注册页面（包括输入框、按钮等），以及用户输入的用户名和密码。

- ViewModel: ViewModel 层主要负责将用户输入的信息转化为可用于Model的数据格式并做进一步的处理，比如来自后台的验证和授权等；ViewModel也通过 数据代理 将数据改变并通知到其他组件或全局广播。

- 数据代理：在登录注册表单的例子中，当用户输入完账号密码并点击登录按钮时，View 组件首先会调用 ViewModel 层的 login 方法进行登录验证。ViewModel层根据请求结果判断是否成功，并且通过数据代理更新登录状态和用户信息的内容。此外，ViewModel 还可以监听用户验证码、忘记密码、重置密码等复杂操作，并调用相应 Model 中的方法进行实现。

示例代码：

```html
<!-- View 表现层 -->
<div id="app">
  <h2>登录</h2>
  <div>
    <label for="username">用户名:</label>
    <input type="text" name="username" id="username" v-model="loginInfo.username">
  </div>
  <div>
    <label for="password">密码:</label>
    <input type="password" name="password" id="password" v-model="loginInfo.password">
  </div>
  <button @click="login">登录</button>
  <p>{{ message }}</p>
</div>

<!-- ViewModel 视图模型 -->
<script>
var vm = new Vue({
  el: '#app',
  data: {
    loginInfo: {
      username: '',
      password: ''
    },
    message: ''
  },
  methods: {
    login() {
        var username = this.loginInfo.username;
        var password = this.loginInfo.password;
        // Login to server
        axios.post('api/auth/login', {username,password})
            .then((response) => { 
              console.log(response);
              // Update user info or do some other things here
              this.message = "Login successfully";
            })
            .catch((error) => {
              console.log(error); 
              this.message = "Login failed: " + error.response.data.errors[0].message;
            });
    }
  }
})
</script>
```

在上述代码中，我们可以看到 ViewModel 层用 Vue 实现并绑定到 View 上，通过 axios 发送异步请求来执行登录功能，在返回结果后通知数据代理管理状态。在登录页面中，ViewModel 层负责处理输入框的响应事件和数据校验等逻辑, 并承载 Model 的具体实现。

这个简单的登录注册表单例子中，我们再次看到了 MVVM 模式和数据代理在应用程序开发中的实践意义，当然，在实际开发中也有很多其他复杂的MVVM模式的实现案例.

> Vue重构todo应用:

以下是使用Vue.js框架重构的代码:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Vue Todo List</title>
</head>
<body>

  <div id="app">
    <h1>Vue Todo List</h1>

    <!-- 输入框 -->
    <div class="input-container">
      <input type="text" placeholder="Enter a task..." v-model="newTodo" @keyup.enter="addTodo">
      <button @click="addTodo">Add</button>
      <button @click="clearAll">Clear All</button>
    </div>

    <!-- 待办事项列表 -->
    <h2>Pending Tasks:</h2>
    <ul class="todo-list">
      <li v-for="(todo, index) in todos" :key="todo.id" v-if="!todo.checked" @click="checkTodo(index)">
        {{ todo.content }}
      </li>
    </ul>

    <!-- 已完成事项列表 -->
    <h2>Completed Tasks:</h2>
    <ul class="done-list">
      <li v-for="(todo, index) in todos" :key="todo.id" v-if="todo.checked" @click="rollback(index)">
        {{ todo.content }}
      </li>
    </ul>
  
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2.6.12/dist/vue.js"></script>
  <script>
    new Vue({
      el: '#app',
      data: {
        todos: [],
        newTodo: ""
      },
      mounted() {
        if (localStorage.todos) {
          this.todos = JSON.parse(localStorage.todos);
        }
      },
      watch: {
        todos: {
          handler(newVal) {
            localStorage.todos = JSON.stringify(newVal);
          },
          deep: true
        }
      },
      methods: {
        // 添加todo项
        addTodo() {
          if (this.newTodo.trim()) {
            this.todos.push({ id: Date.now(), content: this.newTodo, checked: false });
            this.newTodo = "";
          }
        },
        // 将待办事项标记为已完成
        checkTodo(index) {
          this.todos[index].checked = true;
        },
        // 将已完成事项重新变为待完成状态
        rollback(index) {
          this.todos[index].checked = false;
        },
        // 清空已完成事项列表
        clearAll() {
          this.todos = this.todos.filter(todo => !todo.checked);
        }
      }
    })
  </script>
</body>
</html>
```

以上的Vue Todo List做了以下修改：

1. Vue实例的data中新增了一个newTodo属性，用于绑定输入框

2. 使用v-model指令双向绑定输入框和newTodo属性，并给添加按钮添加@click事件监听器，当点击该按钮或在输入框按下Enter键时，调用addTodo方法添加一条新todo项。

3. 利用v-for指令循环遍历todos数组，根据checked属性值来判断待做和已完成任务项。

4. 对Vue的数据进行localStorage存储的操作。在mounted生命周期钩子函数中检查localStorage是否存在，如果存在则将其导入到todos数组中。使用watch选项监听todos数据的变化，并且在每次数据发生变化的过程中改变localStorage中的todos数组。

5. 将click事件监听器与checkTodo、rollback、clearAll方法绑定

相较于原生JavaScript，使用Vue.js框架可以更快速地开发出用户交互友好的web应用。

> 猜数字的游戏

该应用会随机生成1-100的一个整数，玩家需要在输入框中输入一个数字，如果玩家猜错了，应用会给出提示信息；如果猜对了，应用会告知玩家，并且可让玩家选择是否重新开始游戏。

以下是HTML和Vue.js代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Vue Guessing Game</title>
</head>

<body>
  <div id="app">
    <h1>Vue Guessing Game</h1>
    <p v-show="gameOver">Game Over. The number was {{number}}</p>
    <p v-show="correct">You Win!</p>
    <label for="guess">Guess a Number between 1 and 100:</label>
    <input type="text" id="guess" name="guess" v-model="guess" v-show="!correct && !gameOver" @keyup.enter="checkAnswer">
    <button @click="checkAnswer" v-show="!correct && !gameOver">Submit Answer</button>
    <button @click="resetGame" v-show="gameOver || correct">Play Again?</button>
  </div>
    
  <script src="https://cdn.jsdelivr.net/npm/vue@2.6.12/dist/vue.js"></script>
  <script>
    new Vue({
      el: "#app",
      data() {
        return {
          number: Math.floor(Math.random() * 100) + 1,
          guess: "",
          correct: false,
          gameOver: false
        }
      },
      methods: {
        checkAnswer() {
          if (this.guess === "") {
            alert("Please enter a number");
            return;
          } else if (isNaN(parseInt(this.guess))) {
            alert("Please enter a valid number");
            return;
          }
    
          if (parseInt(this.guess) === this.number) {
            this.correct = true;
          } else if (parseInt(this.guess) < this.number) {
            alert("Too low!");
          } else {
            alert("Too high!");
          }
    
          this.guess = "";
          
          if (this.correct) {
            this.gameOver = true;
          }
        },
        resetGame() {
          this.number = Math.floor(Math.random() * 100) + 1;
          this.guess = "";
          this.gameOver = false;
          this.correct = false;
        }
      }
    })
  </script>
  
</body>
</html>
```

我们需要实现三个方法来控制应用逻辑：

1. checkAnswer：检查当前猜测的数字，并根据结果给出对话框提示。如果猜对了，则设置correct为true，并将guess清空，同时将gameOver设置为true，结束游戏。

2. resetGame：在玩家点击“再玩一次”按钮时，重新开始游戏。更新number值以随机生成新的数字，并将guess、correct和gameOver属性归零。

3. 在keyUp.enter事件中锁定监听器，以便在按回车键时调用checkAnswer方法。

> 重构猜数字游戏

你可以使用组合式API来重构这个应用程序。以下是相同功能的代码，使用了Vue.js 3.x版本的Composition API：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Vue Guessing Game</title>
</head>

<body>
  <div id="app">
    <h1>Vue Guessing Game</h1>
    <p v-show="gameOver">Game Over. The number was {{number}}</p>
    <p v-show="correct">You Win!</p>
    <label for="guess">Guess a Number between 1 and 100:</label>
    <input type="text" id="guess" name="guess" v-model="guess" v-show="!correct && !gameOver" @keyup.enter="checkAnswer">
    <button @click="checkAnswer" v-show="!correct && !gameOver">Submit Answer</button>
    <button @click="resetGame" v-show="gameOver || correct">Play Again?</button>
  </div>
    
  <script src="https://unpkg.com/vue@next"></script>
  <script>
    const { ref, reactive } = Vue;
    
    Vue.createApp({
      setup() {
        const number = ref(Math.floor(Math.random() * 100) + 1);
        const guess = ref("");
        const gameOver = ref(false);
        const correct = ref(false);
    
        const checkAnswer = () => {
          if (guess.value === "") {
            alert("Please enter a number");
            return;
          } else if (isNaN(parseInt(guess.value))) {
            alert("Please enter a valid number");
            guess.value = "";
            return;
          }
    
          if (parseInt(guess.value) === number.value) {
            correct.value = true;
          } else if (parseInt(guess.value) < number.value) {
            alert("Too low!");
          } else {
            alert("Too high!");
          }
    
          guess.value = "";
    
          if (correct.value) {
            gameOver.value = true;
          }
        };
    
        const resetGame = () => {
          number.value = Math.floor(Math.random() * 100) + 1;
          guess.value = "";
          gameOver.value = false;
          correct.value = false;
        };
    
        return { number, guess, gameOver, correct, checkAnswer, resetGame };
      }
    }).mount("#app");
  </script>
</body>
</html>
```

在这个版本里，我们使用了Vue的Composition API，它提供的ref和reactive函数来响应性地创建应用程序数据。另外，由于组合式API不再依赖生命周期钩子，而是通过setup函数挂载到Vue实例中，因此我们使用Vue.createApp来代替原来的new Vue。

除此之外，其他部分与选项式API版本相同。

v-model可以与其他指令结合使用，例如v-bind和v-on。v-model本质上是一个语法糖，它结合了**v-bind和v-on**指令。例如，`<input v-model="searchText" />`等价于`<input :value="searchText" @input="searchText = $event.target.value" />`。这意味着v-model在内部使用了v-bind来绑定value属性，**并使用v-on来监听input事件以更新数据** ¹。

MVVM（Model-View-ViewModel）是一种软件架构模式，它有助于将图形用户界面的开发与业务逻辑或后端逻辑（数据模型）的开发分离开来，这是通过置标语言或GUI代码实现的 ¹。

MVVM模式中有三个核心组件：模型（Model）、视图（View）和视图模型（ViewModel） ²。

- 模型（Model）指的是后端传递的数据。
- 视图（View）指的是所看到的页面。
- 视图模型（ViewModel）是一个值转换器，负责从模型中暴露（转换）数据对象，以便轻松管理和呈现对象。在这方面，视图模型比视图做得更多，并且处理大部分视图的显示逻辑 ¹。

MVVM 是 Model-View-ViewModel 的缩写。它是一种设计模式，用于将用户界面（视图）与底层数据模型（模型）分离。在 Vue 中，视图是由组件和模板定义的，而模型是由数据和方法定义的。ViewModel 是一个连接视图和模型的桥梁，它负责监听模型数据的变化并更新视图，同时也负责处理视图上的用户交互并更新模型数据。

MVVM 是 Model-View-ViewModel 的缩写。它是一种设计模式，用于将用户界面（视图）与底层数据模型（模型）分离。在 Vue 中，视图是由组件和模板定义的，而模型是由数据和方法定义的。ViewModel 是一个连接视图和模型的桥梁，它负责监听模型数据的变化并更新视图，同时也负责处理视图上的用户交互并更新模型数据。

下面是一个简单的 Vue 代码示例，演示了 MVVM 模式：

```javascript
// 创建一个 Vue 实例
var vm = new Vue({
  // 指定挂载元素
  el: '#app',
  // 定义数据
  data: {
    message: 'Hello Vue!'
  },
  // 定义方法
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})
```

```html
<!-- 定义视图 -->
<div id="app">
  <p>{{ message }}</p>
  <button v-on:click="reverseMessage">Reverse Message</button>
</div>
```

```javascript
// 在 Vue 原型上添加一个方法
Vue.prototype.$myMethod = function () {
  console.log('This is a method on the Vue prototype.')
}

// 创建一个 Vue 实例
var vm = new Vue({
  el: '#app'
})

// 调用原型上的方法
vm.$myMethod() // 输出 'This is a method on the Vue prototype.'
```
