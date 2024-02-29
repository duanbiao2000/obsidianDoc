---
aliases:

---
20230715 1600
links:
- [Material UI: An open-source React component library that implements Google's Material Design (mui.com)](https://mui.com/material-ui/)
- [Material Design](https://m3.material.io/)
- [Installation - Chakra UI (chakra-ui.com)](https://chakra-ui.com/getting-started)
title:
origin:
tags:

Material UI is an open-source React component library that implements Google's [Material Design](https://m2.material.io/).

- **Beautiful by default:** we're meticulous about our implementation of [Material Design](https://m2.material.io/), ensuring that every Material UI component meets the highest standards of form and function, but diverge from the official spec where necessary to provide multiple great options.
<!--SR:!2023-07-17,1,230-->

## Quickstart

The following code snippet demonstrates a simple app that uses the Material UI [Button](https://mui.com/material-ui/react-button/) component:

```jsx
import * as React from 'react';
import Button from '@mui/material/Button';

export default function MyApp() {
  return (
    <div>
      <Button variant="contained">Hello World</Button>
    </div>
  );
}
```
![[Pasted image 20230715160635.png]]
## Globals

Since Material UI components are built to function in isolation, they don't require any kind of globally scoped styles. For a better user experience and developer experience, we recommend adding the following globals to your app.

### Responsive meta tag

Material UI is a _mobile-first_ component library—we write code for mobile devices first, and then scale up the components as necessary using CSS media queries.

To ensure proper rendering and touch zooming for all devices, add the responsive viewport meta tag to your `<head>` element:

```html
<meta name="viewport" content="initial-scale=1, width=device-width" />
```

### CssBaseline

Material UI provides an optional [CssBaseline](https://mui.com/material-ui/react-css-baseline/) component. It fixes some inconsistencies across browsers and devices while providing resets that are better tailored to fit Material UI than alternative global style sheets like [normalize.css](https://github.com/necolas/normalize.css/).
```jsx
import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';

export default function MyApp() {
  return (
    <React.Fragment>
      <CssBaseline />
      {/* The rest of your application */}
    </React.Fragment>
  );
}
```
## Scoping on children

However, you might be progressively migrating a website to Material UI, using a global reset might not be an option. It's possible to apply the baseline only to the children by using the `ScopedCssBaseline` component.

```jsx
import * as React from 'react';
import ScopedCssBaseline from '@mui/material/ScopedCssBaseline';
import MyApp from './MyApp';

export default function MyApp() {
  return (
    <ScopedCssBaseline>
      {/* The rest of your application */}
      <MyApp />
    </ScopedCssBaseline>
  );
}
```

⚠️ Make sure you import `ScopedCssBaseline` first to avoid box-sizing conflicts as in the above example.

### Default font

Material UI uses the Roboto font by default. See [Installation—Roboto font](https://mui.com/material-ui/getting-started/installation/#roboto-font) for complete details.

# Official examples[](https://mui.com/material-ui/getting-started/example-projects/#official-examples)

You can find some example projects in the [GitHub repository](https://github.com/mui/material-ui) under the [`/examples`](https://github.com/mui/material-ui/tree/master/examples) folder:

[Example projects - Material UI (mui.com)](https://mui.com/material-ui/getting-started/example-projects/)

Next.js
[View JS example](https://github.com/mui/material-ui/tree/master/examples/material-next)/[View TS example](https://github.com/mui/material-ui/tree/master/examples/material-next-ts)


Create React App
[View JS example](https://github.com/mui/material-ui/tree/master/examples/material-cra)/[View TS example](https://github.com/mui/material-ui/tree/master/examples/material-cra-ts)

Tailwind CSS + CRA + TypeScript
[View example](https://github.com/mui/material-ui/tree/master/examples/material-cra-tailwind-ts)

# React Templates
[9+ Free React Templates - Material UI (mui.com)](https://mui.com/material-ui/getting-started/templates/)

## Recommended resources[](https://mui.com/material-ui/getting-started/learn/#recommended-resources)

Beyond our official documentation, there are countless members of our community who create fantastic tutorials and guides for working with Material UI.

The following is a curated list of some of the best third-party resources we've found for learning how to build beautiful apps with our components.

### Free

- **[Material UI v5 Crash Course](https://www.youtube.com/watch?v=o1chMISeTC0)** video by Laith Harb: everything you need to know to start building with the latest version of Material UI.
    
- **[React + Material UI - From Zero to Hero](https://www.youtube.com/playlist?list=PLDxCaNaYIuUlG5ZqoQzFE27CUOoQvOqnQ)** video series by The Atypical Developer: build along with this in-depth series, from basic installation through advanced component implementation.
    
- **[Next.js 11 Setup with Material UI v5](https://www.youtube.com/watch?v=IFaFFmPYyMI)** by Leo Roese: learn how to integrate Material UI into your Next.js app, using Emotion as the style engine.
    
- **[Material UI v5 Crash Course + Intro to React (2022 Edition)](https://www.youtube.com/watch?v=_W3uuxDnySQ)** by Anthony Sistilli: how and why to use Material UI, plus guidance on theming and style customization.
    
- **[Material UI v5 Tutorial Playlist](https://www.youtube.com/playlist?list=PLlR2O33QQkfXnZMMZC0y22gLayBbB1UQd)** by Nikhil Thadani (Indian Coders): a detailed playlist covering almost every component of Material UI with Create React App.
    
- **[The Clever Dev](https://www.youtube.com/channel/UCb6AZy0_D1y661PMZck3jOw)** and **[The Smart Devpreneur](https://smartdevpreneur.com/category/javascript/material-ui/)** by Jon M: dozens of high-quality videos and articles digging deep into the nuts and bolts of Material UI.
<!--SR:!2023-07-17,1,230!2023-07-17,1,230!2023-07-17,1,230!2023-07-17,1,230!2023-07-17,1,230!2023-07-17,1,230!2023-07-17,1,230-->

## Material UI resources[](https://mui.com/material-ui/getting-started/design-resources/#material-ui-resources)

### Figma

[Material UI for Figma](https://mui.com/store/items/figma-react/?utm_source=docs&utm_medium=referral&utm_campaign=installation-figma): a comprehensive component inventory for Figma, including over 1,500 unique elements that cover the full range of states and variations of each component.

### Adobe XD

[Material UI for Adobe XD](https://mui.com/store/items/adobe-xd-react/?utm_source=docs&utm_medium=referral&utm_campaign=installation-adobe-xd): a comprehensive component inventory for Adobe XD, including over 1,500 unique elements that cover the full range of states and variations of each component.

### Sketch

[Material UI for Sketch](https://mui.com/store/items/sketch-react/?utm_source=docs&utm_medium=referral&utm_campaign=installation-sketch): a comprehensive component inventory for Sketch, including over 1,500 unique elements that cover the full range of states and variations of each component, as well as 1,000+ icons in five themes.

## Third-party resources

### UXPin

[Material UI for UXPin](https://www.uxpin.com/merge/mui-library): A large UI kit of Material UI components. The design tool renders the components in a web runtime. It uses the same React implementation as your production environment.

[Frequently Asked Questions - Material UI (mui.com)](https://mui.com/material-ui/getting-started/faq/)
# Frequently Asked Questions

Stuck on a particular problem? Check some of these common gotchas first in the FAQ.Help us keep runningIf you don't mind tech-related ads (no tracking or remarketing), and want to keep us running, please whitelist MUI in your blocker.Thank you! ❤️

If you still can't find what you're looking for, you can refer to our [support page](https://mui.com/material-ui/getting-started/support/).



## Why do the fixed positioned elements move when a modal is opened?

Scrolling is blocked as soon as a modal is opened. This prevents interacting with the background when the modal should be the only interactive content. However, removing the scrollbar can make your **fixed positioned elements** move. In this situation, you can apply a global `.mui-fixed` class name to tell Material UI to handle those elements.
<!--SR:!2023-07-17,1,230-->

## How can I disable the ripple effect globally?  
如何全域禁用漣漪效應？

The ripple effect is exclusively coming from the `BaseButton` component. You can disable the ripple effect globally by providing the following in your theme:

```js
import { createTheme } from '@mui/material';

const theme = createTheme({
  components: {
    // Name of the component ⚛️
    MuiButtonBase: {
      defaultProps: {
        // The props to apply
        disableRipple: true, // No more ripple, on the whole application 💣!
      },
    },
  },
});
```

## How can I disable transitions globally?  
如何全域禁用轉換？

Material UI uses the same theme helper for creating all its transitions. Therefore you can disable all transitions by overriding the helper in your theme:

```js
import { createTheme } from '@mui/material';

const theme = createTheme({
  transitions: {
    // So we have `transition: none;` everywhere
    create: () => 'none',
  },
});
```

It can be useful to disable transitions during visual testing or to improve performance on low-end devices.

You can go one step further by disabling all transitions and animations effects:

```js
import { createTheme } from '@mui/material';

const theme = createTheme({
  components: {
    // Name of the component ⚛️
    MuiCssBaseline: {
      styleOverrides: {
        '*, *::before, *::after': {
          transition: 'none !important',
          animation: 'none !important',
        },
      },
    },
  },
});
```

Notice that the usage of `CssBaseline` is required for the above approach to work. If you choose not to use it, you can still disable transitions and animations by including these CSS rules:

```css
*,
*::before,
*::after {
  transition: 'none !important';
  animation: 'none !important';
}
```

## Do I have to use Emotion to style my app?  
我是否必須使用情感來設置我的應用樣式？

Perhaps, however, you're adding some Material UI components to an app that already uses another styling solution, or are already familiar with a different API, and don't want to learn a new one? In that case, head over to the [Style library interoperability](https://mui.com/material-ui/guides/interoperability/) section, where we show how simple it is to restyle Material UI components with alternative style libraries.


## How do I use react-router?

We detail the [integration with third-party routing libraries](https://mui.com/material-ui/guides/routing/) like react-router, Gatsby or Next.js in our guide.

## How can I access the DOM element?

All Material UI components that should render something in the DOM forward their ref to the underlying DOM component. This means that you can get DOM elements by reading the ref attached to Material UI components:

```jsx
// or a ref setter function
const ref = React.createRef();
// render
<Button ref={ref} />;
// usage
const element = ref.current;
```

If you're not sure if the Material UI component in question forwards its ref you can check the API documentation under "Props" e.g. the [Button API](https://mui.com/material-ui/api/button/#props) includes

The ref is forwarded to the root element.

indicating that you can access the DOM element with a ref.

## My App doesn't render correctly on the server

If it doesn't work, in 99% of cases it's a configuration issue. A missing property, a wrong call order, or a missing component – server-side rendering is strict about configuration.

The best way to find out what's wrong is to compare your project to an **already working setup**. Check out the [reference implementations](https://mui.com/material-ui/guides/server-rendering/#reference-implementations), bit by bit.
<!--SR:!2023-07-17,1,230-->

## Why are the colors I am seeing different from what I see here?

The documentation site is using a custom theme. Hence, the color palette is different from the default theme that Material UI ships. Please refer to [this page](https://mui.com/material-ui/customization/theming/) to learn about theme customization.

## Why does component X require a DOM node in a prop instead of a ref object?

Components like the [Portal](https://mui.com/base-ui/react-portal/components-api/) or [Popper](https://mui.com/material-ui/api/popper/#props) require a DOM node in the `container` or `anchorEl` prop respectively. It seems convenient to simply pass a ref object in those props and let Material UI access the current value.

This works in a simple scenario:

```jsx
function App() {
  const container = React.useRef(null);

  return (
    <div className="App">
      <Portal container={container}>
        <span>portaled children</span>
      </Portal>
      <div ref={container} />
    </div>
  );
}
```

where `Portal` would only mount the children into the container when `container.current` is available. Here is a naive implementation of Portal:

```jsx
function Portal({ children, container }) {
  const [node, setNode] = React.useState(null);

  React.useEffect(() => {
    setNode(container.current);
  }, [container]);

  if (node === null) {
    return null;
  }
  return ReactDOM.createPortal(children, node);
}
```

With this simple heuristic `Portal` might re-render after it mounts because refs are up-to-date before any effects run. However, just because a ref is up-to-date doesn't mean it points to a defined instance. If the ref is attached to a ref forwarding component it is not clear when the DOM node will be available. In the example above, the `Portal` would run an effect once, but might not re-render because `ref.current` is still `null`. This is especially apparent for React.lazy components in Suspense. The above implementation could also not account for a change in the DOM node.

This is why we require a prop with the actual DOM node so that React can take care of determining when the `Portal` should re-render:

```jsx
function App() {
  const [container, setContainer] = React.useState(null);
  const handleRef = React.useCallback(
    (instance) => setContainer(instance),
    [setContainer],
  );

  return (
    <div className="App">
      <Portal container={container}>
        <span>Portaled</span>
      </Portal>
      <div ref={handleRef} />
    </div>
  );
}
```

## What's the clsx dependency for?

[clsx](https://github.com/lukeed/clsx) is a tiny utility for constructing `className` strings conditionally, out of an object with keys being the class strings, and values being booleans.

Instead of writing:

```jsx
// let disabled = false, selected = true;

return (
  <div
    className={`MuiButton-root ${disabled ? 'Mui-disabled' : ''} ${
      selected ? 'Mui-selected' : ''
    }`}
  />
);
```

you can do:

```jsx
import clsx from 'clsx';

return (
  <div
    className={clsx('MuiButton-root', {
      'Mui-disabled': disabled,
      'Mui-selected': selected,
    })}
  />
);
```

## I cannot use components as selectors in the styled() utility. What should I do?

If you are getting the error: `TypeError: Cannot convert a Symbol value to a string`, take a look at the [styled()](https://mui.com/system/styled/#how-to-use-components-selector-api) docs page for instructions on how you can fix this.

## [legacy] I have several instances of styles on the page

If you are seeing a warning message in the console like the one below, you probably have several instances of `@mui/styles` initialized on the page.

It looks like there are several instances of `@mui/styles` initialized in this application. This may cause theme propagation issues, broken class names, specificity issues, and make your application bigger without a good reason.

### Possible reasons

There are several common reasons for this to happen:

- You have another `@mui/styles` library somewhere in your dependencies.
- You have a monorepo structure for your project (e.g, lerna, yarn workspaces) and `@mui/styles` module is a dependency in more than one package (this one is more or less the same as the previous one).
- You have several applications that are using `@mui/styles` running on the same page (e.g., several entry points in webpack are loaded on the same page).

### Duplicated module in node_modules

If you think that the issue may be in the duplication of the @mui/styles module somewhere in your dependencies, there are several ways to check this. You can use `npm ls @mui/styles`, `yarn list @mui/styles` or `find -L ./node_modules | grep /@mui/styles/package.json` commands in your application folder.

If none of these commands identified the duplication, try analyzing your bundle for multiple instances of @mui/styles. You can just check your bundle source, or use a tool like [source-map-explorer](https://github.com/danvk/source-map-explorer) or [webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer).

If you identified that duplication is the issue that you are encountering there are several things you can try to solve it:

If you are using npm you can try running `npm dedupe`. This command searches the local dependencies and tries to simplify the structure by moving common dependencies further up the tree.

If you are using webpack, you can change the way it will [resolve](https://webpack.js.org/configuration/resolve/#resolve-modules) the @mui/styles module. You can overwrite the default order in which webpack will look for your dependencies and make your application node_modules more prioritized than default node module resolution order:

```diff
 resolve: {
+  alias: {
+    '@mui/styles': path.resolve(appFolder, 'node_modules', '@mui/styles'),
+  },
 },
```

### Running multiple applications on one page

If you have several applications running on one page, consider using one @mui/styles module for all of them. If you are using webpack, you can use [CommonsChunkPlugin](https://webpack.js.org/plugins/commons-chunk-plugin/) to create an explicit [vendor chunk](https://webpack.js.org/plugins/commons-chunk-plugin/#explicit-vendor-chunk), that will contain the @mui/styles module:

```diff
  module.exports = {
    entry: {
+     vendor: ['@mui/styles'],
      app1: './src/app.1.js',
      app2: './src/app.2.js',
    },
    plugins: [
+     new webpack.optimize.CommonsChunkPlugin({
+       name: 'vendor',
+       minChunks: Infinity,
+     }),
    ]
  }
```

## [legacy] Why aren't my components rendering correctly in production builds?

The #1 reason this happens is likely due to class name conflicts once your code is in a production bundle. For Material UI to work, the `className` values of all components on a page must be generated by a single instance of the [class name generator](https://mui.com/system/styles/advanced/#class-names).

To correct this issue, all components on the page need to be initialized such that there is only ever **one class name generator** among them.
<!--SR:!2023-07-17,1,230-->

You could end up accidentally using two class name generators in a variety of scenarios:

- You accidentally **bundle** two versions of `@mui/styles`. You might have a dependency not correctly setting Material UI as a peer dependency.
- You are using `StylesProvider` for a **subset** of your React tree.
- You are using a bundler and it is splitting code in a way that causes multiple class name generator instances to be created.
<!--SR:!2023-07-17,1,230!2023-07-17,1,230-->

If you are using webpack with the [SplitChunksPlugin](https://webpack.js.org/plugins/split-chunks-plugin/), try configuring the [`runtimeChunk` setting under `optimizations`](https://webpack.js.org/configuration/optimization/#optimization-runtimechunk).

Overall, it's simple to recover from this problem by wrapping each Material UI application with [`StylesProvider`](https://mui.com/system/styles/api/#stylesprovider) components at the top of their component trees **and using a single class name generator shared among them**.
<!--SR:!2023-07-17,1,230-->

### [legacy] CSS works only on first load and goes missing

The CSS is only generated on the first load of the page. Then, the CSS is missing on the server for consecutive requests.

#### Action to Take

The styling solution relies on a cache, the _sheets manager_, to only inject the CSS once per component type (if you use two buttons, you only need the CSS of the button one time). You need to create **a new `sheets` instance for each request**.
<!--SR:!2023-07-17,1,230-->

Example of fix:

```diff
-// Create a sheets instance.
-const sheets = new ServerStyleSheets();

 function handleRender(req, res) {
+  // Create a sheets instance.
+  const sheets = new ServerStyleSheets();

   //…

   // Render the component to a string.
   const html = ReactDOMServer.renderToString(
```

### [legacy] React class name hydration mismatch

**⚠️ Warning**
<!--SR:!2023-07-17,1,230-->

Prop className did not match.

There is a class name mismatch between the client and the server. It might work for the first request. Another symptom is that the styling changes between initial page load and the downloading of the client scripts.

#### Action to Take

The class names value relies on the concept of [class name generator](https://mui.com/system/styles/advanced/#class-names). The whole page needs to be rendered with **a single generator**. This generator needs to behave identically on the server and on the client. For instance:
<!--SR:!2023-07-17,1,230-->

- You need to provide a new class name generator for each request. But you shouldn't share a `createGenerateClassName()` between different requests:
    
    Example of fix:
    
    ```diff
    -// Create a new class name generator.
    -const generateClassName = createGenerateClassName();
    
     function handleRender(req, res) {
    +  // Create a new class name generator.
    +  const generateClassName = createGenerateClassName();
    
       //…
    
       // Render the component to a string.
       const html = ReactDOMServer.renderToString(
    ```
    
- You need to verify that your client and server are running the **exactly the same version** of Material UI. It is possible that a mismatch of even minor versions can cause styling problems. To check version numbers, run `npm list @mui/styles` in the environment where you build your application and also in your deployment environment.
    
    You can also ensure the same version in different environments by specifying a specific Material UI version in the dependencies of your package.json.
    
    _example of fix (package.json):_
    
    ```diff
      "dependencies": {
        ...
    -   "@mui/styles": "^5.0.0",
    +   "@mui/styles": "5.0.0",
        ...
      },
    ```
    
- You need to make sure that the server and the client share the same `process.env.NODE_ENV` value.
<!--SR:!2023-07-17,1,230-->