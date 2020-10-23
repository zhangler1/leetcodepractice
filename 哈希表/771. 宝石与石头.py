class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """你妈"""
        dic={ a:0 for a in J}
        for a in S:
            if a in dic:
                dic[a]=dic[a]+1
        return  sum(dic.values())


J="aA"
S="aAAbbbb"
print(Solution().numJewelsInStones(J,S))
