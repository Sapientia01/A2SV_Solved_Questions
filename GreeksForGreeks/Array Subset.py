from collections import Counter
class Solution:
    def isSubset(self, a, b):
        freq = Counter(a)
        for num in b:
            if num not in freq or freq[num] == 0:
                return False
            else:
                freq[num] -= 1
                
        return True