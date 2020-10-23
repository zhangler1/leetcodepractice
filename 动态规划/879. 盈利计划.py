# 帮派里有 G 名成员，他们可能犯下各种各样的罪行。
#
# 第 i 种犯罪会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。
#
# 让我们把这些犯罪的任何子集称为盈利计划，该计划至少产生 P 的利润。
#
# 有多少种方案可以选择？因为答案很大，所以返回它模 10^9 + 7 的值。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/profitable-schemes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
G = 5
P = 3
group = [2,2]
profit = [2,3]
from typing import List
class Solution1:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:

        n=len(group)
        psum=sum(profit)
        if P>psum:
            return 0

        dp=[[ 0 for p in range(psum+1)]for g in range(G+1)]
        for g in range(G+1):
            dp[g][0]=1

        for i in range(n):
            if group[i]>G:
                continue
            for g in range(G,group[i],-1):
                for p in range(psum,profit[i],-1):
                        dp[g][p]=(dp[g-group[i]][p-profit[i]]+dp[g][p])% 1000000007
        return  sum(dp[G][P:])%(1000000007)
class Solution2:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        # 初始化dp表，表第0行初始化为1
        dp = [[1] * (G+1)] + [[0] * (G+1) for _ in range(P)]# 注意这里实际有P+1行哦哦哦
        n = len(group)
        # 全任务遍历
        for i in range(n):
            # 针对每项任务，全局更新每种target，cost组合
            # 自底向上，采用原地更新
            for target in reversed(range(P+1)):
                # 由于cost不能小于0，意味着超员，所以cost>=group[i]
                for cost in reversed(range(group[i], G+1)):
                    # profit可以小于0，意味着超额收益，将所有超额都归结至profit=0,在这里target和之前的定义完全不同了，至少为负数的项目合并了。
                    # 所以最后就是dp[-1][-1]而我自己之前就是sum（dp[s][p:]）,仅仅因为定义不同。
                    dp[target][cost] += dp[max(0,target-profit[i])][cost-group[i]]
        return int(dp[-1][-1]%1000000007)
print(Solution2().profitableSchemes(G = 5, P = 3, group = [2,2], profit = [2,3]))
        

        
