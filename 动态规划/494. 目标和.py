
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum1=sum(nums)
        if S>sum1:
            return None
        dp=[1 for _ in range(2*sum1+1)]
        pre= [0 for _ in range(2*sum1+1)]
        pre[sum1]=1
        for i in range(len(nums)):
            for j in range(2*sum1+1):
                dp[j]=(pre[j-nums[i]] if (j-nums[i])>=0 else 0) +(pre[j+nums[i]] if (j+nums[i])<=2*sum1 else 0)
            pre=dp.copy()

        return dp[S+sum1]

if __name__ == '__main__':
    print(Solution().findTargetSumWays([1,1,1,1,1],
    3))