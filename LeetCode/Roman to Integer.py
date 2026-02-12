# Question Link: https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            "I": 1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        intiger = 0

        i = 0

        while i < len(s):
            digit = s[i]

            if digit in ["I","X","C"] and i+1 < len(s):
                if  roman_num[s[i+1]] > roman_num[s[i]]:
                    intiger += (roman_num[s[i+1]] - roman_num[s[i]])
                    i+=2
                    continue  
            intiger += roman_num[digit]
            i += 1

        return intiger    