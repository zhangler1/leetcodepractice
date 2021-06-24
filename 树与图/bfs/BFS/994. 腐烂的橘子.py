from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
            # 统计信息
            if not grid or not grid[0]:
                return 0

            rotOrrage=[]
            freshOrange=[]
            n=len(grid)
            m=len(grid[0])
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                     if grid[i][j]==2:
                         rotOrrage.append((i,j))#搜索现有的腐烂橘子
                     elif grid[i][j]==1:
                         freshOrange.append((i,j))
            num=len(freshOrange)#新鲜橘子树
            curq=deque()
            nextq=deque()
            curq.extend(rotOrrage)#很好位置的信息

            time=0
            while (len(curq)!=0):
                rotloc=curq.pop()
                for direct in [(-1,0),(0,1),(1,0),(0,-1)]:
                    x=rotloc[0]+direct[0]
                    y= rotloc[1]+direct[1]
                    if x<n and x >=0 and y <m and y>=0 and grid[x][y]==1:
                        nextq.append((x,y))
                        grid[x][y]=2
                        num-=1
                if len(curq)==0 and len(nextq)!=0:
                    curq=nextq
                    nextq=deque()
                    time+=1
            if num>0:
                return -1
            else:
                return time
        
if __name__ == '__main__':
    print( Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))


