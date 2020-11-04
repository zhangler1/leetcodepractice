from typing import List
class Solution:
    

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        seta=set(nums1)
        setb=set(nums2)
        return  [a for a  in seta if a in setb ]
                



if __name__ == '__main__':
    print(Solution().intersection([1,2,2,1] ,
[2,2]))


