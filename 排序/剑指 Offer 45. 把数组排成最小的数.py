from typing import List, Text
#今天终于学会了如何比较了

class compare2(str):

    def __lt__(self, x: Text) -> bool:
        return int(self+x)< int(x+self)


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums.sort(key=compare2)
        return "".join([str(a )for a in nums])






    #     输入:
    # 输出: "3033459"
if __name__ == '__main__':
    print(Solution().minNumber([3,30,34,5,9]))