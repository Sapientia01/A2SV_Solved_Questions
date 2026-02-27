# Question link: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

import math
import os
import random
import re
import sys

def countSwaps(nums):
    n = len(nums)
    swaps = 0

    for i in range(n):
        swapped = False
        for j in range(n-1, i, -1):
            if nums[j] <  nums[j-1]:
                    nums[j] ,  nums[j-1] =  nums[j-1] ,  nums[j] 
                    swaps += 1
                    swapped = True 

        if not swapped:
            break
            
    print("Array is sorted in", swaps , "swaps." )
    print("First Element:", nums[0])
    print("Last Element:", nums[-1])          
    
            
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)