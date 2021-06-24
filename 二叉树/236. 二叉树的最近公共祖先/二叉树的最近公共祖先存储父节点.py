class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left : TreeNode= None
        self.right : TreeNode= None

    def __eq__(self, o) -> bool:
        return self.val==o.val

    def __repr__(self) -> str:
        return str (self.val)
#使用了__eq__函数
#
from  typing import List
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(ANS:List[int],Path:List[int],root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
            if not root:
                return
            if len(ANS)==2:
                return
            Path.append(root.val) #leetcode中需要去掉。val
            #加入path，平常是因为进入下层之后不知道选择具体了

            if root==p or root==q:
                ANS.append(Path.copy())
            dfs(ANS,Path,root.left,p,q)
            

            dfs(ANS,Path,root.right,p,q)
            Path.pop()
            #加入退出这栈也退出
        Ans=[]
        dfs(Ans,[],root,p,q)
        pre=None
        for k,(i,j )in enumerate(zip(*Ans)):

            if i!=j:
                return pre#存在不等的情况有一个前驱保存一下
            pre=j
        return Ans[0][k] #全部相等




from 数据结构.二叉树的序列化和反序列化 import Codec
if __name__ == '__main__':
    print(Solution().lowestCommonAncestor(Codec().deserialize([3,5,1,6,2,0,8,None,None,7,4]
    ),TreeNode(7),TreeNode(4)))
