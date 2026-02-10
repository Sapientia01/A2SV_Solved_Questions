# Question Link: https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/description/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num-3) % 3 == 0:
            x = (num - 3) // 3
            return [x, x + 1 , x + 2]

        else:
            return []