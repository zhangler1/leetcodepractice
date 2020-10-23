class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not (name and typed):
            return False

        n = 0
        t = 0
        while (t < len(typed) and name[n] != typed[t]):
            t = t + 1
        if t >= len(typed):
            return False

        while (n < len(name) or t < len(typed)):
            if t >= len(typed):
                return False
            if n < len(name) and t < len(typed) and name[n] == typed[t]:
                n += 1
                t += 1

            elif (t < len(typed) and name[n - 1] == typed[t]):
                t = t + 1

            else:
                return False
        return True
