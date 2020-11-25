#字符串操作要用replace

class Solution:
    def sortString(self, s: str) -> str:
        barrel=[0 for _ in range(26)]
        for char in s:
            barrel[ord(char)-97]+=1
        result=[]
        while(len(result)!=len(s)):
            for i,char in enumerate(barrel):
                if char>0:
                    barrel[i]-=1
                    result.append(chr(i+97))
            for i,char in enumerate(reversed(barrel)):
                if char>0:
                    barrel[25-i]-=1
                    result.append(chr(25-i+97))
        return result

if __name__ == '__main__':
    print(Solution().sortString(s= "aaaabbbbcccc"))