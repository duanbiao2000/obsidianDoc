---
aliases: 
<<<<<<< HEAD
theme: 
priority: false
=======
categories: 
high_priority: false
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
tags: 
source: https://www.bilibili.com/video/BV1yp29YSEq2/
---
![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20241012140754.png)

# 🚀 开发全栈AI图像编辑应用：Expo + Strapi + Clerk + Neon & React Native

`MediaLibrary.createAssetAsync()` 是 React Native 的 `expo-media-library` 库中的一个方法，它用于将本地文件（如图片或视频）保存到设备的媒体库中。下面是一个使用此方法的示例代码。

首先，确保你已经安装了 `expo-media-library` 包。如果没有安装，可以使用 npm 或 yarn 来安装：

```bash
npm install expo-media-library
# 或者
yarn add expo-media-library
```

接下来，在你的 React Native 项目中，你可以这样使用 `createAssetAsync` 方法来将一个本地 URI 对应的媒体文件保存到设备的媒体库中：

```jsx
import * as MediaLibrary from 'expo-media-library';
import * as Permissions from 'expo-permissions';
import { Alert } from 'react-native';

// 假设 localUri 是你要保存到媒体库的本地文件路径
const localUri = 'file:///path/to/your/local/file.jpg';

// 首先检查并请求权限
async function saveToLibrary() {
  const { status } = await Permissions.askAsync(Permissions.MEDIA_LIBRARY);
  if (status !== 'granted') {
    // 如果用户没有授权，则显示警告信息
    Alert.alert('我们需要访问您的媒体库权限才能保存文件');
    return;
  }

  try {
    // 创建一个新的媒体资源
    const asset = await MediaLibrary.createAssetAsync(localUri);
    
    // 可选: 将资产添加到特定相册
    // await MediaLibrary.createAlbumAsync('My Album', asset, false);

    // 成功后提示用户
    Alert.alert('文件已成功保存到您的媒体库！');
  } catch (error) {
    // 出错时处理错误
    console.error('Error saving to media library: ', error);
    Alert.alert('保存文件时发生错误，请稍后再试。');
  }
}

// 调用函数以执行保存操作
saveToLibrary();
```

这段代码首先会检查是否已经获得了访问媒体库的权限。如果没有，它会请求这个权限。一旦权限被授予，它就会尝试通过提供的本地 URI 创建一个新的媒体资源，并将其保存到用户的媒体库中。如果过程中遇到任何错误，它将捕获这些错误并在控制台打印出来，同时给用户一个反馈。

请确保在实际应用中替换 `localUri` 的值为你的文件的实际路径。此外，根据你的应用需求，你可能还需要适当地处理权限请求失败的情况。

`ToastAndroid.show()` 是 Android 平台上用来显示简短消息的一种方式。在 React Native 中，你可以使用 `react-native` 提供的 `ToastAndroid` 模块来实现这一点。这个模块只在 Android 上可用，在 iOS 上不起作用。

首先，确保你的项目中包含了对原生模块的支持。对于大多数 React Native 项目来说，默认情况下就已经包含了这些支持。

下面是如何使用 `ToastAndroid.show()` 的示例代码：

```jsx
import { ToastAndroid } from 'react-native';

// 显示一个简单的 Toast 消息
ToastAndroid.show('这是一个 Toast 消息', ToastAndroid.SHORT);

// 或者使用长时长显示
ToastAndroid.show('这是一个较长显示时间的 Toast 消息', ToastAndroid.LONG);

// 如果你想要自定义位置或更多选项，可以使用 showWithGravity 方法
ToastAndroid.showWithGravity(
  '带有特定位置的 Toast 消息',
  ToastAndroid.SHORT,
  ToastAndroid.CENTER // 这里可以设置为 TOP, BOTTOM, CENTER 等
);

// 更多可选参数
ToastAndroid.showWithGravityAndOffset(
  '带有特定位置和偏移量的 Toast 消息',
  ToastAndroid.LONG,
  ToastAndroid.BOTTOM,
  0, // x-offset (horizontal)
  50  // y-offset (vertical)
);
```

### 参数说明

