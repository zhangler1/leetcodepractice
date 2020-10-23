a=[2,1,0,2,1,1,0]
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partial(nums:List[int],n):
            val=n
            i=0
            j=len(nums)-1
            while(i<j):
                while(nums[j]>=val and j>i):
                    j-=1
                while(nums[i]<=val and i<j):
                    i+=1
                if (i<j) :
                    nums[i], nums[j] = nums[j], nums[i]
        partial(a,1.5)
        partial(a,0.5)




            


Solution().sortColors(a)