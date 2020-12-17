from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        unhold=[0]*(n)
        hold=[0]*(n)
        hold[0]=unhold[0]-prices[0]-fee
         #要过一天买卖才有意义
         #股票价格是当天的
        #初始情况单独处理
        for i,price in enumerate(prices):
            if i>0:
                hold[i]=max(unhold[i-1]-prices[i]-fee,hold[i-1])
                unhold[i]=max(unhold[i-1],hold[i-1]+prices[i])
        return unhold[n-1]

if __name__ == '__main__':
    print(Solution().maxProfit([1, 3, 2, 8, 4, 9],2))
            
