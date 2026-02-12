# Question link: https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1,n+1))
        i = 0

        while len(players) > 1:
            i += (k-1)
            i %= len(players)

            players.pop(i)

        return players[0]