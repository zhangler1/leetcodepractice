from typing import  List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        even=len(nums)-1
        odd=0
        while(odd<even):
            while odd<even and nums[odd]%2!=0:
                odd+=1
            while odd<even and nums[even]%2==0:
                even-=1
            nums[odd],nums[even]=nums[even],nums[odd]
        return nums

if __name__ == '__main__':
    print(Solution().exchange([2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1]))
