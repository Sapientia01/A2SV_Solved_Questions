# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(1,m):
                matrix[i][j] += matrix[i][j-1]

        for i in range(m):
            for j in range(1,n):
                matrix[j][i] += matrix[j-1][i]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        prefix_sum = matrix[row2][col2]

        if row1 > 0:
            prefix_sum -= matrix[row1-1][col2]
        if col1 > 0:
            prefix_sum -= matrix[row2][col1-1]

        if row1 > 0 and col1 > 0:
            prefix_sum += matrix[row1-1][col1-1]

        return prefix_sum