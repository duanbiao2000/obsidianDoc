---
created: 2024-06-03T19:34:52 (UTC +08:00)
tags: [Coze]
source: https://juejin.cn/post/7357716989782442011
author: 掘金酱
---

# 了解扣子：如何用 CozeIDE 制作一个插件 - 掘金

> ## Excerpt
> CozeIDE 是扣子给你提供的插件开发利器，你可以在 CozeIDE 上开发、测试插件，并由扣子帮你托管运行插件代码，你无需关心购买服务器、配置域名等事项。

---
## 一、CozeIDE 是什么？

CozeIDE 是扣子给你提供的插件开发利器，你可以在 CozeIDE 上开发、测试插件，并由扣子帮你托管运行插件代码，你无需关心购买服务器、配置域名等事项。CozeIDE 还内置了 AI 编程助手，无论你是否有编程基础，都可以通过 AI 助手，快速开发插件。

## CozeIDE 有哪些主要功能？

CozeIDE 为插件开发者提供了一整套代码编辑、依赖包管理、测试、元数据管理、发布部署能力，以及 AI 编程助手，解决你开发插件过程中的各种问题。

### 1、代码编辑

CozeIDE 为你提供了代码模板，你只需要在代码模板的基础上进行开发、完善。IDE 提供了 2 种运行时：Node.js 和 Python，满足你不同的诉求。

#### Node.js 模板示例

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65fe0e706970420b80295185feac8306~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3838&h=1982&s=355815&e=png&b=ffffff)

#### Python 模板示例

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/557ea929024c4b01969fc0c8d37494f7~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3838&h=1988&s=350184&e=png&b=ffffff)

### 2、AI 编程助手

如果你写代码过程遇到问题，可通过快捷键唤起 AI 编程助手（macOS 为 `Command + I`、windows 为 `Ctrl + I`）。AI 编程助手可为你提供以下几个便捷的能力：

-   AI 生成代码：输入想要的功能，点击
-   AI 修改代码：选中待修改的代码，唤起 AI 助手，输入想要修改的功能。
-   AI 代码解释/代码注释：选中代码后，输入/ 选择不同指令，由 AI 对代码进行解释，或者自动生成代码注释。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a24f7806dfef4b02817e120adc3a8f54~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=1370&h=398&s=56530&e=png&b=fbfbfb)

### 3、依赖包管理

依赖包是代码运行依赖的外部代码模块。如果你的代码中引用了其他外部的模块，但没有安装依赖，IDE 会提示错误。根据错误信息，点击左下角【添加依赖】，输入依赖的名称即可安装。安装过程中可查看控制台的日志，观察安装进度。

#### 具体示例

未安装依赖时报错

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb5f4c0fdb2c4ffb97d973a969e88798~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=2212&h=1816&s=484582&e=png&b=ffffff)

安装依赖

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/695dfc026ea6435f9cc5f4aa4b39caf3~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=2344&h=1830&s=508690&e=png&b=ffffff)

安装依赖后未报错

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f8ee10f9c94458b9e1227feafc9dd32~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=2308&h=1828&s=471589&e=png&b=ffffff)

若需要指定安装某个版本，你可以通过依赖名@版本号来进行选择。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/857eb4870eaf484dadcf264b08f64614~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=2344&h=1830&s=507621&e=png&b=ffffff)

### 4、元数据

元数据的作用是让大模型理解每个工具输入参数、输出参数有哪些，以及对应的含义。

在以下代码示例中，这个工具接收一个输入参数：name，并返回一个参数：message。因此，我们需要将 name 和 message 补充到元数据面板。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af4b6a1176594b3290084a8b1701c181~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=1870&h=1230&s=284866&e=png&b=ffffff)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fffbe885923c447aaf820e3e06723f93~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3142&h=1540&s=210189&e=png&b=fefefe)

### 5、测试

写完代码和元数据后，需要验证代码是否正常运行。点击右侧的测试，输入测试的数据。

如果你已经填写元数据中的输入参数，则可以点击自动生成，IDE 会生成符合你结构定义的随机数据。你需要修改成你需要的值即可。填写完成后，点击运行，即可看到测试结果。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6a4a80d50a84bb899e8d39fae5acd36~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3838&h=1970&s=493965&e=png&b=ffffff)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73cfb4e9af6a43caaac6a603b9acad47~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3836&h=1986&s=574792&e=png&b=f5f5f8)

