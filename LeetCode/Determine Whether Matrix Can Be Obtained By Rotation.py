# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/

class Solution:
    def rotate90(self, matrix):
        n , m = len(matrix), len(matrix[0])
        rotated_mat = []

        for i in range(m):
            row = []
            for j in range(n):
                row.append(matrix[j][i])
            rotated_mat.append(row[::-1])

        return rotated_mat


    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # 90 deg
        mat1 = self.rotate90(mat)
        # 180 deg
        mat2 = self.rotate90(mat1)
        #  270 deg
        mat3 = self.rotate90(mat2)

        return mat == target or mat1 == target or mat2 == target or mat3 == target