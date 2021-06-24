class Solution:
    def isValid(self, s: str) -> bool:
        oprator= []
        pair={"(":")","[":"]","{":"}"}
        for str in s:
            if str in list(zip(*pair))[0]:
                oprator.append(str)
            else:
                if len(oprator)==0:
                    return False
                peak=oprator.pop()
                if pair[peak]!=str:
                    return False
        if len(oprator):
            return False
        return True

if __name__ == '__main__':
    print(Solution().isValid("()[]{}"))