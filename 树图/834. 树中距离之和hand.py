from typing import List
class Solution:


    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        def dfs1(u,f):
            dp[u]=0
            sz[u]=1 #已经考虑了根节点

            for adj in graph[u]:
                if adj==f: #不会回头，动态规划是有顺序的
                    continue
                dfs1(adj,u)
                dp[u]+=dp[adj]+sz[adj]
                sz[u]+=sz[adj]
        def dfs2(u,f) :
            ans[u]=(dp[u])
            for adj in graph[u]: #换根
                if adj==f:
                    continue

                stackdpu=dp[u]
                stackdpadj=dp[adj]
                stackszadj=sz[adj]
                stackszu = sz[u]

                dp[u]=dp[u]-dp[adj]-sz[adj]
                sz[u] = sz[u] - sz[adj]
                sz[adj] = sz[adj] + sz[u]
                dp[adj] =dp[adj]+dp[u]+sz[u]


                dfs2(adj,u)
                dp[u]=stackdpu
                dp[adj]=stackdpadj
                sz[adj]=stackszadj
                sz[u]=stackszu




        n=N
        dp=[0 for _ in range(n)]
        sz=[0 for _ in range(n)]
        graph=[[] for _ in range(n)]
        ans=[0 for _ in range(n)]
        for edge in edges:
            u=edge[0]
            v=edge[1]
            graph[u].append(v)
            graph[v].append(u)



        dfs1(0,-1)
        dfs2(0,-1)
        return ans

print(Solution().sumOfDistancesInTree(3,[[2,1],[0,2]]))
            