from  typing import List,Any,NoReturn
from math import log,floor,log10
class Solution():
    def LsdRadixSort(self,arr:List[int])->NoReturn:
        barrels=[[] for a in range(10)]
        digits=floor(log10(max(arr)))+1
        for digit in range(digits):
            #distrbution
             for i,num in enumerate(arr):
                 for time in range(digit):
                    num//=10
                 barrels[num%10].append(arr[i])
            #collection
             arr.clear()
             for i in range(10):

                arr.extend(barrels[i]) #append有那种趋势，一般人没有
                barrels[i].clear()
        return arr
if __name__ == '__main__':
    print(Solution().LsdRadixSort([1,1000000]))






