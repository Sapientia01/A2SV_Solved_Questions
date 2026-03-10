# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n, m = len(image), len(image[0])
        for i in range(n):
            row = image[i][::-1]
            for j in range(m):
                image[i][j] = 1 if row[j] == 0 else 0

        return image