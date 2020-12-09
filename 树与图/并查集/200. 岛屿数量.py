#1点解决方案 ，第一传统并查集使用一维数组，这里可以将2维数组转化成一维数组
#2 这里可以使用，十字星扫描法扫描 “地图 ”从而获得最佳的效果。
#3 因为，并查集初始要求，不相邻集合，本题中，0代表无岛屿，1代表“孤立的岛屿” ，将parent数组中，孤立岛屿初始化为-2，无岛屿初始化为-1

from typing import List
from 树与图.并查集.并查集 import UnionFindSet
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:



        rows=len(grid)
        cols=len(grid[0])
        union = UnionFindSet(rows*cols) #为每个岛屿的点确立一个位置
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    union.parent[(row)*cols+col]=-2 #-2表示无节点，同时修改并查集，使得停止条件从x！=-1到x》=0
                    #这里应该是row*列的数量而不是行
        for row in range(rows):
            for col in range(cols):
                for dir in [( -1,0),(1,0),(0,-1),(0,1)] :
                  drow=row+dir[0]
                  dcol=col+dir[1]
                  if drow<rows and 0 <=drow and dcol<cols and dcol>=0:#说明没有出界，这里命名为南十字星方法
                      if grid[row][col]=="1" and grid[drow][dcol]=="1":
                          union.union(cols*(row)+col,cols*(drow)+dcol)

        return union.parent.count(-2)




if __name__ == '__main__':
    print(Solution().numIslands(grid = [["1"],["1"]]
))
