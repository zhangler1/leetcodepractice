class CQueue:

    def __init__(self):
        self.firstStack=[]
        self.secondStack=[]
        


    def appendTail(self, value: int) -> None:
        self.firstStack.append(value)



    def deleteHead(self) -> int:
        if len(self.secondStack)!=0:
            return self.secondStack.pop()
        else:
            if len(self.firstStack)!=0:
                for a in self.firstStack.copy():

                    self.secondStack.append(self.firstStack.pop())

                return self.secondStack.pop()
            else:
                return -1
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()