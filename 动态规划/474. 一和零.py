# 在计算机界中，我们总是追求用有限的资源获取最大的收益。
#
# 现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
#
# 你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ones-and-zeroes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
strs=["10","0001","111001","1","0"]
m=5
n=3
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[ 0  for _ in range(n+1)]for _ in range(m+1)]

        for word in strs:
            w0 = word.count("0")
            w1=word.count("1")

            for i in range(m,-1,-1):
                for j in range(n,-1,-1):
                    if i>=w0 and j>=w1:
                        dp[i][j]=max(dp[i-w0][j-w1]+1,dp[i][j])
        return dp[m][n]

print(Solution().findMaxForm(strs,m,n))
                        
