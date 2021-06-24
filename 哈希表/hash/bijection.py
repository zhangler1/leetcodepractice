class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char2word=dict()
        word2char=dict()
        words=s.split()
        if len(pattern)!=len(words):
            return False
        for char,word in zip(pattern,words):
            if (char in char2word and char2word[char]!=word) or (word in word2char and word2char[word]!=char):
                return False
            else:
                char2word[char]=word
                word2char[word]=char

        return True


if __name__ == '__main__':
    print(Solution().wordPattern("abba","dog cat cat dog"))