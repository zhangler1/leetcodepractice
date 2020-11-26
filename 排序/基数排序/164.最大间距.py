from 排序.基数排序.最小位优先基数排序LeastSignificantDigitFirst import  Solution as sort
from  typing import  List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        sort().LsdRadixSort(nums)

        return max([nums[i]-nums[i-1] for i,num in enumerate(nums)if i>=1 ] )
if __name__ == '__main__':
    print(Solution().maximumGap([1,10000000]))
