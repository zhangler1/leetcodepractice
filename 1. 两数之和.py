class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        map={}
        for i in range(n):
            map[nums[i]]=i

        for i in range(n):
             j=target-nums[i]
             if j in map and i!=map[j]:
                 return [i,map[j]]




if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15] ,
   26))

