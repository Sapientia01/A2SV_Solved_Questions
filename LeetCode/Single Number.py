#question link:  https://leetcode.com/problems/single-number/description/

# O(n) space and Time
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq =  Counter(nums)
        return [num for num in freq if freq[num] == 1 ][0]

# O(1) space and  O(n) Time using XOR operation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s_num = 0
        for num in nums:
            s_num = s_num^num

        return s_num