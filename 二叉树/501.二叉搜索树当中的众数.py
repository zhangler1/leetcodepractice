from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        sequence = []
        Solution.mid(root, sequence)  # 先序遍历，获得排序好的序列。
        return Solution.countmode(sequence)

    def mid(root: TreeNode, sequence: List[any]):
        if (not root):
            return
        if (root.left):
            Solution.mid(root.left,sequence)
        sequence.append(root.val)
        if (root.right):
            Solution.mid(root.right,sequence)

    def countmode(sequence: List[int]) -> List[int] :

        count = 0
        base = -float("inf")
        maxcount = 0
        ans = []
        for a in sequence:
            if a == base:
                count = count + 1
                if count == maxcount:
                    ans.append(base)
                elif count > maxcount:
                    maxcount=count
                    ans.clear()
                    ans.append(a)
            else:
                base = a
                count = 1
                if count == maxcount:
                    ans.append(base)
                elif count > maxcount:
                    maxcount=count
                    ans.clear()
                    ans.append(a)
        return ans

a=[1]

print(Solution.countmode(a))
