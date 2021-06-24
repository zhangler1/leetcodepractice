from 数据结构.二叉树的序列化和反序列化 import Codec, TreeNode
from typing import List

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        curStack=[]
        flag=1
        nextStack=[]
        curStack.append(root)
        ans=[]
        curlevel=[]   #be obscure with level judge
        while (len(curStack)!=0):

            cur=curStack.pop()
            curlevel.append(cur.val)
            if flag==0:
                if cur.right!=None:
                    nextStack.append(cur.right)

                if cur.left!=None:
                    nextStack.append(cur.left)
            else:
                if cur.left:
                    nextStack.append(cur.left)

                if cur.right:
                    nextStack.append(cur.right)
            if len(curStack)==0:
                ans.append(curlevel)
                curlevel=[]
                if len(nextStack)!=0:
                    curStack=nextStack
                    nextStack=[]
                flag=not flag
        return ans

if __name__=='__main__':
    print(Solution().zigzagLevelOrder(Codec().deserialize([3, 9, 20, None, None, 15, 7])))
