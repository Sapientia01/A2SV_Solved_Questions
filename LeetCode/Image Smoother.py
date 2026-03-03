# https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
    
        resImg = [[0]*len(x) for x in img]

        row = len(img)
        col = len(img[0])

        for i in range(row):
            for j in range(col):
                max_row = min((row-1) , (i+1))
                min_row = max(0, i-1 )
                max_col = min((col-1) , (j+1))
                min_col = max(0, j-1 )
                box_sum = 0
                for r in range(min_row ,max_row+1):
                    box_sum += sum(img[r][min_col:max_col+1])
                size = (max_col -min_col +1)  *    (max_row -min_row +1)  
                resImg[i][j]= box_sum//size    

        return resImg
    
        