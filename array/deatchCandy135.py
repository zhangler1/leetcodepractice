from  typing import List

#受困于双边依赖 首先想的还是逐渐解决
#这次试求最小值 将两个依赖分别拆开解决！！！
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        left=[0]*n
        for i in range(n):
            if i>0 and ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
            else:
                left[i]=1

        right=ret=0
        for i in range(n-1, -1, -1):
            if i<n-1 and ratings[i]>ratings[i+1]:
                right+=1
            else:
                right=1
            ret+=max(left[i], right)

        return ret
if __name__ == '__main__':
    print(Solution().candy([1,0,2]))