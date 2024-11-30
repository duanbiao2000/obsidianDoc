---
title: 
date_created: 
categories:
  - Diary
tags:
  - GitHub
  - Code
aliases: 
theme:
---

总结

<!--more-->

Unix 管道（pipe）是一种强大的机制，用于连接多个进程，使得前一个进程的输出作为后一个进程的输入。管道通常与一系列称为过滤器的工具一起使用，这些工具能够对文本进行处理。这些工具通常设计得简单而强大，可以组合起来完成复杂的任务。

下面是一些常用的 Unix 过滤器工具及其基本用法：

### 1. `cat`
- **用途**：显示文件内容或将标准输入复制到标准输出。
- **命令**：
  ```sh
  cat file.txt
  ```

### 2. `grep`
- **用途**：搜索文件中的指定模式。
- **命令**：
  ```sh
  grep "pattern" file.txt
  ```

### 3. `awk`
- **用途**：强大的文本处理工具，可以进行条件判断、数学运算等。
- **命令**：
  ```sh
  awk '{ print $1 }' file.txt  # 输出第一列
  awk '/pattern/ { print }' file.txt  # 匹配模式时打印行
  ```

### 4. `sed`
- **用途**：流编辑器，用于文本转换和过滤。
- **命令**：
  ```sh
  sed 's/pattern/replacement/g' file.txt  # 替换模式
  sed '/pattern/d' file.txt  # 删除匹配模式的行
  ```

### 5. `cut`
- **用途**：从每行分割字段并输出选定的部分。
- **命令**：
  ```sh
  cut -d ',' -f 1,3 file.csv  # 以逗号为分隔符，输出第1和第3列
  ```

### 6. `tr`
- **用途**：替换或删除字符。
- **命令**：
  ```sh
  tr '[:upper:]' '[:lower:]' < file.txt  # 转换为小写
  tr -d '\n' < file.txt > file.txt.new  # 删除换行符
  ```

### 7. `sort`
- **用途**：排序文件的行。
- **命令**：
  ```sh
  sort file.txt
  sort -u file.txt  # 去重
  ```

### 8. `uniq`
- **用途**：过滤相邻重复的行。
- **命令**：
  ```sh
  uniq file.txt
  sort file.txt | uniq  # 先排序再去重
  ```

### 9. `wc`
- **用途**：统计字节数、单词数、行数等。
- **命令**：
  ```sh
  wc -l file.txt  # 统计行数
  wc -w file.txt  # 统计单词数
  ```

### 10. `head` 和 `tail`
- **用途**：输出文件的开头或结尾的若干行。
- **命令**：
  ```sh
  head -n 10 file.txt  # 输出前10行
  tail -n 10 file.txt  # 输出最后10行
  ```

### 组合使用管道的例子

#### 示例 1：查找日志文件中的错误并统计次数
```sh
grep 'error' log.txt | wc -l
```

#### 示例 2：将 CSV 文件的第一列转换为大写并排序
```sh
cut -d ',' -f 1 file.csv | tr '[:lower:]' '[:upper:]' | sort
```

#### 示例 3：从文本文件中删除空白行并去重
```sh
grep -v '^$' file.txt | sort | uniq
```

#### 示例 4：统计文本文件中每个单词出现的次数
```sh
tr ' ' '\n' < file.txt | sort | uniq -c
```

通过组合这些工具，可以非常灵活地处理文本数据。这些命令和工具是 Unix/Linux 系统中不可或缺的一部分，了解它们的基本用法对于日常管理和数据分析非常有帮助。如果您有更具体的需求或问题，请随时提出。