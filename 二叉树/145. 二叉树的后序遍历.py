class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import  List
from  collections import deque
from  collections import deque
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack=deque()
        stack.append(root)
        pre=None
        ans=[]
        while(len(stack)!=0):
            now:TreeNode=stack.pop()
            if pre and (pre==now.right or pre==now.left):#说明已经是第二次访问了。pre既有可能是右子树也有可能是左子树哦！
                ans.append(now.val) #加入答案
            else:#说明是第一次访问，加入自己以及孩子
                stack.append(now)
                if (now.right):
                    stack.append(now.right)
                if (now.left) :
                    stack.append(now.left)
                if (not now.right and not now.left):#对叶子节点单独处理，不想让处理none的结果，不像递归，所以不把none加入stack，这里要对节点进行判断类型，叶子节点要单独处理。
                    stack.pop()
                    ans.append(now.val)
            pre=now
        return ans

