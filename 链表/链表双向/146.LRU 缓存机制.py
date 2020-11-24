from 链表.链表双向.双向链表 import DLinkedList
class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.length=0
        self.cache:DLinkedList=DLinkedList()
        self.map={}


    def get(self, key: int) -> int:
        if key in self.map:
            val=self.cache.pop(self.map[key])
            self.cache.insert(0,val)

    def put(self, key: int, value: int) -> None:
        if self.length<=self.capacity:

            self.map[key]=self.cache.insert(0,(key,value))#映射上链接
        else:

            self.map.__delitem__(self.cache.pop()[0])  #删除最后一个节点的映射
            self.map[key]=self.cache.insert(0,(key,value))

if __name__ == '__main__':
    def do (funcs,args):
        for fun,arg in zip(funcs,args):
            if fun=="LRUCache":
                cache=LRUCache(arg

                )
            if fun=="get":
                cache.get(arg)
            if fun == "put":
                cache.put(
                    arg
                )


func=["LRUCache","put","put","get","put","get","put","get","get","get"]
args=[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
do(func,args)