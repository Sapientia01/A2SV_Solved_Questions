# Question Link: https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        openings = []
        pairs = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for bracket in s:
            if bracket in ["(", "{", "["]:
                openings.append(bracket)
            elif len(openings) > 0 and pairs[bracket] == openings[-1]:
                openings.pop(-1)
            else:
                return False
                
        if len(openings)> 0:
            return False          
        return True