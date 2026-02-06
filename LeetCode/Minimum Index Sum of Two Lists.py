# Question limk: https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:           
        word_index = {word: i for i, word in enumerate(list1)}
        minSum = len(list1) + len(list2) 
        ans = []

        for i, word in enumerate(list2):
            if word in word_index:
                index = word_index[word]
                total = i + index
                if total < minSum:
                    minSum = total
                    ans = [word]
                elif total == minSum:
                    ans.append(word)
        
        return ans