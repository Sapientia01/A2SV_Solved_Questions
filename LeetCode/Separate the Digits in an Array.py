# Question link: https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            cur = list(map(int, str(num)))
            res.extend(cur)

        return res