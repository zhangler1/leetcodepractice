from typing import List
from functools import reduce
class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        dicf=dict()
        dicl=dict()
        for i,char in enumerate(S):
            if char in dicf:
                dicl[char]=i
            else:
                dicf[char]=i
        namelist=[]
        for key,value in dicf.items():
            namelist.append((key,value,dicl.get(key,value)))
        print(namelist)
        def func(x, y):

            if isinstance(x,List) :
                a=x
                x = a.pop()
            else:
                a=[]
            if x[2] >= y[1]:
                if x[2]>=y[2]:
                    a.append((x[0] + y[0], x[1], x[2]))
                else:
                    a.append((x[0] + y[0], x[1], y[2]))
            else:
                a.append(x)
                a.append(y)
            return  a

        return  [period[2]-period[1]+1 for period in reduce(func,namelist)]











if __name__ == '__main__':
    print(Solution().partitionLabels(S = "eccbbbbdec"))