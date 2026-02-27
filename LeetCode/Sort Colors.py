# Question link: https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        new_arr = [0] * 3
        index = 0
        for i in nums:
            new_arr[i] +=1

        for color in range(3):
            for i in range(new_arr[color]):
                nums[index] = color 
                index += 1