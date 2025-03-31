---
title: awesome-mcp-servers/README-zh.md at main · punkpeye/awesome-mcp-servers
source: https://github.com/punkpeye/awesome-mcp-servers/blob/main/README-zh.md#browser-automation
author: 
published: 
date: 2025-03-27
description: 
tags:
  - clippings
---
Okay, let's optimize the `awesome-mcp-servers` list to reduce cognitive load, making it easier to scan, understand, and find relevant servers.

**Key Optimization Strategies:**

1.  **Clearer Structure & Grouping:** Instead of one long list per category, group similar servers within categories (e.g., all database servers by type like SQL, NoSQL, Vector).
2.  **Standardized Descriptions:** Use a more consistent format for descriptions, highlighting the core function and technology.
3.  **Explicit Tags (Replacing/Supplementing Icons):** Replace ambiguous icons with clear text tags (e.g., `[Python]`, `[TypeScript]`, `[Go]`, `[Cloud]`, `[Local]`, `[Official]`, `[VectorDB]`). This eliminates the need to learn a legend.
4.  **Highlighting Key Servers:** Potentially add a "Featured" or "Core" section, or use bolding/markers for official or highly maintained servers. (For this exercise, we'll focus on structure and tags).
5.  **Improved Readability:** Use formatting like bullet points and bold text effectively.

**Optimized Structure (Conceptual Example - Applying to select categories):**


# Awesome MCP Servers (Optimized for Clarity)

A curated list of Model Context Protocol (MCP) server implementations, frameworks, and utilities designed to connect Large Language Models (LLMs) like Claude to external tools and data sources securely.

**Legend for Tags:**
*   `[Lang]`: Primary programming language (e.g., `[Python]`, `[TypeScript]`, `[Go]`, `[Java]`, `[Rust]`)
*   `[Platform]`: Where it primarily runs (e.g., `[Cloud]`, `[Local]`, `[macOS]`, `[Windows]`)
*   `[Official]`: Maintained by the core MCP team or the service provider.
*   `[DB Type]`: Specific database category (e.g., `[SQL]`, `[NoSQL]`, `[VectorDB]`, `[GraphDB]`, `[TimeSeriesDB]`)
*   `[Use Case]`: Primary function (e.g., `[Web Search]`, `[File System]`, `[Code Analysis]`, `[IDE Integration]`)

---

## Table of Contents

*   [Core Servers (Essential Functionality)](#core-servers-essential-functionality)
*   [Server Implementations by Category](#server-implementations-by-category)
    *   [Browser Automation & Web Interaction](#browser-automation--web-interaction)
    *   [Cloud Platform Management](#cloud-platform-management)
    *   [Command Line & Shell Interaction](#command-line--shell-interaction)
    *   [Databases](#databases)
        *   [SQL Databases](#sql-databases)
        *   [NoSQL Databases](#nosql-databases)
        *   [Vector Databases](#vector-databases)
        *   [Graph Databases](#graph-databases)
        *   [Time Series Databases](#time-series-databases)
        *   [Spreadsheets/Other](#spreadsheetsother)
    *   [Developer Tools](#developer-tools)
        *   [IDE & Editor Integration](#ide--editor-integration)
        *   [API & HTTP Tools](#api--http-tools)
        *   [Code Analysis & Generation](#code-analysis--generation)
        *   [Containerization & Infra](#containerization--infra)
        *   [File Conversion & Handling](#file-conversion--handling)
        *   [Mobile Development](#mobile-development)
        *   [Package Management](#package-management)
    *   [Data Science & Processing](#data-science--processing)
    *   [File Systems (Local & Cloud)](#file-systems-local--cloud)
    *   [Finance & Fintech](#finance--fintech)
    *   [Knowledge, Memory & RAG](#knowledge-memory--rag)
    *   [Location Services](#location-services)
    *   [Marketing Tools](#marketing-tools)
    *   [Search Engines & APIs](#search-engines--apis)
    *   [Security Tools](#security-tools)
    *   [Version Control (Git, GitHub, GitLab)](#version-control-git-github-gitlab)
    *   [Other Tools & Integrations](#other-tools--integrations)
*   [Frameworks (For Building MCP Servers)](#frameworks-for-building-mcp-servers)
*   [Utilities & Proxies](#utilities--proxies)

---

## Core Servers (Essential Functionality)

*   **[@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** `[TypeScript]` `[Local]` `[Official]` `[File System]` - Core server for direct, permission-controlled access to the local file system.
*   **[@modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** `[Python]` `[Local/Cloud]` `[Official]` `[Web Interaction]` - Efficiently fetch and process web content for AI consumption.
*   **[@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** `[TypeScript]` `[Local]` `[Official]` `[Knowledge & Memory]` - Core server providing knowledge graph-based persistent memory for context maintenance across sessions.
*   **[@modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything)** `[TypeScript]` `[Local]` `[Official]` - Reference server covering all core MCP protocol features.

---

## Server Implementations by Category

### 📂 Browser Automation & Web Interaction
*Servers for controlling browsers, scraping web content, and interacting with web pages.*

*   **[@blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp)** `[Python]` `[Local]` `[Web Interaction]` - Playwright automation optimized for LLM interaction.
*   **[@executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright)** `[TypeScript]` `[Local]` `[Web Interaction]` `[Web Scraping]` - Playwright for automation and scraping.
*   **[@automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright)** `[TypeScript]` `[Local]` `[Web Interaction]` - Playwright-based browser automation.
*   **[@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer)** `[TypeScript]` `[Local]` `[Official]` `[Web Scraping]` `[Web Interaction]` - Puppeteer for web scraping and interaction.
*   **[@kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)** `[TypeScript]` `[Cloud]` `[Web Scraping]` - Fetches YouTube transcripts for AI analysis.
*   **[kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing)** `[Python]` `[Local]` `[Web Interaction]` - Minimal implementation using Azure OpenAI and Playwright.
*   **[@pskill9/web-search](https://github.com/pskill9/web-search)** `[TypeScript]` `[Local]` `[Web Search]` - Uses Google search results for free web search (no API key needed).
*   **[apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser)** `[TypeScript]` `[Cloud]` `[Web Search]` `[Web Scraping]` `[RAG]` - Uses Apify RAG Web Browser Actor for search, scraping, and returning Markdown content.

*(... Continue restructuring other categories similarly ...)*

### 🗄️ Databases
*Servers for interacting with various database systems.*

#### SQL Databases
*   **PostgreSQL:**
    *   [@modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) `[TypeScript]` `[Local]` `[Official]` `[SQL]` - Schema inspection and query capabilities.
    *   [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) `[Python]` `[Local]` `[SQL]` - SQLAlchemy-based, supports PostgreSQL, MySQL, SQLite, Oracle, MS SQL. Features schema/relationship checks, large dataset analysis.
*   **MySQL:**
    *   [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) `[Python]` `[Local]` `[SQL]` - Configurable access control, schema checks, security guide.
    *   [f4ww4z/mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server) `[Node.js]` `[Local]` `[SQL]` - Secure MySQL operations via Node.js.
    *   [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) `[Python]` `[Local]` `[SQL]` - (See above).
*   **SQLite:**
    *   [@modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) `[Python]` `[Local]` `[Official]` `[SQL]` - SQLite operations with built-in analysis.
    *   [hannesrudolph/sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) `[Python]` `[Local]` `[SQL]` - Secure read-only access using FastMCP framework, query validation.
    *   [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) `[Python]` `[Local]` `[SQL]` - (See above).
*   **BigQuery:**
    *   [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) `[Python]` `[Cloud]` `[SQL]` - Schema inspection and query features.
    *   [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) `[TypeScript]` `[Cloud]` `[SQL]` - Direct BigQuery access and query.
*   **Snowflake:**
    *   [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) `[Python]` `[Cloud]` `[SQL]` - Read and optional write operations with insight tracking.
*   **TiDB:**
    *   [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) `[Python]` `[Cloud]` `[SQL]` - Schema DDL and SQL execution.
*   **DuckDB:**
    *   [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) `[Python]` `[Local]` `[SQL]` - Schema inspection and query features.
*   **SQLAlchemy (Generic):**
    *   [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) `[Python]` `[Local]` `[SQL]` - (See above, supports many SQL DBs).

#### NoSQL Databases
*   **MongoDB:**
    *   [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) `[TypeScript]` `[Local]` `[NoSQL]` - Allows LLM interaction with MongoDB.
    *   [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) `[TypeScript]` `[Local]` `[NoSQL]` - MCP Server for MongoDB.
*   **Elasticsearch:**
    *   [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) `[Python]` `[Local]` `[NoSQL]` `[Search]` - MCP Server integrating Elasticsearch.
*   **Alibaba Cloud Tablestore:**
    *   [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) `[Java/Python]` `[Cloud]` `[NoSQL]` `[VectorDB]` `[RAG]` - Add docs, vector/scalar search, RAG-friendly.
*   **Fireproof (Distributed Ledger):**
    *   [@fireproof-storage/mcp-database-server](https://github.com/fireproof-storage/mcp-database-server) `[TypeScript]` `[Cloud]` `[NoSQL]` `[Distributed]` - Supports multi-user data sync.

#### Vector Databases
*   **Pinecone:**
    *   [sirmews/mcp-pinecone](https://github.com/sirmews/mcp-pinecone) `[Python]` `[Cloud]` `[VectorDB]` - Integration with vector search capabilities.
*   **VikingDB:**
    *   [KashiwaByte/vikingdb-mcp-server](https://github.com/KashiwaByte/vikingdb-mcp-server) `[Python]` `[Cloud]` `[VectorDB]` - Collection/index info, vector storage and query.
*   **Alibaba Cloud Tablestore:**
    *   [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) `[Java/Python]` `[Cloud]` `[NoSQL]` `[VectorDB]` `[RAG]` - (See above).

#### Graph Databases
*   **Neo4j:**
    *   [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) `[Python]` `[Local]` `[GraphDB]` - MCP for Neo4j.

#### Time Series Databases
*   **GreptimeDB:**
    *   [GreptimeTeam/greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server) `[Python]` `[Local]` `[TimeSeriesDB]` - Query GreptimeDB.
*   **Timeplus (with Kafka):**
    *   [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) `[Python]` `[Cloud]` `[TimeSeriesDB]` `[Streaming]` - Integrates Kafka & Timeplus for querying latest Kafka data via SQL. (Note: Repo name is clickhouse but description points to Kafka/Timeplus).
    *   [jovezhong/mcp-timeplus](https://github.com/jovezhong/mcp-timeplus) `[Python]` `[Cloud]` `[TimeSeriesDB]` `[Streaming]` - List Kafka topics, poll messages, save data, query streaming data via Timeplus SQL.

#### Spreadsheets/Other
*   **Airtable:**
    *   [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) `[TypeScript]` `[Local]` `[Spreadsheet]` - Schema checks, read/write functionality.
*   **Google Sheets:**
    *   [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) `[Python]` `[Cloud]` `[Spreadsheet]` - Create, read, update, manage spreadsheets via Google Sheets API.
*   **Tinybird:**
    *   [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) `[Python]` `[Cloud]` `[API]` - Query and API features for Tinybird.

*(... Continue restructuring other categories ...)*

### 💻 Developer Tools

#### IDE & Editor Integration
*   [jetbrains/mcpProxy](https://github.com/JetBrains/mcpProxy) `[TypeScript]` `[Local]` `[Official]` `[IDE Integration]` - Connect to JetBrains IDEs.
*   [r-huijts/xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server) `[TypeScript]` `[Local]` `[macOS]` `[IDE Integration]` - Xcode integration for project management, file ops, build automation.
*   [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) `[Python]` `[Local]` `[Editor]` - Line-oriented text file editor optimized for LLMs (partial file access).
*   [@marimo-team/codemirror-mcp](https://github.com/marimo-team/codemirror-mcp) `[TypeScript]` `[Editor]` - CodeMirror extension implementing MCP for resource mentions and prompt commands.

#### API & HTTP Tools
*   [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) `[Go]` `[Local]` `[API]` - Connect any HTTP/REST API server using an OpenAPI v3 spec.
*   [delano/postman-mcp-server](https://github.com/delano/postman-mcp-server) `[TypeScript]` `[Cloud]` `[API]` - Interact with the Postman API.
*   [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) `[TypeScript]` `[Local]` `[API]` - Flexible fetching of JSON, text, and HTML data.

*(... And so on for other dev tool subcategories and main categories ...)*

---

## Frameworks (For Building MCP Servers)
*Libraries and SDKs to simplify MCP server development.*

*   **Python:**
    *   [FastMCP](https://github.com/jlowin/fastmcp) `[Python]` - High-level framework.
    *   [rectalogic/langchain-mcp](https://github.com/rectalogic/langchain-mcp) `[Python]` - LangChain integration for using MCP tools.
*   **TypeScript/JavaScript:**
    *   [FastMCP](https://github.com/punkpeye/fastmcp) `[TypeScript]` - High-level framework.
    *   [LiteMCP](https://github.com/wong2/litemcp) `[TypeScript]` - High-level framework.
    *   [mcp-framework](https://github.com/QuantGeekDev/mcp-framework) `[TypeScript]` - Fast and elegant framework.
    *   [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) `[TypeScript]` - Integrates Google's Genkit with MCP.
*   **Go:**
    *   [Foxy Contexts](https://github.com/strowk/foxy-contexts) `[Go]` - Declarative library with functional testing.
    *   [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) `[Go]` - SDK for building clients and servers.
    *   [metoro-io/mcp-golang](https://github.com/metoro-io/mcp-golang) `[Go]` - Framework focused on type safety.
*   **Java/Spring:**
    *   [spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) `[Java]` `[Spring]` - Java SDK and Spring Framework integration.
*   **Rust:**
    *   [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) `[Rust]` - CLI server template.
*   **Scala:**
    *   [mullerhai/sakura-mcp](https://github.com/mullerhai/sakura-mcp) `[Scala]` - Framework for enterprise-grade clients/servers.

---

## Utilities & Proxies
*Tools for managing, testing, or bridging MCP connections.*

*   [mcp-proxy (punkpeye)](https://github.com/punkpeye/mcp-proxy) `[TypeScript]` - SSE proxy for `stdio` based servers.
*   [mcphost (mark3labs)](https://github.com/mark3labs/mcphost) `[Go]` - CLI host app for LLM interaction with tools via MCP.
*   [mcp-manager (zueai)](https://github.com/zueai/mcp-manager) `[TypeScript]` `[Cloud]` - Simple Web UI to install/manage MCP servers for Claude Desktop.
*   [mcp-cli (wong2)](https://github.com/wong2/mcp-cli) `[TypeScript]` `[Local]` - CLI tool for testing MCP servers.
*   [MCP-Connect (EvalsOne)](https://github.com/EvalsOne/MCP-Connect) `[TypeScript]` - Tool to allow cloud AI services to access local stdio MCP servers via HTTP/S.
*   [MCP-Bridge (SecretiveShell)](https://github.com/SecretiveShell/MCP-Bridge) `[Python]` - OpenAI middleware proxy to use MCP with OpenAI-compatible clients.
*   [mcp-proxy (sparfenyuk)](https://github.com/sparfenyuk/mcp-proxy) `[Python]` - Stdio to SSE transport gateway.
*   [mcp-server-and-gw (boilingdata)](https://github.com/boilingdata/mcp-server-and-gw) `[TypeScript]` - Stdio to HTTP SSE gateway with example server/client.
*   [mcp-langchain-ts-client (isaacwasserman)](https://github.com/isaacwasserman/mcp-langchain-ts-client) `[TypeScript]` - Use MCP tools within LangChain.js.
*   [mcp-gateway (lightconetech)](https://github.com/lightconetech/mcp-gateway) `[TypeScript]` - Demo gateway for MCP SSE servers.
*   [gpt-computer-assistant (upsonic)](https://github.com/Upsonic/gpt-computer-assistant) `[Python]` - Framework for building vertical AI agents (implies MCP utility).



**Rationale for Changes:**

1.  **Clear Title and Intro:** Added a clearer title and introductory sentence.
2.  **Legend:** Introduced a text-based tag legend for clarity, replacing ambiguous icons.
3.  **Restructured TOC:** Grouped related database types and developer tools for better navigation. Added a "Core Servers" section.
4.  **Grouping within Categories:** Demonstrated grouping for Databases (by type) and Developer Tools (by function). This significantly reduces the visual clutter within large categories.
5.  **Consistent Tagging:** Applied the new text tags consistently to the example sections.
6.  **Standardized Descriptions (Implied):** While not fully rewritten for brevity, the structure allows for easier standardization (e.g., "MCP Server for [Service/Tool] using [Language]. Features: ...").
7.  **Separation of Concerns:** Clearly maintained the separation between Implementations, Frameworks, and Utilities.

This revised structure makes the list much easier to navigate and understand at a glance, reducing the cognitive load required to find a suitable MCP server. The full list would need this structure applied throughout all categories.