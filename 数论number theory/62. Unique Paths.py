from math import comb
# select n-1 items from m+n-2
class Solution:#规定了只有2个方向，从直观上：不会出现循环引用。实际上：动态规划需要顺序
    def uniquePaths(self, m: int, n: int) -> int:
        return  comb(n-1,m+n-2)
