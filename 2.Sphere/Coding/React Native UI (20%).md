---
date: 2025-05-13 00:05
tags:
  - Tech/Code
---

### **核心基础构建块 (Fundamental Building Blocks)**

1. **`View`**

   - **作用：** 这是 React Native 中最基本的容器组件，类似于 Web 中的 `div`。它用于布局、样式化，并且是所有其他组件的基石。
   - **为何重要：** 所有的布局（通过 Flexbox）都是在 `View` 上实现的。没有 `View`，就没有 UI 结构。
   - **掌握点：** 熟练运用它的 `style` 属性（特别是 `flexbox` 属性）、`accessibility` 属性以及事件处理（如 `onLayout`）。
2. **`Text`**

   - **作用：** 专门用于显示文本内容。所有文本都必须嵌套在 `<Text>` 组件内。
   - **为何重要：** 任何需要显示文字的地方都离不开它。
   - **掌握点：** 它的 `style` 属性（字体大小、颜色、行高、对齐方式等）、`numberOfLines`、`onPress` (可点击文本)。
3. **`Image`**

   - **作用：** 用于显示图片，可以是本地图片、网络图片或 Base64 图片。
   - **为何重要：** 几乎所有应用都需要展示图片。
   - **掌握点：** `source` 属性（`uri` 或 `require()`），`style` 中的 `width`, `height`, `resizeMode`。

---

### **用户输入与交互 (User Input & Interaction)**

4. **`TextInput`**

   - **作用：** 用于接收用户的文本输入。
   - **为何重要：** 登录、搜索、评论、表单等任何需要用户输入文本的场景都必须使用它。
   - **掌握点：** `value`, `onChangeText`, `placeholder`, `keyboardType`, `secureTextEntry`, `multiline` 等常用属性，以及如何处理键盘弹出和布局变化。
5. **`Pressable` (或 `TouchableOpacity` / `Button`)**

   - **作用：** 用于创建可点击的区域，响应用户触摸。`Pressable` 是 React Native 0.63+ 引入的，提供了更灵活的交互和样式控制。
   - **为何重要：** 按钮、导航项、可点击列表项等所有用户交互的入口。
   - **掌握点：** `onPress`, `onLongPress`, `android_ripple` (Android 波纹效果)，以及如何利用它的 `pressed` 状态进行样式反馈。如果你还没升级到最新 RN 版本，`TouchableOpacity` 或 `TouchableWithoutFeedback` 依然很常用。`Button` 是一个更简单的基础按钮，但定制性不如 `Pressable`。

---

### **列表与长内容展示 (Lists & Long Content)**

6. **`ScrollView`**

   - **作用：** 当内容超出屏幕大小时，使其可滚动。
   - **为何重要：** 解决内容溢出问题，所有屏幕外的非列表内容都依赖它。
   - **掌握点：** `horizontal`, `showsVerticalScrollIndicator`, `contentContainerStyle`。
7. **`FlatList`**

   - **作用：** 高性能的列表组件，用于渲染大量数据，通过虚拟化技术优化内存和渲染效率。
   - **为何重要：** 几乎所有应用都有列表界面（如新闻列表、好友列表、商品列表），`FlatList` 是处理大量数据的标准组件。
   - **掌握点：** `data`, `renderItem`, `keyExtractor`, `ListHeaderComponent`, `ListFooterComponent`, `ItemSeparatorComponent`, `onEndReached`, `onRefresh`, `refreshing` 等，理解其虚拟化原理和性能优化技巧。

---

### **样式与布局 (Styling & Layout Concepts)**

虽然不是独立的组件，但它们与 UI 组件紧密结合，必须掌握：

8. **`StyleSheet` API**

   - **作用：** 用于创建样式对象，类似于 CSS，但具有性能优化和更好的可维护性。
   - **为何重要：** 推荐的样式定义方式，性能优于内联样式。
   - **掌握点：** `StyleSheet.create()` 的用法，如何合并样式（`[]`），以及理解 `flexbox` 属性在 React Native 中的应用。
9. **Flexbox 布局**

   - **作用：** 一种弹性盒子布局模型，用于在 `View` 组件中排列、对齐和分配空间。
   - **为何重要：** 这是 React Native 中唯一的布局系统。
   - **掌握点：** `flex`, `flexDirection`, `justifyContent`, `alignItems`, `alignSelf`, `padding`, `margin`, `width`, `height` 等所有 Flexbox 相关的属性。

---

### **辅助与平台适配 (Helpers & Platform Adaptation)**

10. **`ActivityIndicator`**

    - **作用：** 显示一个旋转的加载指示器，表示正在进行操作。
    - **为何重要：** 用户体验的关键，提供视觉反馈，避免界面僵死感。
    - **掌握点：** `animating`, `size`, `color` 属性。
11. **`SafeAreaView` (for iOS)**

    - **作用：** 自动处理 iOS 设备上的“安全区域”，如刘海屏、状态栏、Home 指示条等，防止内容被遮挡。
    - **为何重要：** 在 iOS 上构建符合设计规范的界面必备。
    - **掌握点：** 理解其作用，并在合适的根视图或内容区域使用它。
12. **`Platform` API**

    - **作用：** 提供运行时判断当前运行平台（iOS 或 Android）的能力。
    - **为何重要：** 当需要根据平台差异化处理 UI 或功能时（例如不同的样式、不同的组件）。
    - **掌握点：** `Platform.OS`, `Platform.select()` 的使用。

---

**总结：**

掌握以上这些 React Native UI 组件和相关的布局/样式概念，你就已经站在了构建 80% 甚至更多应用的坚实基础之上。这就像学习一门语言先掌握其常用词汇和基本语法一样。

在此之上，你再去学习更高级的组件（如 `SectionList`、`Modal`、`KeyboardAvoidingView`）、动画库（如 `Animated`、`Reanimated`）或第三方 UI 组件库（如 React Native Paper、NativeBase 等），就能更快速高效地扩展你的能力。
