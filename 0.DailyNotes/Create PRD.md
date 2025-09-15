
Create a FOCUSED Product Requirements Document (PRD) for an open-source, self-hosted web application that transforms YouTube videos into embeddable social proof widgets.

CRITICAL CONSTRAINTS - READ FIRST:
- Maximum 400 lines for entire PRD
- Focus on WHAT needs to be built and WHY, not HOW to implement
- NO code examples, TypeScript interfaces, or technical implementations
- NO specific API endpoints, URLs, or request/response formats
- NO UI mockups with pixel dimensions (conceptual descriptions only)
- NO database schemas, cache keys, or environment variables
- NO sprint planning, timelines, or week-by-week breakdowns
- NO error code tables or detailed technical specifications

REMEMBER: Other agents in the design phase will handle:
- ui-designer: Creates actual mockups and component hierarchies
- youtube-api-expert: Defines YouTube API integration specifics
- chatgpt-expert: Handles OpenAI integration details
- shadcn-expert: Selects UI components and design systems
- system-architect: Designs technical implementation
- Your role: Define requirements and business logic ONLY

User Journey:
1. Developer clones the repository and deploys their own instance
2. Developer adds their YouTube API and OpenAI API keys to environment variables
3. Developer visits their instance (e.g., localhost:3000 or their-domain.vercel.app)
4. Developer enters a YouTube URL to generate a widget
5. App generates an embed code pointing to developer's instance
6. Developer embeds the iframe on their website
7. End users see the widget (no API keys needed on their part)

The app should:
Core Functionality

Video Data Extraction: Accept a YouTube URL and retrieve essential metadata via YouTube Data API v3:

Title, description, channel name
View count, like count, comment count
Thumbnail URL, publish date
Video duration
ALWAYS check latest API documentation before implementation


Social Proof Visualization: Design a visually compelling component displaying:

Formatted view count (e.g., "2.3M views")
Like/comment ratios with visual indicators
Engagement rate calculation
Trust badges based on metrics thresholds


Sentiment Analysis:

Fetch the top 20-50 most relevant comments (optimize for API quotas)
Send comments batch to OpenAI API (GPT-3.5-turbo for cost efficiency)
Generate an overall sentiment score (1-5 stars)
Provide a brief AI-generated summary of audience reception (2-3 sentences)
Include confidence score for the analysis


Comment Carousel:

Display 5 highly positive comments in a rotating carousel
Filter for comments with high like counts and positive sentiment
Include commenter names and timestamps
Add verified badge for channel owner responses


Widget Embedding (Self-Hosted Model):

Open-source application that developers self-host
Developers provide their own YouTube & OpenAI API keys
Generate embeddable iframe code pointing to their instance
Widget generator UI at main app (localhost:3000 or their domain)
Embed endpoint at /embed?v=[videoId] serves the widget
Support multiple widgets per page
Customizable size via URL params (?size=small|medium|large)
Widget is a static render (no API keys in client code)



Technical Constraints & Considerations

Self-hosted architecture (developers run their own instance)
Environment variables for API keys (YOUTUBE_API_KEY, OPENAI_API_KEY)
Use YouTube API quotas efficiently (1 unit per video, 1 unit per comment fetch)
Cache video data for 24 hours, sentiment analysis for 7 days
Handle videos with comments disabled gracefully
Implement fallbacks for private/deleted videos
Limit initial comment fetch to 20-50 for cost optimization
Documentation-first approach: Check latest API specs before implementation

Key Requirements to Document (High-Level Only)

Core functionality requirements (what the system must do)
User acceptance criteria (how we know it works)
Performance targets (< 2 second load time)
Business constraints (API quotas, cost considerations)
Success metrics (adoption, performance, quality)

Deployment & Documentation

README with clear setup instructions
.env.template with required API keys
One-click deploy button for Vercel
Docker support (optional, post-MVP)
Example embed code generator
Troubleshooting guide for common issues

Out of Scope (to avoid over-engineering)

Real-time comment updates
Multi-language sentiment analysis (MVP in English only)
Historical tracking of metrics
User authentication system
Comment moderation features
Widget customization UI (use URL parameters instead)
Analytics tracking for widget usage

