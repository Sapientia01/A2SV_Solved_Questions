# Question link: https://leetcode.com/problems/pancake-sorting/description/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        def flip_arr(k):
            for i in range((k+1)//2):
                arr[i],arr[k-i] = arr[k-i],arr[i]

        flips =[]
        max_index = arr.index(1)
        flip_arr(max_index)
        flips.append(max_index+1)

        cur_max = 2

        while cur_max < len(arr)+1:
            max_index = arr.index(cur_max)
            flip_arr(max_index-1)
            flips.append(max_index)

            while(max_index <  len(arr)-1 and  arr[max_index]+1 == arr[max_index+1]):
                cur_max +=1
                max_index+=1 

            if (arr[0]== 1 and arr[max_index-1]+1 == arr[max_index] and arr[-1]==  len(arr) and cur_max >  len(arr)-1):
                break

            flip_arr(max_index)
            flips.append(max_index+1)
            cur_max += 1

        return flips