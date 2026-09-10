

**概述：** Crawl4AI 是一个灵活的 Python 库，用于异步爬取网站并提取结构化内容，尤其适用于 AI 用例。本学习指南涵盖了其核心组件和概念，解释了它们如何协同工作来获取和处理网页数据。

**主要概念和组件：**

1. **AsyncCrawlerStrategy** (抓取策略 - 送货工具)

- 定义了 _如何_ 获取给定 URL 的原始内容 (HTML, CSS, JavaScript 结果)。
- 像一个蓝图，允许多种实现。
- **AsyncPlaywrightCrawlerStrategy:** 默认策略，像一辆完整的送货卡车，启动浏览器，渲染页面，执行 JavaScript。适用于复杂、动态网站。
- **AsyncHTTPCrawlerStrategy:** 像一架简单快速的无人机，只执行基本的 HTTP GET 请求。速度快，效率高，但不支持 JavaScript，只获取原始 HTML。适用于简单、静态网站。
- 选择不同的策略取决于任务需求（速度 vs. 功能）。

1. **AsyncWebCrawler** (网络爬虫 - 总经理)

- 与用户交互的主要类，是启动爬取任务的主要入口点。
- 作为中央协调者，管理整个爬取流程。
- **职责：** 初始化、协调（委托抓取、管理缓存、使用抓取策略、过滤、提取）、结果打包（CrawlResult）、资源管理。
- 主要方法：arun()（爬取单个 URL），arun_many()（爬取多个 URL 并发处理）。
- 通常在 async with 块中使用以确保资源管理。

1. **CrawlerRunConfig** (爬取运行配置 - 指令手册)

- 一个配置类，包含 AsyncWebCrawler 对 _特定_ 抓取任务的所有设置。
- 像一个指令手册，捆绑了如何处理特定 URL 或一组 URL 的具体说明。
- 通过将其作为 config 参数传递给 arun() 或 arun_many() 来使用。
- 允许自定义：缓存模式 (cache_mode)、截屏 (screenshot)、PDF (pdf)、CSS 选择器 (css_selector)、等待特定元素 (wait_for)、超时 (page_timeout)、提取策略 (extraction_strategy)、抓取策略 (scraping_strategy) 等。

1. **ContentScrapingStrategy** (内容抓取策略 - 初步编辑)

- 定义了 _如何_ 对原始 HTML 进行初步处理。
- 像一个“初步编辑”，清理原始 HTML（移除脚本、样式、导航、广告等），并提取基本结构和信息（文本内容、链接、图片、元数据）。
- **WebScrapingStrategy:** 默认实现，使用 BeautifulSoup 库，对不完美的 HTML 鲁棒性好。
- **LXMLWebScrapingStrategy:** 另一种实现，使用 lxml 库，通常速度更快。
- 结果打包在 ScrapingResult 对象中，包含 cleaned_html, links, media, metadata。
- 可以通过 CrawlerRunConfig 的 scraping_strategy 参数显式设置。

1. **RelevantContentFilter** (相关内容过滤器 - 细筛)

- 应用于 ContentScrapingStrategy 清理后的内容，进一步过滤掉与核心目标无关的“噪声”。
- 像一个“细筛”或“相关性筛子”，用于减少噪声，聚焦 AI 处理，提高准确性。
- **BM25ContentFilter:** 基于关键词的相关性评分过滤。
- **PruningContentFilter:** 基于 HTML 结构和特征（如文本密度、常见噪声类名）过滤。
- **LLMContentFilter:** 使用大型语言模型 (LLM) 基于语义理解进行过滤（需要 LLM 访问和配置）。
- 通常集成在 Markdown 生成步骤中，用于生成 fit_markdown（过滤后的 Markdown），与 raw_markdown（原始 Markdown）不同。
- 通过将过滤器实例传递给 Markdown 生成器，然后将生成器传递给 CrawlerRunConfig 的 scraping_strategy（实际上是 markdown_generator，但概念上关联）参数来配置。

1. **ExtractionStrategy** (提取策略 - 分析师)

