class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        seen = []
        def dfs(x, y, i):
            if i == len(word):
                return True
            
            if (x,y) in seen:
                return False
            
            if x < 0 or x >= len(board):
                return False

            if y < 0 or y >= len(board[0]):
                return False
            
            if board[x][y] != word[i]:
                return False

            seen.append((x,y))

            res = (dfs(x+1, y, i+1) or
                    dfs(x-1, y, i+1) or
                    dfs(x, y+1, i+1) or
                    dfs(x, y-1, i+1))
            
            seen.pop()
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0): #we found a starting point
                    return True

        return False