- **message** - 要显示的消息文本。
- **duration** - Toast 显示的时间长度，可以是 `ToastAndroid.SHORT` 或 `ToastAndroid.LONG`。
- **gravity** - Toast 在屏幕上的位置，如 `ToastAndroid.TOP`, `ToastAndroid.CENTER`, `ToastAndroid.BOTTOM`。
- **xOffset** 和 **yOffset** - 可以用来进一步调整 Toast 的位置，相对于指定的 gravity 值。

### 注意事项

- `ToastAndroid` 只能在 Android 设备上运行。如果你的应用也需要在 iOS 上显示类似的消息提示，考虑使用第三方库如 `react-native-toast-message`，它提供了跨平台的支持。
- 当使用 `showWithGravityAndOffset` 时，请注意偏移值是以像素为单位的，这可能需要根据不同的设备进行调整以获得一致的效果。

通过这种方式，你可以在你的应用中轻松地向用户展示即时反馈或通知信息。

看起来你提到的 `GlobalApi.GetAllAiImages()` 并不是一个标准的 API 或库函数。这个方法名暗示它可能是某个特定应用或服务中自定义实现的一个全局API方法，用于获取所有与AI相关的图像。由于这并不是一个广泛认可的标准库或框架中的方法，你需要查看相关文档或源代码来了解其具体用法和参数。

如果这是你自己项目的一部分，或者是一个内部开发的库，那么你应该参照该库的文档或询问开发者以获得正确的使用方式。如果你可以提供更多的上下文信息，比如这个API是从哪里来的，或者是哪个库的一部分，我可以帮助你更具体地理解和使用它。

如果你是想要创建这样一个功能，即从服务器或其他数据源获取所有AI生成或处理过的图片，你可以按照以下步骤来设计这样一个API：

1. **定义API**：在后端服务中定义一个RESTful API端点，如 `/api/ai-images`，用来返回所有AI相关的图片列表。
2. **数据库查询**：编写后端逻辑来查询数据库，获取所有标记为AI生成或处理过的图片记录。
3. **响应格式**：将这些图片的信息（如URL、元数据等）打包成JSON格式，并通过HTTP响应发送给客户端。
4. **前端调用**：在前端React Native应用中，你可以使用Fetch API或Axios等库来调用这个API，并处理返回的数据。

下面是一个简单的示例，展示如何在React Native应用中调用这样的API：

```jsx
import React, { useEffect, useState } from 'react';
import { View, Text, Image, ActivityIndicator, FlatList } from 'react-native';

const App = () => {
  const [images, setImages] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // 调用自定义API获取AI图片
    fetch('https://your-api-url.com/api/ai-images')
      .then(response => response.json())
      .then(data => {
        setImages(data.images || []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching AI images: ', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <ActivityIndicator size="large" color="#0000ff" />;
  }

  return (
    <View>
      <FlatList
        data={images}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => (
          <Image
            source={{ uri: item.url }}
            style={{ width: 200, height: 200, margin: 5 }}
          />
        )}
      />
    </View>
  );
};

export default App;
```

在这个例子中，我们假设有一个后端API位于 `https://your-api-url.com/api/ai-images`，它返回一个包含图片URL和其他相关信息的JSON对象数组。`fetch` 函数被用来异步请求这些数据，并且一旦获取到数据，就更新状态变量 `images` 来渲染图片列表。

请确保替换上述示例中的URL为你实际的API地址，并根据实际情况调整代码逻辑。

在 React Native 中，`Dimensions` 是一个非常有用的模块，它可以让你获取到设备屏幕的尺寸信息。你可以使用 `Dimensions.get('screen')` 来获取整个屏幕的宽度和高度，或者使用 `Dimensions.get('window')` 来获取可使用的窗口大小（不包括状态栏等）。
### Dimensions.get('screen')
你提到的代码片段 `const ColumnWidth = Dimensions.get('screen').width * 0.9;` 是用来计算屏幕宽度的90%。这个值可以用来设置组件的宽度，比如一个列（column）的宽度，以确保它占据屏幕宽度的大部分，同时留有一些边距。

下面是一个完整的示例，展示如何在React Native应用中使用 `Dimensions` 来设置一个视图组件的宽度：

