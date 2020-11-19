from typing import List
class Solution(object):
    def isMonotonic(self, A):
      return  all([A[i]<=A[i+1] for i in range(0,len(A)-1)]) or        all([A[i]>=A[i+1] for i in range(0,len(A)-1)])
if __name__ == '__main__':
    print(Solution().isMonotonic([1,2,2,3]))



