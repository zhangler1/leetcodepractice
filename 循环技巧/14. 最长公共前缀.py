from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            CommonPrefix=[]
            for chars in zip (*strs):
                a =list(chars)

                pre=None
                for char in a:
                    if pre:
                        if pre!=char:
                            return "".join(CommonPrefix)
                        else:pass
                    pre = char

                CommonPrefix.append(char)

            return  "".join(CommonPrefix)




if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))