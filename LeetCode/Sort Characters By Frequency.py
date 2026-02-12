# Question link: https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        order = []

        for ch in freq:
            order.append([freq[ch], ch])
        
        order.sort(reverse= True)

        for i, chars in enumerate(order):
            order[i] = chars[1] * chars[0]

        return "".join(order)