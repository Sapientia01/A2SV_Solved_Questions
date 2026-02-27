# Question link: https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        below = 0
        target_quantity = 0

        for i in nums:
            if i < target:
                below +=1
            if i == target:
                target_quantity +=1
        
        if target_quantity == 0:
            return []
        elif target_quantity == 1:
            return [below]
        else:
            return list(range(below, below + target_quantity))