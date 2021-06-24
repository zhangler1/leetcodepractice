from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = []
        path = []

        def dfs(ans, S: str, path=[], selection=0):
            def isFibonacci(sequence: List[int]):
                return all([sequence[i] + sequence[i + 1] == sequence[i + 2] for i in range(len(sequence) - 2)])

            n = len(S)
            if len(path) >= 3:
                if isFibonacci(path):
                    if selection == n:
                        if not ans:
                            ans.extend(path.copy())
                else:
                    return

            for i in range(selection, n):  # 确立数组是封闭空间
                if S[selection] == "0":
                    path.append(int(S[selection:selection + 1]))
                    dfs(ans, S, path, selection + 1)
                    path.pop()
                    break  # 若无则会在结点2选择 0很多次 所以break很关键
                else:
                    num = int(S[selection:i + 1])
                    if num > 2 ** 31 - 1:
                        break
                    else:
                        path.append(num)
                        dfs(ans, S, path, i + 1)
                        path.pop()

        dfs(ans, S, path, 0)
        return ans


if __name__ == '__main__':
    print(Solution().splitIntoFibonacci(""))
