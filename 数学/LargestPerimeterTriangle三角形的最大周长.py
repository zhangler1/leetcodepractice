from  typing import List
#细节是魔鬼啊，>=的细节也好
#既然是数组直接眼红range索引多好，非要乱搞
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A)-1,-1,-1):

            if i-2>=0 and A[i-1]+A[i-2]>A[i]:
                return   A[i-1]+A[i-2]+A[i]
        return 0
        

if __name__ == '__main__':
    print(Solution().largestPerimeter([2,1,2]))
