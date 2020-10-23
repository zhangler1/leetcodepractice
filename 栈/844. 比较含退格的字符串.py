from  collections import deque
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stacks=deque()
        stackt=deque()

        for _ in S:
            if _=="#" :
                if  len(stacks)!=0 :
                    stacks.pop()
            else:
                stacks.append(_)
        for _ in T:
            if _=="#" :
                if  len(stackt)!=0 :
                    stackt.pop()
            else:
                stackt.append(_)

        return stacks==stackt

print(Solution().backspaceCompare("ab#c",
"ad#c"))



