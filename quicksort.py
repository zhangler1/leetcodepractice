import random
def partition(nums:list[int],l:int,r:int):
    if r-l<1:
        return
    ob=random.randint(l,r)
    nums[ob],nums[l]= nums[l], nums[ob]
    pivot =nums[l]
    i=l
    j=r
    while i<j:
        while i<j and nums[j]>=pivot:
            j-=1
        nums[i]=nums[j]
        while i<j and nums[i]<=pivot:
            i+=1
        nums[j]=nums[i]

    nums[i]=pivot
    return i,pivot
def    sort(nums:list[int]):

    def quicksort(nums:list[int],l:int,r:int) :
        if l>=r:
            return
        i,pivot=partition(nums,l,r)
        quicksort(nums,l,i-1)
        quicksort(nums,i+1,r)


    quicksort(nums,0,len(nums)-1)
    return nums



if __name__ == '__main__':
    print(sort([11111, 654, 9, 65, 24]))



