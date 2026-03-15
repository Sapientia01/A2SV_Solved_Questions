class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n):
            if haystack[i] == needle[0]:
                if i + m <= n and haystack[i:i+m] == needle:
                    return i


        return -1
       
        



# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)

