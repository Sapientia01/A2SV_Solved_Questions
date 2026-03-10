# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ballons = [points[0]]

        for point in points:
            if point[0] <= ballons[-1][1]:
                ballons[-1][0] = point[0]
                ballons[-1][1] = min(point[1],  ballons[-1][1]) 
                
            else:
                ballons.append(point)
                
        return len(ballons)