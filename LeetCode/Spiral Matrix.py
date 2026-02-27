# Question link: https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nums = []
        rotation = ceil( min(len(matrix), len(matrix[0]))/2)

        for i in range(rotation):
            nums.extend(matrix.pop(0))

            for i in range(len(matrix)):
                if matrix[i]:
                    nums.append(matrix[i].pop())

            if matrix:
                nums.extend(matrix.pop()[::-1])

            n = len(matrix)
            for i in range(n):
                if matrix[n-1-i]:
                    nums.append(matrix[n-1-i].pop(0))
        
        return nums