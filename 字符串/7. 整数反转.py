class Solution:
    def reverse(self, x: int) -> int:
         num=int("".join([char for char in reversed(str(abs(x)))]))
         if x<0:
             num=-num
         v_max = 0xffffffff / 2  #32位有符号数 最大是 2的31（32-1符号位）次方-1
         if num > (v_max - 1) or num < (v_max * (-1)):
             num = 0
         return  num
if __name__ == '__main__':
    print(Solution().reverse(1534236469))
