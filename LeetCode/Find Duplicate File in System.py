#Question link: https://leetcode.com/problems/find-duplicate-file-in-system/description/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = {}
        for path in paths:
            directory_name, *files_name = path.split()
            directory_name+= "/"

            for file_name in files_name:
                name, data = file_name[:-1].split("(")
                if data in files:
                    files[data].append(directory_name + name)
                else:
                    files[data] = [directory_name  + name]

        return [value for value in files.values() if len(value) > 1]