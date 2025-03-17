---
aliases: null
createdAt: 2025-03-16 10:40
updateAt: null
categories: null
rate: null
tags: null
---

## 重构优化后

### 使用scrapy

以下是使用 Scrapy 实现上述需求的示例代码。需要注意的是，由于目标站点的网络情况可能会影响程序的运行效果，因此建议在开发时尽量模拟目标站点返回数据，并避免频繁发送请求。

```python
import scrapy


class CarScoreSpider(scrapy.Spider):
    name = 'car_score'
    allowed_domains = ['www.dongchedi.com']
    start_urls = []

    def start_requests(self):
        input_str = input("请输入汽车品牌或车型：").strip()
        if input_str.startswith('bj'):
            url = f"https://www.dongchedi.com/brand/{input_str.lower().replace('bj', '')}"
            yield scrapy.Request(url, callback=self.parse_brand)
        else:
            url = f"https://www.dongchedi.com/{input_str.lower()}.html"
            yield scrapy.Request(url, callback=self.parse_car)

    def parse_brand(self, response):
        brand_name = response.css('.overview h1::text').get()
        cars = response.css('.card-title::attr(href)').getall()
        for car in cars:
            yield response.follow(car, self.parse_car,
                                  cb_kwargs=dict(brand_name=brand_name))

    def parse_car(self, response, brand_name=None):
        car_name = response.css('.summary h1::text').get()
        score = response.css('.score-rank .score::text').get()
        if brand_name:
            yield {
                'brand_name': brand_name.strip(),
                'car_name': car_name.strip(),
                'score': score.strip()
            }
        else:
            yield {'car_name': car_name.strip(), 'score': score.strip()}
```

上述代码将 Scrapy 框架的 `Spider` 类作为主要组件，该类用于控制网络请求和响应处理的流程。`Spider` 类需要定义 `start_requests()` 方法，对起始请求进行配置。具体实现如下：

1. 用户输入车型或品牌名称，作为最初发起的 GET 请求的 URL 地址。
2. 根据 URL 地址判断用户输入的是品牌还是车型。
3. 如果输入字符串以 "bj" 开头，则调整 URL 地址访问指定品牌首页页面，并使用品牌信息下的所有车型链接生成一系列请求。
4. 如果未以 "bj" 开头，则将 URL 直接访问指定车型页面，并提取评分信息。

Scrapy 框架通过 `yield` 关键字产生异步网络请求和响应处理，并将处理结果输送回主线程。对于每一个处理响应的函数，都要实例化为一个“蜘蛛”（Spider）并注册到一个统一的执行器（Crawler）。可以通过命令行解释器等方式启动核心处理单元（Engine），进而启动整个程序。

具体地，`response` 对象是 Scrapy 封装好的 HTTP 响应对象，有多种方法用于选择、过滤、映射 HTML 元素。

需要注意的是：由于 Scrapy 框架本身封装了异步网络请求和回调嵌套机制，在编写代码时需要注意函数之间的作用域和参数传递方式。对于比较复杂的场景，可以采取拆解 "蜘蛛" 的方式划分问题领域和职责，增强项目的可维护性和可扩展性。
