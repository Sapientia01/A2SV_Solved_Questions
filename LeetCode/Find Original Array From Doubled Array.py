# Question Link: https://leetcode.com/problems/find-original-array-from-doubled-array/description/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        freq = Counter(changed)
        keys = sorted(freq.keys())
        res = []

        for num in keys:
            if num in freq and num*2 != num:
                if num*2 not in freq:
                    return []
                elif freq[num] > freq[num*2]:
                    return []

                else:
                    res.extend([num]* freq[num])
                    freq[num*2] -= freq[num]
                    del freq[num]
                    if freq[num*2] == 0:
                        del freq[num*2]

            elif num*2 == num and freq[num] % 2 == 0:
                res.extend([num]* (freq[num]//2))

        if len(res) * 2 != len(changed):
            return []

        return res