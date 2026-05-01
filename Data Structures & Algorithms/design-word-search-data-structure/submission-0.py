class TrieNode:

    def __init__(self):
        self.hmap = {}
        self.wflag = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.hmap:
                curr.hmap[char] = TrieNode()
            curr = curr.hmap[char]
        curr.wflag = True

    def search(self, word: str) -> bool:

        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in curr.hmap.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in curr.hmap:
                        return False
                    curr = curr.hmap[word[i]]

            return curr.wflag
        
        return dfs(0, self.root)


