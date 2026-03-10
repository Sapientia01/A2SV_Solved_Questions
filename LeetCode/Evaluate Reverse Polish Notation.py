# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())

            elif token == "-":
                stack.append(-1 * (stack.pop() - stack.pop()))
                
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif token == "/":
                first = stack.pop()
                second = stack.pop() 
                stack.append(int(second / first))

            else:
                stack.append(int(token))

        return stack[-1]  