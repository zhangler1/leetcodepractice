class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnName=[]
        while columnNumber!=0:

            quotient,remainder=divmod(columnNumber,26)
            if remainder==0:   #因为没有元素表示0，用z表示A0 于是就加z ，减一高位
                if quotient>=0:
                    quotient-=1
            columnNumber=quotient

            codepoint=(remainder-1)%26

            columnName.append(chr(ord('A')+codepoint))
        columnName.reverse()
        return "".join(columnName)



        
if __name__ == '__main__':
    print(Solution().convertToTitle(28))
