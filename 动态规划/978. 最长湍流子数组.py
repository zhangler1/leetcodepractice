# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：
#
# 若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
# 或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
# 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
#
# 返回 A 的最大湍流子数组的长度。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-turbulent-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
[9,4,2,10,7,8,8,1,9]
from typing import List
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A :
            return 0
        n=len(A)
        dp=[2 for _ in range(n)]
        def evenbig( A: List[int],k:int):
            return  int((A[k]>A[k-1]))!=bool((k%2))
        def oddbig( A: List[int],k:int):
            return  int((A[k]>A[k-1]))^(k%2)==0
        for i in range(2,n):
            if oddbig(A,i-1):
                if oddbig(A,i):
                    dp[i]=dp[i-1]+1

            else:
                if evenbig(A,i-1):
                    if evenbig(A, i):
                        dp[i]=dp[i-1]+1

        return dp[n-1]

if __name__ == '__main__':
    print(Solution().maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))



