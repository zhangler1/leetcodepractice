
#find的终结条件while（x！=xparent[x]）也可以使用，这样便于区别类别
from collections import defaultdict

class UnionFindSet():

    def __init__(self) -> None:
        self.parnets=defaultdict(int)
    def find(self,x:str):
        path=[]
        while(self.parnets[x]!=0):
            path.append(x)#注意顺序,如果不小心把终结标识覆盖掉了就完了
            x=self.parnets[x]

        for node in path:
            self.parnets[node]=x
        return x

    def union(self,x:str,y:str):
        xroot=self.find(x)
        yroot=self.find(y)
        if xroot!=yroot:
            self.parnets[xroot]=yroot
            return True
        else:
            return False