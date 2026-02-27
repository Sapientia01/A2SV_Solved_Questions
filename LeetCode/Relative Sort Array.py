# Question link: https://leetcode.com/problems/relative-sort-array/description/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new_arr = [0]*(max(arr1)+1)
        res = []

        for i in arr1:
            new_arr[i] +=1
        
        for i in arr2:
            res.extend([i]*(new_arr[i]))
            new_arr[i] = 0
        
        for i in range(len(new_arr)):
            if new_arr[i] != 0:
                res.extend([i]*(new_arr[i]))
        
        return res        