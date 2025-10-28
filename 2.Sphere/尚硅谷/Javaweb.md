---
date: 2025-05-17 21:50
tags:
  - System/DG/Seedling
source: >-
  https://www.bilibili.com/video/BV13T411372x/?spm_id_from=333.1387.collection.video_card.click&vd_source=7038f96b6bb3b14743531b102b109c43
update: 2025-05-17 21:59
---

---
在 Maven 中，工程的类型由 `<packaging>` 标签指定，决定了 Maven 构建出的**最终产物的形式**，也直接影响其在依赖树中的行为。常见的 Maven 工程类型如下：

---

## ✅ 常见的 Maven 工程类型（Packaging 类型）

|Packaging 类型|用途说明|
|---|---|
|`jar`|默认类型。生成 `.jar` 包，适用于普通 Java 库项目|
|`war`|生成 `.war` 包，适用于 Java Web 项目，部署到如 Tomcat、Jetty|
|`pom`|聚合项目，不能编译代码，仅用于组织多个模块，常见于父工程或 BOM|
|`ear`|生成 `.ear` 包，适用于 JavaEE 应用（含 EJB、WAR 模块），部署到 JBoss/WebLogic|
|`maven-plugin`|构建 Maven 插件，最终产物是一个可供执行的 Maven 插件 JAR|
|`ejb`|构建 Enterprise Java Bean 模块，产物为 `.jar`，部署在应用服务器|
|`bundle`|用于 OSGi 项目，生成 OSGi-compatible JAR（需要使用 `maven-bundle-plugin`）|
|`atlassian-plugin`|用于 Atlassian 开发平台（如 JIRA 插件开发）专用|
|`apk`、`aar`、`apk-lib`|Android 开发中使用的类型，通常配合 Gradle/Maven Android 插件|
|`swf`|生成 Flash 的 `.swf` 文件（已基本淘汰）|

---

## 五、优缺点对比与推荐场景

|工具|优点|缺点|推荐场景|
|---|---|---|---|
|mybatis-plus-generator|快速生成常规代码结构，支持插件化配置|代码风格固定（可通过模板改）|新项目快速搭建，规范项目结构|
|velocity-engine-core|模板简单，性能高，自定义能力强|不适合复杂逻辑、条件分支|自定义模板输出、HTML/Java/配置等|

---
