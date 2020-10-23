from typing import List


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        ans = 0
        arr = [0 for i in range(x + 1)]
        for sta in staple:
            if sta < x:  # 这里存的是食物价格等于sta次数
                arr[sta] += 1

        for i in range(2, x):  # 这里存的是食物价格小于等于i次数（比如食物价格小于等于3的次数，为食物价格等于1的次数+2的次数+3的次数），所以是累加，小于等于1的次数已经是确定的，所以从2开始
            arr[i] += arr[i - 1]
        for drink in drinks:
            lt = x - drink  # 除去这个饮料还剩多少钱可以买食物
            if lt <= 0:  # 小于等于0，说明没有钱买食物了，换个饮料试试
                continue
            ans += arr[lt]  # 若剩下的钱可以买食物，则直接加上食物价格小于等于lt的次数
        return ans % (10 ** 9 + 7)  # 防止数太大取模

if __name__ == '__main__':
    print(Solution().breakfastNumber([10,20,5],[5,5,2],15))