如果你之前未填写元数据的输出参数结构，可以在测试通过后，点击下方的【更新输出参数】，IDE 会自动更新覆盖在元数据区域，你只需要补充完善描述即可。

### 6、发布

测试通过后，就可以去点击发布啦。如果你开发了多个工具，但有些没测试完成不想发布，可以在该入口禁用这些工具，只发布启用的工具。

接着选择“信息收集声明”。如果插件会收集用户信息，请选择“是”并选择具体信息，用户在使用该插件时能了解收集的信息。否则，选择“否”，点击发布即可。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17491025af234205aa74d45aa8c30d87~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3838&h=1990&s=602136&e=png&b=f6f6f9)

## 二、10 分钟快速制作插件

接下来我们以开发实际插件为例，演示整个创建流程。

### 插件一、查询股票价格（难度 🌟 ）

#### 明确目的和方案

首先，需要构思这个插件具备什么能力：根据股票名称查询股票价格。

接着搜索哪些网站可以免费查询股票价格。通过互联网检索，可以得知“alpha vantage”提供了免费查询美股股票价格的能力。明确了目的和方案后，开始开发插件。该插件难度🌟，教程内已提供源码，可直接复制使用。

#### 操作步骤

##### 步骤一：新建插件和工具

1.  打开 [www.coze.cn/](https://link.juejin.cn/?target=https%3A%2F%2Fwww.coze.cn%2F "https://www.coze.cn/") 选择需要所属的团队。
    
2.  点击右上角创建插件，填写名称，选择插件创建方式为“在 Coze IDE 创建”，运行时选择“Node.js”（你也可以根据自己的情况，选择 Python）
    
    1.  插件名称：查询股票价格
    2.  插件描述：查询股票价格
3.  点击“在 IDE 中创建工具”，填写工具名称和介绍：
    
    1.  名称：search\_stock\_prices
    2.  介绍：根据股票名称查询股票价格

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21e65a135c884a35945636ac65bc3db9~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=1170&h=1370&s=142491&e=png&b=f5f7fa)

##### 步骤二：代码编写和开发

1.  因为已经明确需要根据股票名称查询价格，所以可以先在元数据中定义一个输入参数，名称：code，描述为：股票名称

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26d3eadaf07044ee93589b2b5ae2139d~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=2480&h=1356&s=193893&e=png&b=fdfdfd)

_编写元信息_

2.  在代码编辑器中，通过快捷键唤起 AI 助手（macOS 为 `Command + I`、windows 为 `Ctrl + I`），输入我们的需求：根据 input.code，到 alpha vantage 查询股票价格。你也可以手动编写代码。
3.  AI 生成代码后，点击接受，再进行调整，最后得到这样一份代码。（若 AI 生成效果不好，可直接复制本代码使用）

