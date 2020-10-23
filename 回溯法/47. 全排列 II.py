from typing import  List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.dfs(nums,ans,lenth=len(nums))
        return [[x for x in a] for a in set(ans)]
    def dfs(self,nums:List[int],ans=[],arrange=[],lenth=0,hierachy=0 ):
        if hierachy==lenth:
            ans.append(tuple(arrange))
            return
        for i,selection in  enumerate(nums):
            arrange.append(selection)
            candidatenum=nums.copy()
            candidatenum.pop(i)
            self.dfs(candidatenum,ans,arrange,lenth,hierachy+1)
            arrange.pop()
        

print(Solution().permuteUnique(["a","a ","a"]))