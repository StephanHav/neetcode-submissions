class TrieNode:

    def __init__(self):
        self.hmap = {}
        self.wflag = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.hmap:
                curr.hmap[c] = TrieNode()
            curr = curr.hmap[c]
        curr.wflag = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.hmap:
                return False
            curr = curr.hmap[c]
        
        return curr.wflag

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.hmap:
                return False
            curr = curr.hmap[c]

        return True
        