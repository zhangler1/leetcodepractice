def mergesort(nums: list[int], l: int, r:int):
    def merge(nums1: list[int], nums2: list[int])->list[int]:
        lengh=len(nums1)+ len(nums2)
        newnums=[0]*lengh
        i=0
        j=0
        k=0
        while (i<len(nums1) and j<len(nums2)):
            if nums1[i]>=nums2[j]:
                newnums[k]=nums1[i]
                i+=1
                k+=1
            else:
                newnums[k]=nums2[j]
                j+=1
                k+=1
        if i<len(nums1):
            while(i<len(nums1)):
                newnums[k]=nums1[i]
                i+=1
                k+=1
        else:
            while(j<len(nums2)):
                newnums[k]=nums2[j]
                j+=1
                k+=1

        return  newnums

    if l>=r:
        return
    mid=(l+r)//2
    mergesort(nums, l, mid)
    mergesort(nums, mid+1, r)
    nums[l:r+1]=merge(nums[l:mid+1],nums[mid+1:r+1])
    return nums
def sort(nums: list[int]):
    mergesort(nums,0,len(nums)-1)
    return nums
if __name__=='__main__':

    print(sort([11111, 65, 24, 654, 435]))
