# Question lnk : https://leetcode.com/problems/determine-if-two-strings-are-close/description/


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2) or len(word1) != len(word2):
            return False

        word1 = Counter(word1)
        word2 = Counter(word2)

        return sorted(word1.values()) == sorted(word2.values())       