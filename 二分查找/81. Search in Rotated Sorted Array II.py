class Solution:
    def search(self, nums: list[int], target: int) -> bool:
           l=0
           h=len(nums)-1

           while l<h:
               mid=l+h>>1
               if (nums[mid]==target) :
                   return True
               while nums[l]==nums[h]==nums[mid]:
                   l+=1
                   h-=1
                   if (l>h):
                       break

               if target>=nums[l] :
                   if nums[mid]>=nums[l]:
                       if target<nums[mid]:
                           h=mid
                       else:
                           l=mid+1
                   else:
                        h=mid
               else:
                   if nums[mid]<=nums[h]:
                       if target>nums[mid]:
                           l=mid+1
                       else:
                           h=mid
                   else:
                        l=mid+1


           return nums[h]==target
if __name__ == '__main__':
    print(Solution().search([3,1,2,2,2],
    1))