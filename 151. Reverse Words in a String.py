class Solution:
    def reverseWords(self, s: str) -> str:
        ns=s.strip().split()
        ns.reverse()

        return " ".join(ns)

if __name__ == '__main__':
    


