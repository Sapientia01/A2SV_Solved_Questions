# https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n ,m = len(mat), len(mat[0])
        res = []
        i = 0
        j = 0

        while len(res) < n*m:
            res.append(mat[i][j])

            if (i+j) % 2 == 0:
                if j == m-1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == n-1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    j -= 1
                    i += 1

        return res   