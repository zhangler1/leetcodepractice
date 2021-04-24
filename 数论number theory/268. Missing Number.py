class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        return  int(n*(n+1)/2-sum(nums))

if __name__ == '__main__':
    print(Solution().missingNumber([3,0,1]))