# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for i,num in enumerate(nums2):  
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num

            stack.append(num)
            next_greater[num] = -1

        return [next_greater[num] for num in nums1]