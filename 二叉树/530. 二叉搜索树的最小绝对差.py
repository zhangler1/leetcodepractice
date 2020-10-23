### 解题思路
# 1.
# 写连个nonlocal变量存储变量和差值即可
# 2.
# 注意要在中序遍历结束后立马就存储pre的值

### 代码




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        minval = float("inf")
        pre = None

        if not root:
            return None

        def dfs(root: TreeNode):
            nonlocal pre
            nonlocal minval
            if not root:
                return

            if root.right:
                dfs(root.right)
            if pre and abs(root.val - pre.val) < minval:
                minval = abs(root.val - pre.val)
            pre = root
            if root.left:
                dfs(root.left)

            return

        dfs(root)
        return minval

