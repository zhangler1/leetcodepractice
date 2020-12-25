from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        num=0
        i=0
        for cookie in s:
            while (i<len(g)):
                if cookie>=g[i]:
                    num+=1
                    i+=1
                else:
                    break
        return num

if __name__=='__main__':
    print(Solution().findContentChildren([1, 2, 3], [1, 1]))
