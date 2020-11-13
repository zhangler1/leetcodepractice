from collections import  Mapping
class LRUCache:
 #主要是因为忘记了直接加入时也要替换之前已经出现过的key值
    def __init__(self, capacity: int):
        self.cache=[]
        self.index=0
        self.__capacite=capacity
        self.map= {}

    def get(self, key: int) -> int:
        if not key in self.map:
                return -1

        index=self.map[key]
        for row in self.cache:
            row[2] += 1
        self.cache[index][2]=0

        return self.cache[index][1]



    def put(self, key: int, value: int) -> None:
        if len(self.map)<self.__capacite:
            #todo let in
            for row in self.cache:
                row[2]+=1
            if key in self.map:
                replaceloc = self.map[key]
                self.map.__delitem__(self.cache[replaceloc][0])
                self.cache[replaceloc] = [key, value, 0]
                self.map[key] = replaceloc
            else:
                self.cache.append([key,value,0])
                self.map[key]=self.index
                self.index+=1



        else:
             #todo replace
             for row in self.cache:
                 row[2] += 1
             replaceloc=None
             if key in self.map:
                  replaceloc=self.map[key]
             else:
                 maxtime=max([row[2] for row in self.cache])

                 for i,row in enumerate(self.cache):
                     if row[2]==maxtime:
                         replaceloc=i
                         break

             self.map.__delitem__(self.cache[replaceloc][0])
             self.cache[replaceloc] = [key, value, 0]
             self.map[key]=replaceloc

def do (string,args):
    for char,arg in zip(string,args):
        if char=="LRUCache":
            cache=LRUCache(*arg)
        if char=="get":
            cache.get(*arg)
        if char=="put":
            cache.put(*arg)

if __name__ == '__main__':
    do(
        ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"],
        [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]])


