from collections import  Counter
class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        for row in wall:
            for i in range(1,len(row)):
                row[i]=row[i]+row[i-1]
        length= sum(wall[0])

        c=Counter()
        for row in wall:
            for col in row:
                c[col]+=1
        if len(c)<2:
            return len(wall)

        else:
            return len(wall)-c.most_common(2)[1][1]
if __name__ == '__main__':
    print(Solution().leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
