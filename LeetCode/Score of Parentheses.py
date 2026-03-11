# https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for bracket in s:
            if bracket == '(':
                stack.append('(')

            else:
                if stack[-1] == "(":
                    stack[-1] = 1

                else:
                    stack[-1] *= 2
                    stack.pop(-2)

                if len(stack) > 1 and isinstance(stack[-2], (int)):
                    stack[-2] += stack[-1]
                    stack.pop() 



        return stack[0]