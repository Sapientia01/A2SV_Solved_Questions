# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans  = [0] * len(temperatures)
        
        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                ans[stack.pop()] = i - stack[-1]
            
            stack.append(i)

        return ans