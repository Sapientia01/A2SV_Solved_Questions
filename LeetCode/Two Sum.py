# Question Link: https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = {num : i for i,num in enumerate(nums)}
        print(indexs)
        for i, num in enumerate(nums):
            x = target-num
            if x in nums and i != indexs[x]:
                return i, indexs[x]