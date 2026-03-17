class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        cur = max_len = 0
    
        while right < len(nums):
            while right < len(nums) and cur + 1 >= right - left:
                cur += nums[right]
                right += 1
            
            if cur == right -left:
                max_len = max(max_len, cur-1)

            elif cur+1 == right -left or cur + 2 == right - left:
                max_len = max(max_len, cur)

            while left < right and cur +1 < right - left:
                cur -= nums[left]
                left += 1

        return max_len