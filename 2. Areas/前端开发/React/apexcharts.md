---
aliases: 
theme: 
original: 
url: 
author: 
created_date: 
date_updated: 2024-07-24 13:48
type: 
high_priority: false
tags:
---


### 步骤详情

#### 1. 项目初始化

首先，创建一个新的 React 项目并安装 `react-apexcharts`。

```bash
npx create-react-app analytics-dashboard
cd analytics-dashboard
npm install react-apexcharts apexcharts
```

#### 2. 创建分析首页组件

创建一个新的组件 `Dashboard`。

```javascript
import React, { useState, useEffect } from 'react';
import Chart from 'react-apexcharts';

// 假设有一个 API 返回以下数据
const fetchData = async () => {
  return {
    series: [
      {
        name: 'Sales',
        data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
      }
    ],
    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
  };
};

const Dashboard = () => {
  const [data, setData] = useState({ series: [], categories: [] });

  useEffect(() => {
    const getData = async () => {
      const result = await fetchData();
      setData(result);
    };

    getData();
  }, []);

  const options = {
    chart: {
      type: 'line'
    },
    xaxis: {
      categories: data.categories
    }
  };

  return (
    <div>
      <h1>Analytics Dashboard</h1>
      <Chart options={options} series={data.series} type="line" height={350} />
    </div>
  );
};

export default Dashboard;
```

#### 3. 将组件添加到应用程序中

在 `src/App.js` 中导入并使用 `Dashboard` 组件。

```javascript
import React from 'react';
import Dashboard from './Dashboard';

function App() {
  return (
    <div className="App">
      <Dashboard />
    </div>
  );
}

export default App;
```

