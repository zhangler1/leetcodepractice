#原地作用的函数，使用情况和以往不太一样，因为是用一次，就改变了变量，所以不支持连续运算，这一点请务必注意。
from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
            arr.sort()


            arr.sort(key=lambda x:bin(x).count("1"))
            return  arr
if __name__ == '__main__':
    print(Solution().sortByBits([0,1,2,3,4,5,6,7,8]))