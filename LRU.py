from collections import l
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.cache={}
        self.lru=



    def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:
        if self.size<self.capacity:
            self.cache[key]=value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


