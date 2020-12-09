#给字母排数字，可以用-“a“法

from typing import List
from 树与图.并查集.并查集_哈希版本 import UnionFindSet
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equals=[e for e in equations if e[1]=="="]
        notequals=[e for e in equations if e[1]=="!"]

        unionset=UnionFindSet()
        for equaltion in equals:
            x=equaltion[0]
            y =equaltion[3]
            unionset.union(x,y)

        for equaltion in notequals:
            x=equaltion[0]
            y =equaltion[3]
            if unionset.find(x)==unionset.find(y):
                return False
        return True

if __name__ == '__main__':
    print(Solution().equationsPossible(["a==b","b==c","a==c"]))
