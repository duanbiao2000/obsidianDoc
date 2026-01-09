---
view-count: 4
related:
  - "[[2025-12-13-API-First接口优先开发流程]]"
  - "[[2025-12-11-AI在写代码领域的当前水平]]"
---

当自动化脚本遇到**需要人工确认的登录界面**（例如：短信验证码、扫码登录、图形验证码、二次确认弹窗、MFA 多因素认证等），这是 Playwright 或任何浏览器自动化工具的**常见挑战**。这类设计本意就是**阻止自动化**，因此没有“万能全自动”方案，但我们可以根据场景选择**合理策略**。

---

## 🔍 一、先判断“人工确认”的类型

| 类型                              | 示例              | 是否可自动化               |
| ------------------------------- | --------------- | -------------------- |
| **短信/邮箱验证码**                    | 输入手机收到的6位数字     | ❌ 通常不可自动（除非你能读短信/邮箱） |
| **扫码登录**                        | 手机 App 扫码确认     | ❌ 需要物理设备介入           |
| **图形验证码 (CAPTCHA)**             | 拖拽、点选、文字识别      | ❌ 极难自动（除非用 AI 识别）    |
| **MFA（如 Google Authenticator）** | 动态6位令牌          | ⚠️ 可通过算法生成（若你有密钥）    |
| **信任设备确认**                      | “是否在常用设备？”点击“是” | ✅ 可自动（只需点击）          |
| **企业 SSO + 人工审批**               | 管理员需批准登录请求      | ❌ 无法绕过               |

---

## ✅ 二、可行的解决方案（按优先级）

### ✅ 方案1：**使用持久化上下文（Persistent Context）—— 推荐！**

> **核心思想**：只人工登录一次，保存登录状态（Cookie + Storage），后续自动化直接复用。

#### 步骤：

1. **首次人工登录**（带界面）：
   ```python
   from playwright.sync_api import sync_playwright
   import os

   USER_DATA_DIR = "./auth_profile"

   with sync_playwright() as p:
       # 启动带用户数据目录的浏览器（类似 Chrome 的“用户配置文件”）
       browser = p.chromium.launch_persistent_context(
           USER_DATA_DIR,
           headless=False,  # 必须有头，人工操作
           args=["--disable-blink-features=AutomationControlled"]
       )
       page = browser.pages[0]
       page.goto("https://your-login-page.com")
       
       # 👉 此时你手动完成登录（输验证码、扫码等）
       input("✅ 登录完成后，请按回车继续...")
       
       # 关闭浏览器，状态已保存到 USER_DATA_DIR
       browser.close()
   ```

2. **后续自动化直接复用**：
   ```python
   with sync_playwright() as p:
       browser = p.chromium.launch_persistent_context(
           USER_DATA_DIR,
           headless=True  # 可无头运行！
       )
       page = browser.pages[0]
       page.goto("https://your-logged-in-page.com")
       # ✅ 已自动登录！
       page.screenshot(path="logged_in.png")
       browser.close()
   ```

> ✅ **优点**：简单、安全、适用于几乎所有“登录后长期有效”的网站（如微信网页版、企业后台）。\
> ⚠️ **注意**：某些网站会检测自动化或定期失效 Cookie，需定期重新人工登录。

---

### ✅ 方案2：**拦截网络请求，注入 Token（高级）**

如果登录后网站使用 **JWT / Bearer Token**，且你能通过其他方式（如 API、手机抓包）获取 Token：

```python
# 在页面加载前注入认证信息
page.route("**/*", lambda route: route.continue_(
    headers={**route.request.headers, "Authorization": "Bearer your_token_here"}
))
page.goto("https://app.example.com")
```

> 适用场景：内部系统、API 可控、Token 可长期使用。

---

### ✅ 方案3：**自动化 MFA（仅限 TOTP）**

如果你使用的是 **基于时间的一次性密码（TOTP）**，如 Google Authenticator，并且你**拥有密钥（secret key）**，可以用 Python 生成：

```bash
pip install pyotp
```

```python
import pyotp
totp = pyotp.TOTP("YOUR_BASE32_SECRET_KEY")
code = totp.now()  # 生成当前6位码
page.fill("#mfa-input", code)
page.click("#verify-btn")
```

> 🔐 注意：密钥通常在首次绑定 MFA 时显示，需提前保存。

---

### ❌ 不推荐方案（风险高/效果差）

- **OCR 识别图形验证码**：成功率低，易被反爬。
- **模拟手机收短信**：需接入运营商 API（成本高、合规风险）。
- **绕过前端验证**：可能违反服务条款，甚至违法。

---

## 🛡️ 三、最佳实践建议

1. **优先使用 `launch_persistent_context`** 保存登录态。
2. **避免频繁登录**：将登录与业务逻辑分离，登录一次，执行多次任务。
3. **设置合理的 User-Agent 和 viewport**，减少被检测为 bot：
   ```python
   context = browser.new_context(
       user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
       viewport={"width": 1920, "height": 1080}
   )
   ```
4. **监控登录状态**：每次运行前检查是否仍登录，否则触发重新人工登录流程。

---

## 💡 示例：带人工确认的健壮登录流程

```python
import os
from playwright.sync_api import sync_playwright

AUTH_DIR = "auth_state"
LOGIN_URL = "https://example.com/login"
DASHBOARD_URL = "https://example.com/dashboard"

def is_logged_in(page):
    page.goto(DASHBOARD_URL)
    return "欢迎" in page.content()  # 根据实际内容判断

with sync_playwright() as p:
    if not os.path.exists(AUTH_DIR):
        print("⚠️ 首次运行，请人工完成登录...")
        context = p.chromium.launch_persistent_context(AUTH_DIR, headless=False)
        page = context.pages[0]
        page.goto(LOGIN_URL)
        input("✅ 登录完成后按回车...")
        context.close()

    # 正式运行
    context = p.chromium.launch_persistent_context(AUTH_DIR, headless=True)
    page = context.pages[0]
    
    if not is_logged_in(page):
        raise Exception("❌ 登录状态失效，请删除 auth_state 文件夹后重试")
    
    # 执行你的自动化任务
    page.screenshot(path="task.png")
    context.close()
```

---

## 总结

| 场景            | 推荐方案                               |
| ------------- | ---------------------------------- |
| 需要偶尔人工确认（如扫码） | ✅ `launch_persistent_context` 保存会话 |
| 有 TOTP 密钥     | ✅ 用 `pyotp` 自动生成验证码                |
| 内部系统，Token 可控 | ✅ 注入 Authorization Header          |
| 图形验证码 / 短信验证码 | ❌ 建议改用 API 或放弃自动化                  |

> 自动化的边界在于**尊重系统设计意图**。对于强安全验证，人工介入是合理且必要的。

如有具体网站或登录流程，可提供更多信息，我可以给出更针对性的建议！
