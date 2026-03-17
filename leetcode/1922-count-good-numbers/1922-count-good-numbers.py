mod = 10**9 + 7
class Solution:
    memory = {1:5,2:20}
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        elif n == 2:
            return 20

        elif n % 2 == 0:
            if (n//2) % 2 == 0:
                if n not in self.memory:
                    half = self.countGoodNumbers(n//2)
                    res = (half * half) % mod
                    self.memory[n] = res
                    
                return self.memory[n] 
            else:
                if n not in self.memory:
                    res = (self.countGoodNumbers(n//2) * 4 * self.countGoodNumbers(n//2-1)) % mod
                    self.memory[n] = res

                return self.memory[n] 

        elif n % 2 == 1:
                if n not in self.memory:
                    res = (5 * self.countGoodNumbers(n-1)) % mod
                    self.memory[n] = res

                return self.memory[n] 



# class Solution:
#     def countGoodNumbers(self, n: int) -> int:
#         evens = ceil(n/2)
#         odds = n//2

#         total = (pow(5, evens, pow(10,9) + 7)) * (pow(4, odds, pow(10,9) + 7))

#         return total % (pow(10,9) + 7)