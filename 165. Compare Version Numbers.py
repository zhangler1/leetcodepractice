class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=tuple([int(a) for a in version1.split(".")])
        version2=tuple([int(a) for a in version2.split(".")])
        l1=len(version1)
        l2=len(version2)
        mi=min(l1,l2)
        for x,y in zip(version1,version2):
            if x>y:
                return -1
            elif x<y:
                return 1
        if sum(version1[mi:])==sum(version2[mi:]):
            return 0
        else:
            return   1 if sum(version1[mi:])>sum(version2[mi:]) else -1


if __name__ == '__main__':
    print(Solution().compareVersion("1.01",
    "1.001"))