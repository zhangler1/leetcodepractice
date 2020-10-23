from typing import List,NoReturn
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if (not root):
            return
        Path=[root.val]
        ans=[]
        self.dfs(root,Path,sum,ans)
        return ans


    def dfs(self,root:TreeNode,Path:List[int],_sum: int,ans=[])->NoReturn:
        if (not root):
            return
        if (not root.left and not root.right):
            if sum(Path)==_sum:
                ans.append(Path.copy())
                return
            else:
                return
        if root.left:
            Path.append(root.left.val)
            self.dfs(root.left,Path,_sum,ans)
            Path.pop()
        if root.right:
            Path.append(root.right.val)
            self.dfs(root.right,Path,_sum,ans)
            Path.pop()
        return





