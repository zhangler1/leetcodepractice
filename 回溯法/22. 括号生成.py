from typing import List
class Solution:
# 经过我判断，因为只有一种括号不需要栈来 判定是否可以入栈。
# 双结束判断，否则很麻烦

    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(ans:List[str],path:list[int]=[],inTimes=0,outTimes=0):
            if inTimes > n:
                return
            if outTimes==n:
                ans.append("".join(path.copy()))
                return




            path.append("(")
            dfs(ans,path,inTimes+1,outTimes)
            path.pop()
            if inTimes>outTimes:
                path.append(")")
                dfs(ans, path, inTimes , outTimes+1)
                path.pop()
        ans=[]
        dfs(ans)
        return ans
if __name__ == '__main__':

    print(Solution().generateParenthesis(3))
