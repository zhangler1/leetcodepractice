from  collections import deque
class Solution:
    def hammingWeight(self, n: int) -> int:
        weight=0
        while n!=0:
            if (n&1==0o1):
                weight+=1
            n=n>>1
        return weight













if __name__ == '__main__':
    print(Solution().hammingWeight(4))