class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        num_cols = len(matrix[0])
        num_rows = len(matrix)

        res = [matrix[i].copy() for i in range(num_rows)]

        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    res[i] = [0] * num_cols
                    for y in range(num_rows):
                        res[y][j] = 0

        for i in range(num_rows):
            for j in range(num_cols):
                matrix[i][j] = res[i][j]
        return 

