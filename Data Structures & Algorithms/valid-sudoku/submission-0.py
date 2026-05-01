class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for row in board:
            
            uniques = set()
            for num in row:
                if num in uniques:
                    return False
                else:
                    if num.isdigit():
                        uniques.add(num)
            
        for i in range(len(board)):
            uniques = set()
            for j in range(len(board)):
                if board[j][i] in uniques:
                    return False
                else:
                    if board[j][i].isdigit():
                        uniques.add(board[j][i])

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                uniques = set()
                for y in range(0, 3):
                    for x in range(0, 3):

                        if board[i + y][j + x] in uniques:
                            return False
                        else:
                            if board[i + y][j + x].isdigit():
                                uniques.add(board[i + y][j + x])

        return True

