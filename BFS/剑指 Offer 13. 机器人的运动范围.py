from collections import  deque
from typing import Tuple


class point(tuple):#写了一个新类继承了tuple

    def __le__(self, x: Tuple[float, ...]) -> bool:
        return self[0]<=x[0] and self[1]<=x[1] #重写比较函数
    def accecc(self):
        return  sum([int(char) for char in str(self[0])+str(self[1])])

    def __add__(self, x: Tuple[float, ...]) -> Tuple[float, ...]:
        return point((self[0]+x[0],self[1]+x[1]))# 要返回point类的对象。


class Solution:

    def movingCount(self, m: int, n: int, k: int) -> int:
         queue=deque()
         queue.append(point((0,0)))
         ans= set()
         ans.add(point((0,0)))
         while(len(queue)!=0):
             p=queue.pop()
             for dir in [(0,1),(1,0)]:
                 newp:point=p+point(dir)
                 # 很关键原本用了newp in queue这个条件，但是实际上有东西会重复弹出，不能完整代表答案，会出错
                 if newp<=point((m-1,n-1)) and not newp in ans and newp.accecc()<=k :
                     ans.add(newp)
                     queue.append(newp)
         return len(ans)#用集合来去重
if __name__ == '__main__':
    print(Solution().movingCount(3,2,17))



        