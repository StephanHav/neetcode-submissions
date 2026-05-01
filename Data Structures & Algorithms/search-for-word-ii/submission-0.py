class TrieNode:
    def __init__(self):
        self.hmap = {}
        self.wflag = False
    
    def insert(self, word):
        node = self
        for char in word:
            if char not in node.hmap:
                node.hmap[char] = TrieNode()
            node = node.hmap[char]
        node.wflag = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()

        for word in words:
            root.insert(word)

        rows = len(board)
        cols = len(board[0])
        
        visit = set()
        res = set()

        def dfs(i, j, curr, word):
            if (i < 0 or j < 0 or 
                i == rows or j == cols or
                (i,j) in visit or board[i][j] not in curr.hmap):
                return
            
            visit.add((i,j))

            curr = curr.hmap[board[i][j]]
            word += board[i][j]

            if curr.wflag:
                res.add(word) 
            
            coords = [(i,j+1),
                        (i+1,j),
                        (i,j-1),
                        (i-1,j)]
            
            for coord in coords:
                dfs(coord[0], coord[1], curr, word)

            visit.remove((i,j))
            return


        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, '')

        return list(res)