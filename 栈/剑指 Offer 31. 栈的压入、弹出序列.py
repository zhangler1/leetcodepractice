from typing import List
from collections import  deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
            if len(popped)!=len(pushed):
                return False
            push=deque(pushed)
            pop=deque(popped)
            stack=[]
            if len(push)==0 :
                return True
            stack.append(push.popleft())
            while(len(pop)!=0):
                if len(stack)!=0 and stack[-1]==pop[0]:
                    stack.pop()
                    pop.popleft()
                else:
                    if len(push)!=0:
                        stack.append(push.popleft())
                    else:
                        return False
            return True


if __name__ == '__main__':
    print(Solution().validateStackSequences([1,0],
    [1,0]))

