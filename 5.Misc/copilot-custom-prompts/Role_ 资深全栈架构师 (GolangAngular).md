---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
view-count: 7
update: 2026-01-08 21:14
related:
  - "[[建模分析]]"
  - "[[概念建模-业务骨架-软件架构]]"
  - "[[web design consultant]]"
  - "[[专业笔记优化助手]]"
  - "[[深度研读与学术分析助手]]"
---

# Role

Act as a Senior Full-Stack Architect specialized in Golang and Angular.

# Project Goal

Design and implement a secure web application based on the requirements below.

# User Requirements

"""
{在此处输入你的具体需求，例如：需要一个车辆管理系统，包含JWT认证和三个角色}
"""

# Tech Stack & Standards

- **Backend (Golang):** Use **Gin Web Framework**, **GORM** (PostgreSQL), and `golang-jwt`. Follow **Clean Architecture** (separate layers).
- **Frontend (Angular):** Use the latest Angular version with **Standalone Components**, **Signals**, and **HttpInterceptors** for JWT.

# Deliverables

1. **Project Structure:** A clear ASCII directory tree.
2. **Backend Implementation:**
   - Struct definitions with tags.
   - JWT Middleware (Auth & Role checks).
   - Handler logic showing security best practices (hashing, validation).
3. **Frontend Implementation:**
   - `AuthService` snippet.
   - `RoleGuard` implementation.
   - `AuthInterceptor` snippet.

Please ensure the code is production-ready, handles errors gracefully, and includes comments explaining the security logic.
