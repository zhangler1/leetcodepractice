# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7



from typing import List
class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if ( len(inorder)<=0 or len(postorder)<=0 ):
            return None
        root=TreeNode(postorder.pop())
        inroot=inorder.index(root.val)

        root.right=self.buildTree(inorder[inroot+1:],postorder[inroot:])
        root.left=self .buildTree(inorder[0:inroot],postorder[0:inroot])

        return root

Solution().buildTree([9,3,15,20,7],
[9,15,7,20,3])