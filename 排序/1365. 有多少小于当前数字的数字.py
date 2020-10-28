from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums.sort()
        return [nums.index(num) for num in nums]
