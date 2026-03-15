class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        equal_skill = skill[0] + skill[-1]
        chemistry_sum = 0
        n = len(skill)
        i = 0
        while i<(n//2):
            if skill[i] + skill[n-i-1] != equal_skill:
                return -1
            else:
                chemistry_sum += (skill[i] * skill[n-i-1] )

            i+=1

        return chemistry_sum



        











# class Solution:
#     def dividePlayers(self, skill: List[int]) -> int:
#         skill.sort()
#         equal_skill = skill[0] + skill[-1]
#         chemistry_sum = 0
#         n = len(skill)
#         for i in range(n//2):
#             if skill[i] + skill[n-i-1] != equal_skill:
#                 return -1
#             else:
#                 chemistry_sum += (skill[i] * skill[n-i-1] )

#         return chemistry_sum



        