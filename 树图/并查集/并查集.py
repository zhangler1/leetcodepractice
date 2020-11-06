#1.并查集并不属于一种表示数据本身相貌的结构，而是一种为了表示，关系而存在的数据结构，和图这种数据结构的功能上，并不重合。
#2. 主要支持2种操作：1union 合并，就是把2树树根相连，使得其求根节点会结果相同。
#3. find 查询某一个元素属于哪一个集合，一般来说可以用根节点表示。
#4. 需要在二者不一致时对根节点数组进行赋值，一致时说明是同一集合中，无需合并需判断下，因为很多关系因为双向的，所以会赋值2次
class UnionFindSet( ):
    def __init__(self,n) -> None:
        self.parent=[-1]*n

    def union(self,x:int,y:int):
        xroot=self.find(x)
        yroot=self.find(y)
        #需要在二者不一致时赋值，一致时说明是同一集合中，无需合并，因为很多关系因为双向的，所以会赋值2次
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


