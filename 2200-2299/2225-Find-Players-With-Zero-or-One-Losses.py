from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}        
        for winner, loser in matches:
            if winner not in d:
                d[winner] = {'winner': 0, 'loser': 0}

            if loser not in d:
                d[loser] = {'winner': 0, 'loser': 0}
                
            d[winner]['winner'] += 1
            d[loser]['loser'] += 1

        winners = []
        losers = []
        for k, v in d.items():
            if v['loser'] == 0:
                winners.append(k)
            
            if v['loser'] == 1:
                losers.append(k)

        winners.sort()
        losers.sort()
        return [winners, losers]
