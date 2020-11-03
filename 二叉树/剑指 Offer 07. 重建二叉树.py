from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return 
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])

        root.left=self.buildTree(preorder[1:mid+1],inorder[0:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
if __name__ == '__main__':
    print(Solution().buildTree(preorder = [3,9,20,15,7],inorder = [9,3,15,20,7]))