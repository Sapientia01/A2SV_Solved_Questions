# Question link: https://leetcode.com/problems/majority-element/description/

# O(1) space and O(n) time
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = None
        count = 0
        for num in nums:
            if num == cur:
                count += 1
            elif count == 0:
                cur = num
                count = 1
            else:
                count -= 1

        return cur



# O(1) space and O(nlog(n)) time
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        max_count = 1
        cur_count = 1
        max_num = nums[0]


        for i  in range(1,len(nums)):

            if  nums[i] ==  nums[i-1]:
                cur_count += 1

            else:
                if cur_count > max_count:
                    max_count = cur_count
                    max_num = nums[i-1]

                cur_num = nums[i]
                cur_count = 1

        if cur_count > max_count:
            max_num = nums[i-1]

        return max_num


# O(n) space and O(nlog(n)) time
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0
        max_num = 0
        freq = {}
        for num in nums:
            if num not in  freq:
                freq[num] = 1
                if max_count == 0:
                    max_count = 1
                    max_num = num
            else:
                    freq[num] += 1
                    if freq[num] > max_count:
                        max_count = freq[num]
                        max_num = num
        return max_num