# 编写一个程序判断给定的数是否为丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。
class Solution:
    def isUgly(self, num: int) -> bool:
        x,y,z=0,0,0
        if num==0:
            return False
        while(num%2==0):
            x+=1
            num/=2
        while(num%3==0):
            y+=1
            num/=3
        while (num % 5 == 0):
            z += 1
            num /= 5
        if num==1:
            return True
        else:
            return False




if __name__ == '__main__':
    print(Solution().isUgly(0))