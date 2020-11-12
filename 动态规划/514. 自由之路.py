class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        nRing=len(ring)
        nKey=len(key)
        def findall(arr:list[int],target:str):
            return [i for i,item in enumerate(arr)if item==target]



        dp=[ [ 0 for j in range(nRing)] for i in range(nKey)]

        for  indicei in findall(ring,key[0]):
           dp[0][indicei] =min(indicei-0%nRing,-indicei%nRing)+1
        for i in range(1,nKey):
            indicei=findall(ring,key[i])
            for indexi in indicei:
                indicej=findall(ring,key[i-1])#每次都找也可以 但是这样每次都找也行
                dp[i][indexi]=min([dp[i-1][indexj]+(indexj-indexi)%nRing +1 for indexj in indicej]+[dp[i-1][indexj]+(indexi-indexj)%nRing +1 for indexj in indicej])
        return min([dp[nKey-1][j] for j in findall(ring,key[-1])])





if __name__ == '__main__':
    # def findall(arr: list[str], target: str):
    #     return [i for i, item in enumerate(arr) if item == target]
    # print(findall(["a","b","a"],"a"))
    print(Solution().findRotateSteps(ring = "godding", key = "gd"))
