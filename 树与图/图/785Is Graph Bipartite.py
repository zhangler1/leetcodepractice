from collections import  deque
from enum import Enum
class Color(Enum):
    Uncolored = 0
    red=1
    black=2
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n=len(graph)
        color=[Color.Uncolored]*n  #use a 数组array to indicate properties of graph vertex
        valid:bool=True # use a singnal to indicate whether to jump of dfs
        def dfs(vertex:int ,toBeDyed:Color):
            nonlocal valid
            if not valid:
                return
            if color[vertex]==Color.Uncolored:
                color[vertex]=toBeDyed
            elif color[vertex]==toBeDyed:
                pass
                return
            else:
                valid=False
                return
            for adj in graph[vertex]:
                dfs(adj,Color.black if toBeDyed==Color.red else Color.red)

        for anyVertex in range(n):
            if color[anyVertex]==Color.Uncolored: #dye any uncolored nodes
                dfs(anyVertex,Color.red)
        return valid

    def isBipartiteBfS(self, graph: list[list[int]]) -> bool:
        n=len(graph)
        color=[Color.Uncolored]*n  #use a 数组array to indicate properties of graph vertex
        que=deque()


        for anyVertex in range(n):
            if color[anyVertex]==Color.Uncolored: #dye any uncolored nodes
                que.append(anyVertex)
                color[anyVertex]=Color.red

            while not len(que)==0:
                node=que.pop()
                for anyadj in graph[node]: #for any adjacent node
                    if  color[anyadj]==Color.Uncolored: # put in queue if not  dyed
                        que.append(anyadj)
                        color[anyadj]=Color.red if color[node]==Color.black else Color.black
                    elif color[anyadj]==color[node]:
                        return False
        return True

if __name__ == '__main__':
    print(Solution().isBipartiteBfS([[1,2,3],[0,2],[0,1,3],[0,2]]))