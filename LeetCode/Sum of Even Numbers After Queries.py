#  Question Link : https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = sum([num for num in nums if num % 2 == 0])
        res = []
        for val,index in queries:
            cur = nums[index]
            if cur % 2 == 1 and (cur + val) % 2 == 0:
                evens += cur + val

            elif cur % 2 == 0 and (cur + val) % 2 == 0:
                evens += val
                     
            elif cur % 2 == 0 and (cur + val) % 2 == 1:
                evens -= cur

            res.append(evens)
            nums[index] += val
        
        return res