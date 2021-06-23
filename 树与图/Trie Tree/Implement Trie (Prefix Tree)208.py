class TrieNode:
    def __init__(self):
        """
        Initialize your Node data structure here.

        """
        self.children=[None]*26
        self.endcount=0

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node=self.head
        for ch in word:
            if node.children[ord(ch)-ord("a")] is None:  # if none
                node.children[ord(ch)-ord("a")]=TrieNode()
            node=node.children[ord(ch)-ord("a")]
        node.endcount+=1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node=self.head
        for ch in word:
            if node.children[ord(ch)-ord("a")] is not None:
                node=node.children[ord(ch)-ord("a")]
            else:
                return False
        return bool(node.endcount)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.head
        for ch in prefix:
            if node.children[ord(ch)-ord("a")] is not None:
                node=node.children[ord(ch)-ord("a")]
            else:
                return False
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
