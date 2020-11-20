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
        if not root:
            return None

        def isCA( root: 'TreeNode', q: 'TreeNode' ) ->bool:
            if not root:
                return False
            if root==q or isCA(root.left,q) or isCA(root.right,q):
                return True
        while(isCA(root.left,q) and isCA(root.left,p) or isCA(root.right,q) and isCA(root.right,p)):
            if  isCA(root.left,q):
                 root=root.left
            else:
                root=root.right
        return root
from 二叉树.二叉树的序列化和反序列化 import Codec
if __name__ == '__main__':
    print(Solution().lowestCommonAncestor(Codec().deserialize([3,5,1,6,2,0,8,None,None,7,4]
    ),TreeNode(7),TreeNode(4)))


        
        
        