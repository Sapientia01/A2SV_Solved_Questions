# Question link : https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_piles = 0
        
        for i in range(len(piles)//3):
            my_i = len(piles) - 2 - (2 * i) 
            max_piles += piles[my_i]

        return max_piles