### 树（Tree）

树是一种层次化的数据结构，由节点（Node）组成，其中一个节点作为根（Root），其余节点通过边（Edge）连接。每个节点可以有零个或多个子节点，但只有一个父节点（除了根节点）。树的常见类型包括二叉树（Binary Tree）、平衡树（Balanced Tree）、B树（B-Tree）等。

#### 二叉树的深度优先搜索（DFS）

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(root):
    if root is None:
        return

    # 访问当前节点
    print(root.value, end=' ')

    # 递归遍历左子树
    dfs(root.left)

    # 递归遍历右子树
    dfs(root.right)

# 创建一个简单的二叉树
#     1
#    / \
#   2   3
#  / \
# 4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 执行深度优先搜索
dfs(root)
```