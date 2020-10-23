from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}
        for i,a in enumerate(nums):
           if target-a in dictionary:
               return [dictionary[target-a],i]
           else:
               dictionary[a]=i

        return None









nums=[2, 7, 11, 15]
target= 9
print(Solution().twoSum(nums,target))