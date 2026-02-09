# Question link: https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = sorted(freq.keys(), key = lambda x : freq[x], reverse = True)
        return res[:k]