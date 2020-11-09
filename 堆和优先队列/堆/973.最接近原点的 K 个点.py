# 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
#
# （这里，平面上两点之间的距离是欧几里德距离。）
#
# 你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。
#先使用最小堆反转试试看
import heapq
import math
from typing import List
from typing import  Tuple
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def EuclidDistance(x:Tuple[complex,complex],y:Tuple[complex,complex]=(0,0)):
            return math.sqrt((x[0]-y [0])**2+(x[1]-y [1])**2)
        heap=[]


        for p in points:
            heapq.heappush(heap,(-EuclidDistance(tuple(p)),p))
        while(len(heap)!=K):
            heapq.heappop(heap)
        # for p in points:
        #     heapq.heappush(heap,(EuclidDistance(tuple(p)),p))
        #
        #
        #
        # return  [heapq.heappop(heap) for i in range(K)]
        return [t[1] for t in heap]





if __name__ == '__main__':
    print(Solution( ).kClosest( [[3,3],[5,-1],[-2,4]],
    2))