```undefined
import { Args } from '@/runtime'; import { Input, Output } from "@/typings/search_stock_prices/search_stock_prices"; import axios from 'axios'; export async function handler({ input, logger }: Args<Input>): Promise<Output> { const code = input.code; const apiKey = 'YOUR_ALPHA_VANTAGE_API_KEY'; const url = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${code}&apikey=${apiKey}`; try { const response = await axios.get(url); const data = response.data['Global Quote']; return { code: code, price: data['05. price'], }; } catch (error) { logger.error(`Error fetching stock price for ${code}: ${error}`); return { code: code, price: null, }; } }
```

4.  左侧安装 axios 依赖，安装该依赖后可发起请求查询数据。未安装依赖时会提示错误。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fef13ab79a8d48c3bbb174d3ec513c37~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3836&h=1990&s=505878&e=png&b=ffffff)

_安装依赖后正常_

##### 步骤三：测试

1.  点击自动生成测试数据，修改 code 为 AAPL（苹果），点击运行。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96f9f32e24e3434381cee3938d537c1d~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3836&h=1980&s=558860&e=png&b=f6f6f9)

2.  点击“更新输出参数”，然后切换到“元数据”面板，修改输出参数中 code 和 price 的描述。修改后，需再次运行测试，避免修改错误导致运行出现问题。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adbdd6a4c06a4579b0a4c70841660a2c~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3834&h=1982&s=382134&e=png&b=f5f5f8)

3.  测试通过后，就可以进行发布

##### 步骤四：发布

1.  点击右上角发布，点击下一步，选择“否”，点发布。
2.  发布成功后，就可以去创建 Bot 使用啦

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee6833b7fb304c3e968781bb5017d280~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3836&h=1992&s=447646&e=png)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daccae6bd65f47d7aca5648024ff5610~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3838&h=1990&s=432651&e=png&b=f9f9fb)

##### 步骤五：创建 Bot 使用该插件，使用 Bot

1.  回到 Bot 列表，点击创建 Bot，填写名称和功能描述：
    
    1.  名称：查询股票价格
        
    2.  功能介绍：查询股票价格
        

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/777c9360aa9f470197e4de9d29795de2~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=1142&h=1172&s=126057&e=png&b=f3f5f8)

1.  关联刚刚发布的插件，并且填写 Bot 的回复逻辑，点击“优化”

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6e21b586fe0405384976bebbda7ecc9~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3836&h=1984&s=348965&e=png&b=ffffff)

_关联插件、填写Prompt_

3.  优化完 Prompt 后，就可以和 Bot 进行对话，查询公司股票啦。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/748076ff988c43a2a50bc53d7874dffc~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=2878&h=1616&s=457514&e=png&b=ffffff)

_自动优化Prompt，进行使用_

4.  更多 Bot 配置和高阶玩法，可参考[官方文档](https://link.juejin.cn/?target=https%3A%2F%2Fwww.coze.cn%2Fdocs%2Fguides%2Ffunction_overview "https://www.coze.cn/docs/guides/function_overview")

### 插件二、掘金插件（难度 🌟🌟🌟 ）

#### 明确目的和方案

首先，需要明确插件具有哪些能力：

1.  列出掘金上的热门文章
2.  按主题搜索掘金上的热门文章

该插件难度🌟🌟🌟 ，教程内未提供源码，你可自行调研方案。

#### 操作步骤

##### 步骤一：新建插件和工具

1.  打开 [www.coze.cn/](https://link.juejin.cn/?target=https%3A%2F%2Fwww.coze.cn%2F "https://www.coze.cn/") 选择需要所属的团队。
    
2.  点击右上角创建插件，填写名称，选择插件创建方式为“在 Coze IDE 创建”，运行时选择“Node.js”（你也可以根据自己的情况，选择 Python）
    

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10ccfb32c6f0457fb0cf279beaed015b~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=1168&h=1482&s=150854&e=png&b=f5f7fa)

1.  点击“在 IDE 中创建工具”，创建一个 search 的工具

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/629a28f0070d4188adf4346a32368ed1~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3022&h=1710&s=445569&e=png&b=ffffff)

##### 步骤二：代码编写和开发

进行代码开发、安装依赖包安装等

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb61c2a204b244748391a4b18e4cc5ea~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3022&h=1710&s=445569&e=png&b=ffffff)

##### 步骤三：测试

开发完成后，填写测试数据，进行测试。这个阶段你可能会反复执行和调试代码，查看输出结果是否符合预期、增加异常处理、对 API 返回的脏数据的处理等。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/907dccd38a3c4fc19770d24cdd2a187c~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3022&h=1710&s=568368&e=png&b=f6f6f9)

更新元数据：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cf854267f1d4719adab2273eb5411cf~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3022&h=1712&s=494231&e=png&b=f4f4f8)

##### 步骤四：发布

点击右上角发布，点击下一步，选择“否”，点发布。发布成功后，就可以去创建 Bot 使用啦。

##### 步骤五：创建 Bot 使用该插件，使用 Bot

回到 Bot 列表，创建一个 Bot，或选择现有的 Bot，进入 Bot 编排页面，关联这个插件后进行使用。更多 Bot 配置和高阶玩法，可参考[官方文档](https://link.juejin.cn/?target=https%3A%2F%2Fwww.coze.cn%2Fdocs%2Fguides%2Ffunction_overview "https://www.coze.cn/docs/guides/function_overview")

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9832223ed99e41b5a9c55fd5ee4fbd69~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp#?w=3022&h=1710&s=702578&e=png&b=ffffff)

以上就是 2 个插件和 Bot 开发的完整过程，赶快去试试开发你的 IDE 插件吧。

#### 体验一下

如果想体验以上掘金 Bot，点击下方链接即可快速体验

[www.coze.cn/store/bot/7…](https://link.juejin.cn/?target=https%3A%2F%2Fwww.coze.cn%2Fstore%2Fbot%2F7356502654404804634 "https://www.coze.cn/store/bot/7356502654404804634")