```jsx
import React from 'react';
import { View, Text, StyleSheet, Dimensions } from 'react-native';

// 获取屏幕宽度并计算ColumnWidth
const screenWidth = Dimensions.get('screen').width;
const ColumnWidth = screenWidth * 0.9;

const App = () => {
  return (
    <View style={styles.container}>
      <View style={[styles.column, { width: ColumnWidth }]}>
        <Text>这是一个占据屏幕宽度90%的列</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#f0f0f0',
  },
  column: {
    backgroundColor: '#fff',
    padding: 20,
    borderRadius: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 5,
    elevation: 3, // Android阴影效果
  },
});

export default App;
```

在这个示例中：

- 我们首先导入了 `Dimensions` 模块。
- 使用 `Dimensions.get('screen').width` 获取屏幕的宽度。
- 计算 `ColumnWidth` 为屏幕宽度的90%。
- 在 `App` 组件中，我们创建了一个 `View` 容器，并在其内部放置了一个宽度为 `ColumnWidth` 的子 `View`，该子 `View` 的样式被设置为白色背景、圆角、阴影等。

这样，无论用户的设备屏幕有多宽，你的列都会占据其90%，从而提供一致的用户体验。如果你的应用需要响应屏幕方向的变化（如从纵向变为横向），你还可以监听 `Dimensions` 的变化事件来更新布局。

### 阴影效果
在 React Native 中，`elevation` 属性用于在 Android 平台上实现阴影效果。`elevation` 对应于 Android 的原生 API，它会影响视图在空间中 z 轴上的顺序，从而创建出阴影效果。这个属性在 Android 5.0 以上版本才支持，并且它会影响到视图的层叠顺序。在 Android 上，如果两个同一层级的定位组件（position: "absolute"）都有 `elevation` 属性，则 `elevation` 大的组件会在上层显示。如果两个组件只有 `zIndex` 属性而没有 `elevation` 属性，则 `zIndex` 大的组件会在上层。如果两个组件都没有 `zIndex` 属性和 `elevation` 属性，则它们的层叠关系由它们在代码中的摆放位置决定，放在下面的组件会在上层显示。

对于 iOS 平台，阴影效果通常通过 `shadowColor`、`shadowOffset`、`shadowOpacity` 和 `shadowRadius` 这些属性来实现，而 `elevation` 属性在 iOS 上是无效的。因此，开发者在编写跨平台应用时需要注意这些差异，并可能需要使用条件语句来为不同的平台应用不同的样式。

此外，还有一些第三方库如 `react-native-shadow` 可以提供一致的阴影效果，无论在 iOS 还是 Android 上，都能实现类似的阴影效果。这些库通常会处理不同平台之间的差异，使得开发者可以写出更少的平台特定代码。
### FlatList
`FlatList` 是 React Native 中一个非常高效且强大的组件，用于显示长列表数据。它只渲染屏幕上可见的项目，这对于性能优化非常重要，特别是当你的列表很长时。`FlatList` 提供了许多有用的特性，如分页加载、滚动事件处理等。

### 基本用法

下面是一个简单的 `FlatList` 示例，展示如何创建一个基本的列表：

```jsx
import React from 'react';
import { FlatList, Text, View, StyleSheet } from 'react-native';

const data = [
  { id: '1', title: 'Item 1' },
  { id: '2', title: 'Item 2' },
  { id: '3', title: 'Item 3' },
  // 更多数据...
];

const App = () => {
  return (
    <View style={styles.container}>
      <FlatList
        data={data}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <Text style={styles.item}>{item.title}</Text>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 20,
    backgroundColor: '#f5fcff',
  },
  item: {
    padding: 10,
    fontSize: 18,
    height: 44,
  },
});

export default App;
```

### 主要属性

- **data**：传递给 `FlatList` 的数据数组。
- **keyExtractor**：为每个项目提供一个唯一的键。这通常是从数据项中提取一个唯一标识符。
- **renderItem**：这是一个函数，用来渲染列表中的每一个项目。它接收一个对象作为参数，其中包含当前项目的数据（`item`）和其他一些元数据。
- **numColumns**（可选）：设置列数，如果需要创建一个多列布局。
- **onEndReached** 和 **onEndReachedThreshold**（可选）：这两个属性可以用来实现无限滚动或分页加载功能。`onEndReached` 是一个回调函数，在用户接近列表底部时被调用；`onEndReachedThreshold` 设置了触发 `onEndReached` 的阈值。

