# Question link: https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        cur_num = "".join(sorted(str(n)))
         
        while cur_num not in nums:
            nums.add(cur_num)
            cur_sum = 0

            for num in cur_num:
                cur_sum += int(num) ** 2
            
            if cur_sum == 1:
                return True
            else:
                cur_num = "".join(sorted(str(cur_sum)))

        return False