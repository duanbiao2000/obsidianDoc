#!/usr/bin/env python3

import os
from collections import Counter
import jieba
import string

# 定义文件路径和输出文件名
docs_dir = "wordFreq"
output_file = "热词榜top100.md"
stopwords_file = "stopwords.txt"

# 提示用户词频统计和文件生成开始
print("Generating word frequency list from docs directory...")
print(f"Generating {output_file} file...")

# 提取文本内容，并统计词频
word_counts = Counter()

# 读取屏蔽词列表文件
stopwords = set()
with open(stopwords_file, 'r', encoding='utf-8') as f:
    for line in f:
        stopwords.add(line.strip())

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
            text = f.read()
            # 使用 jieba 进行中文分词
            words = jieba.cut(text)
            word_counts.update(words)

# 输出标题和分隔线到文件
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("Top 100 Hot Words\n")
    f.write("==================\n\n")

# 生成过滤后的词频列表
filtered_word_counts = [
    (word, count)
    for word, count in word_counts.items()
    if len(word) > 1  # 排除单个字
    and not word.isdigit()  # 排除纯数字
    and word not in stopwords
    and word not in string.whitespace
    and word not in string.punctuation
]

# 按词频从高到低排序
filtered_word_counts.sort(key=lambda x: x[1], reverse=True)

# 取前 100 个词频
top_100_word_counts = filtered_word_counts[:100]

# 输出词频到文件
with open(output_file, 'a', encoding='utf-8') as f:
    for word, count in top_100_word_counts:
        f.write(f"{count}\t{word}\n")


# 提示用户文件生成完毕
print(f"Generation of {output_file} complete.")

# 提示用户结果已保存
print(f"Results saved to {output_file}")
