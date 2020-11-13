from math import factorial,comb,floor
class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if n==0:
            return 0
        if k==n**2:
            return 1
        methodNums=0
        for i in range(0,n):

            j=(k-n*i)/(n-i)
            if j==floor(j) and j<n and j>=0:
                methodNums+=comb(n,int(j))*comb(n,i)
        return methodNums
if __name__ == '__main__':
    print(Solution().paintingPlan(2,
    2))