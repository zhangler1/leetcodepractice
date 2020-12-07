from typing import  List


#二分查找分两种
def binarySearch(nums: List[int], target: int, leftside=True):
    # 因为本次输出用到了数组所以会出现数组越界的情况

    if len(nums) == 0:
        return -1

    left = 0
    right = len(nums)#用了多一位 过while时直接跳出
    if not leftside:
        while (left < right):
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid
            elif nums[mid] <= target:
                left = mid+1    #使用mid+1是因//2的特性总是向下偏转
        if left-1>=0 and nums[left-1] == target:
            return left-1
        else:
            return -1
    else:
        while (left < right):
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if right< len(nums) and nums[right] == target:   #因为使用了right所以要格外关注所以说关注一点
            return right
        else:
            return -1

from 二分查找.Bisect import bisect_left,bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [binarySearch(nums, target), binarySearch(nums, target, False)]



# from 二分查找.Bisect import bisect_right,bisect_left
# #官方对于不存在元素的查找非常马虎 天啊
if __name__ == '__main__':
    print(Solution().searchRange([31,3],3))

