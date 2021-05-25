class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        numindx=numRows-1
        final=[]
        i=0
        j=-1
        flagdown=True
        row=[""]*numRows
        for c in s:
           if flagdown:
               j+=1
               row[j]=c
               if j==numindx:
                   flagdown=False
                   final.append(row)
                   row=[]#重要的正常结束标志
           else:
               i+=1
               j-=1
               if j==0:
                   row=[""]*numRows
                   row[j]=c
                   flagdown=True
               else:
                   lrow=[""]*numRows
                   lrow[j]=c
                   final.append(lrow)
        if row!=[]:
            final.append(row)
        ans=""
        for iter in zip(*final):
            for i in iter:
                ans+=i
        return ans

if __name__ == '__main__':
    print(Solution().convert(
        "PAYPALISHIRING" ,
        3))