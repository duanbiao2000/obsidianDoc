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
---
SWR（Stale-While-Revalidate）是一个用于 React 的数据获取库，它可以帮助你轻松地管理数据获取的状态，如加载中、错误等。在你的代码中，`useSWR` 被用来获取客户端数据和交易数据。

`useSWR` 的基本用法如下：

```javascript
import useSWR from 'swr'

const fetcher = (url) => fetch(url).then(res => res.json())

function MyComponent() {
  const { data, error } = useSWR('/api/data', fetcher)

  if (error) return <div>Failed to load</div>
  if (!data) return <div>Loading...</div>

  return <div>My data: {data}</div>
}
```

在这个例子中，`useSWR` 被用来获取 `/api/data` 的数据。`fetcher` 函数被用来获取数据，然后 `useSWR` 返回的数据和错误状态被用来渲染组件。

在你的代码中，`useSampleClients` 和 `useSampleTransactions` 函数使用了 `useSWR` 来获取客户端数据和交易数据。这两个函数返回的数据、加载状态和错误状态被用来渲染组件。

总的来说，SWR 是一个非常有用的库，可以帮助你轻松地管理数据获取的状态。