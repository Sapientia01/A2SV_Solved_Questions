# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:
    def __init__(self, k: int):
        self.que = [-1] * k
        self.front = 0
        self.rear = 0


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.que[self.front] != -1:
            self.front -= 1
            self.front = (self.front + len(self.que))  % len(self.que)

        self.que[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        self.rear = (self.rear + len(self.que))  % len(self.que)

        if self.isFull():
            return False

        if self.que[self.rear] != -1:
            self.rear += 1
            self.rear = (self.rear + len(self.que))  % len(self.que)

        self.que[self.rear] = value
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False 

        self.que[self.front] = -1
        if not self.isEmpty():
            self.front += 1
            self.front = (self.front + len(self.que))  % len(self.que)

        return True
        

    def deleteLast(self) -> bool:
        if  self.isEmpty():
            return False 

        self.que[self.rear] = -1
        if not self.isEmpty():
            self.rear -= 1
            self.rear = (self.rear + len(self.que))  % len(self.que)
        return True
        

    def getFront(self) -> int:
        return self.que[self.front]
        

    def getRear(self) -> int:
        return self.que[self.rear]
        

    def isEmpty(self) -> bool:
        return len(self.que) == self.que.count(-1)
        

    def isFull(self) -> bool:
        return 0 == self.que.count(-1)