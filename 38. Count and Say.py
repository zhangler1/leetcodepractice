class Solution:
    def countAndSay(self, n: int) -> str:
        o="1"
        for i in range(1,n):
            moto=''
            count=0
            newstr=''
            for c in o:
                if moto==c:
                    count=count+1
                else:
                    if count!=0:
                        newstr+=str(count)+moto
                    count=1
                    moto=c
            newstr+=str(count)+moto
            o=newstr
        return o
if __name__ == '__main__':
    print(Solution().countAndSay(1))








