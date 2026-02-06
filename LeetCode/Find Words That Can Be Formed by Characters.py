# Question links: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from collections import Counter 

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        chars = Counter(chars)
        for word in words:
            if Counter(word) <= chars:
                res += len(word)

        return res