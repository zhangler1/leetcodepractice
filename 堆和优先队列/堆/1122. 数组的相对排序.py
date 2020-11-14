from typing import List
import heapq
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        heap=[]
        n=len(arr2)
        numtolevel={}
        for i,_ in enumerate(arr2):#建立数字到level的映射表
            numtolevel[_]=n-i

        #通过映射表来得到arr1中数字的优先级,考虑正常优先级别n-i属于（1,6），给默认值0

        arr1withLevel=[((-numtolevel.get(a,0),a),a)  for a in arr1]

        for item in arr1withLevel:
            heapq.heappush(heap,item)

        ans=[]
        while(len(heap)!=0):
            ans.append(heapq.heappop(heap)[1])

            
        return ans

if __name__ == '__main__':
    print(Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19] ,
    [2,1,4,3,9,6]))
            
        