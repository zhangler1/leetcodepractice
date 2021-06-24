class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        n=numCourses
        graph=[[0]*n for _ in range(n)]
        for arc in prerequisites:
            graph[arc[1]][arc[0]]=1

        resn=n
        path=[]
        in_degrees=[ sum([graph[i][j] for i in range(n)]) for j in range(n)]
        while resn>0:

            update=0
            for i,out in enumerate(in_degrees):
                if out==0 and i not in path:
                    path.append(i)
                    update=1
                    resn-=1
                    for pre in prerequisites:
                        if pre[1]==i:
                            in_degrees[pre[0]]-=1

            if update==0:
                return []

        return path

            



if __name__ == '__main__':
    print(Solution().findOrder(2,
    [[1,0]]))