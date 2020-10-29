# 给你一个整数数组
# arr，请你帮忙统计数组中每个数的出现次数。
#
# 如果每个数的出现次数都是独一无二的，就返回
# true；否则返回
# false。
#
#
#
# 示例
# 1：
#
# 输入：arr = [1, 2, 2, 1, 1, 3]
# 输出：true
# 解释：在该数组中，1
# 出现了
# 3
# 次，2
# 出现了
# 2
# 次，3
# 只出现了
# 1
# 次。没有两个数的出现次数相同。
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if not arr:
            return False
        chartimes={}
        for char in arr:
            chartimes[char]=chartimes.get(char,0)+1
        times={}
        for key,value in chartimes.items():
            if not chartimes in times:
                times[value]=key
            else:
                return False
        return True
