# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] *(n+1)
        total_subarr =  0
        cur_sum  = 0
        sum_freq = {0:1}

        for i,num in enumerate(nums):
            cur_sum += num
            prefix_sum[i+1] = cur_sum

            if cur_sum not in sum_freq:
                sum_freq[cur_sum] = 1
            else:
                sum_freq[cur_sum] += 1
        
        for i,left in enumerate(prefix_sum):
            sum_freq[left] -= 1
            right = k + left 

            if right in sum_freq:
                total_subarr += sum_freq[right]
                
        return total_subarr