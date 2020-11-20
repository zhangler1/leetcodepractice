from typing import  List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left=0
        right=len(nums)
        while(left<right):
            mid=(left+right)//2
            if mid==nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return mid
        #TODO 此情况有点复杂下回再继续弄


if __name__ == '__main__':
    print( Solution().missingNumber( [0,1,2,3,4,5,6,7,9]))