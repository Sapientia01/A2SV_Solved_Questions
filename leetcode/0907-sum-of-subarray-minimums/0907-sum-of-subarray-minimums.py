# https://leetcode.com/problems/sum-of-subarray-minimums/description/

class Solution(object):
    def sumSubarrayMins(self, nums):
        mod = (10**9) + 7
        n = len(nums)

        # to find previous smaller number index using monotonically increasing stack
        prev_smaller = [-1]*n
        stack = []
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()

            if stack:
                prev_smaller[i] = stack[-1]

            stack.append(i)

        # to find a range at which the cut number will be smaller
        for i in range(n):
            prev_smaller[i] = i+1 if prev_smaller[i] == -1 else i - prev_smaller[i]


        # to find next smaller number index using monotonically increasing stack
        next_smaller = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                next_smaller[stack.pop()] = i

            stack.append(i)

        # to find a range at which the cut number will be smaller
        for i in range(n):
            next_smaller[i] = n-i if next_smaller[i] == -1 else next_smaller[i] - i


        return sum(next_smaller[i]*prev_smaller[i]*nums[i] for i in range(n)) % mod