class Solution:
    def KMP(self,String:str,sub:str):
        next=[0*len(sub)]
        def getnext(sub:str):
            next[0]=0
            next[1]=0
            j=0
            i=2
            while (i<len(sub)) :
                if sub[i-1]==sub[j]:
                    next[i]=next[i-1]+1
                    i+=1
                    j+=1
                elif j!=0:
                   j=next[j]
                else:
                    next[i]=0
        return next

if __name__ == '__main__':
    print(Solution().KMP("abaacababcac","ababc"))


