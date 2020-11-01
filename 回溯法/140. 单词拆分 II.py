
# 1. 选择怎么确定，需要传递参数吗 ，还是只需要单单的其他参数？
# 2. 需要每一层递归保留至今的选择吗 ？用path参数。或者层次传递？用局部变量保留结果 。
# 3. 如何返回结果？ans传递，还是层次传递
# 4. 普通出口和搜索穷尽口这两个出口要确定，普通口在搜索穷尽口的部分要返回结果！
from functools import lru_cache#使用LRu要注意参数的简单性，所以不应该使用复杂的参数列表
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)#递归使用缓存，一解决超时的问题
        def backtrack(index: int) -> List[List[str]]:
            if index == len(s):
                return [[]] #搜索到结果的口
            ans = list()         #回溯算法建立，建立ans列表用于返回答案。按层次返回，开始时都没有，最后承接下层递归答案。
            for i in range(index + 1, len(s) + 1):
                word = s[index:i] #从index开始一个个试探
                if word in wordSet:
                    nextWordBreaks = backtrack(i) #总体有多种，这里也应该可想到是多种 。若是后者不行，则会变成ans始终是[],也就没有结果。
                    for nextWordBreak in nextWordBreaks: #这里关键， 普通口，和搜索穷尽口，返回结果在这里区别。
                        ans.append(nextWordBreak.copy() + [word]) #这里是通过普通口按层次返回，多种选择，多种拆分方法
            return ans #两个出口，普通口，和搜索穷尽口，普通口可以继续，而搜索穷尽口不行。搜索穷尽口则返回[]不会加结果



        wordSet = set(wordDict)#将单词列表转换成集合
        breakList = backtrack(0)
        return [" ".join(words[::-1]) for words in breakList]



if __name__ == '__main__':
    print(Solution().wordBreak(s = "catsanddog",
        wordDict = ["cat", "cats", "and", "sand", "dog"]))


