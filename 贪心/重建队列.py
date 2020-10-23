

people=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
from typing import List
from inspect import signature
class Solution:
    def reconstrucQueue(self,people:List[List[int]])-> List[List[int]]:
        people.sort(key=lambda a:(-a[0],a[1]))
        new=[]
        for a in people:
            new.insert(a[1],a)
        return new



print( Solution().reconstrucQueue(people) )

        
