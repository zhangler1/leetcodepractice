from typing import List
#前序和排序 不是原数组排序，所以不影响结果 ，
#但是注意，如果一次性排序好，则结果不对，这里特点是分成2组，2组分别有序， 而且组间才是计算的战场
# 用前序和可以很好代替原数组

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0

        def mergesort(nums,sort,left,right):#记住左右端点是一定要的
            if (right-left+1)<=1:
                return 0
            mid=(left+right)//2
            leftsum=mergesort(nums,sort,left,mid)
            rightsum=mergesort(nums,sort,mid+1,right)

            ans = 0
            for le in range(mid - left + 1):  # 变量居然写错了
                r = mid + 1
                l = mid + 1

                while (r <= right and nums[r] - nums[left + le] <= upper):
                    r += 1

                while (l <= right and nums[l] - nums[left + le] < lower):  # 还是要l<=r的 等号也要,实际上l一定小于r。只要l<=right
                    l += 1
                ans += r - l
            # 现在合并2个数组

            p = left
            l = left + 0
            r = mid + 1
            while (l <= mid and r <= right):
                if nums[l] > nums[r]:
                    sort[p] = nums[r]
                    p += 1
                    r += 1
                else:
                    sort[p] = nums[l]
                    p += 1
                    l += 1
            if l <= mid:
                while (l <= mid):  #######
                    sort[p] = nums[l]
                    p += 1
                    l += 1
            else:
                while (p <= right):  ##### p <= right与  p < right
                    sort[p] = nums[r]
                    p += 1
                    r += 1
            for i in range(left, right + 1):
                nums[i] = sort[i]

            return leftsum+rightsum+ans

        #转化为前序和
        sum=0
        i=0
        presum=[0 for num in range(len(nums)+1) ]
        while(i<len(nums)):
            sum+=nums[i]
            presum[i+1]=sum
            i+=1
        #前序和结束，问题转化为presum[j]-presum[i]处于某范围的问题了
        sort = [0 for a in range(len(presum))]
        return  mergesort(presum,sort,0,len(presum)-1)
if __name__ == '__main__':
    print(Solution().countRangeSum())