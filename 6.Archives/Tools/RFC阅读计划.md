---
view-count: 3
---

## 🧠 一、入门友好 & 必读经典

| RFC 编号              | 标题                                                         | 为什么值得读                                               |
| ------------------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| **RFC 2119**        | _Key words for use in RFCs to Indicate Requirement Levels_ | 定义了 MUST、SHOULD、MAY 等关键词的语义。**所有其他 RFC 的“语法基础”**，必读！ |
| **RFC 1122 / 1123** | _Requirements for Internet Hosts_                          | TCP/IP 主机实现的权威指南，涵盖 IP、TCP、UDP、ICMP 等，体现早期互联网设计原则。   |
| **RFC 1958**        | _Architectural Principles of the Internet_                 | 阐述互联网核心设计哲学：“简单性、端到端、尽力而为”等，思想性极强。                   |
| **RFC 1925**        | _The Twelve Networking Truths_                             | 幽默又深刻的网络箴言（如“协议总是会变得复杂”），适合培养工程直觉。                   |

> ✅ **建议**：先读 RFC 2119 + RFC 1925，轻松入门；再看 RFC 1958 建立宏观认知。

---

## 🌐 二、核心协议类（互联网基石）

|RFC 编号|协议/主题|说明|
|---|---|---|
|**RFC 791**|IP (Internet Protocol)|IPv4 的原始定义，理解网络层基础。|
|**RFC 793**|TCP (Transmission Control Protocol)|TCP 的经典规范，状态机、可靠性机制的源头。|
|**RFC 1034 / 1035**|DNS (Domain Name System)|DNS 架构与协议细节，至今仍是解析系统的核心。|
|**RFC 2616 → RFC 9110~9114**|HTTP/1.1 → HTTP Semantics & Caching|旧版 RFC 2616 已被拆分为现代系列（RFC 9110 等），建议直接读新版。|
|**RFC 6455**|WebSocket Protocol|实时双向通信协议的标准，Web 开发重要参考。|
|**RFC 7950**|YANG Data Modeling Language|网络配置自动化（如 NETCONF）的数据建模语言，现代网络管理关键。|

> 💡 提示：HTTP 新标准已更新，优先阅读 [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)（HTTP Semantics）。

---

## 🔒 三、安全与加密类

|RFC 编号|主题|亮点|
|---|---|---|
|**RFC 5280**|Internet X.509 Public Key Infrastructure|PKI 证书体系的核心规范，HTTPS 依赖的基础。|
|**RFC 8446**|TLS 1.3|最新 TLS 协议，性能与安全性大幅提升，现代加密通信标杆。|
|**RFC 4086**|Randomness Requirements for Security|讲解密码学中“随机性”的重要性，常被忽视但极其关键。|
|**RFC 6241**|NETCONF Protocol|安全网络设备配置协议，结合 YANG 使用。|

---

## 🛠 四、实用工具与编码规范

|RFC 编号|内容|应用场景|
|---|---|---|
|**RFC 4648**|Base16, Base32, Base64 Encodings|所有 Base64 编码的官方定义，开发中高频使用。|
|**RFC 3986**|URI Syntax|统一资源标识符（URL/URI）的权威语法规范。|
|**RFC 7519**|JWT (JSON Web Token)|身份认证令牌标准，现代 Web API 广泛采用。|
|**RFC 8949**|CBOR (Concise Binary Object Representation)|类似 JSON 的二进制序列化格式，用于 IoT 和高效传输。|

---

## 🎯 五、思想性 & 趣味性 RFC（非标准但经典）

|RFC 编号|标题|特点|
|---|---|---|
|**RFC 1149**|_IP over Avian Carriers_|用信鸽传 IP 包！愚人节 RFC，但后来真有人实验成功 😄|
|**RFC 2324**|_Hyper Text Coffee Pot Control Protocol (HTCPCP)_|“咖啡壶控制协议”，HTTP 扩展的幽默之作。|
|**RFC 7414**|_A Roadmap for TCP Specification Documents_|TCP 协议演进路线图，帮助理清复杂 RFC 之间的关系。|

> 这些虽非正式标准，但体现了工程师文化中的幽默与创造力，也常被引用讨论。

---

## 📚 学习建议

1. **从兴趣出发**：如果你做 Web 开发，优先读 HTTP、TLS、JWT；做网络运维，重点看 IP/TCP/DNS。
2. **对照实现**：边读 RFC 边看 Wireshark 抓包或开源代码（如 Linux 内核、Nginx、OpenSSL），加深理解。
3. **善用中文资源**：可参考 [RFC 中文翻译一览（trustywolf）](https://github.com/trustywolf/rfc-trans) 或 CSDN 上的解读。
4. **不要死磕**：RFC 语言严谨但枯燥，初期可跳过数学公式或状态机细节，先抓主干逻辑。

---

## 🔗 官方查阅地址

- 英文原版：[https://www.rfc-editor.org/](https://www.rfc-editor.org/)
- 搜索技巧：在站内搜索关键词（如 "HTTP"、"TLS"），或直接访问 `https://www.rfc-editor.org/rfc/rfcXXXX.html`

---

通过研读这些经典 RFC，你不仅能掌握协议细节，更能理解**互联网为何如此设计**——这才是真正的“第一性原理”学习。