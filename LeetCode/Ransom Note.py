# Question link: https://leetcode.com/problems/ransom-note/description/
 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)