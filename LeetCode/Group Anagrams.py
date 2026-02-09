# Questions link: https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            anagram = ''.join(sorted(list(word)))
            if anagram in anagrams:
                anagrams[anagram].append(word)
            else:
                anagrams[anagram] = [word]
    