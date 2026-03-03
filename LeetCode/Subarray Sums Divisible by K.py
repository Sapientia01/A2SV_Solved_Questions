# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0 for i in range(n+1)]
        sum_freq = {0:1}
        count = 0
        cur_sum = 0

        for i,num in enumerate(nums):
            cur_sum += num
            remender = cur_sum % k
            prefix_sum[i+1] = remender

            if remender not in sum_freq:
                sum_freq[remender] = 1
            else:
                sum_freq[remender] += 1

        for remender in prefix_sum:
            sum_freq[remender] -= 1
            count += sum_freq[remender] 

        return count