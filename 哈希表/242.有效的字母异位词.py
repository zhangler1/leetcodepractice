from  collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charset=defaultdict(int)
        for a in s:
            charset[a]=charset[a]+1

        for b in t:
            charset[b]=charset[b]-1

        return  all([  item==0 for item in charset.values()])
if __name__ == '__main__':
    print(Solution().isAnagram("anagram","nagaram"))