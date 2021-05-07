class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        avg=round(sum(nums)/n)

        return sum(map(lambda x:abs(x-avg),nums))

if __name__ == '__main__':
    print(Solution().minMoves2([1,2,10]))