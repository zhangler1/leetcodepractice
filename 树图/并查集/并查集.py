#并查集并不属于一种表示数据本身相貌的结构，而是一种为了表示，关系而存在的数据结构，和图
#这种数据结构的功能上，并不重合。
#主要支持2种操作：1union 合并，就是把2树树根相连，使得其求根节点会结果相同。
# 2 find 查询某一个元素属于哪一个集合，一般来说可以用根节点表示。
#烦的第一个错误就是发现，并查集是disjoint集合的运算，这里遇到了对角线情况 ，有重复元素的话，就不是怎么表示了。
class UnionFindSet( ):
    def __init__(self,n) -> None:
        self.parent=[-1]*n

    def union(self,x:int,y:int):
        xroot=self.find(x)
        yroot=self.find(y)
        #需要在二者不一致时赋值，一致时说明是统一集合中，无需合并
        if xroot!=yroot:
            self.parent[xroot]=yroot
    def find(self,x:int):
        # 顺着路径找到根节点
        # 修改根节点
        path=[]
        while(self.parent[x]!=-1):
            path.append(x)
            x=self.parent[x]
        #以根结束
        for node in path: #把路径上的每一个节点的父节点均设置为，
            self.parent[node]=x
        return x


