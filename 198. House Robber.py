#key point is to know how the state transfering
class Solution:
    def rob(self, nums: list[int]) -> int:
        l=len(nums)
        dp=[0]*l
        if l<2:
            return nums[0]
        if l>=2:

            dp[0]=nums[0]
            dp[1]=max(dp[0],nums[1])
        for i in range(2,l):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])

        return dp[l-1]
if __name__ == '__main__':
    print(Solution().rob([2,7,9,3,1]))