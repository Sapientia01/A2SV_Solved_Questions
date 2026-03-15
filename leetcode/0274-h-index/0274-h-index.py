class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted([x for x in citations if x != 0])
        print(citations)
        n = len(citations)
        h = 0

        for i in range(n):
            if citations[i] <= n -i:
                h = citations[i]
            else:
                h = max(n-i, h)

        return h