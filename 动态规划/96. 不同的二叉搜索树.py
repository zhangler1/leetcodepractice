class Solution:
    def __init__(self):
        self.dic={0:1}
    def numTrees(self, n: int) -> int:
        if n in self.dic.keys():
            return self.dic[n]
        i=0
        sum=0
        while(i<n):
            sum=self.numTrees(i)*self.numTrees(n-i-1)+sum
            i+=1

        self.dic[n]=sum
        return sum

            

print(Solution().numTrees(3))