- 定义了 _如何_ 从处理后的内容中提取特定的、结构化的数据（如产品名称、价格）。
- 像一个“分析师”，根据指令从内容中找出精确的数据点并以结构化格式（通常是 JSON）返回。
- **JsonCssExtractionStrategy / JsonXPathExtractionStrategy:** 精确定位器，使用 CSS 选择器或 XPath 表达式，需要精确的结构知识，速度快但对网站结构变化敏感。
- **LLMExtractionStrategy:** 智能解释器，使用 LLM 根据 schema 或自然语言指令理解内容并提取数据，对结构变化鲁棒性更好，但需要 LLM 访问，速度较慢。
- 通过将策略实例赋给 CrawlerRunConfig 的 extraction_strategy 参数来配置。
- 提取的数据存储在 CrawlResult 的 extracted_content 字段中（JSON 字符串）。

1. **CrawlResult** (爬取结果 - 最终报告/交付包)

- 一个 Python 对象（Pydantic 模型），作为单个爬取任务所有结果的容器。
- 是 AsyncWebCrawler.arun() 和 arun_many() 的返回值（或 arun_many(stream=True) 的生成器中的项）。
- 包含：url, success (布尔值，最重要!), html (原始), cleaned_html, markdown (包含 raw_markdown 和 fit_markdown), extracted_content (JSON 字符串), metadata, links, media, screenshot (路径), pdf (数据), error_message, status_code, response_headers, redirected_url 等。
- 通过属性访问数据（如 result.success, result.metadata['title'], result.markdown.fit_markdown）。

1. **DeepCrawlStrategy** (深度爬取策略 - 探险家)

- 定义了 _如何_ 通过跟随链接探索网站，爬取单个起始 URL 以外的页面。
- 像一个“探险计划”，管理要访问的 URL 队列，并协调它们的爬取。
- 通过将策略实例赋给 CrawlerRunConfig 的 deep_crawl_strategy 参数来启用。
- **BFSDeepCrawlStrategy:** 广度优先探索（层层深入）。
- **DFSDeepCrawlStrategy:** 深度优先探索（一条路走到黑）。
- **BestFirstCrawlingStrategy:** 最佳优先探索（根据评分优先爬取）。
- 通常与过滤器 (Filters) 和评分器 (Scorers) 配合使用，指导探索方向。
- 通过装饰器机制拦截 arun() 调用，将控制权交给深度爬取策略。

1. **CacheContext & CacheMode** (缓存上下文与模式 - 缓存策略与决策者)

- 用于管理本地存储爬取结果的机制，避免重复抓取，提高效率。
- **CacheMode:** 你在 CrawlerRunConfig 中设置的缓存 _策略_ 或 _规则_。
- ENABLED: 使用缓存，无则抓取并保存 (默认)。
- BYPASS: 总是抓取新的，但仍保存到缓存。
- DISABLED: 完全不使用缓存。
- READ_ONLY: 只读缓存，无则失败。
- WRITE_ONLY: 只写缓存，总是抓取新的。
- **CacheContext:** Crawl4AI 内部的决策者，根据 CacheMode 和 URL 类型决定是否读写缓存。
- 通过 CrawlerRunConfig 的 cache_mode 参数控制。

1. **BaseDispatcher** (基础调度器 - 交通控制器/任务调度器)

- 在爬取多个 URL（主要通过 arun_many()）时，管理并发执行的系统。
- 像一个“交通控制器”，决定同时可以运行多少个爬取任务，避免系统或目标网站过载。
- **SemaphoreDispatcher:** 使用简单的计数器限制并发数量。
- **MemoryAdaptiveDispatcher:** 根据系统内存使用情况自适应调整并发数量 (arun_many() 的默认)。
- 通过将调度器实例赋给 arun_many() 的 dispatcher 参数来显式设置，否则使用默认的 MemoryAdaptiveDispatcher。
- 调度器内部调用单个 URL 的 crawler.arun() 方法，并用并发控制逻辑包裹它们。

**如何协同工作（简化流程）：**

1. 用户创建 AsyncWebCrawler 实例。
2. 用户调用 crawler.arun(url, config=run_config) 或 crawler.arun_many(urls, config=run_config, dispatcher=...)。
3. 如果使用 arun_many 或配置了 deep_crawl_strategy，则 BaseDispatcher 或 DeepCrawlStrategy 接管，管理 URL 队列和并发。它们内部会调用单 URL 的 crawler.arun。
4. 对于单个 URL 的 arun 调用：

