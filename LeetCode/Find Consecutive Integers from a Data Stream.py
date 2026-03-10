# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:
    def __init__(self, value: int, k: int):
        self.que = deque()
        self.val = value
        self.count = 0
        self.max = k
        
    def consec(self, num: int) -> bool:
        self.que.append(num)
        if num == self.val:
            self.count += 1
        
        if len(self.que) > self.max:
            cur = self.que.popleft()
            if cur == self.val:
                self.count -= 1


        return len(self.que) == self.max == self.count