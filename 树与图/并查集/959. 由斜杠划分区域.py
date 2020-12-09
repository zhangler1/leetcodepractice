#1. 本来想到了多重划分，可是迟疑了，不知道怎么表示，但实际上也就是数组，相互关系一定可以通过数学来表示的
#2. 对一个对角线格子，顺序编号0-3 ，然后依次处理，相邻的格子关系，以及内部由于划线而形成的关系。
#3. 最后形成的大并查集非常容易解决划分几块的问题。
from 树与图.并查集.并查集 import UnionFindSet
from  typing import List
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
         edgeMap={1:3,2:0,3:1,0:2}#建立一个边的映射关系
         n=len(grid)
         ufset=UnionFindSet(n**2*4)
         for row in range(n):
             for col in range(n):
                 cellbase=(row*n+col)*4
                 for i,dir in enumerate([(-1,0),(0,1),(1,0),(0,-1)]):#处理相邻的格子，方向错了好几次
                     drow=row+dir[0]
                     dcol=col+dir[1]
                     if drow>=0 and drow<n and dcol>=0 and dcol <n :
                         ufset.union((row*n+col)*4+i,(drow*n+dcol)*4+edgeMap[i])
                 if grid[row][col]==" ":#处理格子内部的关系
                     for i in range(0,4):#少做一次合并
                         ufset.union(cellbase,cellbase+i)
                 if grid[row][col]=="\\":#处理格子内部的关系
                     ufset.union(cellbase,cellbase+1)
                     ufset.union(cellbase+2,cellbase+3)
                 if grid[row][col]=="/":#处理格子内部的关系
                     ufset.union(cellbase,cellbase+3)
                     ufset.union(cellbase+1,cellbase+2)
         print()
         return ufset.parent.count(-1)
if __name__ == '__main__':
    print(Solution().regionsBySlashes( [" /", "/ "]))






