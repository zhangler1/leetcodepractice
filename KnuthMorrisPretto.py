class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def KMP(objstr:str,sub:str):
            if sub=="":
                return 0
            if len(sub)<2:
                for i,a in enumerate(haystack):
                    if a==sub:
                        return i
                return -1
            next=[0]*len(sub)
            def getnext(sub:str):
                next[0]=0
                next[1]=0
                j=0
                i=2
                while (i<len(sub)) :
                    if sub[i-1]==sub[j]:
                        next[i]=j+1
                        i+=1
                        j+=1
                    elif j!=0:
                       j=next[j]
                    else:
                        next[i]=0
                        i+=1
            getnext(sub)

            i=0
            j=0
            while(i-j<=len(objstr)-len(sub)):
                if objstr[i]==sub[j]:
                    if j==len(sub)-1:
                        return  i-j
                    i+=1
                    j+=1
                elif j!=0 :j=next[j]
                else:
                    i+=1
            return -1
        return KMP(haystack,needle)

if __name__ == '__main__':
    print(Solution().strStr("aabaaabaaac"  ,
    "aabaaac"))


