import heapq
class Solution:
    # region  bad smell of code :too many iterations and hav'ent latency dellete
    def getSkylineBadsmell(self, buildings: list[list[int]]) -> list[list[int]]:
        scanLineheap=[]
        heapq.heapify(scanLineheap)
        #Ο(N)的复杂度
        n= max([x[1] for x in buildings])+1

        ans=[]
        preheight=0
        for scanline in range(n):#Ο(N)的复杂度
            for ledge, redge,heifht in buildings:#Ο(N)的复杂度
                if scanline==redge:
                    scanLineheap.remove(-heifht)#O(nlogn)
                    heapq.heapify(scanLineheap)#O(nlogn)
                if scanline ==ledge:
                    heapq.heappush( scanLineheap,-heifht)#(nlogn)

            currentheight=scanLineheap[0] if scanLineheap!=[] else 0
            if currentheight!=preheight:
                ans.append([scanline,-currentheight])
            preheight=currentheight
        return ans
    # endregion
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        timelineheap=[]
        preskyline=0
        ans=[]
        border=[]
        for build in buildings:
            border.append(build[0])
            border.append(build[1])
        border=list(set(border))
        border.sort()

        for b in border:
            for l,r,h in buildings:
                if l==b:
                    heapq.heappush(timelineheap,(-h,r))
            while timelineheap!=[] and timelineheap[0][1]<=b:
                heapq.heappop(timelineheap)
            currentskyline=timelineheap[0][0]if timelineheap!=[]else 0
            if currentskyline!=preskyline:
                ans.append([b,-currentskyline])
            preskyline=currentskyline
        return ans





if __name__ == '__main__':
    print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))


