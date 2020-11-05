from  typing import  List
from math import  ceil,floor

from 二分查找.binarySearch import Solution as Search#给之前的写的程序写了一个别名
#要记住呀！！ 名字里面带点号的，包引入的时候回变得麻烦。
#对数组的操作最好是，新建立一个数组
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        all=[]
        for _ in intervals:
            for a in _:
               all.append(a)

        print(all)
        left=Search().search(all,newInterval[0])
        right=Search().search(all,newInterval[1])
        if floor(left)%2==0:
            if left==floor(left) :
                left+=1
            else:
                left=floor(left)
            leftval=all[left]
        else:
            left=ceil(left)
            leftval=newInterval[0]
        if floor(right)%2==0:
            if right==ceil(right):
                right+=1
            else:
                right=ceil(right)

            rightval=all[right]
        else:
            right=floor(right)
            rightval=newInterval[1]

        new=[]
        for i,a in enumerate(all):
            if i<left or i>right:
              new.append(a)
        new.insert(left,leftval)
        new.insert(left+1,rightval)
        return  [ list(k)for k in zip([_ for i,_ in enumerate(new) if i%2==0],[_ for i,_ in enumerate(new) if i%2!=0])]










if __name__ == '__main__':
    print(Solution().insert( [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8] ))
