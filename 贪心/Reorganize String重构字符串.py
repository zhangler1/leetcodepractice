import heapq
from collections import  defaultdict
class Solution:
    def reorganizeString(self, S: str) -> str:
        n=len(S)
        charset=defaultdict(int)
        for char in S:
            charset[char]+=1
        heap=[]
        for key in charset.keys():
            if charset[key]<=(n+1)//2:

                heapq.heappush(heap,(-charset[key],key))
            else:return ""
        i=0
        k=(n)//2
        s=[]
        while(i<k):
            a=heapq.heappop(heap)
            s.append(a[1])
            charset[a[1]]-=1
            b=heapq.heappop(heap)
            s.append(b[1])
            charset[b[1]]-=1
            if  charset[a[1]]>0:
                heapq.heappush(heap,(-charset[a[1]],a[1]))
            if  charset[b[1]]>0:
                heapq.heappush(heap,(-charset[b[1]],b[1]))
            i+=1
        if len(heap)!=0:
            s.append(heapq.heappop(heap)[1])
        return "".join(s)
if __name__ == '__main__':
    print(Solution().reorganizeString("abbabbaaab"))