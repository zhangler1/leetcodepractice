from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        setA=[0 for _ in range(len(nums))]
        setB=[0 for _ in range(len(nums))]
        n=len(nums)
        nums.sort(reverse=True)
        for i,num in enumerate(nums):
             if (abs(setA[i-1]+num-setB[i-1])<abs(setB[i-1]+num-setA[i-1])) :
                 setA[i] = setA[i - 1] + num
                 setB[i] =setB[i-1]
             else :
                 setB[i] =setB[i-1] +num
                 setA[i]=setA[i-1]


        return setA[n-1]==setB[n-1]
        

print(Solution().canPartition([1, 5, 11, 5]))


