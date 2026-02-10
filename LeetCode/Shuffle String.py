# Question link: https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        indexs = {indices[i]: s[i] for i in range(len(s))}
        suffeled = [indexs[i] for i in range(len(s))]
        return "".join(suffeled)