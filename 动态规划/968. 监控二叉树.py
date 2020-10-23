
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        a, b, c = dfs(root)
        return b


def dfs(root: TreeNode, ) -> (int, int, int):
    if not root:
        return float('inf'), 0, 0
    al, bl, cl = dfs(root.left)
    ar, br, cr = dfs(root.right)

    a = cl + cr + 1
    c = min(bl + br, a)
    b = min(a, al + br, ar + bl)
    return a, b, c


        

