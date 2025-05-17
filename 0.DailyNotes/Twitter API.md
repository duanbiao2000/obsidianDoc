**TLDR**: 图展示 Twitter API 认证密钥的界面，包含 Consumer Keys（API Key 和 Secret）、Bearer Token 和 Access Token & Secret，区别在于用途和认证方式，分别支持应用级、单用户或多用户授权。

---

### 详细讲解（简洁版，符合 TLDR 风格）

#### 1. **Consumer Keys (API Key and Secret)**
- **定义**：应用级认证凭证，由 Twitter 分配给开发者账户。
- **用途**：用于 OAuth 1.0a 认证，代表应用身份，访问 API 端点（如获取公共 Tweet）。
- **生成**：点击 "Regenerate" 重置，"Reveal API Key hint" 显示提示。
- **特点**：无需用户授权，适合服务器端调用，安全性高但需保密。

#### 2. **Bearer Token**
- **定义**：应用级 OAuth 2.0 认证令牌。
- **用途**：用于无用户上下文的 API 请求（如批量提取公开数据），支持 v2 API。
- **生成**：点击 "Generate" 获取，单 Token 有效。
- **特点**：简化认证，无需用户授权，适合高频自动化任务，但限额较低（约 10,000 Tweet/月免费）。

#### 3. **Access Token and Secret**
- **定义**：用户级 OAuth 1.0a 认证凭证，绑定特定用户（如 @duanbiao）。
- **用途**：代表用户身份，访问受限数据（如用户私密 Tweet），需用户授权。
- **生成**：点击 "Generate" 创建，需指定用户名。
- **特点**：支持个性化操作，但需管理多个 Token，安全性依赖用户权限。

#### 4. **区别与选择**
- **认证方式**：
  - Consumer Keys + Access Token：OAuth 1.0a，双重签名，安全但复杂。
  - Bearer Token：OAuth 2.0，单 Token，简单但权限受限。
- **使用场景**：
  - Bearer Token：无用户场景（如分析趋势）。
  - Access Token：用户特定任务（如个人数据提取）。
- **安全性**：Consumer Keys 和 Access Token 需加密存储，Bearer Token 易泄露，建议定期更新。

#### 5. **建议**
- 免费测试用 Bearer Token，生产环境用 Consumer Keys + Access Token。
- 截至 2025年5月16日09:14 PM MST，关注 Twitter 政策更新。

如需代码示例，告诉我！