Please structure the PRD with these FOCUSED sections:
1. Executive Summary (100-150 words): Problem, solution, value proposition
2. User Stories (5-10 stories): User needs with acceptance criteria
3. Functional Requirements (Bullet points): WHAT the system does, not HOW
4. Technical Approach (50-100 words): High-level tech stack only
5. Success Metrics (5-8 metrics): Measurable outcomes
6. Risks & Assumptions (Brief list): Key dependencies and risks

SKIP THESE (other agents will handle):
- Detailed technical architecture → system-architect
- API implementation details → api experts
- UI component specifications → ui-designer
- Implementation timelines → orchestrator
- Code examples or interfaces → implementation agents

IMPORTANT ARCHITECTURE NOTE: This is a self-hosted, open-source application where developers deploy their own instances and use their own API keys. See docs/notes.md for detailed architecture rationale. Focus on making it easy for developers to deploy and customize their own instance.

FINAL REMINDER - OUTPUT VALIDATION:
✓ If your PRD exceeds 400 lines, you're over-engineering
✓ If you're writing code or API URLs, stop - that's for implementation
✓ If you're creating ASCII mockups, stop - that's for ui-designer
✓ If you're defining cache strategies, stop - that's for system-architect
✓ Focus on business requirements and user needs ONLY"

---
### 执行摘要（120字）  
开发者难以直观展示YouTube视频的社交价值，直接嵌入缺乏吸引力。本开源自托管工具将视频数据转化为可视化社交证明小工具，动态展示视图数、情感分析及高赞评论，提升用户信任度。无需第三方服务依赖，开发者完全掌控数据，安全且低成本。适用于内容创作者、教育平台及营销团队，强化内容可信度与参与度。

---

### 用户故事  
- 作为开发者，我能输入YouTube视频链接生成嵌入代码，快速集成到网站中。  
  *验收标准：生成的iframe代码正确渲染社交证明数据。*  
- 作为开发者，系统自动提取视频元数据（标题、频道、视图数等）并以视觉化方式呈现。  
  *验收标准：关键数据格式化显示（如“2.3M views”），无技术错误。*  
- 作为开发者，系统分析评论情感生成星级评分与简短摘要，附带置信度。  
  *验收标准：摘要为2-3句话，星级评分符合实际评论情绪。*  
- 作为开发者，系统展示5条高赞评论轮播，过滤负面内容并显示验证标识。  
  *验收标准：轮播内容为高点赞评论，显示评论者名称与时间戳。*  
- 作为开发者，系统处理视频删除或评论禁用情况，显示友好错误提示。  
  *验收标准：无崩溃，明确提示问题原因（如“视频不可用”）。*  
- 作为开发者，嵌入小工具支持尺寸调整（小/中/大），通过URL参数控制。  
  *验收标准：调整参数后，小工具尺寸按预期变化。*  

---

### 功能要求  
- 提取视频核心元数据（标题、描述、频道、视图、点赞、评论数、时长、缩略图）。  
- 计算并可视化参与度指标（如点赞率、评论率），用直观图表展示。  
- 通过AI分析评论情感，生成1-5星评分和简短总结，附带置信度指标。  
- 展示高赞评论轮播，过滤无效或负面内容，显示验证标识。  
- 生成安全的iframe嵌入代码，指向自托管实例，无需客户端API密钥。  
- 缓存视频数据24小时，情感分析结果7天，减少API调用频率。  
- 处理API配额限制，优雅降级（如使用缓存数据、显示提示信息）。  
- 支持视频被删除、私有或评论禁用的情况，提供清晰反馈。  

---

### 技术方法  
采用现代前端框架构建，支持静态部署。集成第三方API进行数据获取与AI分析。设计为轻量级、无状态应用，确保开发者快速部署。重点优化API调用效率，保障性能与成本可控。  

---

### 成功指标  
- 嵌入小工具加载时间<2秒（95%请求）  
- 每视频平均API调用≤3次（YouTube+OpenAI）  
- 部署实例数量月增长≥20%  
- 情感分析准确率≥85%（人工验证样本）  
- 用户错误率<5%（无效视频输入处理）  

---

### 风险与假设  
- YouTube API配额限制可能影响性能，需合理缓存数据。  
- OpenAI成本需控制，仅分析必要评论数量。  
- 假设视频数据可访问，但需处理删除/私有情况。  
- 仅支持英语评论分析，多语言需后续扩展。