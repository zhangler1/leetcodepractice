class Solution:
    def isHappy(self, n: int) -> bool:
        se=set()
        while(True):
            s=sum([int(i)**2 for i in str(n)])
            if s==1:
                return True
            elif s in se:
                return False
            n=s
            se.add(s)



if __name__ == '__main__':
    print(Solution().isHappy(19))