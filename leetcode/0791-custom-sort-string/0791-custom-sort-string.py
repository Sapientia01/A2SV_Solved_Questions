class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = ""
        for ch in order:
            if ch in freq:
                res += ch * freq[ch]
                del freq[ch]
      
        for ch in freq:
            res += ch * freq[ch]

        return res
        