class Solution:
    memory = {}
    def fib(self, n: int) -> int:
        if n < 2 :
            return n


        if n not in self.memory:
            self.memory[n] = self.fib(n-1) + self.fib(n-2)


        return self.memory[n] 