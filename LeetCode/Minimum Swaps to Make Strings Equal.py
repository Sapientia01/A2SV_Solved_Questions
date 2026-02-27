# Question link: https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/description/

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0
        count = 0
        
        for i in range(len(s1)):
            if s1[i] + s2[i] == "xy":
                xy += 1
            if s1[i] + s2[i] == "yx":
                yx += 1

        count += xy//2 + yx//2
        count += (xy % 2 == yx % 2 == 1) * 2


        return -1 if xy % 2 != yx % 2 else count