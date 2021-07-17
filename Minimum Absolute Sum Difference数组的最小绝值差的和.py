import bisect
class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        n=len(nums1)

        replica_nums1:list[int]=nums1.copy()
        replica_nums1.sort()
        mod=10**9+7
        minv=mod
        for i,num2 in enumerate(nums2):
            candi=bisect.bisect_left(replica_nums1,num2)
            if candi>=n:
                candi=n-1

            candi2=0
            if candi>=1:
                candi2=candi-1
            m=min(abs(replica_nums1[candi]-num2)-abs(nums1[i]-num2),abs(replica_nums1[candi2]-num2)-abs(nums1[i]-num2))
            if m<minv:
                minv=m
        return  (sum([abs(nums1[i]-nums2[i]) for i,num2 in enumerate(nums2)])+minv)%mod





if __name__ == '__main__':
    print(Solution().minAbsoluteSumDiff([53,48,14,71,31,55,6,80,28,19,15,40,7,21,69,15,5,42,86,15,11,54,44,62,9,100,2,26,81,87,87,18,45,29,46,100,20,87,49,86,14,74,74,52,52,60,8,25,21,96,7,90,91,42,32,34,55,20,66,36,64,67,44,51,4,46,25,57,84,23,10,84,99,33,51,28,59,88,50,41,59,69,59,65,78,50,78,50,39,91,44,78,90,83,55,5,74,96,77,46]
,[39,49,64,34,80,26,44,3,92,46,27,88,73,55,66,10,4,72,19,37,40,49,40,58,82,32,36,91,62,21,68,65,66,55,44,24,78,56,12,79,38,53,36,90,40,73,92,14,73,89,28,53,52,46,84,47,51,31,53,22,24,14,83,75,97,87,66,42,45,98,29,82,41,36,57,95,100,2,71,34,43,50,66,52,6,43,94,71,93,61,28,84,7,79,23,48,39,27,48,79]))