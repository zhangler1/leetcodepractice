from typing  import List,Any
class Solution:

    def matrixScore(self, A: List[List[int]]) -> int:
        def negate(a:int):
            if a ==1:
                return 0
            elif a==0:
                return 1
            else:
                raise Exception("error input")


        def negateArray(array:List[Any]):
            for i in range(len(array)):
                array[i]=negate(array[i])
                #needn't return this answer
                # i make a mistake about linking A[0]=A ,a delimma
        n=len(A)
        m=len(A[0])
        for row in range(n):
            if A[row][0]!=1:
                negateArray(A[row])
        for col in range(1,m):
            onenum=0
            for row in range(n):
                  if A[row][col]==1:
                      onenum+=1
            if onenum<=n//2:
                for row in range(n):
                    A[row][col]=negate(A[row][col])
        sum=0
        for row in range(n):
            for col in range(m):
                if A[row][col]==1:
                    sum+=2**(m-1-col)


        return sum
if __name__ == '__main__':
    print(Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))



