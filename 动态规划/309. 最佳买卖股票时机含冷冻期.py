from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        empty=[a for a in  range(n)]
        hold=[a for a in  range(n)]
        empty_freezre=[a for a in  range(n)]
        empty[0]=0
        hold[0]=empty[0]-prices[0]
        empty_freezre[0]=hold[0+prices[0]]

        i=1
        while(i<n):
            empty[i]=max(empty[i-1],empty_freezre[i-1])
            empty_freezre[i]=hold[i-1]+prices[i]
            hold[i]=max(hold[i-1],empty[i-1]-prices[i])
            i=i+1

        return max(empty[n-1],empty_freezre[n-1],hold[n-1])

print(Solution().maxProfit([1,2,3,0,2]))