from typing import List
#重大失误，完全没有理解中序遍历树的递归方法
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        recursionStack=[]
        if not root:
            return None
        ans=[]
        cur=root
        while(cur!=None or len(recursionStack)!=0):
            while(cur!=None):
                recursionStack.append(cur)
                cur=cur.left
            cur=recursionStack.pop()
            ans.append(cur.val)
            cur=cur.right                    
        return ans

from 二叉树.二叉树的序列化和反序列化 import Codec

if __name__ == '__main__':
    print(Solution().inorderTraversal(Codec().deserialize([3,5,1,6,2,0,8,None,None,7,4])))



