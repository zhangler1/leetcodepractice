from  typing import  List
[1,3]
[2]

class Solution:
            def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:



                def getKthElement(k:int)->int :
                    indexA = 0
                    indexB = 0

                    while True:

                        if indexB==len(nums2):
                            return nums1[indexA+k-1]
                        if indexA==len(nums1):
                            return nums2[indexB+k-1]
                        if k==1:
                            return min(nums1[indexA],nums2[indexB])


                        newindexA=min(indexA + k // 2 - 1, len(nums1) - 1)
                        newindexB=min(indexB + k // 2 - 1, len(nums2) - 1)
                        if nums1[newindexA]>=nums2[newindexB] :
                            k=k-(newindexB-indexB+1)
                            indexB=newindexB+1
                        else:
                            k = k - (newindexA-indexA+1)
                            indexA = newindexA+1



                medianindex = (len(nums1) + len(nums2)) // 2

                return getKthElement(((len(nums1) + len(nums2))+1) // 2) if (len(nums1)+len(nums2))%2!=0 else (getKthElement(medianindex)+getKthElement(medianindex+1))/2

print(Solution().findMedianSortedArrays([1,2]    ,
[3,4]))