- CacheContext 根据 run_config.cache_mode 决定是否尝试从缓存读取 (CacheMode.ENABLED, READ_ONLY)。
- 如果缓存命中，返回缓存结果。
- 如果缓存未命中或被绕过 (CacheMode.BYPASS, DISABLED, WRITE_ONLY)：
- AsyncWebCrawler 委托给配置的 AsyncCrawlerStrategy (run_config.crawler_strategy 或默认 AsyncPlaywrightCrawlerStrategy) 抓取原始 HTML。
- AsyncCrawlerStrategy 根据 run_config 中的设置（如 page_timeout, wait_for, screenshot, pdf）执行抓取。
- ContentScrapingStrategy (run_config.scraping_strategy 或默认 WebScrapingStrategy) 处理原始 HTML，进行清理，提取基本结构和元数据。
- Markdown 生成器（可能包含 RelevantContentFilter）根据清理后的 HTML 生成 raw_markdown 和 fit_markdown。
- 如果配置了 ExtractionStrategy (run_config.extraction_strategy)，则运行提取过程，得到结构化数据。
- CacheContext 根据 run_config.cache_mode 决定是否将新结果写入缓存 (CacheMode.ENABLED, BYPASS, WRITE_ONLY)。
- AsyncWebCrawler 将所有收集到的信息（原始 HTML、清理后 HTML、Markdown、链接、媒体、元数据、提取数据、错误信息等）打包到一个 CrawlResult 对象中。

1. arun() 返回单个 CrawlResult。arun_many() 或深度爬取策略返回 CrawlResult 列表或生成器。
2. 用户检查 result.success 并访问 CrawlResult 的各个属性来获取数据。

**Crawl4AI 核心概念小测验**

请用 2-3 句话简要回答以下问题：

1. AsyncCrawlerStrategy 的作用是什么？请举出至少两种实现。
2. AsyncWebCrawler 在 Crawl4AI 中扮演什么角色？它如何与策略互动？
3. CrawlerRunConfig 的目的是什么？你如何将其应用于爬取任务？
4. ContentScrapingStrategy 和 RelevantContentFilter 有什么区别？它们处理的是内容的哪个阶段？
5. ExtractionStrategy 主要用于解决什么问题？LLMExtractionStrategy 和 JsonCssExtractionStrategy 各有什么优缺点？
6. CrawlResult 对象包含了哪些关键信息？在处理结果时首先应该检查哪个属性？
7. DeepCrawlStrategy 如何改变 AsyncWebCrawler.arun() 的行为？请列出至少两种不同的深度爬取策略类型。
8. CacheMode.ENABLED 和 CacheMode.BYPASS 有什么不同？CacheContext 的作用是什么？
9. 为什么 Crawl4AI 需要 BaseDispatcher？SemaphoreDispatcher 和 MemoryAdaptiveDispatcher 主要区别在哪里？
10. 如果你想只抓取一个页面的主要文章内容，移除导航和广告，并提取文章标题和发布日期，你会使用 Crawl4AI 的哪些核心组件和策略？

**小测验答案键**

1. AsyncCrawlerStrategy 定义了如何获取网页的原始内容。实现包括 AsyncPlaywrightCrawlerStrategy（使用浏览器）和 AsyncHTTPCrawlerStrategy（简单 HTTP 请求）。
2. AsyncWebCrawler 是主要的协调者和入口点。它不自己抓取或处理内容，而是委托给不同的策略类执行任务。
3. CrawlerRunConfig 用于捆绑特定抓取任务的所有配置设置。通过创建其实例并将其作为 config 参数传递给 arun() 或 arun_many() 来使用。
4. ContentScrapingStrategy 进行初步 HTML 清理和基本结构提取，处理原始 HTML。RelevantContentFilter 在初步清理后进一步过滤内容，保留相关部分，处理的是清理后的内容。
5. ExtractionStrategy 用于从内容中提取特定的结构化数据。LLMExtractionStrategy 基于 AI 理解，灵活但可能慢；JsonCssExtractionStrategy 基于精确选择器，快但对结构变化敏感。
6. CrawlResult 包含了原始 HTML、清理 HTML、Markdown、元数据、链接、提取数据、错误信息等。处理结果时首先应该检查 success 属性。
7. DeepCrawlStrategy 通过装饰器机制改变 arun()，使其不只爬取单个页面，而是根据策略（如 BFSDeepCrawlStrategy、DFSDeepCrawlStrategy）跟随链接进行探索。
8. CacheMode.ENABLED 会优先使用缓存，无则抓取并保存；CacheMode.BYPASS 总是抓取新的，但仍保存到缓存。CacheContext 是内部决策者，根据 CacheMode 和 URL 类型决定缓存操作。
9. BaseDispatcher 用于管理多个并发爬取任务，防止系统或网站过载。SemaphoreDispatcher 使用固定计数限制并发，MemoryAdaptiveDispatcher 根据内存使用情况自适应调整并发。
10. 你会使用 AsyncWebCrawler 进行协调，ContentScrapingStrategy 进行初步清理，RelevantContentFilter（可能是 Pruning 或 LLM）过滤掉导航和广告，ExtractionStrategy（可能是 JsonCss 或 LLM）提取标题和日期，并将这些配置放入 CrawlerRunConfig，最终通过 CrawlResult 获取结果。

