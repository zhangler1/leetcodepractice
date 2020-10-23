from typing import  List

def dfs(n: int, k: int, combine: List[int]=[], ans: List[int]=[], select: int=0, hierachy: int=0):
    if (hierachy == k):
        ans.append(combine.copy())
        return

    while (select < n):
        select= select+1
        combine.append(select)
        dfs(n, k, combine, ans, select, hierachy + 1)
        combine.pop()

class Solution:
    def fCombine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        dfs(n,k,ans=ans)
        return ans
print(len(Solution().fCombine(7,2)))