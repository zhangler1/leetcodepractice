class Solution:
    def minimumOperations(self, leaves: str) -> int:
        """

        :rtype: object

        """
        def isYellow(color:str):
            return int(color=="y")

        def isRed(color:str):
            return int(color=="r")

        n = len(leaves)
        dp=[[float("inf"),float("inf"),float("inf")] for _ in range(n)]


        dp[0][0]=isYellow(leaves[0]) #初始化状态矩阵

        i=1
        while(i<n):
            for j in [0,1,2]:
                dp[i][0]=dp[i-1][0]+ isYellow(leaves[i])
                dp[i][1]=min(dp[i-1][0]+isRed(leaves[i]),dp[i-1][1]+isRed(leaves[i]))
                dp[i][2]=min(dp[i-1][1]+isYellow(leaves[i]),dp[i-1][2]+isYellow(leaves[i]))
            i=i+1

        return dp[n-1][2]

print(Solution().minimumOperations("rrryyyrryyyrr"))


