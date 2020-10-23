# from typing import
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        sum=0
        pre=None
        path=[]
        rightprior(root,path)
        return root
def rightprior( root: TreeNode,path:[int]) :
        if (not root):
            return 0
        if(root.right):
            rightprior(root.right,path)
        path.append(root.val)
        root.val=sum(path)
        if (root.left):
            rightprior(root.left,path)

        