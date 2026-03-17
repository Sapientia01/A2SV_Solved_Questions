class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evens = ceil(n/2)
        odds = n//2

        total = (pow(5, evens, pow(10,9) + 7)) * (pow(4, odds, pow(10,9) + 7))

        return total % (pow(10,9) + 7)