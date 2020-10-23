from typing import  List
class Solution :
     def longestPalindrome(s:str) ->str : #串的长度
        n=len(s)
        dp:List[List[bool]] = [ [False]*n for _ in range(n)]#初始化一个布尔二维数组
        ans = ""
        for l,_ in enumerate(s,0)   :      #枚举子串的长度0：原地 1 单个字符
            i=0
            while (i + l < n):
                j = i + l
                if (l == 0) :
                    dp[i][j] = True
                elif(l == 1) :
                     dp[i][j] = (s[i] == s[j])
                else:
                         dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
                if (dp[i][j] and l + 1 > len(ans)):
                    ans = s[i:i+l + 1]
                i=i+1

        return ans

print(Solution.longestPalindrome("adsfsvasfsdfaba"))


