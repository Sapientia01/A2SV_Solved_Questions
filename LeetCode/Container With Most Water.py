# Question link: https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        left = 0 
        right = len(height)-1
        while left< right:
            max_volume = max(max_volume, min(height[left],height[right]) * (right-left))
            
            if height[left] > height[right] :
                right -=1
            else:
                left += 1

        return max_volume        


        