### 分页加载示例

如果你想要在用户滚动到列表底部时加载更多数据，你可以使用 `onEndReached` 属性：

```jsx
import React, { useState, useEffect } from 'react';
import { FlatList, Text, View, StyleSheet, ActivityIndicator } from 'react-native';

const App = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(1);

  const fetchData = (newPage = page + 1) => {
    setLoading(true);
    setTimeout(() => {
      const newData = Array.from({ length: 10 }, (_, i) => ({
        id: `${newPage}-${i}`,
        title: `Item ${newPage * 10 + i}`,
      }));
      setData((prevData) => [...prevData, ...newData]);
      setPage(newPage);
      setLoading(false);
    }, 1000); // 模拟网络延迟
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <View style={styles.container}>
      <FlatList
        data={data}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <Text style={styles.item}>{item.title}</Text>
        )}
        onEndReached={() => {
          if (!loading) {
            fetchData();
          }
        }}
        onEndReachedThreshold={0.5} // 当剩余内容距离底部还有50%时触发
        ListFooterComponent={loading ? <ActivityIndicator size="large" color="#0000ff" /> : null}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 20,
    backgroundColor: '#f5fcff',
  },
  item: {
    padding: 10,
    fontSize: 18,
    height: 44,
  },
});

export default App;
```

在这个例子中，我们模拟了一个异步数据获取的过程，并且在用户滚动到列表底部时加载更多的数据。`ListFooterComponent` 用于在列表底部显示一个加载指示器，以提示用户正在加载更多数据。

通过这些基本的配置和选项，你可以构建出非常强大和高效的列表界面。如果你有更复杂的需求，比如不同的布局、动态高度等，`FlatList` 也提供了足够的灵活性来满足这些需求。

### ActivityIndicator
`ActivityIndicator` 是 React Native 中用于显示加载指示器的组件。它通常用来告诉用户当前正在进行一些处理，比如从网络加载数据或执行一个耗时的操作。`ActivityIndicator` 在 Android 和 iOS 上有不同的默认样式，但你可以通过属性来自定义其外观。

### 基本用法

下面是一个简单的 `ActivityIndicator` 示例：

```jsx
import React, { useState } from 'react';
import { View, Button, ActivityIndicator, StyleSheet } from 'react-native';

const App = () => {
  const [loading, setLoading] = useState(false);

  const startLoading = () => {
    setLoading(true);
    // 模拟一个异步操作
    setTimeout(() => {
      setLoading(false);
    }, 3000); // 3秒后结束加载
  };

  return (
    <View style={styles.container}>
      <Button title="开始加载" onPress={startLoading} />
      {loading && (
        <View style={styles.activityIndicatorContainer}>
          <ActivityIndicator size="large" color="#0000ff" />
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  activityIndicatorContainer: {
    marginTop: 20,
  },
});

export default App;
```

在这个示例中，当用户点击“开始加载”按钮时，`ActivityIndicator` 会显示出来，并在3秒后消失。

### 主要属性

- **size**：指定指示器的大小。可以是 `'small'`, `'large'` 或者自定义数值（例如 `50`）。
- **color**：指定指示器的颜色。可以使用颜色名称、十六进制值等。
- **animating**：布尔值，控制指示器是否显示。如果设置为 `false`，则指示器不会显示动画。
- **hidesWhenStopped**：布尔值，默认为 `true`。当 `animating` 为 `false` 时，如果这个属性也为 `true`，则指示器将完全隐藏。

### 自定义样式

你还可以通过 `StyleSheet` 来进一步自定义 `ActivityIndicator` 的样式和位置。例如：

```jsx
const styles = StyleSheet.create({
  activityIndicator: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  customIndicator: {
    backgroundColor: '#f0f0f0',
    borderRadius: 10,
    padding: 20,
  },
});
```

然后在你的 `ActivityIndicator` 组件中应用这些样式：

```jsx
<View style={styles.activityIndicator}>
  <View style={styles.customIndicator}>
    <ActivityIndicator size="large" color="#0000ff" />
  </View>
</View>
```

### 使用场景

- **数据加载**：在网络请求或其他异步操作期间显示。
- **长时间操作**：在执行耗时较长的操作时显示，以告知用户系统正在工作。
- **过渡效果**：在页面或视图之间切换时作为过渡效果显示。

