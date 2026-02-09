# Question link: https://leetcode.com/problems/insert-delete-getrandom-o1/description/

from random import choice 
class RandomizedSet:

    def __init__(self):
        self.data = {} 
        self.list = list()
        
    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data[val] = len(self.list)
        self.list.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        
        self.list[self.data[val]] = self.list[-1]
        self.data[self.list[-1]] = self.data[val]
        del self.data[val]
        self.list.pop()
        return True
        

    def getRandom(self) -> int:
        return choice(self.list)