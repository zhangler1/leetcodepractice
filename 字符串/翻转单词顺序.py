class Solution:
    def reverseWords(self, s: str) -> str:
        s=[word for word in s.split(" ") if word!="" ]
        return  " ".join(s[::-1])

if __name__ == '__main__':
    print(Solution().reverseWords("  hello world!  "))