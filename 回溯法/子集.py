# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
from typing import List,NoReturn
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        dfs(nums=nums,ans=ans)
        return ans
def dfs(nums:List[List[any]],path:List[any]=[],selection:bool=True,hierachy:int=0,ans:List[List[int]]=[])->NoReturn:
    if(hierachy>len(nums)):
        return
    if(hierachy==len(nums)):
        ans.append(path.copy())
        return

    for selection in True,False :
        if selection:

            path.append(nums[hierachy])
            dfs(nums,path,selection,hierachy+1,ans)
            path.pop()
        else:
            dfs(nums,path,selection,hierachy+1,ans)

print(Solution().subsets([2,4,5,9]))




















