# Question link: https://leetcode.com/problems/minimum-index-of-a-valid-split/description/

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_dominant = [""] * n
        cur = count = 0
        freq = {}
        for i in range(n-1, -1, -1):
            num = nums[i]
            if num not in  freq:
                freq[num] = 1
                if count == 0:
                    count = 1
                    cur = num
            else:
                    freq[num] += 1
                    if freq[num] > count:
                        count = freq[num]
                        cur = num

            if count * 2 > n - i:
                left_dominant[i] = cur


        cur = count = 0
        freq = {}
        for i,num in enumerate(nums):
            if num not in  freq:
                freq[num] = 1
                if count == 0:
                    count = 1
                    cur = num
            else:
                    freq[num] += 1
                    if freq[num] > count:
                        count = freq[num]
                        cur = num

            if count * 2 > i+1 and i < n-1 and cur == left_dominant[i+1]:
                return i

        return -1