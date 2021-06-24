from typing import List
class Solution:

    def sortArrayByParityII(self, A: List[int]) -> List[int]:

         if len(A)<=2:
             return A
         n=len(A)
         odd:int=1
         even:int=0
         for i in range(len(A)):
             while(odd<n and A[odd]%2==1):
                 odd+=2
             while(even<n and A[even]%2==0):
                 even+=2
             if even<n and  odd<n:
                A[odd],A[even]=A[even],A[odd]

         return A



if __name__ == '__main__':
    print(Solution().sortArrayByParityII([4, 2, 5, 7]))