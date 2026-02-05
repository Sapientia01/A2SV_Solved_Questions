# O(1) space and O(n) Time
class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        n = len(nums)
        total_sum =  n * (n+1) // 2

        for num in nums:
            total_sum -= num

        return total_sum

# O(n) space and O(n) Time
class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        nums_range = [0 for i in range(len(nums)+1)] 

        for num in nums:
            nums_range[num] += 1

        print(nums_range)

        for i, num in enumerate(nums_range):
            if num == 0:
                return i