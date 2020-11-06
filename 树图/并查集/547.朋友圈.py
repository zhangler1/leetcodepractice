#并查集并不属于一种表示数据本身相貌的结构，而是一种为了表示，关系而存在的数据结构，和图
#这种数据结构的功能上，并不重合。
#主要支持2种操作：1union 合并，就是把2树树根相连，使得其求根节点会结果相同。
# 2 find 查询某一个元素属于哪一个集合，一般来说可以用根节点表示。
#烦的第一个错误就是发现，并查集是disjoint集合的运算，这里遇到了对角线情况 ，有重复元素的话，就不是怎么表示了。
from  typing import List
from  树图.并查集.并查集 import UnionFindSet
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        disjointSets=UnionFindSet(len(M))
        if not M:
            return 0
        for row in range(len(M)):
               for col in range(row+1,len(M)):
                  if M[row][col]==1:
                        disjointSets.union(row,col)
        return disjointSets.parent.count(-1)



if __name__ == '__main__':
    print(Solution().findCircleNum([[1,1,1],[1,1,1],[1,1,1]]))