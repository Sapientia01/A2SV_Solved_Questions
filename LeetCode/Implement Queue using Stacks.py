# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        nums = []
        while self.stack:
            nums.append(self.stack.pop())
        x = nums.pop()

        while nums:
            self.stack.append(nums.pop())
            
        return x

    def peek(self) -> int:
        nums = []
        while self.stack:
            nums.append(self.stack.pop())
        x = nums[-1]

        while nums:
            self.stack.append(nums.pop())

        return x
        

    def empty(self) -> bool:
        return len(self.stack) == 0