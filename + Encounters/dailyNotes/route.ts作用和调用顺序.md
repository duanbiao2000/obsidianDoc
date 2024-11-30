---
aliases: 
theme: 
priority: false
tags:
---
### @route.ts 的执行调用顺序

1. **接收请求**
    
    - 接收到一个 `POST` 请求。
2. **获取客户端 IP 地址**
    
    - 使用 `requestIp.getClientIp()` 获取客户端 IP 地址，并将其作为限流标识符。
3. **创建新的 Headers 对象**
    
    - 创建一个新的 `Headers` 对象，用于后续添加自定义限流头信息。
4. **条件性限流检查**
    
    - 检查是否需要执行限流。
    - 如果需要限流且环境变量配置正确，则执行限流检查。
    - 根据限流结果设置自定义头信息。
    - 如果限流失败，返回 429 状态码。
5. **解析请求体中的 JSON 数据**
    
    - 从请求体中解析出 JSON 数据。
6. **提取请求参数**
    
    - 从解析出的 JSON 数据中提取 `imageUrl`, `roomType`, `roomTheme`, `buildingType`, `buildingTheme` 等参数。
7. **开始图像生成过程**
    
    - 向 `https://api.replicate.com/v1/predictions` 发送 `POST` 请求，开始图像生成过程。
    - 设置请求头信息和请求体内容。
8. **解析初始化响应的 JSON 数据**
    
    - 解析初始化响应的 JSON 数据，提取预测 ID (`id`)。
9. **轮询 API 直到图像生成完成**
    
    - 每隔一秒轮询 `https://api.replicate.com/v1/predictions/{id}`，直到图像生成完成。
    - 如果生成成功，获取生成的图像 URL。
    - 如果生成失败，抛出错误。
10. **返回生成的图像 URL**
    
    - 将生成的图像 URL 作为响应返回。如果生成失败，则返回错误信息。

## @route.ts 文件的作用

app/predict/route.ts 文件定义了一个 Next.js API 路由，用于处理图像生成请求。它接收用户提供的参数，调用 Replicate API 生成图像，并返回生成的图像 URL。

主要功能：

- 速率限制: 使用 Upstash Redis 和 Ratelimit 库实现请求速率限制，防止滥用。

- 图像生成: 接收用户请求，调用 Replicate API 生成图像。

- 轮询和结果处理: 轮询 Replicate API 获取生成结果，并在生成完成后返回图像 URL。

在项目中的作用:

该文件是项目中图像生成功能的核心，负责处理用户请求并与 Replicate API 交互。它实现了速率限制以保护 API，并通过轮询机制确保返回最终生成的图像 URL。