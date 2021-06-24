from typing import List
import heapq
from  collections import  defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
          numToHeap=defaultdict(list)
          for num in nums:
                  if len(numToHeap[num-1])!=0:
                      q=heapq.heappop(numToHeap[num-1])+1
                      heapq.heappush(numToHeap[num],q)
                  else:
                      heapq.heappush(numToHeap[num],1)
          for num in numToHeap:
              if len(numToHeap[num])!=0:
                 if  heapq.heappop(numToHeap[num])<3:
                     return False
          return True




if __name__ == '__main__':
    print(Solution().isPossible([1,2,3,3,4,5] ))

                               

