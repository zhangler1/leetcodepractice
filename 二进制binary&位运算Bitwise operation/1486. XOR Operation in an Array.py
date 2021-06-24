class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result=0
        for i in range(n):
            result=start^result
            start=start+2
        return result


if __name__ == '__main__':
            print(Solution().xorOperation(5,
            0))

    