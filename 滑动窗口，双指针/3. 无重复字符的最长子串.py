from  typing import Set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxlenth=1
        maxlenstr=s[0]
        uniquestr=s[0]
        leftp=0
        abtained:Set=set()  #注意初始化空集合的方式  ={}只能是初始化字典。
        abtained.add(s[leftp])
        rightp=1
        while(rightp<=len(s)-1):
            if s[rightp] in abtained:
                uniquestr=s[leftp:rightp]
                if len(uniquestr)>maxlenth:
                    maxlenth=len(uniquestr)
                    maxlenstr=uniquestr

                abtained.remove(s[leftp])#当leftp右移的时候要去除集合中的第一个字符
                leftp+=1#先删除，再改动leftp ，脏读错误。
            else:
                abtained.add(s[rightp])
                rightp+=1
        uniquestr = s[leftp:rightp]
        if len(uniquestr) > maxlenth:
            maxlenth = len(uniquestr)
            maxlenstr = uniquestr

        return maxlenth


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
