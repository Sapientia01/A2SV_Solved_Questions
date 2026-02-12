# Question Link: https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uniq_nums = set(nums)
        max_num = max(uniq_nums)
        min_num = min(uniq_nums)
        max_len = 1

        for num in nums:
            if num-1 not in uniq_nums and num+1 not in uniq_nums:
                uniq_nums.discard(num)


        while uniq_nums:
            cur_len = 1
            num1 = uniq_nums.pop() + 1 
            num2 = num1 - 2

            while uniq_nums and num1 in uniq_nums and num1 <= max_num:
                cur_len += 1
                uniq_nums.remove(num1)
                num1 += 1

            while uniq_nums and num2 in uniq_nums and num2 >= min_num:
                cur_len += 1
                uniq_nums.remove(num2)
                num2 -= 1

            max_len = max(max_len, cur_len)

        return max_len