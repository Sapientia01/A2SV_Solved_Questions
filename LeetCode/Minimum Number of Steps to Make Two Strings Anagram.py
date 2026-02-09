# Question Link: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        chars1 = Counter(s) 
        chars2 = Counter(t)
        steps = 0
        for key in chars2:
            if key in chars1 and:
                if chars1[key] < chars2[key]:
                    steps += chars2[key] - chars1[key]
            else:
                steps += chars2[key]

        return steps