class Solution:
    def translateNum(self, num: int) -> int:
        num=[ int(char)for char in str(num)]
        dp=[1]*len(num)
        trans={str(num):chr(ord("a") +num) for num in range(26) }
        for i in range(1,len(num)):
            dp[i]=(dp[i-1] if i-1>=0 else 1)+ ((dp[i-2]if i-2>=0 else 1) if i-1>=0 and "".join( [str(item)for item in num[i-1:i+1]])in trans else 0)
        return dp[len(num)-1]



# 5
if __name__ == '__main__':
    print(Solution().translateNum(506))
