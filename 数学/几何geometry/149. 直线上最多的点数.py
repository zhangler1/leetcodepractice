from collections import Counter
from math import  gcd
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n=len(points)
        maxnum=0
        maxline=None# (x,j,(Δx,Δy))
        for i in range(n):
            x1,y1=points[i]
            lines=Counter()
            for j in range(i+1,n):

                    x2,y2=points[j]
                    if (x1,y1)==(x2,y2):
                        continue
                    #判断斜率，判断点是否在同一条直线上，是否在同一条直线
                    y=y2-y1  #Δx
                    x=x2-x1  #Δy
                    numerator=(y2-y1)//gcd(x,y) #分子
                    denominator=(x2-x1)//gcd(x,y)   #分母
                    if denominator<0:
                        denominator=-denominator
                        numerator=-numerator
                    if numerator==0:
                        lines[(x1, y1, (0,1))]+=1
                    elif denominator==0:
                        lines[(x1,y1,(1,0))] +=1
                    else:
                        slope_k=(numerator,denominator)
                        lines[(x1,y1,slope_k)]+=1

            #统计最多的
            if lines.most_common(1)!=[]:
                l,s=lines.most_common(1)[0]
                if s>maxnum:
                    maxnum=s
                    maxline=l
        return (maxline,maxnum+1)











        
if __name__ == '__main__':
    print(Solution().maxPoints([[0,1],[0,0],[0,4],[0,-2],[0,-1],[0,3],[0,-4]]))