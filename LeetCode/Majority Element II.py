# Question link:  https://leetcode.com/problems/majority-element-ii/description/

# O(n) space and O(n) Time
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        return [num for num in freq if freq[num] > n//3]

# O(1) space and O(n) Time using Boyer-Moore Voting Algorithm,
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cand1 = cand2 = None
        count1 = count2 =  0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        return[num for num in [cand1,cand2] if nums.count(num) > n//3]