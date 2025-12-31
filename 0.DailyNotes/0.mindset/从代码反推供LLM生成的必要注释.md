# AI代码生成提示模板：Windows批处理构建脚本

## 整体功能注释
```
@echo off
REM ======================================================================
REM 项目构建脚本：打包 Python 后端供 Tauri 前端使用
REM 功能：清理旧构建、打包 Python 后端为可执行文件、适配 Tauri 要求
REM 注意：此脚本需要在 Windows 环境下运行，并依赖 Python、PyInstaller 和 Rust 环境
REM ======================================================================
```

## 关键函数/操作定义

### 1. 环境初始化
```
REM 切换到脚本所在目录的上级目录（项目根目录）
REM 使用 %~dp0 获取脚本所在路径，.. 表示上级目录
REM 输出当前工作目录以便验证
```

### 2. 依赖检查函数
```
REM 依赖检查函数：验证所有必需工具是否可用
REM 检查项：
REM   - Python 是否在 PATH 中
REM   - PyInstaller Python 包是否安装
REM   - Rust 编译器 (rustc) 是否可用
REM 每项检查失败时输出明确错误信息并退出
REM 使用统一的日志格式：[+] 成功，[!] 错误，[*] 进行中
```

### 3. 旧构建清理函数
```
REM 安全清理函数：删除旧构建产物
REM 操作目录：
REM   - backend\dist (PyInstaller 最终输出目录)
REM   - backend\build (PyInstaller 临时工作目录)
REM   - BillNote_frontend\src-tauri\bin (Tauri 二进制文件目录)
REM 使用条件删除 (if exist) 避免因目录不存在而报错
REM 重定向输出 (>nul 2>nul) 保持控制台整洁
```

### 4. 目录结构准备
```
REM 创建 Tauri 所需的目录结构
REM 确保 BillNote_frontend\src-tauri\bin 目录存在
REM 检查创建操作是否成功，失败时退出脚本
```

### 5. 平台信息获取
```
REM 获取 Rust target triple 函数
REM 使用命令: rustc -Vv | findstr "host"
REM 处理输出提取目标平台标识
REM 去除提取值两端的空格
REM 验证获取结果，失败时退出脚本
```

### 6. 环境文件处理
```
REM .env 文件处理函数
REM 逻辑：
REM   1. 检查 .env.example 是否存在
REM   2. 不存在时提供警告并创建默认配置
REM   3. 存在时复制为 backend\.env（临时文件）
REM   4. 验证复制操作是否成功
REM 这是关键步骤，确保 PyInstaller 能正确打包配置文件
```

### 7. PyInstaller 打包函数
```
REM PyInstaller 打包函数
REM 参数说明：
REM   -y: 覆盖现有文件
REM   --name BillNoteBackend: 指定输出可执行文件名（统一命名）
REM   --paths backend: 指定模块搜索路径
REM   --distpath: 指定最终输出目录（Tauri 二进制目录）
REM   --workpath: 指定临时工作目录
REM   --specpath: 指定 .spec 文件生成位置
REM   --hidden-import: 添加隐式依赖包
REM   --add-data: 添加额外数据文件（特别注意 .env 文件）
REM 检查打包结果，失败时清理临时文件并退出
```

### 8. 临时文件清理
```
REM 临时文件清理函数
REM 删除 backend\.env 临时文件
REM 确保即使在错误情况下也会执行清理
```

### 9. Tauri 适配重命名
```
REM Tauri 适配函数：重命名可执行文件
REM Tauri 要求格式：应用名-目标平台.扩展名
REM 例如：BillNoteBackend-x86_64-pc-windows-msvc.exe
REM 步骤：
REM   1. 定义原始路径和新路径
REM   2. 验证原始文件是否存在
REM   3. 执行重命名操作
REM   4. 验证重命名是否成功
```

### 10. 构建验证函数
```
REM 构建验证函数
REM 操作：
REM   1. 列出构建目录内容
REM   2. 专门验证 .env 文件是否包含在构建产物中
REM   3. 根据验证结果提供明确反馈
REM   4. 提供下一步操作建议
```

## 技术约束与要求
```
REM 技术约束：
REM 1. 必须使用延迟变量扩展 (enabledelayedexpansion)
REM 2. 所有文件路径必须使用双引号包裹，处理可能的空格
REM 3. 每个关键步骤后必须检查 errorlevel
REM 4. 错误处理必须包含清理操作
REM 5. 日志输出必须使用统一格式：[+] 成功，[!] 错误/警告，[*] 操作中
REM 6. 批处理续行必须使用 ^ 符号
REM 7. 所有删除/移动操作必须使用 /Y 参数避免确认提示
REM 8. 临时文件必须在脚本结束前清理

REM 命名规范：
REM 1. 统一使用 "BillNote" 作为项目前缀（不是 "BiliNote"）
REM 2. 后端可执行文件命名为 "BillNoteBackend"
REM 3. 变量命名使用大写字母和下划线 (如 TARGET_TRIPLE)
```

## 脚本结构要求
```
REM 脚本结构：
REM 1. 开头包含整体功能注释
REM 2. 逻辑分段，每段有明确标题注释
REM 3. 段落顺序：
REM    - 环境初始化
REM    - 依赖检查
REM    - 旧构建清理
REM    - 目录准备
REM    - 平台信息获取
REM    - 环境文件处理
REM    - PyInstaller 打包
REM    - 临时文件清理
REM    - Tauri 适配重命名
REM    - 构建验证
REM    - 结束处理
REM 4. 每个主要操作后提供状态反馈
REM 5. 结尾包含明确的构建结果状态
```

## 示例错误处理模式
```
REM 错误处理标准模式：
REM if %errorlevel% neq 0 (
REM     echo [!] 错误：描述错误
REM     REM 如有必要，执行清理
REM     exit /b 1
REM )
```

## 最终输出要求
```
REM 脚本结束时提供清晰的构建结果：
REM 1. 成功时提供下一步指导
REM 2. 失败时提供可能的解决方案
REM 3. 使用 exit /b 0 正常退出
```

将以上注释和定义提供给AI，它应该能够生成一个结构良好、错误处理完善的批处理构建脚本，完全符合您对BillNote项目的构建需求。关键是提供了详细的函数定义、技术约束和结构要求，使AI能够理解脚本的完整上下文和特定需求。