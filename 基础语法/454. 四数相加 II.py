from collections import  Counter
from typing import  List
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

            countab=Counter([a+b for a in A for b in B])
            ans=0
            for c in C:
                for d in D:
                    if -(c+d) in countab:
                        ans+=countab[-(c+d)]
            return ans
if __name__ == '__main__':
    print(Solution().fourSumCount([1,2], [-2,-1],[-1,2],[0,2]))