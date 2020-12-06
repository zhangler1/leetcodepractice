from typing import  List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 输入: nums = [-1, 0, 3, 5, 9, 12], target = 9
        # 输出: 4
        # 解释: 9
        # 出现在+
        
        # nums
        # 中并且下标为
        # 4
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        pre=None
        while(left<=right):
            pre=mid
            if nums[mid]>target:
                right=mid-1
                mid=(left+right)//2
            elif nums[mid]<=target:
                left=mid+1
                mid=(left+right)//2
            else:
                return mid
        return (left+right)/2
if __name__ == '__main__':
    print(Solution().search([-1,0,3,5,9,12], 7))

