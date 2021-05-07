class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result=0
        a=0
        b=0
        for x in nums:
            b=~a&~b&x| ~a&b&~x
            a=~a&~b&x| a&~b&~x
        return b

if __name__ == '__main__':
    print(Solution().singleNumber([2,2,3,2]))