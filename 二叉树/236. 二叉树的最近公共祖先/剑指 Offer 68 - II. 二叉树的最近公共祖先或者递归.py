class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, o) -> bool:
        return self.val==o.val

    def __repr__(self) -> str:
        return str (self.val)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=None
        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode')->bool:#设置了一个特别的函数，子树中含有p，q任何一个
            #在后序遍历的过程中，不仅产生结果，还有返回值，一石二鸟。
            if not root:
                return  False
            left=dfs(root.left,p,q)
            right=dfs(root.right,p,q)
            if left and right or ((root==p or root==q) and (left or right)):
                nonlocal ans
                ans=root.val
            return left or right or root==q or root==p
        dfs(root,p,q)
        return ans



from 二叉树.二叉树的序列化和反序列化 import Codec
if __name__ == '__main__':
    print(Solution().lowestCommonAncestor(Codec().deserialize([3,5,1,6,2,0,8,None,None,7,4]) ,TreeNode(5),TreeNode(4)))
