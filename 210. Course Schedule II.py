class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        n=numCourses
        graph=[[0]*n for _ in range(n)]
        for arc in prerequisites:
            graph[arc[0]][arc[1]]=1

        resn=n
        path=[]
        while resn>0:
            out_degrees=[sum([a  for a in graph[:][i]]) for i in range(n)]
            for i,out in enumerate(out_degrees):
                if out==0 and i not in path:
                    path.append(i)
                    resn-=1
                    for ind,ver in enumerate(graph[i][:]):
                        graph[i][ind] =0
                    break
                return []

        return path

            



if __name__ == '__main__':
    print(Solution().findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))