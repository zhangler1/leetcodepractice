class Solution:#推导当前方向利用l
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[0]*n for i in range(n)]
        ans=0
        start=0
        maxoff=0
        for i in range(n):
            dp[i][i]=1
            if i+1<n and s[i]==s[i+1]:
                 dp[i][i+1]=2
                 ans=2
                 start=i
                 maxoff=1

        for off in range(2,n):
            for i in range(n):
                if i+off<n and dp[i+1][i+off-1] and s[i]==s[i+off]:
                    dp[i][i+off]=dp[i+1][i+off-1]+2
                    if dp[i][i+off]>ans:
                        ans=off+1
                        start=i
                        maxoff=off




        return s[start:start+maxoff+1]
        
if __name__ == '__main__':
    print(Solution().longestPalindrome("cbbd"))