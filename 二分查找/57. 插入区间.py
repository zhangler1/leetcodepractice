from  typing import  List
from math import  ceil,floor

from 二分查找.binarySearch import Solution as Search#给之前的写的程序写了一个别名
#要记住呀！！ 名字里面带点号的，包引入的时候回变得麻烦。
#对数组的操作最好是，新建立一个数组
#大脑负担而来一个超级序数公式，还要表示一个数学范围，实际上并不能完成，一步步完成可好？ 集中体现了我编程数学能力的欠缺

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left=newInterval[0]
        right=newInterval[1]
        last=-1
        ans=[]
        for i,interval in enumerate(intervals):
            ileft=interval[0]
            iright=interval[1]
            if iright<left or ileft>right:
                ans.append([ileft,iright])
                if iright<left :
                    last=i #最后插入位置
            else:
                left=min(left,ileft)
                right=max(right,iright)
        ans.insert(last+1,[left,right])
        return ans
if __name__ == '__main__':
    print(Solution().insert( [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8] ))
