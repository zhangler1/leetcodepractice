#use 分类的方法 变成而来可以解决的问题 nice啊综合起来还是分类的思想 和计数的分类分步思想一样，加法 （不重复 不遗漏）乘法（步骤之后数量相同） 原理 ，
# 减法（反向求补容易时思考） 除法（方法数量对应 如环排列=排列/环的长度）。
class Solution:
    def rob(self, nums: list[int]) -> int:
        l=len(nums)
        dp=[0]*l
        dp2=[0]*l
        dp[0]=nums[0]
        dp2[0]=0
        if l>=2:
            dp[1]=max(nums[1],nums[0])
            dp2[1]=max(dp2[0],nums[1])
        for i in range(2,l-1):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        for i in range(2,l):
            dp2[i]=max(dp2[i-1],dp2[i-2]+nums[i])
        return max(dp[l-2],dp2[l-1])

if __name__ == '__main__':
    print(Solution().rob([2,3,2]))
