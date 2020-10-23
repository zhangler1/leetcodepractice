from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[ 0 for _ in range(n)]
        i=0
        while(i<n):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            i=i+1

        return max(dp)


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))