通过合理地使用 `ActivityIndicator`，你可以提高用户体验，让用户知道应用程序正在响应他们的操作。

### Sonner
`Sonner` 是一个用于 React 的通知组件库，它提供了简单易用的 API 来显示各种类型的通知消息，如成功、警告、错误和信息提示。`Sonner` 的设计简洁且易于定制，支持多种配置选项，并且可以轻松地集成到现有的 React 项目中。

### 安装 Sonner

首先，你需要安装 `sonner` 库。你可以使用 npm 或 yarn 来安装：

```bash
npm install sonner
# 或者
yarn add sonner
```

### 基本用法

下面是一个简单的示例，展示如何在 React 项目中使用 `Sonner` 组件来显示不同类型的通知。

1. **创建一个新的 React 项目**（如果你还没有的话）：

   ```bash
   npx create-react-app my-sonner-app
   cd my-sonner-app
   ```

2. **安装 Sonner**：

   ```bash
   npm install sonner
   # 或者
   yarn add sonner
   ```

3. **在项目中使用 Sonner**：

   编辑 `src/App.js` 文件，添加以下代码：

   ```jsx
   import React from 'react';
   import { useNotifications } from 'sonner';

   const App = () => {
     const { notify } = useNotifications();

     const showSuccessNotification = () => {
       notify({
         title: '操作成功',
         description: '您的操作已成功完成。',
         status: 'success',
       });
     };

     const showErrorNotification = () => {
       notify({
         title: '发生错误',
         description: '处理过程中出现了一个错误，请稍后再试。',
         status: 'error',
       });
     };

     const showInfoNotification = () => {
       notify({
         title: '信息提示',
         description: '这是一个信息提示。',
         status: 'info',
       });
     };

     const showWarningNotification = () => {
       notify({
         title: '警告',
         description: '请注意，这是一条警告消息。',
         status: 'warning',
       });
     };

     return (
       <div style={{ padding: 20 }}>
         <h1>Sonner 通知示例</h1>
         <button onClick={showSuccessNotification}>显示成功通知</button>
         <button onClick={showErrorNotification}>显示错误通知</button>
         <button onClick={showInfoNotification}>显示信息通知</button>
         <button onClick={showWarningNotification}>显示警告通知</button>
       </div>
     );
   };

   export default App;
   ```

4. **运行项目**：

   ```bash
   npm start
   # 或者
   yarn start
   ```

### 详细说明

- **`useNotifications` Hook**：`useNotifications` 是 `Sonner` 提供的一个 Hook，它返回一个 `notify` 函数，你可以使用这个函数来显示通知。
- **`notify` 函数**：`notify` 函数接受一个对象作为参数，该对象包含通知的配置项，如 `title`, `description`, 和 `status`。
  - `title`：通知的标题。
  - `description`：通知的描述文本。
  - `status`：通知的状态，可以是 `'success'`, `'error'`, `'info'`, 或 `'warning'`。

### 自定义样式

`Sonner` 允许你通过传递额外的属性来自定义通知的样式。例如，你可以设置自定义的类名或内联样式。

```jsx
notify({
  title: '自定义样式通知',
  description: '这是一个带有自定义样式的通知。',
  status: 'info',
  className: 'custom-notification',
  style: { backgroundColor: '#f0f0f0', color: '#333' },
});
```

然后在你的 CSS 文件中定义相应的样式：

```css
.custom-notification {
  /* 你的自定义样式 */
}
```

### 高级功能

- **持续时间**：你可以设置通知的持续时间，或者让它一直显示直到用户手动关闭。
- **位置**：你可以设置通知的位置，如顶部、底部等。
- **回调函数**：你可以在通知关闭时执行一些操作，通过 `onClose` 回调函数来实现。

```jsx
notify({
  title: '高级功能通知',
  description: '这是一个带有高级功能的通知。',
  status: 'info',
  duration: 5000, // 显示 5 秒钟
  position: 'top-right', // 位置为右上角
  onClose: () => {
    console.log('通知已关闭');
  },
});
```

通过这些基本用法和高级功能，你可以轻松地在你的 React 项目中集成并使用 `Sonner` 来显示各种类型的通知。