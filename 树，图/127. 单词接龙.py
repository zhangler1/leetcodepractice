import collections
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum #给单词编号，你仔细想想，平常编号不都是节点号么  ，这样才能矩阵运算
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)  #增加本命节点
            id1 = wordId[word]
            chars = list(word)                         #分解成字符串了，用list
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord) #增加虚拟节点
                id2 = wordId[newWord]
                edge[id1].append(id2)    #增加各种临边
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)         #起始的目标也需要添加入数据结构
        if endWord not in wordId:  #如果目标不在最终目标中说明不可达
            return 0

        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]#转换成id
        dis[beginId] = 0

        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)

        return 0
if __name__ == '__main__':
    print(Solution().ladderLength("hit",
    "cog" ,
    ["hot","dot","dog","lot","log","cog"]))

