---
aliases: 
createdAt: 2025-03-17 16:45
updateAt: 2025-03-24 17:17
categories: 
Rating: 
tags:
  - Effective/Tools
---
## Unix 过滤器示例

Unix 系统提供了许多过滤器工具，这些工具可以用于各种文本处理任务。以下是一些常见的过滤器工具及其实用示例：

### 1. `cut`

`cut` 命令用于从文件中分割并输出选定的字段。

- **示例**：从CSV文件中提取特定列
  ```sh
  cut -d ',' -f 1,3 file.csv
  ```

### 2. `awk`

`awk` 是一种强大的文本处理工具，可以进行条件判断、数学运算等。

- **示例**：统计文件中每个单词出现的次数
  ```sh
  awk '{for(i=1;i<=NF;i++) {if(!seen[$i]) {seen[$i]++}}}' file.txt
  ```

### 3. `sort`

`sort` 命令用于排序文件的行。

- **示例**：按照年龄对人员列表进行排序
  ```sh
  sort file.txt | sort -k 3rn
  ```

### 4. `uniq`

`uniq` 命令用于去重，可以用于删除文件中相邻的重复行。

- **示例**：去重并按年龄排序
  ```sh
  sort file.txt | uniq | sort -k 3rn
  ```

### 5. `tr`

`tr` 命令用于替换或删除字符。

- **示例**：删除文本中的空格
  ```sh
  tr ' ' '<file.txt > file.txt.new
```

### 6. `paste`

`paste` 命令用于将多个文件的内容并排显示。

- **示例**：将两个文本文件的内容并排显示
  ```sh
  paste file1.txt file2.txt
  ```

### 7. `expand` 和 `collapse`

`expand` 命令用于展开制表符为空格，`collapse` 命令则相反。

- **示例**：将制表分隔符（tab）替换为空格
  ```sh
  expand -t 4 file.txt > file.txt.new
  ```

- **示例**：将多个文本文件合并为一个文件
  ```sh
  cat file1.txt file2.txt > file3.txt
  ```

### 8. `col`

`col` 命令用于将多列数据对齐显示。

- **示例**：对齐显示两个文本文件的内容
  ```sh
  col -w 25 file1.txt file2.txt
  ```

### 9. `split`

`split` 命令用于将大文件分割成小文件。

- **示例**：将日志文件分割成每天的文件
  ```sh
  split -d -a 6 -k date.log
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