from typing import List
from collections import defaultdict


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rank_count = defaultdict(int)
        suit_count = set(suits)

        if len(suit_count) == 1:
            return "Flush"

        max_rank = 0
        for rank in ranks:
            rank_count[rank] += 1
            if rank_count[rank] > max_rank:
                max_rank = rank_count[rank]
        
        if max_rank >= 3:
            return "Three of a Kind"
        elif max_rank == 2:
            return "Pair"
        
        return "High Card"