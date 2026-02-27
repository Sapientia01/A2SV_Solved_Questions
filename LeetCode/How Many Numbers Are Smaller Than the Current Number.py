# Question link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_num = max(nums)+1
        arrangmentNums = [0 for i in range( max_num)] 

        for i in nums:
            arrangmentNums[i] += 1

        num_sum = 0    
        for i in range(max_num):
            num_sum+= arrangmentNums[i]
            arrangmentNums[i] = num_sum
        res = []

        for i in nums:
            less_nums = 0
            if i > 0:
                less_nums = arrangmentNums[i-1]
            res.append(less_nums)

        return res
