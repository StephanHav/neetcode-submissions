class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        uniques = set()
        for i in range(9):
            for j in range(9):

                num = board[i][j]
                if num.isdigit():
                    row_marker = (i, num)
                    col_marker = (num, j)
                    box_marker = (i // 3, j // 3, num)

                    if row_marker in uniques or col_marker in uniques or box_marker in uniques:
                        return False
                    else:
                        uniques.add(row_marker)
                        uniques.add(col_marker)
                        uniques.add(box_marker)
        return True