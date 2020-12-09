class Solution:#规定了只有2个方向，从直观上：不会出现循环引用。实际上：动态规划需要顺序
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*m for _ in range(n)] # 因为列表*n是非常危险的举动
        for j in range(1,m):
            for i in range(1,n):
                 dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[n-1][m-1]
if __name__ == '__main__':
    print(Solution().uniquePaths(7,3))
