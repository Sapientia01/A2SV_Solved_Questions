# Question link : https://leetcode.com/problems/sort-the-people/description/

#  Using selection sorting
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)

        for i in range(n):
            for j in range(i+1,n):
                if heights[j] >  heights[i]:
                     heights[j] ,  heights[i] =  heights[i] ,  heights[j] 
                     names[j],  names[i] =  names[i] ,  names[j]

        return names


#  Using bubble sorting
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)

        for i in range(n):
            swapped = False
            for j in range(n-1, i, -1):
                if heights[j] >  heights[j-1]:
                     heights[j] ,  heights[j-1] =  heights[j-1] ,  heights[j] 
                     names[j],  names[j-1] =  names[j-1] ,  names[j]
                     swapped = True 

            if not swapped:
                break

        return names