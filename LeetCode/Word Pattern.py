# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False

        pattern_map = {}
        word_map = {}
        
        for i in range(len(s)):
            pat = pattern[i]
            word = s[i]

            if pat not in pattern_map and word not in word_map:
                pattern_map[pat] = word
                word_map[word] = pat

            elif pat in pattern_map and word in word_map:
                if pattern_map[pat] != word or word_map[word] != pat:
                    return False
            else:
                return False

        return True        