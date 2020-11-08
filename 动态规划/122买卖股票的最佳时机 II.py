from typing import List
import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        empty = [0] * (len(prices)+1)
        hold = [0] * (len(prices)+1)
        empty[0] = 0
        emptyset=[""]* (len(prices)+1)  #    用于记录路径
        hold[0] = -prices[0]
        holdset=[""]* (len(prices)+1)   #   用于记录路径
        for i in range(1,len(prices)+1):
            empty[i]=max(empty[i-1],hold[i-1]+prices[i-1])
            mi=np.argmax((empty[i-1],hold[i-1]+prices[i-1]))
            emptyset[i]=("不买入\n"+emptyset[i-1],holdset[i-1]+f"卖出第{i}天股票\n")[mi]

            hold[i]=max(hold[i-1],empty[i-1]-prices[i-1])
            hi=np.argmax((hold[i-1],empty[i-1]-prices[i-1]))
            holdset[i]=("不买入\n"+holdset[i-1],emptyset[i-1]+f"买入第{i}天股票\n")[hi]

        print(emptyset[np.argmax(empty)])
        return max(empty)
if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
        