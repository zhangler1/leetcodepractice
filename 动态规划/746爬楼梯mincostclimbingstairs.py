from typing import List
class Solution:
#审题原因 只要多加一个后位置就行，最需要注意的事状态一个状态到一个状态的转移 ，一定要建好模型才行
    def minCostClimbingStairs(self, cost: List[int]) -> int:
          n=len(cost)
          dp=[0]*(n+1)
          dp[0]=0
          dp[1]=0
          for i in range(2,n+1):
              dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
          return dp[n]



if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))