**Crawl4AI 核心概念论文/问答题建议**

以下是五个可以用于深入探讨您对 Crawl4AI 核心概念理解的论文或问答格式题目：

1. 详细比较 AsyncPlaywrightCrawlerStrategy 和 AsyncHTTPCrawlerStrategy 在不同网页类型（静态 HTML、JavaScript 动态加载内容）上的表现差异，并讨论在何种场景下选择哪种策略更为合适。
2. 阐述 AsyncWebCrawler 如何作为整个 Crawl4AI 流程的“总经理”。详细描述它是如何协调 AsyncCrawlerStrategy、ContentScrapingStrategy、RelevantContentFilter 和 ExtractionStrategy 等不同组件来处理一个完整的爬取请求的。
3. 解释 CrawlerRunConfig 在 Crawl4AI 中的重要性及其灵活性来源。讨论如何通过配置不同的参数（如 cache_mode, css_selector, extraction_strategy）来显著改变同一个 URL 的爬取结果和行为。
4. 深入分析 ContentScrapingStrategy 和 RelevantContentFilter 在内容处理管道中的作用。讨论不同的 RelevantContentFilter 实现（BM25, Pruning, LLM）各自的原理、优缺点及适用场景，以及它们如何影响最终的 fit_markdown 输出。
5. 比较并对比 Crawl4AI 中用于爬取多个 URL 的两种主要机制：使用 arun_many() 配合 BaseDispatcher 和使用 arun() 配合 DeepCrawlStrategy。讨论它们各自的设计目的、适用场景以及如何通过配置 Dispatcher 和 DeepCrawlStrategy 的参数来控制并发和探索行为。

**Crawl4AI 核心术语词汇表**

