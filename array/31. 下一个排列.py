from  typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        for i in reversed(range(len(nums))):
            min=float("inf")
            minidx=None      #用于记录最小值
            for j in range(i+1,len(nums)): #从高一位开始，

                if nums[i]<nums[j]:
                    if nums[j]-nums[i]<min:
                        min=nums[j]-nums[i]
                        minidx=j

            if min!=float("inf"):
                nums[i],nums[minidx]= nums[minidx],nums[i]
                tem=nums[i + 1:]               #切片是浅复制
                tem.sort()                      #将切片排序 ,要特别注意in-place算法的原地性
                nums[i+1:]=tem                 #将排序好的元素组赋值
                return nums

        #若全称没有逆序，将整个数组从头到尾翻转过来。
        lp=0
        rp=len(nums)-1
        while(lp<rp):
            nums[rp],nums[lp]=nums[lp],nums[rp]
            lp+=1
            rp-=1
        return  nums









if __name__ == '__main__':
    print(Solution().nextPermutation([1,2,3]))

