from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        if n<4 :
            return []
        i=0
        ans=[]
        while(i<n-3):
            if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target):
                while (i+1<n and nums[i] == nums[i+1]):
                    i = i + 1
                i = i + 1
                break
            if (nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target):
                while (i + 1 < n and nums[i] == nums[i + 1]):
                    i = i + 1
                i = i + 1
                continue
            j = i + 1
            while(j<n-2):
                if (nums[i] + nums[j] + nums[j + 1] + nums[i + 2] > target):
                    while (j + 1 < n and nums[j] == nums[j + 1]):
                        j = j + 1
                    j = j + 1
                    break
                if (nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target):
                    while (j + 1 < n and nums[j] == nums[j + 1]):
                        j = j + 1
                    j = j + 1
                    continue
                left=j+1
                right=n-1
                while (right>left):
                     sum=nums[i] + nums[j] + nums[left] + nums[right]
                     if sum>target:

                         while (right > left and nums[right] == nums[right -1]):
                            right = right -1
                         right = right - 1
                     if sum<target:
                         while (left+1<n and nums[left]==nums[left+1]):

                            left=left+1
                         left = left + 1
                     if sum==target:
                         ans.append([nums[i],nums[j],nums[left],nums[right]])
                         while (right-1>0 and  nums[right] == nums[right - 1]):
                             right = right - 1
                         right = right - 1
                         while (left + 1 < n and nums[left] == nums[left + 1]):
                             left = left + 1
                         left = left + 1
                while (j+1<n-2 and nums[j]==nums[j+1]) :
                    j=j+1
                j=j+1
            while (i+1<n-1 and nums[i]==nums[i+1]) :
                i=i+1
            i=i+1
        return ans

if __name__ == '__main__':     
    a=[-4,0,-4,2,2,2,-2,-2]
    t=7
    print(Solution().fourSum(a,t))