- **AsyncCrawlerStrategy:** 定义了获取网页原始内容的方法或技术。
- **AsyncPlaywrightCrawlerStrategy:** 使用无头浏览器 (Playwright) 获取内容的抓取策略，支持 JavaScript 渲染。
- **AsyncHTTPCrawlerStrategy:** 使用简单 HTTP GET 请求获取内容的抓取策略，不支持 JavaScript。
- **AsyncWebCrawler:** Crawl4AI 的主要协调类和入口点，管理整个爬取流程。
- **arun():** AsyncWebCrawler 中用于启动单个 URL 爬取的方法。
- **arun_many():** AsyncWebCrawler 中用于启动多个 URL 并发爬取的方法。
- **CrawlerRunConfig:** 包含特定爬取任务所有配置设置的类。
- **ContentScrapingStrategy:** 定义了对原始 HTML 进行初步清理和结构提取的方法。
- **WebScrapingStrategy:** ContentScrapingStrategy 的默认实现，使用 BeautifulSoup 进行 HTML 清理。
- **LXMLWebScrapingStrategy:** ContentScrapingStrategy 的实现，使用 lxml 进行 HTML 清理，通常速度更快。
- **RelevantContentFilter:** 在初步清理后进一步过滤内容，保留相关部分的策略。
- **BM25ContentFilter:** 基于关键词相关性过滤内容的 RelevantContentFilter。
- **PruningContentFilter:** 基于 HTML 结构和特征过滤内容的 RelevantContentFilter。
- **LLMContentFilter:** 使用 LLM 基于语义理解过滤内容的 RelevantContentFilter。
- **ExtractionStrategy:** 定义了从内容中提取特定结构化数据的方法。
- **JsonCssExtractionStrategy:** 使用 CSS 选择器提取结构化数据的 ExtractionStrategy。
- **JsonXPathExtractionStrategy:** 使用 XPath 表达式提取结构化数据的 ExtractionStrategy。
- **LLMExtractionStrategy:** 使用 LLM 提取结构化数据的 ExtractionStrategy。
- **CrawlResult:** 单个爬取任务结果的容器对象，包含所有收集到的信息。
- **success:** CrawlResult 中的布尔属性，指示爬取是否成功完成。
- **html:** CrawlResult 中包含原始 HTML 源代码的属性。
- **cleaned_html:** CrawlResult 中包含 ContentScrapingStrategy 清理后 HTML 的属性。
- **markdown:** CrawlResult 中包含不同 Markdown 表示形式（raw_markdown, fit_markdown）的对象属性。
- **extracted_content:** CrawlResult 中包含提取的结构化数据（通常为 JSON 字符串）的属性。
- **metadata:** CrawlResult 中包含页面元数据（如标题）的字典属性。
- **links:** CrawlResult 中包含找到的链接列表（内部和外部）的对象属性。
- **media:** CrawlResult 中包含找到的媒体项列表（图片、视频等）的对象属性。
- **screenshot:** CrawlResult 中包含截屏文件路径的字符串属性（如果请求）。
- **pdf:** CrawlResult 中包含 PDF 数据（字节）的属性（如果请求）。
- **DeepCrawlStrategy:** 定义了通过跟随链接探索网站的策略。
- **BFSDeepCrawlStrategy:** 广度优先深度爬取策略。
- **DFSDeepCrawlStrategy:** 深度优先深度爬取策略。
- **BestFirstCrawlingStrategy:** 最佳优先深度爬取策略。
- **CacheMode:** 控制 Crawl4AI 如何使用本地缓存存储和检索结果的策略设置。
- **CacheContext:** Crawl4AI 内部根据 CacheMode 和 URL 类型决定缓存读写操作的决策者。
- **BaseDispatcher:** 管理并发爬取任务执行的抽象系统。
- **SemaphoreDispatcher:** 使用固定计数限制并发的 BaseDispatcher 实现。
- **MemoryAdaptiveDispatcher:** 根据系统内存使用情况自适应调整并发的 BaseDispatcher 实现，是 arun_many 的默认调度器。
## 角色列表

