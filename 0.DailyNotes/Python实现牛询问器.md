# Python实现牛询问器（Cow Interrogator）

```python
import os
import sys

class CowInterrogator:
    @staticmethod
    def get_name():
        """Gets name from standard input"""
        return input("What is your name? ").strip()
    
    @staticmethod
    def get_cow_lover():
        """Gets user's response about liking cows (y/n)"""
        return input("Do you like cows? [y|n] ").strip().lower()
    
    @staticmethod
    def cow_art():
        """Reads cow ASCII art from support/cow.txt file"""
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to cow.txt
        cow_path = os.path.join(current_dir, "support", "cow.txt")
        
        try:
            with open(cow_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print("Error: cow.txt file not found")
            sys.exit(1)
    
    @staticmethod
    def interrogate():
        """Main function that asks questions and displays results"""
        name = CowInterrogator.get_name()
        response = CowInterrogator.get_cow_lover()
        
        if response == 'y':
            print(f"Great! Here's a cow for you {name}:")
            print(CowInterrogator.cow_art())
        elif response == 'n':
            print(f"That's a shame, {name}.")
        else:
            print("You should have entered 'Y' or 'N'.")

if __name__ == "__main__":
    # Run the main interrogate function
    CowInterrogator.interrogate()
```

## 测试代码（可选）

```python
import unittest
import os
import tempfile
import sys
from io import StringIO
from contextlib import redirect_stdout

class TestCowInterrogator(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test
        self.temp_dir = tempfile.mkdtemp()
        # Create a test cow.txt file
        self.cow_path = os.path.join(self.temp_dir, "cow.txt")
        with open(self.cow_path, 'w') as f:
            f.write("(=^o^=)")
        
        # Save original sys.path
        self.original_path = sys.path[:]
        # Add temp directory to sys.path
        sys.path.insert(0, self.temp_dir)
    
    def tearDown(self):
        # Clean up temporary directory
        import shutil
        shutil.rmtree(self.temp_dir)
        # Restore sys.path
        sys.path = self.original_path
    
    def test_cow_art_returns_string(self):
        # Mock the current directory to use our temp directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(self.temp_dir)
        
        # Call cow_art method
        art = CowInterrogator.cow_art()
        
        # Check if the first character is '('
        self.assertEqual(art.strip()[0], '(')
    
    def test_interrogate_with_y_response(self):
        # Capture output
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            # Mock input responses
            def mock_input(prompt):
                if "What is your name?" in prompt:
                    return "Alice"
                elif "Do you like cows?" in prompt:
                    return "y"
                return ""
            
            # Save original input function
            original_input = __builtins__.input
            __builtins__.input = mock_input
            
            # Call interrogate
            CowInterrogator.interrogate()
            
            # Restore original input function
            __builtins__.input = original_input
        
        output = captured_output.getvalue()
        self.assertIn("Great! Here's a cow for you Alice:", output)
        self.assertIn("(=^o^=)", output)
    
    def test_interrogate_with_n_response(self):
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            def mock_input(prompt):
                if "What is your name?" in prompt:
                    return "Bob"
                elif "Do you like cows?" in prompt:
                    return "n"
                return ""
            
            original_input = __builtins__.input
            __builtins__.input = mock_input
            
            CowInterrogator.interrogate()
            __builtins__.input = original_input
        
        output = captured_output.getvalue()
        self.assertIn("That's a shame, Bob.", output)
    
    def test_interrogate_with_invalid_response(self):
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            def mock_input(prompt):
                if "What is your name?" in prompt:
                    return "Charlie"
                elif "Do you like cows?" in prompt:
                    return "x"
                return ""
            
            original_input = __builtins__.input
            __builtins__.input = mock_input
            
            CowInterrogator.interrogate()
            __builtins__.input = original_input
        
        output = captured_output.getvalue()
        self.assertIn("You should have entered 'Y' or 'N'.", output)

if __name__ == "__main__":
    unittest.main()
```

## 使用说明

1. 创建项目结构：
   ```
   cow_interrogator/
   ├── cow_interrogator.py
   ├── support/
   │   └── cow.txt
   └── test_cow_interrogator.py
   ```

2. 在`support/cow.txt`中添加牛的ASCII艺术（例如）：
   ```
   (=^o^=)
   ```

3. 运行程序：
   ```bash
   python cow_interrogator.py
   ```

4. 运行测试（可选）：
   ```bash
   python test_cow_interrogator.py
   ```

## 与Elixir版本的对比

- Python使用`input()`代替Elixir的`IO.gets()`
- Python使用`print()`代替Elixir的`IO.puts()`
- Python使用`os.path`处理文件路径，而不是Elixir的`Path.expand()`
- Python使用`with open()`处理文件读取，而不是Elixir的`File.read()`
- Python使用`sys.exit(1)`处理文件未找到错误，而不是Elixir的`System.halt(1)`
- Python的测试使用`unittest`框架，而不是Elixir的`ExUnit`

这个Python实现完全保留了Elixir版本的功能，同时遵循了Python的惯用写法和最佳实践。