# Question link: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [num for num in freq if freq[num] > 1]