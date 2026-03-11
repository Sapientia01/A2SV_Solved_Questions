# https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        pattern = []
        third = "null"

        for num in nums[::-1]:
            if third != "null" and third > num:
                return True

            while pattern and num > pattern[-1]:
                third = pattern.pop()

            pattern.append(num)

        return False