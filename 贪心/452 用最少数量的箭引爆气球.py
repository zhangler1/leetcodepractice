from typing import List, Tuple


class Point(tuple):

    def __lt__(self, x: Tuple[int,int]) -> bool:
        return self[0]<x[0]


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
          if not points:
              return 0
          
          points.sort(key=Point)
          left=0
          right=float("inf")
          ans=[]
          for point in points:
              if point[0] > right:
                  ans.append((left, right))
                  left = point[0]
                  right = float("inf")
              if point[0]>left:
                  left=point[0]
              if point[1]<right:
                  right=point[1]


          ans.append((left,right))
          return len(ans)



if __name__ == '__main__':
    print(Solution().findMinArrowShots([]))
