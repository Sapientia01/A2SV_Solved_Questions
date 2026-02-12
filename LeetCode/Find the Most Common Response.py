# Question link: https://leetcode.com/problems/find-the-most-common-response/description/


def isLexicographicallySmaller(a,b):
    n = min(len(a), len(b))
    if a[:n] == b[:n]:
        return len(a) < len(b)

    return a[:n] < b[:n]

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        max_freq = 0 
        freq = defaultdict(int)
        for responce in responses:
            for word in set(responce):
                freq[word] += 1
                max_freq = max(max_freq, freq[word])

        ans = responses[0][0]
        for responce in freq:
            n = min(len(ans), len(responce))
            if freq[responce] > freq[ans] or ( freq[responce] == freq[ans] \
               and isLexicographicallySmaller(responce,ans)):
                     ans = responce


        return ans