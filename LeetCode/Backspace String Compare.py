# https://leetcode.com/problems/backspace-string-compare/description/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = j = 0
        n , m = len(s), len(t)
        s_chars = []
        t_chars = []
        equal = True

        for i in range(n):
            if i < n and s[i] != "#":
                s_chars.append(s[i])

            elif s_chars and s[i] == "#":
                s_chars.pop()


        for i in range(m):
            if  t[i] != "#":
                t_chars.append(t[i])

            elif t_chars and t[i] == "#":
                t_chars.pop()

        return s_chars == t_chars