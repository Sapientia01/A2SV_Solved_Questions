    # Question Link: https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/description/

class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)

        for i in range(len(s)-1):
            num1, num2 = s[i:i+2]
            if num1 != num2 and freq[num1] == int(num1)  and freq[num2] == int(num2):
                return s[i:i+2]

        return ""
        