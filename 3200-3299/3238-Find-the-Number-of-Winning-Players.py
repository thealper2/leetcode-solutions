from collections import defaultdict
from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        player_color_counts = defaultdict(lambda: defaultdict(int))
        
        for player_id, color_id in pick:
            player_color_counts[player_id][color_id] += 1
        
        winners = 0
        for player in range(n):
            for color in player_color_counts[player]:
                if player_color_counts[player][color] > player:
                    winners += 1
                    break
        return winners
