# https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        chars = list(s)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        total_shifts = [0]*(len(s)+1)

        for start, end, direction in shifts:
            shift = 1 if direction == 1 else -1
            total_shifts[start] shift
            total_shifts[end+1] -= shift

        cur_move = 0
        for i in range(len(total_shifts)-1):
            cur_move += total_shifts[i]
            ch = chars[i] 
            new_ch = (alphabet.index(ch) + cur_move) % 26
            chars[i] = alphabet[new_ch]

        return "".join(chars)
    


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        total_shifts = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            shift = 1 if direction == 1 else -1
            total_shifts[start] += shift
            total_shifts[end+1] -= shift

        cur_move = 0
        ans = ''
        for i, ch in enumerate(s):
            char_ord = ord(ch) - ord('a') # 0-25
            cur_move += total_shifts[i]
            char_ord += cur_move 
            ans += chr(char_ord%26 + ord("a"))

        return ans
