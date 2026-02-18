# Qustion Link : https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros_row = set()
        zeros_col = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeros_row.add(row)
                    zeros_col.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zeros_row or  col in zeros_col:
                    matrix[row][col] = 0