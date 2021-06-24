from typing import List,Dict,Tuple
from collections import defaultdict
#python的 list不可hash 必须
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            charCounter=[0]*26
            groupdict:Dict[Tuple,List]=defaultdict(list)

            for word in strs:
                for char in word:
                    codepoint=ord(char)-ord("a")
                    charCounter[codepoint]+=1
                groupdict[tuple(charCounter)].append(word)
                charCounter=[0]*26
            return [ groupdict[a] for a in groupdict]

if __name__ == '__main__':

    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))