# https://leetcode.com/problems/car-fleet/
from collections import Counter,deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        finishing_time = {}
        queue = deque()
        fleet = 0

        for i,pos in enumerate(position):
            finishing_time[pos] = (target-pos)/ speed[i]
        
        position.sort(reverse=True)
        for pos in position:
            cur = finishing_time[pos]
            if queue and queue[0] < cur:
                fleet += 1
            while queue and queue[0] < cur:
                queue.popleft()

            queue.append(cur)

        if queue:
            fleet += 1

        return fleet