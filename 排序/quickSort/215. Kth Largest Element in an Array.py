from random import  random,randrange
import heapq


class Solution:
    def findKthLargest1(self, nums: list[int], k: int) -> int:
        def partition(nums: list[int], l:int ,r: int) :
            x=nums[r]
            i=l
            for j in range(l,r):#j jump over big number while i can‘t
                if (nums[j]<=x):
                    nums[i],nums[j]=nums[j],nums[i]   #i indica last biger number than x
                    i+=1 # when swaped plus 1  ，usually i indic a bigernumber and run slower than j
            nums[i],nums[r]=nums[r],nums[i]     #swao pivot and last big number
            return i

        def partitial(nums:list[int],start:int=0,stop:int=len(nums)-1)->int:
            l=start
            r=stop
            p=randrange(start,stop+1)#random location of pivot
            nums[start],nums[p] = nums[p],nums[start]
            pivot=nums[start]
            while (l<r):
                while(r>l and nums[r]>=pivot) :
                    r-=1
                nums[l]=nums[r]
                while(r>l and nums[l]<pivot):
                    l+=1
                nums[r]=nums[l]
            nums[r]=pivot
            return r

        left=0
        right=len(nums)-1
        while(True):
            axis=partition(nums,left,right)
            if  len(nums)-axis>k:
                left=axis+1      #    VERY IMPOTANT
            if len(nums)-axis<k:
                right=axis-1      #
            if len(nums)-axis==k:
                break
        return nums[axis]
    def findKthLargest2(self, nums: list[int], k: int) -> int:
        heap=[[-a,a]for a in nums ]  #because python has implemented comp key functiong of list or tuple
        heapq.heapify(heap)
        for i in range(k):
            result=heapq.heappop(heap)
        return result[1]



if __name__ == '__main__':
    print(Solution().findKthLargest2(
        [3, 2, 1, 5, 6, 2] ,
    1))