from 链表.链表双向.双向链表 import DLinkedList
class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.length=0
        self.cache:DLinkedList=DLinkedList([])
        self.map={}


    def get(self, key: int) -> int:
        if key in self.map:
            val=self.cache.pop(self.map[key])
            self.map[key]=self.cache.insert(0,val) #明明换了节点（舍弃原来的几点）却没有更新映射表里面的值
            return val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:           #重复键值的加入时最让我恶心的！！！！！！！！！！！！
            self.cache.pop(self.map[key])
            self.map[key]=self.cache.insert(0,(key,value))#映射上链接 最让我高兴的事 这里其实引用，返回的节点，链接没有变。

        elif self.length<self.capacity:
            self.length +=1
            self.map[key]=self.cache.insert(0,(key,value))#映射上链接
        else:
            self.map.__delitem__(self.cache.pop()[0])  #删除最后一个节点的映射
            self.map[key]=self.cache.insert(0,(key,value))

if __name__ == '__main__':
    def do (funcs,args):
        for fun,arg in zip(funcs,args):
            if fun=="LRUCache":
                cache=LRUCache(*arg

                )
            if fun=="get":
                print(cache.get(*arg))
            if fun == "put":
                cache.put(
                    *arg
                )


func= ["LRUCache","put","put","get","put","get","get"]


args=[[2],[2,1],[1,1],[2],[4,1],[1],[2]]
do(func,args)