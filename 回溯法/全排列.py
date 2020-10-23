from  typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        dfs(nums,ans)
        return ans

def dfs(nums:List[any],ans:List=[[]],arrange:[int]=[],select:int=1,hierachy:int=0):
    if (len(nums)==hierachy)  :
        ans.append(arrange.copy())
        return

    for select in list(set(nums).difference(arrange)) :
        arrange.append(select)
        dfs(nums,ans,arrange,select,hierachy+1)
        arrange.pop()













print(Solution().permute(["1","1","3"]))