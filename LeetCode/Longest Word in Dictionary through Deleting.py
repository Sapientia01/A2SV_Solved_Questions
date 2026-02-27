# Question link:  https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/

def is_subsequace(s1,s2):
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j] :
            i += 1
        j += 1
    return i >= len(s1)


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longest_word = ""
        for word in dictionary:
            if is_subsequace(word,s):
                 if  len(word) > len(longest_word):
                    longest_word = word
                 elif len(word) == len(longest_word) and word < longest_word:
                    longest_word = word


        return longest_word