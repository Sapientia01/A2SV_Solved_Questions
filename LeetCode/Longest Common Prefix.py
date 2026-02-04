class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        i = 0
        largestPrefix = ''

        for i in range(len(strs[0])):
            pref = strs[0][i]

            for word in strs :
                if i >= len(word):
                     return largestPrefix
                if word[i] != pref:
                     return largestPrefix
      
            largestPrefix += pref

        return largestPrefix