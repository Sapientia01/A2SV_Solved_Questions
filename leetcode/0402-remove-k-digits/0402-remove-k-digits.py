class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        new_num = []

        for i,digit in enumerate(num):
            while new_num and new_num[-1] > digit and n-i + len(new_num) > n-k:
                new_num.pop()

            new_num.append(digit)

        while len(new_num) > n-k:
            new_num.pop()

        while len(new_num) > 1 and new_num[0] == "0":
            new_num.pop(0)

        return "0" if k == len(num) else "".join(new_num)