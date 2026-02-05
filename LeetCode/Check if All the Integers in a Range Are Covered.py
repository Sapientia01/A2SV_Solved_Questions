# using Sets  
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered_range = set()

        for start,end in ranges:
            covered_range.update(list(range(start,end+1)))

        return set(list(range(left,right+1))) <= covered_range




# using prefix sum
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered_range = [0] * 52

        for start,end in ranges:
            covered_range[start] += 1
            covered_range[end+1] -= 1

        for i in range(1,52):
            covered_range[i] += covered_range[i-1] 
        print(covered_range)

        for i in range(left,right+1):
            if covered_range[i] == 0:
                return False

        return True