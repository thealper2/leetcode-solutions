
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        count = 0
        n = len(players)
        
        for trainer in trainers:
            if trainer >= players[count]:
                count += 1
                if count == n:
                    break

        return count