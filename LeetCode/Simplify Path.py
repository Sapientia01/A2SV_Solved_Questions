# https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        directorys = path.split("/")
        stack = []

        for directory in directorys:
            if not directory or directory == ".":
                continue

            if  directory != "..":
                stack.append(directory)
            
            elif stack and directory == "..":
                stack.pop()



        return "/" + "/".join(stack)
