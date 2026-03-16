class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, c**0.5//1
        while left <= right:
            if right**2 + left**2 > c:
                right -= 1

            elif right**2 + left**2 < c:
                left += 1
            else:
                return True

        return False