- **AsyncCrawlerStrategy**： Crawl4AI 中的一个核心抽象概念，定义了如何下载给定 URL 的内容。它是一个蓝图，允许根据需要替换具体的抓取机制。
- **AsyncPlaywrightCrawlerStrategy**： AsyncCrawlerStrategy 的默认实现。它使用 Playwright 库启动浏览器、渲染页面并执行 JavaScript，适用于复杂的动态网站。
- **AsyncHTTPCrawlerStrategy**： AsyncCrawlerStrategy 的实现，使用简单的 HTTP GET 请求下载内容。它速度快且资源效率高，但不支持 JavaScript 执行或页面渲染后的动态内容。
- **AsyncWebCrawler**： Crawl4AI 中的主要类和主要入口点。它是整个抓取操作的“总经理”，负责协调获取、缓存、抓取、过滤和提取等所有步骤。用户主要通过 arun()（单 URL）和 arun_many()（多 URL）方法与其交互。
- **CrawlerRunConfig**： 一个配置类，封装了特定抓取任务的所有设置和指令。它像一个“指令手册”，告诉 AsyncWebCrawler 如何处理特定的 URL 或一组 URL。
- **ContentScrapingStrategy**： 一个抽象概念，定义了原始 HTML 的初始处理方式。它扮演着“初次编辑”的角色，负责清理 HTML、移除不必要的标签并提取基本结构、文本、链接和媒体信息。
- **WebScrapingStrategy**： ContentScrapingStrategy 的默认实现，使用 BeautifulSoup 库进行 HTML 解析和清理。它是一个可靠、经验丰富的“编辑”。
- **LXMLWebScrapingStrategy**： ContentScrapingStrategy 的实现，使用 lxml 库进行 HTML 解析。它是一个通常速度更快的“编辑”。
- **RelevantContentFilter**： 一个抽象概念，表示过滤清洗过的 HTML 内容的方法，仅保留与特定目标相关的部分。它像一个“相关性筛子”，帮助减少噪声。
- **BM25ContentFilter**： RelevantContentFilter 的实现，使用 BM25 搜索算法根据关键词对内容块进行评分和过滤。它是“关键词筛子”。
- **PruningContentFilter**： RelevantContentFilter 的实现，根据 HTML 结构和特征（如文本密度和常见噪声词）过滤内容。它是“结构筛子”。
- **LLMContentFilter**： RelevantContentFilter 的实现，利用大型语言模型 (LLM) 根据自然语言指令进行基于语义和上下文的内容过滤。它是“AI 筛子”。
- **DefaultMarkdownGenerator**： Crawl4AI 中将清洗过的 HTML 转换为 Markdown 的组件。它可以选择性地使用 RelevantContentFilter 来生成聚焦的 Markdown 输出。
- **ExtractionStrategy**： 一个抽象概念，定义了从处理过的内容中提取特定结构化数据的方法。它代表了我们提供给“分析师”的指令。
- **JsonCssExtractionStrategy**： ExtractionStrategy 的实现，使用 CSS 选择器和预定义的模式从 HTML 中提取结构化数据。它是一个使用精确“定位器”的分析师。
- **JsonXPathExtractionStrategy**： ExtractionStrategy 的实现，使用 XPath 表达式和预定义的模式从 HTML 中提取结构化数据。它也是一个使用精确“定位器”的分析师。
- **LLMExtractionStrategy**： ExtractionStrategy 的实现，利用大型语言模型 (LLM) 根据模式或自然语言指令从内容中提取结构化数据。它是一个“智能解释器”分析师。
- **CrawlResult**： 一个 Pydantic 模型对象，作为单个抓取任务的“最终报告文件夹”或“交付包裹”。它包含抓取到的所有信息，如原始 HTML、清洗过的 HTML、Markdown、元数据、链接、媒体、提取的数据、错误信息、状态码等。
- **DeepCrawlStrategy**： 一个概念，定义了通过跟踪链接探索和抓取多个页面的逻辑或“探索计划”。它将爬虫从单页访问者转变为网站探索者。
- **BFSDeepCrawlStrategy**： DeepCrawlStrategy 的实现，按层级探索网站（广度优先搜索）。它是“层级探索者”。
- **DFSDeepCrawlStrategy**： DeepCrawlStrategy 的实现，沿着一条路径深入探索（深度优先搜索）。它是“深路径探索者”。
- **BestFirstCrawlingStrategy**： DeepCrawlStrategy 的实现，根据链接的得分（优先级）探索网站。它是“优先探索者”。
- **Filters (DomainFilter, URLPatternFilter, ContentTypeFilter)**： 与 DeepCrawlStrategy 配合使用的组件，定义了是否应考虑抓取发现的链接的规则。它们是探索者的“指南”。
- **Scorers (KeywordRelevanceScorer, PathDepthScorer)**： 与 BestFirstCrawlingStrategy 配合使用的组件，为潜在链接分配分数以帮助确定优先级。它们是探索者的“宝藏地图标记”。
- **DeepCrawlDecorator**： 一个 Python 装饰器，拦截 AsyncWebCrawler 的 arun 调用，以在配置中存在 DeepCrawlStrategy 时将控制权委托给它。
- **CacheMode**： 一个枚举（CacheMode.ENABLED, CacheMode.BYPASS, CacheMode.DISABLED 等），指定了抓取任务如何与缓存交互的策略或“缓存策略”。
- **CacheContext**： Crawl4AI 使用的内部帮助器，根据 CacheMode 和 URL 类型在运行时决定是否从缓存中读取或写入缓存。它是一个“决策者”。
- **BaseDispatcher**： 一个抽象概念，定义了管理多个并发抓取任务执行的系统或“流量控制器”。它用于 arun_many() 和 DeepCrawlStrategy 来控制并发。
- **SemaphoreDispatcher**： BaseDispatcher 的实现，使用固定数量的信号量来限制同时运行的抓取任务数量。它是“简单计数器”控制器。
- **MemoryAdaptiveDispatcher**： BaseDispatcher 的默认实现，根据系统内存使用情况自适应地调整并发级别。它是“资源感知控制器”。
- **RateLimiter**： 一个可选组件，可以与调度器配合使用，以实施礼貌规则并管理对特定网站的请求速率。