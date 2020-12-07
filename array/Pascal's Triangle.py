from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            ans.append([1]*(i+1))
            if i>0:
                for j in range(1,i):
                    ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
        return ans
if __name__ == '__main__':
    print(Solution().generate(5))
