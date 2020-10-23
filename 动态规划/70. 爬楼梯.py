class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[1 for _ in range(n+1)]
        i=2
        dp[1]=1
        while(i<=n):
            dp[i]=dp[i-1]+dp[i-2]
            i=i+1

        return dp[n]




if __name__=="__main__":
    print(Solution().climbStairs(2))