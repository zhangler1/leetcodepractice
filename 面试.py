import numpy as np

def bi_search(nums: list[int], l:int,r:int,target: int):
    l: int=l
    r: int=r
    while (l<r):
        mid=(l+r)//2
        if nums[mid]>=target:
            r=mid
        elif nums[mid]<target:
            l=mid+1
    m=min([abs(target-a) for a in [nums[r-1], nums[r], nums[r+1]]])
    if nums[r-1]==m:
        return m
    if nums[r]==m:
        return m
    if nums[r+1]==m:
        return m

    return r

print(bi_search([1, 5, 5, 7, 9, 10], 6))

def sumofthree(nums: list[int],target:int):
    n=len(nums)
    nums=sorted(nums)
    for i in range(n):
        for j in range(i,n):
            k=bi_search(nums,j+1,len(nums),target-nums[i]-nums[j])

