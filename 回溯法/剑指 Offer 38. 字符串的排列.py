from typing import  List
class Solution:
    def permutation(self, s: str) -> List[str]:
        #有哪些选择？
        #记录自己的选择
        #终结条件
        def dfs(ans:List[str],candidate:List[str],Path:List[str] =[]):
            #candidate的长度可以确定层次
            if len(candidate)==0:
                ans.append(tuple(Path.copy()))
                return

            for i, choice in enumerate(candidate):
                Path.append(choice)
                #不可以东canidate在循环呢
                newcan=candidate.copy()
                newcan.pop(i)
                dfs(ans,newcan,Path)
                Path.pop()
        ans=[]
        dfs(ans,list(s))
        return [ "".join(s) for s in set(ans)]



if __name__ == '__main__':
    print(Solution().permutation("abc"))