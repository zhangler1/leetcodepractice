from typing import List


class Solution:
    # 坐标变换到中心->转动90度，用三角公式->再回到数组坐标
    # 问题：
    # 1坐标变换公式，原点变迁去反
    # 2与其用temp一部分一部分交换，不如用不覆盖的整体变换

    # 关键 奇数： 0+k+=n-1-k  k1=(n-1)/2
    #    偶数： 0+k+1=n-1-k  k2=(n-2)/2 因为k2（整数）=（n-2）/2==(n-1)/2（此时不是整数）-1/2
    #       也就是-1/2后到达正到达整数，所以可以用（n-1）//2

    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)

        # 上下翻转数组
        for ridx in range((n-1)//2+1):
            matrix[ridx], matrix[n-1-ridx]=matrix[n-1-ridx], matrix[ridx]
        for ridx in range(n):
            for lidx in range(ridx, n):
                matrix[ridx][lidx], matrix[lidx][ridx]=matrix[lidx][ridx], matrix[ridx][lidx]


if __name__=='__main__':
    print(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
