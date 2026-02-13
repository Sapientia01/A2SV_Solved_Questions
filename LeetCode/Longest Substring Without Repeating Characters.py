# Question Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        un_repeted = set()
        n = len(s)
        left = 0
        right = 0
        max_len = 0
        while right < n:
            while right < n and s[right] not in un_repeted :
                un_repeted.add(s[right])
                print(un_repeted)
                right += 1

            if len(un_repeted) == right - left:
                max_len = max(max_len,  right - left)
            
            while left < right < n and s[right] != s[left]:
                un_repeted.remove(s[left])
                print("-",un_repeted)
                left += 1
                
            left += 1
            right += 1

        return max_len



        



            

        