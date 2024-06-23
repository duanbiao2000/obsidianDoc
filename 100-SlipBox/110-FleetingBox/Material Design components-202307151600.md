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
