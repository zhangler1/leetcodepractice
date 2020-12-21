"bcabc"
#2个关键点 1 单调栈其实就是只处理末尾的元素这里，未特别用到后进先出的关系，根据大小关系 ，
#               连续弹出（会受到不同的限制本题受到数量限制）
#        2 一开始思考时就被后面未知的信息所局限，存储是否见过，后未来是否有。
#       所以存货数组告诉自己是否可以继续弹出
#       vis告诉自己是否满足要求，a弹出其他时 改变vis数组让其他人再进入


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        def chartoidx(s: str):
            return ord(s)-ord("a")

        vis=set()
        stubnum=[0]*26
        for c in s:
            stubnum[ord(c)-ord("a")]+=1

        ans=[]
        for c in s:
            if not c in vis:  #havn't seen
                vis.add(c)
                while (ans!=[] and ans[len(ans)-1]>c and stubnum[chartoidx(ans[len(ans)-1])]>=1):
                    vis.remove(ans.pop())
                    #我把条件写到while里面了所以看起来不一样
                ans.append(c)
            stubnum[chartoidx(c)]-=1

        return ans
if __name__=='__main__':
    print(Solution().removeDuplicateLetters("bcabc"))
