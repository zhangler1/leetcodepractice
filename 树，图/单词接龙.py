from collections import deque
from typing import Mapping
from typing import List
from collections import defaultdict
class Solution:
    nodenum=0
    wordid={}
    edge=defaultdict(list)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #建设图
        def addnode(word:str): #既可以把所有的字符转换成编号
            if word not in  Solution.wordid: #对于字典可以直接in 啊
                Solution.wordid[word]=Solution.nodenum
                Solution.nodenum+=1

        def addedge(word:str):#原本是要一对对测试变的，现在变成了对于每一个节点加边。
            addnode(word)
            for char in word:
                tem=word
                tem=tem.replace(char,"*")
                addnode(tem)
                Solution.edge[Solution.wordid[word]].append(Solution.wordid[tem])
                Solution.edge[Solution.wordid[tem]].append(Solution.wordid[word])

        for word in wordList:
            addedge(word)

        addedge(beginWord)
        if endWord not in wordList:
            return 0
        dis=[float("inf")]*Solution.nodenum  #建立数字，逐步更新距离，同时十分关键的：用这个判断是否见过这个节点
        dis[Solution.wordid[beginWord]]=0   #初始只有到自己的距离是最短的

        queue=deque()
        queue.append(Solution.wordid[beginWord])
        while(len(queue)!=0): #可以不管只要遇到即可
            curNodeId=queue.popleft()
            if Solution.wordid[endWord]==curNodeId:
                return dis[curNodeId]/2+1

            for edgenode in Solution.edge[curNodeId]:
                    if dis[edgenode]==float("inf"):#，用大的初值作为初始值，表示第一次赋值
                        dis[edgenode]=dis[curNodeId]+1
                        queue.append(edgenode)#第一次来才会登录，用距离来判定是否登录过
        return 0#搜索不到
if __name__ == '__main__':
    print(Solution().ladderLength("hot",
    "dog" ,
    ["hot","dog"]))