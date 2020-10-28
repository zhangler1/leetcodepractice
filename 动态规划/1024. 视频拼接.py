from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        n=len(clips)
        dp=[float("inf") for _ in range(T+1)]
        dp[0]=0

        for i in range(0,n):
            for t in reversed(range(T+1)):
                 if clips[i][1]>=t and clips[i][0]<t:
                    dp[t]=min([dp[t]]+[dp[k]+1 for k in  range(clips[i][0],t)])
        return dp[T]



if __name__ == '__main__':
    print(Solution().videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]] ,10))