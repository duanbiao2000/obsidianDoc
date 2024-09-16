---
aliases: 
theme: 
high_priority: false
tags:
---
我们可以使用 OpenAI 的 API 来生成文件的摘要，并将其作为新的文件名。以下是一个 Python 脚本，它会读取 `@dailyNotes` 目录下的每个文件，使用 OpenAI 的 API 生成摘要，并将其作为新的文件名。

### 步骤

1. **安装 OpenAI Python 库**:
   ```bash
   pip install openai
   ```

2. **设置 OpenAI API Key**:
   你需要在脚本中设置你的 OpenAI API Key。

3. **运行脚本**:
   将以下代码保存为 `rename_notes_with_ai.py`，并在终端中运行：
   ```bash
   python rename_notes_with_ai.py
   ```

### 代码

```python
import os
import openai

# 设置 OpenAI API Key
openai.api_key = 'your-openai-api-key'

def generate_summary(content):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text in one sentence:\n\n{content}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                summary = generate_summary(content)
                if summary:
                    new_filename = f"{summary}.md"
                    new_file_path = os.path.join(directory, new_filename)
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    directory = "@dailyNotes"
    rename_files_in_directory(directory)
```

### 说明

1. **generate_summary 函数**:
   - 使用 OpenAI 的 `text-davinci-003` 模型生成文件内容的摘要。
   - 摘要将作为新的文件名。

2. **rename_files_in_directory 函数**:
   - 遍历指定目录下的所有文件。
   - 读取每个文件的内容，生成摘要。
   - 如果生成摘要成功，则将其作为新的文件名，并重命名文件。

3. **主程序**:
   - 指定目录为 `@dailyNotes`。
   - 调用 `rename_files_in_directory` 函数进行重命名。

### 注意事项

- 你需要将 `your-openai-api-key` 替换为你的实际 OpenAI API Key。
- 确保你有足够的 OpenAI API 配额来处理所有文件。

这个脚本会自动将 `@dailyNotes` 目录下的文件重命名为 AI 生成的摘要标题。