#Question link : https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners  = {}
        losers = {}
        for winner , loser in matches:
            if winner in winners:
                winners[winner] += 1
            else:
                winners[winner] = 1

            if loser in losers:
                losers[loser] += 1
            else:
                losers[loser] = 1

        not_loser = sorted([num for num  in winners if num not in losers])
        one_loser = sorted([num for num  in losers if losers[num] == 1])

        return [not_loser, one_loser]