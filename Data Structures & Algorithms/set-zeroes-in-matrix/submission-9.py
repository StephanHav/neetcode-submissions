class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        num_cols = len(matrix[0])
        num_rows = len(matrix)
        row_zero = False

        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0

                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        row_zero = True

        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        

        
        if matrix[0][0] == 0:
            for j in range(num_rows):
                matrix[j][0] = 0
        
        if row_zero:
            matrix[0] = [0] * num_cols

        return 

