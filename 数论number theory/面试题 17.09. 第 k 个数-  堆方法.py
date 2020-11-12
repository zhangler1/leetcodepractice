import heapq
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
         #此题关键还是数学上明白丑数的生成模式，是dp[i]
        #动态规划的关键是将候选的生成的遗物作比较
        # 将大量的比较集合放到堆中堆非常适合得到局部最小，用集合去去掉重复
         #每个元素将依次取出，同时该元素*3 *5 *7 将放入，保证所有元素均加入
        seq=set()
        heap=[]
        heapq.heappush(heap,1)
        i=0
        while(len(heap)!=0):
            cur=heapq.heappop(heap)
            if not  cur in seq:
                seq.add(cur)
                i+=1
                for factor in [3,5,7]:
                    heapq.heappush(heap,cur*factor)
            if (len(seq)==k):
                return cur





if __name__ == '__main__':
    print(Solution().getKthMagicNumber(5))