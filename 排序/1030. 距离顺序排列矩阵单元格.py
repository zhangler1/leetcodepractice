#!!!!!!!!!!好省略号就是个字面值,只是他不想写全罢了，
#none既是一个类型有又是一个字面值
from  typing import  List
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int,l:...=...) -> List[List[int]]:
        def Manhattan (x,y):
           return  abs(x[0]-y[0])+abs(x[1]-y[1])

        ans=[[r,c]for c in range(C) for r in range(R)]
        ans.sort()

        ans.sort(key=lambda x: Manhattan(x, [r0, c0]))
        print(l)
        return  ans
if __name__ == '__main__':
    print(Solution().allCellsDistOrder(1,
    2,                                            0,
    0))

