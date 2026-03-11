# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        next_min = []
        next_max = []
        max_len = left = right = 0

        while right < len(nums):
            while next_min and next_min[-1] > nums[right]:
                next_min.pop()
            next_min.append(nums[right])

            while next_max and next_max[-1] < nums[right]:
                next_max.pop()
            next_max.append(nums[right])

            right += 1

            while abs(next_min[0]- next_max[0]) > limit:
                if nums[left] == next_min[0]:
                    next_min.pop(0)
                if nums[left] == next_max[0]:
                    next_max.pop(0)

                left += 1

            max_len = max(max_len, right-left)

        return max_len