---
aliases: 
theme: 
priority: false
tags:
---
# 用户界面
[传递数据到新页面 | Flutter 中文文档 - Flutter 中文开发者网站 - Flutter](https://docs.flutter.cn/cookbook/navigation/passing-data)
# Flutter 命令行文档
[Flutter 命令行文档 | Flutter 中文文档 - Flutter 中文开发者网站 - Flutter](https://docs.flutter.cn/reference/flutter-cli)

# Flutter widget列表

[Widget 目录 | Flutter 中文文档 - Flutter 中文开发者网站 - Flutter](https://docs.flutter.cn/reference/widgets)
![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20241022003025.png)


在 Flutter 中，`Widget` 是构建用户界面的基本单元。Flutter 提供了丰富的内置 `Widget`，可以用来创建各种复杂的 UI。以下是一些主要的 `Widget` 类别及其常见示例：

### 1. 基础布局 `Widget`

这些 `Widget` 用于控制其他 `Widget` 的布局和排列。

- **Container**：一个通用的 `Widget`，可以设置背景颜色、边距、填充、边框等。
  ```dart
  Container(
    color: Colors.blue,
    padding: EdgeInsets.all(16.0),
    child: Text('Hello, World!'),
  )
  ```

- **Row** 和 **Column**：水平和垂直排列子 `Widget`。
  ```dart
  Row(
    children: [
      Text('Left'),
      Text('Right'),
    ],
  )

  Column(
    children: [
      Text('Top'),
      Text('Bottom'),
    ],
  )
  ```

- **Stack**：允许子 `Widget` 堆叠在一起。
  ```dart
  Stack(
    children: [
      Container(color: Colors.blue, width: 200, height: 200),
      Positioned(
        top: 50,
        left: 50,
        child: Container(color: Colors.red, width: 100, height: 100),
      ),
    ],
  )
  ```

- **Expanded** 和 **Flexible**：在 `Row` 和 `Column` 中扩展或灵活分配空间。
  ```dart
  Row(
    children: [
      Expanded(child: Container(color: Colors.blue, height: 50)),
      Flexible(child: Container(color: Colors.red, height: 50)),
    ],
  )
  ```

### 2. 容器和装饰 `Widget`

这些 `Widget` 用于添加装饰、边距、填充等。

- **Padding**：为子 `Widget` 添加内边距。
  ```dart
  Padding(
    padding: EdgeInsets.all(16.0),
    child: Text('Padded Text'),
  )
  ```

- **DecoratedBox**：为子 `Widget` 添加背景颜色、边框等装饰。
  ```dart
  DecoratedBox(
    decoration: BoxDecoration(
      color: Colors.blue,
      border: Border.all(color: Colors.black, width: 2.0),
    ),
    child: Text('Decorated Text'),
  )
  ```

### 3. 文本和图标 `Widget`

这些 `Widget` 用于显示文本和图标。

- **Text**：显示文本。
  ```dart
  Text(
    'Hello, Flutter!',
    style: TextStyle(fontSize: 24.0, fontWeight: FontWeight.bold),
  )
  ```

- **Icon**：显示图标。
  ```dart
  Icon(Icons.favorite, color: Colors.red, size: 32.0)
  ```

### 4. 按钮和交互 `Widget`

这些 `Widget` 用于处理用户交互。

- **ElevatedButton**（以前称为 `RaisedButton`）：带阴影的按钮。
  ```dart
  ElevatedButton(
    onPressed: () {
      // 按钮点击事件
    },
    child: Text('Click Me'),
  )
  ```

- **TextButton**（以前称为 `FlatButton`）：平面按钮。
  ```dart
  TextButton(
    onPressed: () {
      // 按钮点击事件
    },
    child: Text('Click Me'),
  )
  ```

- **IconButton**：带图标的按钮。
  ```dart
  IconButton(
    icon: Icon(Icons.add),
    onPressed: () {
      // 按钮点击事件
    },
  )
  ```

### 5. 列表和滚动 `Widget`

这些 `Widget` 用于显示可滚动的内容列表。

- **ListView**：垂直滚动的列表。
  ```dart
  ListView(
    children: List.generate(10, (index) => ListTile(title: Text('Item $index'))),
  )
  ```

- **GridView**：网格布局的列表。
  ```dart
  GridView.count(
    crossAxisCount: 2,
    children: List.generate(10, (index) => Center(child: Text('Item $index'))),
  )
  ```

### 6. 表单和输入 `Widget`

这些 `Widget` 用于处理用户输入。

- **TextField**：单行文本输入框。
  ```dart
  TextField(
    decoration: InputDecoration(labelText: 'Enter your name'),
  )
  ```

- **TextFormField**：带验证功能的文本输入框。
  ```dart
  TextFormField(
    decoration: InputDecoration(labelText: 'Enter your email'),
    validator: (value) {
      if (value == null || value.isEmpty) {
        return 'Please enter your email';
      }
      return null;
    },
  )
  ```

- **DropdownButton**：下拉菜单。
  ```dart
  DropdownButton<String>(
    value: selectedValue,
    onChanged: (newValue) {
      setState(() {
        selectedValue = newValue;
      });
    },
    items: <String>['Option 1', 'Option 2', 'Option 3'].map<DropdownMenuItem<String>>((String value) {
      return DropdownMenuItem<String>(value: value, child: Text(value));
    }).toList(),
  )
  ```

### 7. 导航和路由 `Widget`

这些 `Widget` 用于页面导航和路由管理。

- **Navigator**：用于页面之间的导航。
  ```dart
  Navigator.push(
    context,
    MaterialPageRoute(builder: (context) => SecondPage()),
  );
  ```

- **Scaffold**：提供默认的 Material Design 布局结构，包括 `AppBar`、`Body`、`FloatingActionButton` 等。
  ```dart
  Scaffold(
    appBar: AppBar(title: Text('My App')),
    body: Center(child: Text('Welcome to my app!')),
    floatingActionButton: FloatingActionButton(
      onPressed: () {
        // 按钮点击事件
      },
      child: Icon(Icons.add),
    ),
  )
  ```

### 8. 动画和效果 `Widget`

这些 `Widget` 用于实现动画和视觉效果。

- **AnimatedContainer**：带有动画效果的容器。
  ```dart
  AnimatedContainer(
    duration: Duration(seconds: 1),
    curve: Curves.easeInOut,
    width: _width,
    height: _height,
    color: _color,
  )
  ```

- **FadeTransition**：淡入淡出动画。
  ```dart
  FadeTransition(
    opacity: _animation,
    child: Container(
      width: 100,
      height: 100,
      color: Colors.blue,
    ),
  )
  ```

### 总结

以上是一些常见的 Flutter `Widget`，它们可以帮助你构建丰富且功能强大的用户界面。Flutter 的 `Widget` 生态系统非常丰富，你可以根据具体需求选择合适的 `Widget` 来构建你的应用。如果你有更具体的需求或想了解某个特定 `Widget` 的详细用法，请告诉我！