from typing import List
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minstack=[]



    def push(self, x: int) -> None:
        self.stack.append(x)
        if  self.stack or x<=self.minstack[-1]  :
            self. minstack.append(x)



    def pop(self) -> None:
        pop = self.stack.pop()

        if  pop==self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:
        return self.minstack[-1]





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()