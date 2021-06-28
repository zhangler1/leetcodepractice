class Solution:
    def getKthMagicNumber(self, k: int) -> int:
         #此题关键还是数学上明白丑数的生成模式，是dp[i]
        #动态规划的关键是将候选的生成的遗物作比较
       #一步一步找到最接近的值，和上次不一样，《下一个排列》中用规律找到下一个数，而此题可以生成，因为之前是数是排列构成的，
#今天的数是由3,5,7相乘得来的
        #这一次又三个dp[p3]有意思啊。还挺花式的。 dp[i]和dp[i-1]i　
        dp=[0]*k
        dp[0]=1
        p3 = 0
        p5 = 0
        p7 = 0
        for i in range(1,k):


            dp[i]=min(dp[p3 ]*3,dp[p5]*5,dp[p7]*7)
            #如果有2个候选相同都要改变
            if dp[i]==dp[p3 ]*3:
                p3+=1
            if dp[i]==dp[p5 ]*5:
                p5+=1
            if dp[i]==dp[p7 ]*7:
                p7+=1

        return dp[k-1]





if __name__ == '__main__':
    print(Solution().getKthMagicNumber(5))