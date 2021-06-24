from typing import  List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        zero=0
        noZero=0

        while zero<n and noZero<n:
            noZero=zero
            while zero<n and nums[zero]!=0:
                zero+=1
            while noZero <n and nums[noZero]==0:
                noZero+=1
            if zero!= n and noZero!=n:
                if zero<noZero:
                    nums[noZero],nums[zero]=nums[zero],nums[noZero]
                # else:
                #     break
        return nums
if __name__ == '__main__':
    print(Solution().moveZeroes([1,0,1]))