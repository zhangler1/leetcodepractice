from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0 or len(matrix[0])==0:
            return []
        if len(matrix)==1:
            return matrix[0]
        if len(matrix[0])==1:
            return [row[0] for row in matrix]
        ans=[]
        ans.extend(matrix[0])
        ans.extend([row[-1] for row in matrix[1:]])
        ans.extend(matrix[-1][-2::-1])
        ans.extend([row[0] for row in matrix[-2:0:-1]])
        ans.extend(self.spiralOrder([row[1:-1] for row in matrix[1:-1]]))

        return  ans
        # [1, 2, 3, 6, 9, 8, 7, 4, 5]
if __name__ == '__main__':
    print(Solution().spiralOrder(     matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
           ))
