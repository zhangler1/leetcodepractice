from typing import List
from functools import reduce
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        charset= reduce(lambda x,y:x.intersection(y),[set([char for char in str] ) for str in A ])
        minnumofChar={}
        if len(charset)==0:
            return
        for str in A:
            charnumset = {}
            for char in str:
                if char in charset:
                    charnumset[char]=1+charnumset.get(char,0)
            for key in charset:
                if charnumset[key]<minnumofChar.get(key,float("inf")):
                    minnumofChar[key]=charnumset[key]
        x=[[key for a in range(value)] for key, value in minnumofChar.items()]

        return          reduce(lambda x, y: x+y, x)


if __name__ == '__main__':
    A=["bella", "label", "roller"]

    print(    Solution().commonChars(A))
