# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        stack=[]
        stack.append(root)
        traverse=[]
        while(len(stack)!=0):
            cur=stack.pop()
            traverse.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return traverse
            

