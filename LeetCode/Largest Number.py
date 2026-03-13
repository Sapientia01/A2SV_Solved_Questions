# https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = list(map(str,nums))

        for i in range(n):
            for j in range(i+1,n):
                a = nums[i]
                b = nums[j]
                if b+a > a+b:
                    nums[i], nums[j] = nums[j], nums[i]

        return str(int("".join(nums)))