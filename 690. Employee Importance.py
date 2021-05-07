
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list[Employee], id: int) -> int:
        empdict={}
        for emp in employees:
            empdict[emp.id]=emp

        sum=0
        def dfs(id:int):
            nonlocal sum
            if id in empdict:
                sum+=empdict[id].importance
                for e in empdict[id].subordinates:
                    dfs(e)
        dfs(id)
        return sum


if __name__ == '__main__':
    Solution().getImportance([[1,2,[2]], [2,3,[]]],
    2)
