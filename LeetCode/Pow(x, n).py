# Question Link: https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, number: float, power: int) -> float:
        # if power is zero
        if power == 0:
            return 1

        # if power is negative
        if power < 0:
            return 1/self.myPow(number, -power)

        # if power is positive 
        if power % 2 == 1:
            return number * self.myPow(number, power-1)

        else:
            half = self.myPow(number, power//2)
            return half * half    