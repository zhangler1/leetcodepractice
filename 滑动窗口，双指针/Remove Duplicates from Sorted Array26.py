class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        j=0
        for j in range(len(nums)) :
            if nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                i+=1
        return i+1


if __name__ == '__main__':
    print(Solution().removeDuplicates([1,1,2]))