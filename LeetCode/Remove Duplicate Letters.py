# https://leetcode.com/problems/remove-duplicate-letters/

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cur_freq = Counter(s)
        stack = []

        for ch in s:
            while stack and stack[-1] >= ch and cur_freq[stack[-1]] > 0 and ch not in stack:
                stack.pop() 

            if ch not in stack:
                stack.append(ch)
            cur_freq[ch] -= 1
        
        return "".join(stack)