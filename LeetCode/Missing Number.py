#  Question link : https://leetcode.com/problems/missing-number/description/


# O(1) space and O(n) Time
class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        n = len(nums)
        total_sum =  n * (n+1) // 2
        return total_sum - sum(nums)
    

#O(n) space and O(n) Time  using set 
class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        actual_nums = set(list(range(len(nums)+1)))
        missing_number = actual_nums - set(nums)
        return missing_number.pop()



# O(n) space and O(n) Time using list
class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        nums_range = [0 for i in range(len(nums)+1)] 

        for num in nums:
            nums_range[num] += 1

        print(nums_range)

        for i, num in enumerate(nums_range):
            if num == 0:
                return i