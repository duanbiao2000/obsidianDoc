---
aliases:
  - React中跨域代理
source:
author:
createdAt:
updateAt:
categories:
high_priority: false
tags:
---
在React应用中配置跨域代理有几种常见方案。我可以为您概述主要的方法:

1. 使用Create React App的代理功能:

如果您的项目是使用Create React App创建的,可以在package.json中添加"proxy"字段:

```json
{
  "proxy": "http://api.example.com"
}
```

这会将未知请求代理到指定的URL。

2. 使用http-proxy-middleware:

这种方法允许更灵活的配置。首先安装http-proxy-middleware:

```
npm install http-proxy-middleware
```

然后在src目录下创建setupProxy.js文件:

```javascript
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://api.example.com',
      changeOrigin: true,
    })
  );
};

```

这会将所有/api开头的请求代理到指定的目标URL。

3. 在生产环境中使用服务器配置:

在生产环境中,通常会使用Nginx或Apache等Web服务器来处理代理。例如,Nginx的配置可能如下:

```nginx
location /api/ {
    proxy_pass http://api.example.com;
}
```



当然,我可以提供一个更具体的项目实例。让我们假设我们正在开发一个天气预报应用,需要从OpenWeatherMap API获取数据。我们将使用Create React App创建项目,并配置代理以解决跨域问题。

首先,创建一个新的React项目:

```bash
npx create-react-app weather-forecast-app
cd weather-forecast-app
```

现在,让我们配置代理并创建一个组件来获取和显示天气数据。

1. 配置代理:

在`package.json`文件中添加以下行:

```json
{
  ...
  "proxy": "https://api.openweathermap.org"
}
```

2. 创建一个Weather组件:

```tsx
import React, { useState, useEffect } from 'react';

const API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'; // 请替换为您的实际API密钥

export default function Weather() {
  const [weatherData, setWeatherData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchWeather();
  }, []);

  const fetchWeather = async () => {
    try {
      const response = await fetch(`/data/2.5/weather?q=London,uk&appid=${API_KEY}&units=metric`);
      if (!response.ok) {
        throw new Error('Weather data not available');
      }
      const data = await response.json();
      setWeatherData(data);
      setLoading(false);
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="weather-container">
      <h2>Weather in {weatherData.name}</h2>
      <p>Temperature: {weatherData.main.temp}°C</p>
      <p>Condition: {weatherData.weather[0].main}</p>
      <p>Description: {weatherData.weather[0].description}</p>
    </div>
  );
}

```

3. 在App.js中使用Weather组件:

```jsx
import React from 'react';
import Weather from './Weather';

function App() {
  return (
    <div className="App">
      <h1>My Weather App</h1>
      <Weather />
    </div>
  );
}

export default App;
```

4. 运行应用:

```bash
npm start
```

现在,让我解释一下这个例子:

1. 我们使用了OpenWeatherMap的实际API端点(`https://api.openweathermap.org`)作为代理目标。

2. 在Weather组件中,我们向`/data/2.5/weather`发送请求。由于我们配置了代理,这个请求实际上会被发送到`https://api.openweathermap.org/data/2.5/weather`。

3. 我们使用了一个具体的城市(London)和真实的API参数(`appid`和`units`)。

4. 组件在加载时获取天气数据,并显示温度、天气状况和描述。

这个例子展示了如何在一个真实的React应用中处理跨域请求。通过在`package.json`中配置代理,我们可以在开发环境中轻松解决CORS问题,而无需修改API服务器。

请注意,在生产环境中,您可能需要使用不同的方法,例如在您的web服务器(如Nginx)中配置代理,或者使用后端服务来转发请求。

