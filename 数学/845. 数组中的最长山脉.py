# 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
#
# B.length >= 3
# 存在 0 < i< B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
#
# 给出一个整数数组 A，返回最长 “山脉”的长度。
#
# 如果不含有 “山脉”则返回 0。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-mountain-in-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        maxdistance=0
        lastLocalminmumindex=None
        for i in range(len(A)):

           if i>1:
               if i<len(A)-1 :
                   if A[i-1]<=A[i] and A[i]<=A[i+1]:
                       Localminmumindex=i
                       if lastLocalminmumindex:
                           if Localminmumindex-lastLocalminmumindex > maxdistance:
                               maxdistance=Localminmumindex-lastLocalminmumindex
                       lastLocalminmumindex=Localminmumindex


               elif A[i-1]<=A[i]:
                   Localminmumindex = i
                   if lastLocalminmumindex:
                       if Localminmumindex - lastLocalminmumindex > maxdistance:
                           maxdistance = Localminmumindex - lastLocalminmumindex
                   lastLocalminmumindex = Localminmumindex
           elif A[i]<=A[i+1]:
               Localminmumindex = i
               if lastLocalminmumindex:
                   if Localminmumindex - lastLocalminmumindex > maxdistance:
                       maxdistance = Localminmumindex - lastLocalminmumindex
               lastLocalminmumindex = Localminmumindex
        return maxdistance

print(Solution().longestMountain([2,1,4,7,3,2,5]))