
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        num=[int(char)for char in str(N)]
        for i in range(len(num)-1,-1,-1):
            while(i>0):
                if num[i]<num[i-1]:
                    num[i-1]-=1
                    num[i:]=[9]* len(num[i:])
                else:


                    i-=1
        return int("".join([str(_) for _ in num]))
if __name__ == '__main__':
    print(Solution().monotoneIncreasingDigits(332))