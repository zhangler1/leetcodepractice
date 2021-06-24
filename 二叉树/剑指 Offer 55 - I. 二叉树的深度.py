from 数据结构.二叉树的序列化和反序列化 import Codec,TreeNode
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

if __name__ == '__main__':
    print(Solution().maxDepth(Codec().deserialize([3,9,20,None,None,15,7])))