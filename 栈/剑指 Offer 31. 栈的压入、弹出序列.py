from typing import List
from collections import  deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
            if len(popped)!=len(pushed):
                return False
            push=deque(pushed)
            pop=deque(popped)
            stack=[]

            while(len(stack)!=0 or len(pop)!=0):

                if len(stack)==0 or stack[-1]!=pop[0]:
                    if len(push) != 0:
                        stack.append(push.popleft())
                    else:
                        return False  # 也许根本没有入这个数

                else: #相等
                    pop.popleft()
                    stack.pop()
            return True

if __name__ == '__main__':
    print(Solution().validateStackSequences([1,2,3,4,5],[4,3,5,1,2]))

