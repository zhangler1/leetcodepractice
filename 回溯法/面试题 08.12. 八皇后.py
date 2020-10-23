from  typing import  List
from math import log
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(ans,numOfQueen:int,board:List[List[str]]=[],column:int=0,columins:int=0,diagonal1:int=0,diagonal2:int=0,hierachy:int=0):
            if hierachy==numOfQueen:
                ans.append(board.copy())
                return

            if column!=-1:
                column=2**column
                diagonal1=(((column<<1)-2**(numOfQueen-1) if (column<<1 >2**(numOfQueen)) else column<<1 )|diagonal1<<1) #界定范围也是，大于2**n这减去x**n-1
                diagonal2=column>>1|diagonal2>>1 #忘记了diagonal也要移动位置
                columins=columins|column
            constrain=columins|diagonal2|diagonal1

            for col in range(numOfQueen):
                if 2**col&constrain==0:
                    board.append("".join([ "Q" if a==col else "." for a in range(numOfQueen)]) )
                    dfs(ans,numOfQueen,board,col,columins,diagonal1,diagonal2,hierachy+1)
                    board.pop()

        ans=[]
        dfs(ans,n,column=-1)
        return ans
if __name__ == '__main__':
    print(Solution().solveNQueens(5))




            

