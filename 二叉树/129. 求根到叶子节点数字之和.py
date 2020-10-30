class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, Path=[]) -> int:
            if not root:
                return 0

            if not root.left and not root.right:
                return
                #fixme return sum([num * 10 ** (i) for i, num in enumerate(reversed(Path))])
                #   sdf
                #                  

            Path.append(root.left.val)
            a = dfs(root.left, Path)
            Path.pop()
            Path.append(root.right.val)
            b = dfs(root.right, Path)
            Path.pop()
            return a + b

        path = []
        path.append(root.val)
        return dfs(root, path)

if __name__ == '__main__':
    print(Solution().sumNumbers())