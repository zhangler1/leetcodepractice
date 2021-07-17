import bisect
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l=bisect.bisect_left(nums,target)
        r=bisect.bisect_right(nums,target)
        return r-l
