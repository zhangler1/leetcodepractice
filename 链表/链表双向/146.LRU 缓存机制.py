from 链表.链表双向.双向链表 import DLinkedList
class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.length=0
        self.cache:DLinkedList=DLinkedList()
        self.map={}


    def get(self, key: int) -> int:



    def put(self, key: int, value: int) -> None:
        if self.length<=self.capacity:
            self.cache.insert(0,value)

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



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)