# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        que = deque([[0,-1]])
        cur,min_len = 0, n+1

        for i,num in enumerate(nums):
            cur += num

            while que and cur - que[0][0] >= k:
                min_len = min(min_len, i - que.popleft()[1])

            # This is to keep monotoniclly incresing que to avoid -ve no
            while que and que[-1][0] > cur:
                que.pop()

            que.append([cur, i])

        return min_len if min_len < n+1 else -1