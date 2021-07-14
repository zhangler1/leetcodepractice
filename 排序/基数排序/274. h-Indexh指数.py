from collections import  Counter
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        m=max(citations)
        counter=[0]*(m+1)
        for i in citations:
            counter[i]+=1
        h=0
        while(h<=m+1):
            if  sum(counter[h:])>=h:
                h += 1
            else:
                return h-1






if __name__ == '__main__':
    print(Solution().hIndex([0]))