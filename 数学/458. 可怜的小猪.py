n=1000
m=15
p=60
import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
         status=minutesToTest//minutesToDie+1
         n= math.log(buckets,3)/math.log(status,3)
         return math.ceil(n)



print(Solution().poorPigs(n,m,p))