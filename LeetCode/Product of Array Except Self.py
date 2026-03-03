# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * (n+1)
        right = [1] * (n+1)
        zeros = 0
        for i in range(n):
            if nums == 0:
                zeros+= 1
            else:
                left[i+1] *= left[i] * nums[i]
                right[n-i-1] *= right[n-i] * nums[n-i-1]

        if zeros == 1:
            return [0 if num != 0 else left[-1]  for num in  nums]
        else:
            return [left[i] * right[i+1] if zeros == 0 else 0 for i in  range(n)]
        

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num

        if zeros == 1:
            return [0 if num != 0 else product  for num in  nums]
        else:
            return [product//num if zeros == 0 else 0 for num in  nums]