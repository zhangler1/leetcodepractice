# 509. 斐波那契数
# 斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
from typing import Dict
class Solution:
    def fib(self, N: int) -> int:
        dp={0:1,1:1}
        return self.f(N,dp)
    def f(self,N:int,dp:Dict[int,int])->int:
        if N in dp.keys():
            return dp[N]
        else:
            return Solution().f(N-1,dp) +Solution().f(N-2,dp)

if __name__=="__main__":
    print(Solution().fib(20))

