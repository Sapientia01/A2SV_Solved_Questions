# Question link:  https://leetcode.com/problems/remove-comments/description/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        inBlock = False
        cur_line = []

        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if not inBlock and i < n-1 and line[i:i+2] == "//":
                    break
                elif not inBlock and i < n-1 and line[i:i+2] == "/*":
                    inBlock = True
                    i += 2
                elif inBlock and i < n-1 and line[i:i+2] == "*/":
                    inBlock = False
                    i += 2
                elif not inBlock:
                    cur_line.append(line[i])
                    i += 1
                else:
                    i += 1

            if cur_line and not inBlock:
                res.append("".join(cur_line))
                cur_line = []

        return res