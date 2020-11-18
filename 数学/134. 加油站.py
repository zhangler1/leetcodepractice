from typing import List
class Solution:
#数组变环用取模
#用下标，索引不好确定的话，尝试使用长度，但需要2变量，一个基准一个长度
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
          n=len(gas)
          start=0
          p=0


          while start<n:
              gasStub = 0
              while(p<n):
                  gasStub+=gas[(start+p)%n]
                  gasStub-=cost[(start+p)%n]
                  if gasStub>=0:
                      p+=1
                  else:
                      break
              if p==n:
                  return start
              else:
                  start = (start+p+1) #这里不需要取余因为，它实际上很搞笑
                  p = 0
          return -1


if __name__ == '__main__':
           print(Solution().canCompleteCircuit([3,3,4], [3,4,4]))